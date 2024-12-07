import json
from telebe import Telebe
from muellim import Muellim
from universitet import Universitet

# Universitetlərin saxlanılması üçün siyahı.
universitetler = []

def menu_goster():
    # Əsas menyu funksiyası.
    print("""
    ==== Tələbə İdarəetmə Sistemi ====
    1. Universitet əlavə et
    2. Universitetləri göstər
    3. Universitet sil
    4. Tələbə əlavə et
    5. Tələbələri göstər
    6. Tələbəni sil
    7. Müəllim əlavə et
    8. Müəllimləri göstər
    9. Müəllimi sil
    10. Universitet büdcəsini artır
    11. Universitet büdcəsini azalt
    12. Universitet məlumatlarını JSON-a yaz
    13. Tələbəyə qiymət əlavə et
    14. Universitetin qruplarını göstər
    15. Universitetin ixtisaslarını göstər
    16. Universitetin vəzifələrini göstər
    17. Çıxış
    """)

def universitet_elave_et():
    # Yeni universitet əlavə edir.
    ad = input("Universitetin adı: ")
    yeni_universitet = Universitet(ad)
    universitetler.append(yeni_universitet)
    print(f"{ad} universitetlərə əlavə olundu.")

def universitetleri_goster():
    # Universitetlərin siyahısını göstərir.
    if not universitetler:
        print("Heç bir universitet əlavə edilməyib.")
    else:
        for idx, uni in enumerate(universitetler, start=1):
            print(f"{idx}. {uni.ad}")

def universitet_sil():
    # Universiteti silir və onun tələbələrini və müəllimlərini təmizləyir.
    universitetleri_goster()
    idx = int(input("Silinəcək universitetin nömrəsini daxil edin: ")) - 1
    if 0 <= idx < len(universitetler):
        silinen = universitetler.pop(idx)
        print(f"{silinen.ad} universiteti və onunla əlaqəli məlumatlar silindi.")
    else:
        print("Yanlış seçim.")

