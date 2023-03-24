import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa_on_riittavasti(self):
        kortti = Maksukortti(400)
        kortti.ota_rahaa(400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_riittavasti(self):
        kortti = Maksukortti(150)

        kortti.ota_rahaa(200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.50 euroa")

    def test_metodi_palauttaa_true_jos_rahat_riittivat(self):
        kortti = Maksukortti(400)
        
        self.assertEqual(kortti.ota_rahaa(200), True)