# BÀI TẬP LỚN MÔN TRÍ TUỆ NHÂN TẠO
# Đề tài: Xây dựng chương trình mô phỏng trò chơi cờ tướng bằng Backtracking

- Sinh viên: …
- Mã sinh viên: …
- Lớp: …
- Giảng viên hướng dẫn: …

## CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI

### 1.1. Lý do chọn đề tài

Cờ tướng là trò chơi đối kháng hai người với nhiều khả năng lựa chọn ở mỗi lượt. Để chọn nước đi, chương trình phải mô phỏng các phương án và phản ứng của đối thủ. Đề tài giúp vận dụng tìm kiếm đệ quy, quay lui, biểu diễn trạng thái và hàm đánh giá trong một bài toán trực quan.

### 1.2. Mục tiêu

Xây dựng bàn cờ 9 cột × 10 hàng; mô phỏng cách đi của Tướng, Sĩ, Tượng, Mã, Xe, Pháo, Tốt; loại nước tự chiếu; hỗ trợ người đấu máy và hai người trên cùng máy; dùng Backtracking để duyệt cây trạng thái, kết hợp Minimax để lựa chọn nước đi. Người học quan sát được số nút tìm kiếm, số lần cắt tỉa, độ sâu và thời gian.

### 1.3. Phạm vi

Phần mềm phục vụ thực hành môn học. Đỏ đi trước. Bên đến lượt không có nước hợp lệ bị xử thua. Lặp thế ba lần được xử hòa theo quy ước riêng của mô phỏng. Chưa áp dụng đầy đủ quy định thi đấu về chiếu dai, đuổi dai và các loại hòa khác.

## CHƯƠNG 2. CƠ SỞ LÝ THUYẾT

### 2.1. Backtracking

Backtracking (quay lui) là phương pháp xây dựng lời giải từng bước. Tại một trạng thái, thuật toán thử một lựa chọn, tiếp tục tìm kiếm và sau đó khôi phục trạng thái để xét lựa chọn khác. Trong đề tài, lựa chọn là một nước cờ hợp lệ.

Một nhánh tìm kiếm có thể được mô tả: Đỏ đi nước A → Đen đáp B → Đỏ đáp C. Khi đã đánh giá nhánh này, chương trình hoàn tác C, B và A tương ứng với từng lần trả về của lời gọi đệ quy. Sau đó tiếp tục xét các nhánh khác. Không lưu đè kết quả của một nhánh lên trạng thái dùng cho nhánh kế tiếp.

### 2.2. Vì sao kết hợp Minimax?

Backtracking cung cấp cơ chế thử và hoàn tác; bản thân nó không quy định nước nào tốt. Minimax mô hình hóa đối thủ cũng cố chọn phương án tốt cho mình. Điểm gốc của bàn cờ dương khi có lợi cho Đỏ, âm khi có lợi cho Đen.

Mã nguồn sử dụng Negamax, một cách viết gọn của Minimax cho trò chơi tổng bằng không. Mỗi bên tối đa hóa điểm nhìn từ phía mình:

`V(s, p, d) = max(-V(sau_khi_di(s, m), -p, d-1))`

Trong đó `p` bằng 1 cho Đỏ và -1 cho Đen. Tại lá, trả về `p * danh_gia(s)`. Do đó một điểm có lợi cho đối phương sẽ đổi dấu khi quay về bên đang xét.

### 2.3. Alpha–Beta

Alpha lưu cận dưới tốt nhất đã biết cho người đang xét; beta là cận trên của cửa sổ tìm kiếm. Khi `alpha >= beta`, các nước còn lại ở nút đó không thể cải thiện quyết định của tổ tiên trong cửa sổ hiện tại, nên có thể dừng xét. Khi cùng độ sâu, cùng đánh giá và tìm kiếm hoàn tất, Alpha–Beta giữ nguyên giá trị Minimax. Thứ tự xét nước ăn quân trước hỗ trợ tăng khả năng cắt tỉa.

### 2.4. Điều kiện dừng

1. Không có nước hợp lệ: trả điểm thua `-1_000_000 + ply`.
2. Đạt độ sâu 0: trả điểm heuristic từ phía bên đang xét.
3. Hết ngân sách thời gian: hủy vòng tìm kiếm hiện tại, sử dụng kết quả của vòng độ sâu đã hoàn tất trước đó.

Điều kiện hết nước được xét trước điều kiện độ sâu, tránh đánh giá nhầm thế kết thúc thành một thế vật chất bình thường. Nếu không hoàn tất nổi độ sâu 1, máy vẫn có một nước hợp lệ dự phòng.

