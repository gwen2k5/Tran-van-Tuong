"""Luật cờ: đỏ là số dương, đen là số âm; hàng 0 ở phía đen."""
TUONG, SI, VOI, MA, XE, PHAO, TOT = range(1, 8)
TEN = {1: 'Tướng', 2: 'Sĩ', 3: 'Tượng', 4: 'Mã', 5: 'Xe', 6: 'Pháo', 7: 'Tốt'}
GIA = {1: 100000, 2: 120, 3: 120, 4: 300, 5: 600, 6: 350, 7: 70}


def ban_dau():
    b = [[0] * 9 for _ in range(10)]
    b[0] = [-p for p in (XE, MA, VOI, SI, TUONG, SI, VOI, MA, XE)]
    b[9] = [-p for p in b[0]]
    for c in (1, 7):
        b[2][c], b[7][c] = -PHAO, PHAO
    for c in range(0, 9, 2):
        b[3][c], b[6][c] = -TOT, TOT
    return b


def trong_ban(r, c):
    return 0 <= r < 10 and 0 <= c < 9


def trong_cung(r, c, phe):
    return 3 <= c <= 5 and (7 <= r <= 9 if phe == 1 else 0 <= r <= 2)


def nuoc_gia(b, r, c):
    """Sinh đích theo cách di chuyển; chưa lọc nước tự chiếu tướng."""
    p = b[r][c]
    if not p:
        return []
    phe, loai = (1 if p > 0 else -1), abs(p)
    ds = []

    def them(x, y):
        if trong_ban(x, y) and b[x][y] * phe <= 0:
            ds.append((x, y))

    if loai in (XE, PHAO):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y, ngan = r + dr, c + dc, False
            while trong_ban(x, y):
                q = b[x][y]
                if loai == XE:
                    them(x, y)
                    if q:
                        break
                elif not ngan:
                    if q:
                        ngan = True
                    else:
                        ds.append((x, y))
                elif q:
                    if q * phe < 0:
                        ds.append((x, y))
                    break
                x, y = x + dr, y + dc
    elif loai == MA:
        for dr, dc in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                       (1, 2), (-1, 2), (1, -2), (-1, -2)):
            chan_r = r + (dr // 2 if abs(dr) == 2 else 0)
            chan_c = c + (dc // 2 if abs(dc) == 2 else 0)
            if trong_ban(chan_r, chan_c) and not b[chan_r][chan_c]:
                them(r + dr, c + dc)
    elif loai == VOI:
        for dr, dc in ((2, 2), (2, -2), (-2, 2), (-2, -2)):
            x, y = r + dr, c + dc
            if trong_ban(x, y) and (x >= 5 if phe == 1 else x <= 4):
                if not b[r + dr // 2][c + dc // 2]:
                    them(x, y)
    elif loai == SI:
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            if trong_cung(r + dr, c + dc, phe):
                them(r + dr, c + dc)
    elif loai == TUONG:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if trong_cung(r + dr, c + dc, phe):
                them(r + dr, c + dc)
        # Hai tướng đối mặt: dùng để phát hiện nước đi bất hợp lệ.
        for dr in (-1, 1):
            x = r + dr
            while trong_ban(x, c):
                if b[x][c]:
                    if b[x][c] == -phe * TUONG:
                        ds.append((x, c))
                    break
                x += dr
    elif loai == TOT:
        them(r - phe, c)
        if (r <= 4 if phe == 1 else r >= 5):
            them(r, c - 1)
            them(r, c + 1)
    return ds


def bi_chieu(b, phe):
    vua = next(((r, c) for r in range(10) for c in range(9)
                if b[r][c] == phe * TUONG), None)
    if vua is None:
        return True
    return any(vua in nuoc_gia(b, r, c) for r in range(10)
               for c in range(9) if b[r][c] * phe < 0)


def thu_nuoc(b, m):
    r, c, x, y = m
    an = b[x][y]
    b[x][y], b[r][c] = b[r][c], 0
    return an


def hoan_tac(b, m, an):
    r, c, x, y = m
    b[r][c], b[x][y] = b[x][y], an


def hop_le(b, phe):
    ds = []
    for r in range(10):
        for c in range(9):
            if b[r][c] * phe <= 0:
                continue
            for x, y in nuoc_gia(b, r, c):
                # Kết thúc bằng hết nước hợp lệ, không chơi tiếp bằng ăn tướng.
                if abs(b[x][y]) == TUONG:
                    continue
                m = (r, c, x, y)
                an = thu_nuoc(b, m)
                try:
                    if not bi_chieu(b, phe):
                        ds.append(m)
                finally:
                    hoan_tac(b, m, an)
    return ds


def danh_gia(b):
    """Điểm dương có lợi cho đỏ. Hàm heuristic, không bảo đảm thắng."""
    diem = 0
    for r in range(10):
        for c in range(9):
            p = b[r][c]
            if not p:
                continue
            phe = 1 if p > 0 else -1
            gia = GIA[abs(p)]
            if abs(p) == TOT:
                tien = 9 - r if phe == 1 else r
                gia += tien * 6
                if tien >= 5:
                    gia += 45
            if abs(p) in (MA, XE, PHAO):
                gia += 4 - abs(c - 4)
            diem += phe * gia
    return diem
