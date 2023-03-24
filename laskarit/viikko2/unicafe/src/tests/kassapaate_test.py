import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteessa_oikea_maara_rahaa_ja_myytyja_tuotteita(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_raha_riittaa(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_raha_ei_riita(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200)))

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_raha_riittaa(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_raha_ei_riita(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200)))

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    

    def test_lataa_negatiivinen_maara_rahaa_kortille_kassan_raha_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_negatiivinen_maara_rahaa_kortin_saldo_ei_muuto(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.maksukortti.saldo, 1000)

        

    