import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_rahaa_euroina_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_edul_kateisella_nostaa_kassapaatteen_rahaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_syo_edul_kateisella_palauttaa_oikean_maaran_rahaa(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(takaisin, 60)

    def test_syo_edul_kateisella_jos_raha_ei_riita_kassa_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_edul_kateisella_ei_vahenna_rahaa_jos_raha_ei_riita(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(takaisin, 100)

    def test_syo_edul_kateisella_kasvattaa_myytyja_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukk_kateisella_nostaa_kassapaatteen_rahaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukk_kateisella_palauttaa_oikean_maaran_rahaa(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(takaisin, 100)

    def test_syo_maukk_kateisella_jos_raha_ei_riita_kassa_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukk_kateisella_ei_vahenna_rahaa_jos_raha_ei_riita(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(takaisin, 100)

    def test_syo_maukk_kateisella_kasvattaa_myytyja_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edul_kortilla_palauttaa_true_muuten_false(self):
        maksukortti = Maksukortti(240)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_syo_edul_kortilla_kasvattaa_myytyja_oikein(self):
        maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukk_kortilla_palauttaa_true_muuten_false(self):
        maksukortti = Maksukortti(400)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_syo_maukk_kortilla_kasvattaa_myytyja_oikein(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_lataa_kortille_rahaa_lisaa_kassaan_oikean_maaran(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)

    def test_negatiivinen_kateismaara_ei_lisaa_kassaan_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(-240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        self.kassapaate.syo_maukkaasti_kateisella(-400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)