### 2.5. Độ phức tạp

Gọi `b` là số nước hợp lệ trung bình và `d` là độ sâu. Duyệt toàn bộ cây có số nút cỡ `O(b^d)`, chưa tính chi phí sinh nước và kiểm tra luật ở từng nút. Alpha–Beta vẫn có trường hợp xấu nhất `O(b^d)`; với thứ tự nước lý tưởng có thể giảm mạnh về gần `O(b^(d/2))`. Đây là mô hình lý thuyết, không phải số đo của chương trình.

Bàn cờ được sửa và hoàn tác tại chỗ trong tìm kiếm. Ngăn xếp đệ quy có độ sâu `O(d)`; vì mỗi lời gọi còn giữ danh sách tối đa `b` nước, bộ nhớ làm việc của triển khai khoảng `O(bd)`, ngoài bàn cờ kích thước cố định. Lịch sử cả ván được lưu riêng tại giao diện.

## CHƯƠNG 3. PHÂN TÍCH VÀ THIẾT KẾ

### 3.1. Yêu cầu chức năng

| Chức năng | Mô tả |
|---|---|
| Khởi tạo | Xếp 32 quân đúng vị trí khai cuộc |
| Chọn và đi quân | Hiển thị đích hợp lệ, di chuyển và ăn quân |
| Kiểm tra luật | Cản Mã, cản Tượng, Pháo có ngòi, giới hạn cung và sông |
| Bảo vệ Tướng | Loại nước tự chiếu hoặc làm hai Tướng đối mặt |
| Máy tính | Tìm nước bằng quay lui và Minimax |
| Kết thúc | Phát hiện hết nước hợp lệ và hòa lặp thế theo quy ước |
| Đi lại | Khôi phục bàn cờ, bên đến lượt và lịch sử |
| Thống kê | Số nút, số lần cắt, thời gian, độ sâu hoàn tất |

### 3.2. Biểu diễn trạng thái

Bàn cờ là danh sách hai chiều `b[10][9]`. Hàng 0 nằm phía Đen; hàng 9 nằm phía Đỏ. Giá trị 0 là ô trống. Số dương là quân Đỏ, số âm là quân Đen.

| Mã tuyệt đối | Quân | Điểm cơ bản |
|---|---|---|
| 1 | Tướng | 100000 |
| 2 | Sĩ | 120 |
| 3 | Tượng | 120 |
| 4 | Mã | 300 |
| 5 | Xe | 600 |
| 6 | Pháo | 350 |
| 7 | Tốt | 70 |

Một nước đi là `(r, c, x, y)`: từ hàng r, cột c đến hàng x, cột y. Trạng thái chơi còn bao gồm bên đến lượt, lịch sử nước, quân bị ăn và các thế đã xuất hiện. Để xét lặp thế, khóa bao gồm cả bàn cờ và bên đến lượt.

### 3.3. Kiểm tra nước hợp lệ

Đầu tiên sinh đích theo cách đi riêng của từng quân. Với mỗi đích, tạm thực hiện nước đi, kiểm tra Tướng của bên vừa đi có bị đối phương tấn công không rồi hoàn tác. Chỉ giữ các nước không làm Tướng mình bị chiếu. Cách đi đối mặt của Tướng được dùng trong kiểm tra tấn công. Giao diện kết thúc bằng hết nước hợp lệ, không yêu cầu người chơi ăn Tướng.

### 3.4. Hàm đánh giá

`E(s) = tổng giá trị quân Đỏ − tổng giá trị quân Đen`

Giá trị gồm điểm cơ bản và điểm vị trí. Tốt được cộng điểm khi tiến lên và thêm điểm khi qua sông. Xe, Mã, Pháo có một phần thưởng nhỏ khi gần cột giữa. Các trọng số do người xây dựng lựa chọn để minh họa, chưa được huấn luyện hay tối ưu bằng thực nghiệm. Tướng có giá trị lớn nhưng chiến thắng thực tế được nhận diện bằng trạng thái hết nước.

### 3.5. Tổ chức chương trình

- `luat_co.py`: biểu diễn, sinh nước, kiểm tra chiếu, thử nước, hoàn tác và đánh giá.
- `ai.py`: tìm kiếm có giới hạn thời gian và độ sâu.
- `main.py`: giao diện và quản lý ván.
- `test_co_tuong.py`: kiểm thử tự động.

Luồng nền tính toán trên bản sao bàn cờ để cửa sổ vẫn phản hồi. Luồng nền trả kết quả qua hàng đợi; chỉ luồng giao diện thao tác với Tkinter. Mỗi ván/lần hoàn tác có mã phiên để kết quả tính toán cũ không bị áp dụng vào trạng thái mới.