def telebe_elave_et():
    # Universitetə tələbə əlavə edir.
    universitetleri_goster()
    idx = int(input("Tələbə əlavə etmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        ad = input("Tələbənin adı: ")
        soyad = input("Tələbənin soyadı: ")
        yas = int(input("Tələbənin yaşı: "))
        ixtisas = input("Tələbənin ixtisası: ")
        qrup = input("Tələbənin qrupu: ")
        fennler = input("Fənnlər (vergüllə ayırın): ").split(',')
        telebe = Telebe(ad, soyad, yas, ixtisas, qrup, set(fennler))
        uni.telebe_elave_et(telebe)
        print(f"{telebe.tam_ad()} tələbələrə əlavə olundu.")
    else:
        print("Yanlış seçim.")

def telebeleri_goster():
    # Universitetin tələbələrini göstərir.
    universitetleri_goster()
    idx = int(input("Tələbələri göstərmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        if not uni.telebeler:
            print("Bu universitetdə tələbə yoxdur.")
        else:
            for tidx, telebe in enumerate(uni.telebeler, start=1):
                print(f"{tidx}. {telebe.telebe_melumatlari()}")
    else:
        print("Yanlış seçim.")

def telebe_sil():
    # Universitetdən tələbəni silir.
    universitetleri_goster()
    idx = int(input("Tələbəni silmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        telebeleri_goster()
        tidx = int(input("Silinəcək tələbənin nömrəsini daxil edin: ")) - 1
        if 0 <= tidx < len(uni.telebeler):
            silinen = uni.telebeler.pop(tidx)
            print(f"{silinen.tam_ad()} silindi.")
        else:
            print("Yanlış seçim.")
    else:
        print("Yanlış seçim.")

def muellim_elave_et():
    # Universitetə müəllim əlavə edir.
    universitetleri_goster()
    idx = int(input("Müəllim əlavə etmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        ad = input("Müəllimin adı: ")
        soyad = input("Müəllimin soyadı: ")
        yas = int(input("Müəllimin yaşı: "))
        vezife = input("Müəllimin vəzifəsi: ")
        kafedra = input("Müəllimin kafedrası: ")
        fennler = input("Fənnlər (vergüllə ayırın): ").split(',')
        muellim = Muellim(ad, soyad, yas, vezife, kafedra, fennler)
        uni.muellim_elave_et(muellim)
        print(f"{muellim.tam_ad()} müəllimlərə əlavə olundu.")
    else:
        print("Yanlış seçim.")

def muellimleri_goster():
    # Universitetin müəllimlərini göstərir.
    universitetleri_goster()
    idx = int(input("Müəllimləri göstərmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        if not uni.muellimler:
            print("Bu universitetdə müəllim yoxdur.")
        else:
            for midx, muellim in enumerate(uni.muellimler, start=1):
                print(f"{midx}. {muellim.muellim_melumatlari()}")
    else:
        print("Yanlış seçim.")

def muellim_sil():
    # Universitetdən müəllimi silir.
    universitetleri_goster()
    idx = int(input("Müəllimi silmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        muellimleri_goster()
        midx = int(input("Silinəcək müəllimin nömrəsini daxil edin: ")) - 1
        if 0 <= midx < len(uni.muellimler):
            silinen = uni.muellimler.pop(midx)
            print(f"{silinen.tam_ad()} silindi.")
        else:
            print("Yanlış seçim.")
    else:
        print("Yanlış seçim.")

def universitet_budce_artir():
    # Universitet büdcəsini artırır.
    universitetleri_goster()
    idx = int(input("Büdcəni artırmaq üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        mebleg = int(input("Artırılacaq məbləğ: "))
        universitetler[idx].butce_artir(mebleg)
        print(f"{universitetler[idx].ad} universitetinin büdcəsi artırıldı.")
    else:
        print("Yanlış seçim.")

def universitet_budce_azalt():
    # Universitet büdcəsini azaldır.
    universitetleri_goster()
    idx = int(input("Büdcəni azaltmaq üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        mebleg = int(input("Azaldılacaq məbləğ: "))
        universitetler[idx].butce_azalt(mebleg)
        print(f"{universitetler[idx].ad} universitetinin büdcəsi azaldıldı.")
    else:
        print("Yanlış seçim.")

def universitet_qruplari_goster():
    # Universitetdəki sabit qrupları göstərir.
    universitetleri_goster()
    idx = int(input("Qrupları göstərmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        print("Qruplar:", universitetler[idx].qrup_siyahisi())
    else:
        print("Yanlış seçim.")

def universitet_ixtisaslari_goster():
    # Universitetdəki sabit ixtisasları göstərir.
    universitetleri_goster()
    idx = int(input("İxtisasları göstərmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        print("İxtisaslar:", universitetler[idx].ixtisas_siyahisi())
    else:
        print("Yanlış seçim.")

def universitet_vezifeleri_goster():
    # Universitetdəki sabit vəzifələri göstərir.
    universitetleri_goster()
    idx = int(input("Vəzifələri göstərmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        print("Vəzifələr:", universitetler[idx].vezife_siyahisi())
    else:
        print("Yanlış seçim.")

def universitet_melumatlarini_yaz():
    # Bütün universitet məlumatlarını JSON faylına yazır.
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump([uni.melumatlari_goster() for uni in universitetler], file, ensure_ascii=False, indent=4)
    print("Məlumatlar JSON-a yazıldı.")

def telebe_qiymet_elave_et():
    # Tələbəyə qiymət əlavə edir.
    universitetleri_goster()
    idx = int(input("Qiymət əlavə etmək üçün universitetin nömrəsini seçin: ")) - 1
    if 0 <= idx < len(universitetler):
        uni = universitetler[idx]
        telebeleri_goster()
        tidx = int(input("Qiymət əlavə etmək üçün tələbənin nömrəsini seçin: ")) - 1
        if 0 <= tidx < len(uni.telebeler):
            telebe = uni.telebeler[tidx]
            fenn = input("Fənn adı: ")
            qiymet = int(input("Qiymət: "))
            telebe.qiymet_elave_et(fenn, qiymet)
            print(f"{telebe.tam_ad()} tələbəsinə {fenn} fənnindən {qiymet} qiyməti əlavə edildi.")
        else:
            print("Yanlış seçim.")
    else:
        print("Yanlış seçim.")

def main():
    # Əsas idarəetmə funksiyası.
    while True:
        menu_goster()
        secim = input("Seçiminizi daxil edin: ")
        if secim == "1":
            universitet_elave_et()
        elif secim == "2":
            universitetleri_goster()
        elif secim == "3":
            universitet_sil()
        elif secim == "4":
            telebe_elave_et()
        elif secim == "5":
            telebeleri_goster()
        elif secim == "6":
            telebe_sil()
        elif secim == "7":
            muellim_elave_et()
        elif secim == "8":
            muellimleri_goster()
        elif secim == "9":
            muellim_sil()
        elif secim == "10":
            universitet_budce_artir()
        elif secim == "11":
            universitet_budce_azalt()
        elif secim == "12":
            universitet_melumatlarini_yaz()
        elif secim == "13":
            telebe_qiymet_elave_et()
        elif secim == "14":
            universitet_qruplari_goster()
        elif secim == "15":
            universitet_ixtisaslari_goster()
        elif secim == "16":
            universitet_vezifeleri_goster()
        elif secim == "17":
            print("Sistemdən çıxılır.")
            break
        else:
            print("Yanlış seçim. Yenidən cəhd edin.")

if __name__ == "__main__":
    main()

