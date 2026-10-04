# BÀI TẬP LỚN TRÍ TUỆ NHÂN TẠO
## Mô phỏng trò chơi cờ tướng bằng thuật toán Backtracking

Bản mẫu dùng Python và Tkinter, không cần cơ sở dữ liệu hoặc thư viện pip. Khuyến nghị Python 3.10 trở lên có Tkinter. Chương trình không phụ thuộc ảnh quân cờ: tên quân được vẽ bằng tiếng Việt.

## 1. Chạy trên Windows

1. Giải nén toàn bộ thư mục `co_tuong_backtracking`.
2. Mở thư mục đó, gõ `cmd` vào thanh địa chỉ File Explorer rồi Enter.
3. Kiểm tra Python: `py -3 --version`.
4. Chạy: `py -3 main.py`.
5. Nếu máy dùng lệnh `python` thay vì `py`, chạy `python main.py`.

Có thể nháy đúp `CHAY_WINDOWS.bat` khi đã cài Python Launcher. Nếu báo không nhận lệnh Python, cần cài Python và bật tùy chọn thêm Python vào PATH. Nếu báo thiếu `tkinter`, cần bổ sung thành phần Tcl/Tk của bản cài Python. Không đặt tên tệp riêng là `tkinter.py`, vì sẽ che khuất thư viện chuẩn.

## 2. Cách chơi

- Đỏ ở phía dưới, đi trước; máy luôn cầm Đen.
- Bấm quân của mình, sau đó bấm một chấm xanh để đi.
- Nước khiến Tướng của mình bị chiếu bị loại bỏ.
- Chọn chế độ rồi bấm **Chơi mới** để áp dụng.
- **Hai người**: hai người chơi luân phiên trên cùng một máy.
- **Đi lại**: chế độ đấu máy hoàn tác một lượt người + máy; nếu máy đang nghĩ thì hoàn tác nước người vừa đi. Chế độ hai người hoàn tác một nước.
- Độ sâu 1, 2, 3 tính theo nửa lượt: mỗi bên đi một nước là một mức.
- Mỗi lượt máy có ngân sách khoảng 4 giây. Giao diện hiển thị độ sâu thực tế đã hoàn tất; chọn 3 không bảo đảm luôn hoàn tất 3.
- Không còn nước hợp lệ thì bên đến lượt thua, kể cả khi không bị chiếu.
- Chương trình quy ước hòa nếu cùng thế cờ, cùng bên đến lượt xuất hiện 3 lần.

## 3. Các tệp

| Tệp | Vai trò |
|---|---|
| `main.py` | Giao diện Tkinter, lượt chơi, lịch sử, hoàn tác, gọi máy ở luồng nền |
| `luat_co.py` | Khởi tạo bàn cờ, cách đi 7 loại quân, kiểm tra chiếu, sinh nước hợp lệ, chấm điểm |
| `ai.py` | Backtracking, Minimax dạng Negamax, Alpha–Beta, tăng dần độ sâu |
| `test_co_tuong.py` | 15 kiểm thử tự động cho luật và thuật toán |
| `BAO_CAO_THAM_KHAO.md` | Nội dung báo cáo, giả mã và câu hỏi bảo vệ |
| `CHAY_WINDOWS.bat` | Chạy trên Windows có Python Launcher |

## 4. Kiểm thử

Chạy `py -3 test_co_tuong.py` hoặc `python test_co_tuong.py`.

Khi xây dựng, 15 kiểm thử đã chạy thành công. Đã kiểm tra cú pháp tất cả các tệp Python. Môi trường tạo bài không có màn hình đồ họa, nên chưa kiểm thử thao tác trực tiếp với cửa sổ Tkinter. Cần chạy trên máy của bạn và thực hiện các ca thủ công dưới đây trước khi nộp:

| Mã | Thao tác | Mong đợi |
|---|---|---|
| UI01 | Chạy `main.py` | Hiện đủ 32 quân trên bàn 9 × 10 |
| UI02 | Chọn Tốt Đỏ trước khi qua sông | Chỉ có đích tiến một ô nếu không bị chặn |
| UI03 | Đi một nước ở chế độ đấu máy | Máy đi Đen, rồi trả lượt Đỏ |
| UI04 | Bấm Đi lại sau khi máy đi | Bàn cờ và lịch sử lùi hai nước |
| UI05 | Bấm Chơi mới lúc máy đang nghĩ | Trở về khai cuộc, không áp dụng kết quả ván cũ |
| UI06 | Chọn Hai người, bấm Chơi mới | Điều khiển lần lượt cả hai bên |
| UI07 | Thay độ sâu rồi chơi | Hiển thị số nút, số lần cắt và độ sâu thực tế |
| UI08 | Lặp một thế hợp lệ đủ ba lần | Thông báo hòa, không nhận thêm nước |

Không ghi các ca thủ công là đạt cho đến khi đã thực sự thực hiện.

## 5. Phạm vi và hạn chế

Đây là mô phỏng phục vụ môn học, không phải phần mềm thi đấu chính thức. Chưa có luật phân xử chiếu dai/đuổi dai, luật hòa theo số nước không ăn quân, lưu/tải ván, chơi mạng, đồng hồ thi đấu hoặc cơ sở dữ liệu khai cuộc. AI chưa dùng bảng băm hoặc tìm kiếm ổn định ở lá. Máy chấm điểm vật chất và vị trí đơn giản nên có thể bỏ lỡ chiến thuật ngoài độ sâu tìm kiếm. Việc lặp thế được xét ở lớp ván chơi, chưa đưa vào cây tìm kiếm của máy.

Báo cáo đi kèm là bản tham khảo theo mã nguồn, cần bổ sung tên trường, lớp, thành viên, giảng viên, ảnh chương trình chạy thật và kết quả thử trên máy của bạn theo mẫu giảng viên.
