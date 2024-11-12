import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12.0)

    def test_ota_rahaa_ottaa_oikean_maaran_rahaa(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
    
    def test_ota_rahaa_ei_ota_rahaa_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_jos_riittaa_ja_false_jos_ei(self):
        self.assertEqual(self.maksukortti.ota_rahaa(800), True)
        self.assertEqual(self.maksukortti.ota_rahaa(300), False)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_tulostus_on_oikeassa_muodossa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