## CHƯƠNG 4. CÀI ĐẶT THUẬT TOÁN

### 4.1. Giả mã quay lui

```text
BACKTRACKING(bàn, phe, độ_sâu, alpha, beta):
    Nếu hết thời gian: phát tín hiệu dừng
    Sinh danh sách nước hợp lệ
    Nếu không có nước: trả điểm thua
    Nếu độ_sâu = 0: trả phe × đánh_giá(bàn)
    best ← âm vô cùng
    Với mỗi nước m (ưu tiên ăn quân):
        quân_bị_ăn ← THỬ_NƯỚC(bàn, m)
        Thử:
            điểm ← -BACKTRACKING(bàn, -phe, độ_sâu-1, -beta, -alpha)
        Luôn thực hiện, kể cả khi hết thời gian:
            HOÀN_TÁC(bàn, m, quân_bị_ăn)
        Cập nhật best và nước tốt nhất
        alpha ← max(alpha, điểm)
        Nếu alpha >= beta: dừng xét các nước còn lại
    Trả best và nước tốt nhất
```

### 4.2. Đoạn mã thể hiện Backtracking

```python
an = thu_nuoc(b, m)                 # Thử lựa chọn
try:
    d, _ = self.backtracking(
        b, -phe, sau - 1, -beta, -alpha, ply + 1)
    d = -d                         # Đổi góc nhìn về bên hiện tại
finally:
    hoan_tac(b, m, an)              # Khôi phục trước khi thử nhánh khác
```

`finally` cần thiết vì hết thời gian được xử lý bằng ngoại lệ. Nếu chỉ hoàn tác sau lời gọi đệ quy mà không có `finally`, ngoại lệ có thể bỏ qua bước hoàn tác và làm bàn cờ tìm kiếm sai.

### 4.3. Ví dụ tính điểm Minimax

Ví dụ minh họa, không phải kết quả đo một ván cụ thể: Đỏ có hai nước A, B. Sau A, đối thủ có thể làm điểm từ góc nhìn Đỏ thành 100 hoặc -50; Đen sẽ chọn -50. Sau B, đối thủ có thể làm điểm thành 20 hoặc 10; Đen sẽ chọn 10. Đỏ chọn B vì `max(min(100,-50), min(20,10)) = 10`. Qua mỗi nhánh, bàn cờ đều phải được hoàn tác trước khi xét nhánh kế tiếp.

## CHƯƠNG 5. KIỂM THỬ VÀ ĐÁNH GIÁ

### 5.1. Kết quả kiểm thử tự động

15 kiểm thử đi kèm đã được thực thi thành công trong môi trường xây dựng:

| STT | Nội dung |
|---|---|
| 1 | Khai cuộc có 32 quân và mỗi bên có 44 nước hợp lệ |
| 2 | Mã không đi qua chân bị cản |
| 3 | Tượng bị cản mắt và không qua sông |
| 4 | Pháo ăn khi có đúng một ngòi, không ăn qua hai ngòi |
| 5 | Xe không nhảy qua hoặc ăn quân cùng phe |
| 6 | Tốt đi đúng trước/sau qua sông cho cả hai phía |
| 7 | Sĩ và Tướng bị giới hạn trong cung |
| 8 | Không cho nước làm hai Tướng đối mặt |
| 9 | Không cho bỏ mặc Tướng đang bị chiếu |
| 10 | Hoàn tác trả lại cả quân di chuyển và quân bị ăn |
| 11 | Nhận diện một thế chiếu bí |
| 12 | Nhận diện hết nước khi không bị chiếu |
| 13 | AI trả nước hợp lệ và không sửa bàn đầu vào |
| 14 | Hết thời gian tìm kiếm vẫn bảo toàn bàn cờ |
| 15 | AI chọn ăn Xe có lợi trong thế kiểm thử đơn giản |

Đây là kiểm thử theo các tình huống đại diện, không phải chứng minh bao phủ tất cả các thế cờ. Giao diện chưa được kiểm thử tương tác trực tiếp trong môi trường xây dựng không có màn hình. Cần thực hiện các ca UI trong `HUONG_DAN.md`, chụp ảnh và ghi nhận kết quả thực tế trước khi nộp.

### 5.2. Đề xuất thực nghiệm khi làm báo cáo chính thức

