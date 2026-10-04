import unittest
from luat_co import *
from ai import MayTinh


def rong():
    b = [[0]*9 for _ in range(10)]
    b[0][4], b[9][4], b[5][4] = -TUONG, TUONG, TOT
    return b


class KiemThu(unittest.TestCase):
    def test_khai_cuoc(self):
        b = ban_dau()
        self.assertEqual(sum(bool(p) for row in b for p in row), 32)
        self.assertEqual(len(hop_le(b, 1)), 44)
        self.assertEqual(len(hop_le(b, -1)), 44)

    def test_ma_chan(self):
        b = rong(); b[7][1] = MA; b[6][1] = TOT
        self.assertNotIn((5, 2), nuoc_gia(b, 7, 1))
        self.assertIn((8, 3), nuoc_gia(b, 7, 1))

    def test_tuong_chan_va_song(self):
        b = rong(); b[5][2] = VOI
        self.assertNotIn((3, 0), nuoc_gia(b, 5, 2))
        b[6][1] = TOT
        self.assertNotIn((7, 0), nuoc_gia(b, 5, 2))
        self.assertIn((7, 4), nuoc_gia(b, 5, 2))

    def test_phao(self):
        b = rong(); b[7][1] = PHAO; b[3][1] = -XE
        self.assertNotIn((3, 1), nuoc_gia(b, 7, 1))
        b[5][1] = TOT
        self.assertIn((3, 1), nuoc_gia(b, 7, 1))
        self.assertNotIn((4, 1), nuoc_gia(b, 7, 1))
        b[4][1] = -TOT
        self.assertNotIn((3, 1), nuoc_gia(b, 7, 1))

    def test_xe_khong_nhay(self):
        b = rong(); b[7][0] = XE; b[5][0] = TOT
        self.assertNotIn((4, 0), nuoc_gia(b, 7, 0))
        self.assertNotIn((5, 0), nuoc_gia(b, 7, 0))

    def test_tot(self):
        b = rong(); b[6][0] = TOT
        self.assertEqual(nuoc_gia(b, 6, 0), [(5, 0)])
        b[4][0] = TOT
        self.assertEqual(set(nuoc_gia(b, 4, 0)), {(3, 0), (4, 1)})
        b[5][8] = -TOT
        self.assertEqual(set(nuoc_gia(b, 5, 8)), {(6, 8), (5, 7)})

    def test_cung(self):
        b = rong(); b[9][3] = SI
        self.assertEqual(nuoc_gia(b, 9, 3), [(8, 4)])
        self.assertTrue(all(trong_cung(r, c, 1) for r, c in nuoc_gia(b, 9, 4)))

    def test_lo_mat_tuong(self):
        b = rong(); b[5][4] = XE
        self.assertNotIn((5, 4, 5, 3), hop_le(b, 1))
        b[5][4] = 0
        self.assertTrue(bi_chieu(b, 1))
        self.assertTrue(bi_chieu(b, -1))

    def test_phai_giai_chieu(self):
        b = rong(); b[8][0] = -XE; b[9][0] = XE
        b[8][4] = -XE
        self.assertTrue(bi_chieu(b, 1))
        self.assertNotIn((9, 0, 8, 0), hop_le(b, 1))

    def test_hoan_tac_an_quan(self):
        b = rong(); b[7][0] = XE; b[6][0] = -TOT
        cu = [row[:] for row in b]; m = (7, 0, 6, 0)
        an = thu_nuoc(b, m); hoan_tac(b, m, an)
        self.assertEqual(b, cu)

    def test_chieu_bi(self):
        b = [[0]*9 for _ in range(10)]
        b[0][4], b[9][4] = -TUONG, TUONG
        b[1][4], b[1][3], b[1][5] = XE, XE, XE
        self.assertTrue(bi_chieu(b, -1))
        self.assertEqual(hop_le(b, -1), [])

    def test_het_nuoc_khong_chieu(self):
        b = [[0]*9 for _ in range(10)]
        b[0][4], b[9][4], b[5][4] = -TUONG, TUONG, TOT
        b[2][3], b[2][5], b[1][0] = XE, XE, XE
        self.assertFalse(bi_chieu(b, -1))
        self.assertEqual(hop_le(b, -1), [])
        m, _ = MayTinh().tim(b, -1)
        self.assertIsNone(m)

    def test_ai_hop_le_va_khong_doi_ban(self):
        b = ban_dau(); cu = [row[:] for row in b]
        m, stats = MayTinh().tim(b, -1, 2, 8)
        self.assertIn(m, hop_le(b, -1))
        self.assertEqual(b, cu)
        self.assertEqual(stats['sau'], 2)

    def test_het_gio_khong_doi_ban(self):
        b = ban_dau(); cu = [row[:] for row in b]
        m, stats = MayTinh().tim(b, 1, 3, 0.03)
        self.assertIn(m, hop_le(b, 1))
        self.assertEqual(b, cu)

    def test_ai_chon_an_xe(self):
        b = rong(); b[7][0], b[6][0] = XE, -XE
        m, _ = MayTinh().tim(b, 1, 1, 3)
        self.assertEqual(m, (7, 0, 6, 0))


if __name__ == '__main__':
    unittest.main(verbosity=2)
