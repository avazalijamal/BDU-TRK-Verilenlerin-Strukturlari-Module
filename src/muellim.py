# Müəllim sinfi Adam sinfindən miras alır və əlavə olaraq vəzifə, kafedra və tələbə məlumatlarını idarə edir.
from adam import Adam

class Muellim(Adam):
    def __init__(self, ad, soyad, yas, vezife, kafedra, fennler=None):
        super().__init__(ad, soyad, yas)
        # Müəllimin vəzifəsi və aid olduğu kafedra.
        self.vezife = vezife
        self.kafedra = kafedra
        # Müəllimin tədris etdiyi fənnlər tuple olaraq saxlanılır.
        self.fennler = tuple(fennler) if fennler else ()
        # Müəllimin tədris etdiyi tələbələr (siyahı şəklində saxlanılır).
        self.telebeler = []

    def fenn_siyahisi(self):
        # Müəllimin tədris etdiyi fənnlərin siyahısını qaytarır.
        return self.fennler

    def telebe_elave_et(self, telebe):
        # Müəllimə tələbə təyin edir.
        if telebe not in self.telebeler:
            self.telebeler.append(telebe)

    def telebeleri_goster(self):
        # Müəllimin tədris etdiyi tələbələrin tam adlarını qaytarır.
        return [telebe.tam_ad() for telebe in self.telebeler]

    def muellim_melumatlari(self):
        # Müəllimin bütün məlumatlarını dictionary şəklində qaytarır.
        return {
            "Ad": self.ad,
            "Soyad": self.soyad,
            "Yaş": self.yas,
            "Vəzifə": self.vezife,
            "Kafedra": self.kafedra,
            "Fənnlər": self.fenn_siyahisi(),
            "Tədris Etdiyi Tələbələr": self.telebeleri_goster()
        }

    def __repr__(self):
        # Müəllim obyektinin string təsviri.
        return f"Muellim(ad='{self.ad}', soyad='{self.soyad}', yas={self.yas}, vezife='{self.vezife}', kafedra='{self.kafedra}')"
