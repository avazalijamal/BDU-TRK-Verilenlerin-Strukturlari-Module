# Adam sinfi bütün digər siniflər üçün əsas sinifdir.
# Bu sinifdə ad, soyad və yaş məlumatları saxlanılır və əsas funksionallıqlar təmin edilir.
class Adam:
    def __init__(self, ad, soyad, yas):
        # Adamın adı, soyadı və yaşı.
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def tam_ad(self):
        # Adamın tam adını qaytarır: "Ad Soyad" formatında.
        return f"{self.ad} {self.soyad}"

    def __repr__(self):
        # Adam obyektinin string təsviri.
        return f"Adam(ad='{self.ad}', soyad='{self.soyad}', yas={self.yas})"
