"""Backtracking + Minimax dạng Negamax + cắt tỉa Alpha–Beta."""
import time
from luat_co import GIA, hop_le, thu_nuoc, hoan_tac, danh_gia


class HetGio(Exception):
    pass


class MayTinh:
    def __init__(self):
        self.nut = 0
        self.cat = 0
        self.han = 0

    def tim(self, b, phe, do_sau=2, gioi_han=4.0):
        start = time.perf_counter()
        self.han = start + gioi_han
        self.nut = self.cat = 0
        ds = hop_le(b, phe)
        if not ds:
            return None, {'nut': 0, 'cat': 0, 'sau': 0, 'giay': 0}
        tot_nhat, diem, dat = ds[0], 0, 0
        # Tăng dần độ sâu, chỉ dùng kết quả của vòng đã hoàn tất.
        for sau in range(1, do_sau + 1):
            try:
                d, m = self.backtracking(b, phe, sau, -10**9, 10**9, 0)
            except HetGio:
                break
            tot_nhat, diem, dat = m, d, sau
        return tot_nhat, {'nut': self.nut, 'cat': self.cat, 'sau': dat,
                          'diem': diem, 'giay': time.perf_counter() - start}

    def backtracking(self, b, phe, sau, alpha, beta, ply):
        if time.perf_counter() >= self.han:
            raise HetGio()
        self.nut += 1
        ds = hop_le(b, phe)
        if not ds:
            # Trong cờ tướng, hết nước đi cũng thua dù không bị chiếu.
            return -1000000 + ply, None
        if sau == 0:
            return phe * danh_gia(b), None
        ds.sort(key=lambda m: GIA.get(abs(b[m[2]][m[3]]), 0), reverse=True)
        best, nuoc = -10**9, ds[0]
        for m in ds:
            an = thu_nuoc(b, m)                  # 1. THỬ
            try:
                d, _ = self.backtracking(        # 2. ĐỆ QUY
                    b, -phe, sau - 1, -beta, -alpha, ply + 1)
                d = -d
            finally:
                hoan_tac(b, m, an)               # 3. QUAY LUI
            if d > best:
                best, nuoc = d, m
            alpha = max(alpha, d)
            if alpha >= beta:
                self.cat += 1
                break
        return best, nuoc
