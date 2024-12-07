# Universitet sinfi tələbələr, müəllimlər və kafedralar ilə əlaqəli məlumatları idarə edir.
from telebe import Telebe
from muellim import Muellim

class Universitet:
    def __init__(self, ad):
        # Universitetin adı və aid olduğu məlumatlar.
        self.ad = ad
        self.telebeler = []
        self.muellimler = []
        self.kafedralar = {}
        self.budce = 0  # Universitetin büdcəsi.
        # Sabit qrup siyahısı tuple olaraq saxlanılır.
        self.qruplar = ("İN01", "İN02", "FZ01", "FZ02")
        # Sabit ixtisas siyahısı tuple olaraq saxlanılır.
        self.ixtisaslar = ("İnformatika", "Fizika", "Kimya")
        # Vəzifələr tuple olaraq saxlanılır.
        self.vezifeler = ("Professor", "Dosent", "Baş müəllim")

    def telebe_elave_et(self, telebe: Telebe):
        # Universitetə yeni tələbə əlavə edir.
        self.telebeler.append(telebe)

    def muellim_elave_et(self, muellim: Muellim):
        # Universitetə yeni müəllim əlavə edir.
        self.muellimler.append(muellim)
        if muellim.kafedra not in self.kafedralar:
            self.kafedralar[muellim.kafedra] = []
        self.kafedralar[muellim.kafedra].append(muellim)

    def kafedra_siyahisi(self):
        # Universitetin kafedralarının siyahısını qaytarır.
        return list(self.kafedralar.keys())

    def butce_artir(self, mebleg):
        # Universitetin büdcəsini artırır.
        self.budce += mebleg

    def butce_azalt(self, mebleg):
        # Universitetin büdcəsini azaldır.
        if mebleg <= self.budce:
            self.budce -= mebleg
        else:
            print("Yetərli büdcə yoxdur!")

    def qrup_siyahisi(self):
        # Universitetin sabit qruplarını qaytarır.
        return self.qruplar

    def ixtisas_siyahisi(self):
        # Universitetin sabit ixtisaslarını qaytarır.
        return self.ixtisaslar

    def vezife_siyahisi(self):
        # Universitetdə mövcud olan sabit vəzifələri qaytarır.
        return self.vezifeler

    def melumatlari_goster(self):
        # Universitetin bütün məlumatlarını dictionary şəklində qaytarır.
        return {
            "Universitet": self.ad,
            "Tələbələr": [telebe.telebe_melumatlari() for telebe in self.telebeler],
            "Müəllimlər": [muellim.muellim_melumatlari() for muellim in self.muellimler],
            "Kafedralar": self.kafedra_siyahisi(),
            "Qruplar": self.qrup_siyahisi(),
            "İxtisaslar": self.ixtisas_siyahisi(),
            "Vəzifələr": self.vezife_siyahisi(),
            "Büdcə": self.budce
        }

    def __repr__(self):
        # Universitet obyektinin string təsviri.
        return f"Universitet(ad='{self.ad}', budce={self.budce})"

