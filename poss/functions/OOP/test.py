
import unittest
from drugiPokusaj import cudo1, cudo2
from drugiPokusaj import cudo3, OdabirNajmocnijeg
 
class TestPrvoCudo(unittest.TestCase):
   
    def test_provjeriIme(self):
        i = cudo1().dajIme()
        self.assertAlmostEqual(i, "cudak1")

    def test_provjeriZdravlje(self):
        z = cudo1().dajZdravlje()
        self.assertAlmostEqual(z, 100)

    def test_provjeriMocUdara(self):
        m = cudo1().dajMocUdara()
        self.assertAlmostEqual(m, 12)

class TestTreceCudo(unittest.TestCase):
   
    def test_provjeriNjegovoZdravlje(self):
        z3 = cudo3().dajZdravlje()
        self.assertAlmostEqual(z3, 160)

    def test_provjeriMetoduZaStetu(self):
        steta = cudo3().dajStetu(cudo1().dajMocUdara())
        self.assertAlmostEqual(steta, 148)


class IntegrationPrvi(unittest.TestCase):
   
    def test_dajMiSvePodatkeDrugogCudovista(self):
        pod = cudo2().dajMiPodatke()
        self.assertAlmostEqual(pod, ('cudak2', 18, 100))

    def test_kojeCudovisteJeNajzdravije(self):
        zadnjaKlasa = OdabirNajmocnijeg().dajMiCudovisteSaNajviseEnergije()
        self.assertAlmostEqual(zadnjaKlasa, "trece je najzdravije 160")

if __name__ == '__main__':
   
    unittest.main()