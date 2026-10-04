"""Chạy: python main.py. Chỉ dùng thư viện chuẩn Python."""
import queue
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from luat_co import ban_dau, hop_le, bi_chieu, thu_nuoc, hoan_tac, TEN
from ai import MayTinh


class UngDung:
    def __init__(self, root):
        self.root = root
        root.title('Cờ tướng • Backtracking | Bài tập lớn Trí tuệ nhân tạo')
        root.configure(bg='#f4efe5')
        root.resizable(False, False)
        self.che_do = tk.StringVar(value='Người đấu máy')
        self.do_sau = tk.StringVar(value='2')
        self.trang_thai = tk.StringVar()
        self.thong_ke = tk.StringVar(value='Chưa có lượt tìm kiếm của máy.')
        self.hang_doi = queue.Queue()
        self.phien = 0
        self.dang_tinh = False
        self.canvas = tk.Canvas(root, width=580, height=650,
                                bg='#eed4a5', highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=16, pady=16)
        self.canvas.bind('<Button-1>', self.chon)
        panel = ttk.Frame(root, padding=15)
        panel.grid(row=0, column=1, sticky='ns', padx=(0, 16), pady=16)
        ttk.Label(panel, text='CỜ TƯỚNG', font=('Arial', 22, 'bold')).pack(anchor='w')
        ttk.Label(panel, text='Backtracking + Minimax + Alpha–Beta').pack(anchor='w', pady=(0, 20))
        ttk.Label(panel, text='Chế độ (áp dụng khi chơi mới)').pack(anchor='w')
        ttk.Combobox(panel, textvariable=self.che_do, state='readonly', width=29,
                     values=['Người đấu máy', 'Hai người']).pack(fill='x', pady=5)
        ttk.Label(panel, text='Độ sâu máy: 1 dễ · 2 vừa · 3 khó hơn').pack(anchor='w')
        ttk.Combobox(panel, textvariable=self.do_sau, state='readonly',
                     values=['1', '2', '3']).pack(fill='x', pady=5)
        ttk.Button(panel, text='Chơi mới', command=self.moi).pack(fill='x', pady=(12, 5))
        ttk.Button(panel, text='Đi lại', command=self.di_lai).pack(fill='x', pady=5)
        ttk.Label(panel, textvariable=self.trang_thai, wraplength=300,
                  font=('Arial', 12, 'bold')).pack(anchor='w', pady=12)
        ttk.Label(panel, textvariable=self.thong_ke, wraplength=300).pack(anchor='w', pady=5)
        ttk.Label(panel, text='Lịch sử • cột A–I, hàng 0–9').pack(anchor='w', pady=(15, 5))
        self.lich = tk.Listbox(panel, width=39, height=13, font=('Arial', 10))
        self.lich.pack(fill='both', expand=True)
        ttk.Label(panel, text='Đỏ đi trước. Chọn quân rồi chọn chấm xanh.\n'
                  'Máy cầm đen. Hết nước hợp lệ là thua.\n'
                  'Lặp thế 3 lần: hòa theo quy ước mô phỏng.',
                  wraplength=300).pack(anchor='w', pady=(15, 0))
        self.moi()
        self.root.after(80, self.nhan_ket_qua)

    def khoa(self):
        return tuple(tuple(row) for row in self.b), self.phe

    def moi(self):
        self.phien += 1  # Kết quả AI của ván cũ sẽ bị bỏ qua.
        self.dang_tinh = False
        self.b, self.phe, self.chon_o = ban_dau(), 1, None
        self.may = self.che_do.get() == 'Người đấu máy'
        self.stack, self.van = [], []
        self.van.append(self.khoa())
        self.lich.delete(0, tk.END)
        self.thong_ke.set('Chưa có lượt tìm kiếm của máy.')
        self.cap_nhat()

    def cap_nhat(self):
        self.ds = hop_le(self.b, self.phe)
        self.xong = False
        ten = 'Đỏ' if self.phe == 1 else 'Đen'
        if not self.ds:
            self.xong = True
            ly_do = 'bị chiếu bí' if bi_chieu(self.b, self.phe) else 'hết nước hợp lệ'
            self.trang_thai.set(f'{ten} {ly_do}. {"Đen" if self.phe == 1 else "Đỏ"} thắng!')
        elif self.van.count(self.khoa()) >= 3:
            self.xong = True
            self.trang_thai.set('Hòa: cùng thế cờ và lượt đi lặp lại 3 lần.')
        else:
            self.trang_thai.set(f'Lượt {ten}' + (' — đang bị chiếu!' if bi_chieu(self.b, self.phe) else ''))
        self.ve()
        if not self.xong and self.may and self.phe == -1:
            self.chay_may()

    def ve(self):
        cv = self.canvas
        cv.delete('all')
        for r in range(10):
            y = 55 + r * 58
            cv.create_line(55, y, 519, y, fill='#684820', width=2)
            cv.create_text(28, y, text=str(r), fill='#684820')
        for c in range(9):
            x = 55 + c * 58
            cv.create_text(x, 28, text=chr(65 + c), fill='#684820')
            if c in (0, 8):
                cv.create_line(x, 55, x, 577, fill='#684820', width=2)
            else:
                cv.create_line(x, 55, x, 287, fill='#684820')
                cv.create_line(x, 345, x, 577, fill='#684820')
        for r in (0, 7):
            cv.create_line(229, 55 + r * 58, 345, 55 + (r + 2) * 58, fill='#684820')
            cv.create_line(345, 55 + r * 58, 229, 55 + (r + 2) * 58, fill='#684820')
        cv.create_text(287, 316, text='S Ô N G   •   RANH GIỚI', fill='#92612a', font=('Arial', 15))
        last = self.stack[-1][0] if self.stack else ()
        for r in range(10):
            for c in range(9):
                x, y = 55 + c * 58, 55 + r * 58
                if last and (r, c) in (last[:2], last[2:]):
                    cv.create_rectangle(x-26, y-26, x+26, y+26, outline='#b78a19', width=3)
                p = self.b[r][c]
                if p:
                    selected = self.chon_o == (r, c)
                    cv.create_oval(x-24, y-24, x+24, y+24,
                                   fill='#fff9e9' if not selected else '#d4ebcb',
                                   outline='#bd342d' if p > 0 else '#253742', width=3)
                    cv.create_text(x, y, text=TEN[abs(p)],
                                   fill='#bd342d' if p > 0 else '#253742',
                                   font=('Arial', 10, 'bold'))
        if self.chon_o:
            for r, c, x, y in self.ds:
                if (r, c) == self.chon_o:
                    px, py = 55 + y * 58, 55 + x * 58
                    cv.create_oval(px-7, py-7, px+7, py+7, fill='#438745', outline='white')
        cv.create_text(287, 620, text='ĐEN ở trên  •  ĐỎ ở dưới', fill='#684820', font=('Arial', 11))

    def chon(self, event):
        if self.xong or self.dang_tinh or (self.may and self.phe == -1):
            return
        c, r = round((event.x - 55) / 58), round((event.y - 55) / 58)
        if not (0 <= r < 10 and 0 <= c < 9):
            return
        if abs(event.x - (55+c*58)) > 27 or abs(event.y - (55+r*58)) > 27:
            return
        if self.b[r][c] * self.phe > 0:
            self.chon_o = (r, c)
            self.ve()
        elif self.chon_o:
            m = (*self.chon_o, r, c)
            if m in self.ds:
                self.di(m)
            else:
                self.root.bell()

    def di(self, m):
        r, c, x, y = m
        p = self.b[r][c]
        an = thu_nuoc(self.b, m)
        self.stack.append((m, an))
        self.lich.insert(tk.END, f'{len(self.stack):02d}. {"Đỏ" if p > 0 else "Đen"} '
                         f'{TEN[abs(p)]}: {chr(65+c)}{r} → {chr(65+y)}{x}'
                         + (f' ăn {TEN[abs(an)]}' if an else ''))
        self.lich.see(tk.END)
        self.phe *= -1
        self.chon_o = None
        self.van.append(self.khoa())
        self.cap_nhat()

    def di_lai(self):
        if not self.stack:
            return
        self.phien += 1
        self.dang_tinh = False
        n = 1
        if self.may and self.phe == 1 and len(self.stack) >= 2:
            n = 2
        for _ in range(n):
            m, an = self.stack.pop()
            hoan_tac(self.b, m, an)
            self.phe *= -1
            self.van.pop()
            self.lich.delete(tk.END)
        self.chon_o = None
        self.thong_ke.set('Đã hoàn tác nước đi.')
        self.cap_nhat()

    def chay_may(self):
        self.dang_tinh = True
        self.trang_thai.set('Máy đang tìm kiếm nước đi…')
        b = [row[:] for row in self.b]
        phien, sau = self.phien, int(self.do_sau.get())

        def worker():
            try:
                m, stats = MayTinh().tim(b, -1, sau, 4.0)
                self.hang_doi.put((phien, m, stats, None))
            except Exception as e:
                self.hang_doi.put((phien, None, None, str(e)))
        threading.Thread(target=worker, daemon=True).start()

    def nhan_ket_qua(self):
        try:
            while True:
                phien, m, stats, loi = self.hang_doi.get_nowait()
                if phien != self.phien:
                    continue
                self.dang_tinh = False
                if loi:
                    self.trang_thai.set('Máy gặp lỗi. Chọn Đi lại hoặc Chơi mới.')
                    messagebox.showerror('Lỗi tìm kiếm', loi)
                elif m in self.ds:
                    self.thong_ke.set(f'Độ sâu hoàn tất: {stats["sau"]}\n'
                                      f'Số nút: {stats["nut"]:,} | Lần cắt: {stats["cat"]:,}\n'
                                      f'Thời gian: {stats["giay"]:.2f} giây')
                    self.di(m)
        except queue.Empty:
            pass
        self.root.after(80, self.nhan_ket_qua)


if __name__ == '__main__':
    app = tk.Tk()
    UngDung(app)
    app.mainloop()
