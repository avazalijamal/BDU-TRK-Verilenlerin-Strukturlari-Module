# Tələbə sinfi Adam sinfindən miras alır və əlavə olaraq ixtisas, qrup və qiymət məlumatlarını idarə edir.
from adam import Adam

class Telebe(Adam):
    def __init__(self, ad, soyad, yas, ixtisas, qrup, fennler=None):
        super().__init__(ad, soyad, yas)
        # Tələbənin ixtisası və qrupu.
        self.ixtisas = ixtisas
        self.qrup = qrup
        # Tələbənin oxuduğu fənnlər (set olaraq saxlanılır).
        self.fennler = fennler if fennler else set()
        # Tələbənin qiymətləri (fənn adı -> qiymət cütləri şəklində saxlanılır).
        self.qiymetler = {}
        # Qiymət kateqoriyaları tuple olaraq saxlanılır.
        self.qiymet_kateqoriyalari = ("Əla", "Yaxşı", "Kafi", "Qeyri-Kafi")

    def fenn_elave_et(self, fenn):
        # Tələbəyə yeni fənn əlavə edir.
        self.fennler.add(fenn)

    def qiymet_elave_et(self, fenn, qiymet):
        # Tələbənin bir fənn üçün qiymətini əlavə edir.
        if fenn in self.fennler:
            self.qiymetler[fenn] = qiymet
        else:
            print(f"{fenn} tələbənin fənnləri arasında deyil!")

    def ortalama_qiymet(self):
        # Tələbənin bütün qiymətlərinin ortalamasını qaytarır.
        if self.qiymetler:
            return sum(self.qiymetler.values()) / len(self.qiymetler)
        return 0

    def qiymet_kateqoriyalari_goster(self):
        # Qiymət kateqoriyalarını qaytarır.
        return self.qiymet_kateqoriyalari

    def telebe_melumatlari(self):
        # Tələbənin bütün məlumatlarını dictionary şəklində qaytarır.
        return {
            "Ad": self.ad,
            "Soyad": self.soyad,
            "Yaş": self.yas,
            "İxtisas": self.ixtisas,
            "Qrup": self.qrup,
            "Fənnlər": list(self.fennler),
            "Qiymətlər": self.qiymetler,
            "Ortalama Qiymət": self.ortalama_qiymet(),
            "Qiymət Kateqoriyaları": self.qiymet_kateqoriyalari_goster()
        }

    def __repr__(self):
        # Tələbə obyektinin string təsviri.
        return f"Telebe(ad='{self.ad}', soyad='{self.soyad}', yas={self.yas}, ixtisas='{self.ixtisas}', qrup='{self.qrup}')"