Chọn cùng một thế cờ, cùng bên đến lượt và cùng ngân sách thời gian; chạy từng độ sâu 1, 2, 3. Ghi độ sâu yêu cầu, độ sâu hoàn tất, số nút, số lần cắt, thời gian và nước máy chọn. Không dùng độ sâu yêu cầu để so sánh nếu một vòng bị dừng giữa chừng. Nên chạy lặp lại và lấy trung bình thời gian, ghi cấu hình máy.

Bộ đếm số nút/lần cắt hiện cộng dồn qua các vòng tăng độ sâu, bao gồm cả phần đã duyệt của vòng bị dừng. Khi trình bày, cần giải thích đúng ý nghĩa này. Các thông số này không phải số thế độc nhất vì có thể duyệt lại một thế.

### 5.3. Hạn chế

Tìm kiếm bị giới hạn độ sâu; hàm đánh giá đơn giản; chưa có quiescence search, bảng chuyển vị hoặc sách khai cuộc. Quy tắc lặp thế được xét ở lớp ván chơi, chưa tích hợp vào cây tìm kiếm, nên máy có thể tự dẫn đến hòa. Chưa hỗ trợ đầy đủ luật thi đấu chính thức, lưu ván, chơi mạng hay đồng hồ.

## KẾT LUẬN

### 1. Các nội dung đã đạt được

Đã xây dựng mã nguồn mô phỏng bàn cờ và các luật di chuyển cơ bản; kiểm tra chiếu và lọc nước hợp lệ; cài đặt Backtracking theo cơ chế thử–đệ quy–hoàn tác; kết hợp Minimax dạng Negamax và cắt tỉa Alpha–Beta; có hai chế độ chơi, lịch sử, đi lại và thống kê tìm kiếm. Bộ 15 kiểm thử luật và AI đã chạy đạt.

### 2. Các nội dung chưa đạt được

Chưa đánh giá toàn diện giao diện trên máy người dùng và sức mạnh AI qua nhiều ván; chưa triển khai đầy đủ luật thi đấu, xử lý hòa trong tìm kiếm, lưu/tải ván và chơi trực tuyến. Chưa có thực nghiệm so sánh hiệu năng giữa các biến thể thuật toán.

### 3. Dự kiến phát triển

Bổ sung kiểm thử tương tác, tinh chỉnh hàm đánh giá, tìm kiếm ổn định ở lá, bảng chuyển vị, nhận biết lặp thế trong cây tìm kiếm, lưu ván và luật xử lý chiếu dai/đuổi dai. Có thể thêm chế độ giải thế cờ bắt buộc chiếu bí trong N nước để thể hiện rõ hơn việc tìm lời giải bằng quay lui.

## CÂU HỎI BẢO VỆ

**1. Backtracking nằm ở đâu?** Ở các bước `thu_nuoc`, gọi đệ quy và `hoan_tac` trong `MayTinh.backtracking`. Sinh nước hợp lệ cũng dùng thử và hoàn tác để loại nước tự chiếu.

**2. Vì sao không dùng Backtracking đơn thuần?** Quay lui chỉ duyệt các lựa chọn; cần tiêu chí để chọn giữa chúng. Minimax là tiêu chí ra quyết định khi giả định đối thủ cũng chọn nước tốt.

**3. Vì sao dùng dấu âm trong đệ quy?** Vì đổi bên đến lượt đồng thời đổi góc nhìn đánh giá; lợi thế của bên này là bất lợi của bên kia.

**4. Thuật toán có chắc thắng không?** Không. Chương trình dừng ở độ sâu hữu hạn và dùng heuristic, không giải hoàn toàn trò chơi.

**5. Alpha–Beta có làm bỏ mất nước tốt không?** Nếu triển khai đúng và tìm kiếm cùng độ sâu đến hoàn tất, cắt tỉa giữ nguyên giá trị Minimax; thứ tự nước chỉ ảnh hưởng hiệu quả và lựa chọn giữa những nước đồng điểm.

**6. Vì sao hết nước mà không bị chiếu vẫn thua?** Chương trình áp dụng cách kết thúc của cờ tướng: bên đến lượt không có nước hợp lệ thua, khác với quy tắc pat hòa của cờ vua.

**7. Độ sâu 2 là hai lượt của mỗi bên không?** Không. Độ sâu 2 là hai nửa lượt: một nước bên hiện tại và một nước đáp của đối thủ.

**8. Cần sửa gì trước khi nộp?** Điền thông tin cá nhân, điều chỉnh theo mẫu môn học, chạy kiểm thử giao diện trên máy thật, thêm ảnh minh chứng và số đo thực nghiệm; hiểu được ba bước quay lui để tự giải thích mã.
