import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaaten_luonti_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    def test_kassapaaten_luonti_oikea_edumaara(self):
        self.assertEqual(self.kassapaate.edulliset,0)
    def test_kassapaaten_luonti_oikea_maukmaara(self):
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_syo_maukkaasti_kateisella_oikea_vahihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)
    	
    def test_syo_maukkaasti_kateisella_oikea_vahihtorahaa_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(150),150)	
    	
    def test_syo_maukkaasti_kateisella_myyntimaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_maukkaasti_kateisella_rahaat_ei_riita_myyntimaara_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat,0)
    	
    def test_syo_maukkaasti_kateisella_kassassa_rahaa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
    	
    def test_syo_maukkaasti_kateisella_kassassa_rahaa_ei_kasvaa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    
    
    
    
    def test_syo_edullisesti_kateisella_oikea_vahihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
    	
    def test_syo_edullisesti_kateisella_oikea_vahihtorahaa_jos_rahat_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(150),150)
    	
    	
    def test_syo_edullisesti_kateisella_myyntimaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(450)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_syo_edullisesti_kateisella_rahaat_ei_riita_myyntimaara_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset,0)
    	
    def test_syo_edullisesti_kateisella_kassassa_rahaa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
    	
    def test_syo_edullisesti_kateisella_kassassa_rahaa_ei_kasvaa_jos_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
        
        
        
        
        
        
        
        
        
    def test_syo_maukkaasti_kortilla_palautetaan_true(self):
        kortti = Maksukortti(450)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),True)
    	
    def test_syo_maukkaasti_kortilla_palautetaan_false_jos_rahat_ei_riita(self):
        kortti = Maksukortti(150)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
    	
    	
    def test_syo_maukkaasti_kortilla_myyntimaara_kasvaa(self):
        kortti = Maksukortti(450)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_maukkaasti_kortilla_rahaat_ei_riita_myyntimaara_ei_kasvaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,0)
    	
    def test_syo_maukkaasti_kortilla_kortti_saldo_vahenee(self):
        kortti = Maksukortti(450)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti),"Kortilla on rahaa 0.50 euroa")
    	
    def test_syo_maukkaasti_kortilla__kortti_saldo_ei_vahenee_rahat_ei_riita(self):
        kortti = Maksukortti(40)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti),"Kortilla on rahaa 0.40 euroa")
    
    
    
    
    
    def test_syo_edullisesti_kortilla_palautetaan_true(self):
        kortti = Maksukortti(450)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),True)
    	
    def test_syo_edullisesti_kortilla_palautetaan_false_jos_rahat_ei_riita(self):
        kortti = Maksukortti(150)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
    	
    	
    def test_syo_edullisesti_kortilla_myyntimaara_kasvaa(self):
        kortti = Maksukortti(450)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_syo_edullisesti_kortilla_rahaat_ei_riita_myyntimaara_ei_kasvaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset,0)
    	
    def test_syo_edullisesti_kortilla_kortti_saldo_vahenee(self):
        kortti = Maksukortti(290)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti),"Kortilla on rahaa 0.50 euroa")
    	
    def test_syo_edullisesti_kortilla__kortti_saldo_ei_vahenee_rahat_ei_riita(self):
        kortti = Maksukortti(40)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti),"Kortilla on rahaa 0.40 euroa")
        
    def test_lataa_rahaa_kortille_kortin_lataaminen(self):
        kortti= Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(str(kortti),"Kortilla on rahaa 6.00 euroa")
    def test_lataa_rahaa_kortille_kassan_lataaminen(self):
        kortti= Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100100)
        
    def test_lataa_rahaa_kortille_kortin_lataaminen_summa_vaarin(self):
        kortti= Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti,-1)
        self.assertEqual(str(kortti),"Kortilla on rahaa 5.00 euroa")
    def test_lataa_rahaa_kortille_kassan_lataaminen_summa_vaarin(self):
        kortti= Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti,-1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
