import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_kortin_saldo_alussa_oikein(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(str(maksukortti),"Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvatta_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 11.00 euroa")
    
    def test_rahan_ottaminen_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 9.00 euroa")
    
    def test_rahan_ottaminen_liika_saldo_ei_vahenee(self):
        self.maksukortti.ota_rahaa(100000)
        
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_ottaminen_liika_paulauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100000),False)
    
    def test_rahan_ottaminen_liika_paulauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100),True)
