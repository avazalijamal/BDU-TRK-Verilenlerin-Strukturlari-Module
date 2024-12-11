# BDU-TRK-Verilenlerin-Strukturlari-Module

BDU TRK Verilenlerin Strukturlari Module for Python

---

# **Tələbə İdarəetmə Sistemi**

Bu layihə **Tələbə İdarəetmə Sistemi**dir və Python proqramlaşdırma dilində yazılmışdır. Sistem, tələbələr, müəllimlər və universitetlərlə bağlı məlumatların idarə edilməsini təmin edir. Layihə bir neçə moduldan ibarətdir və hər modulun öz spesifik funksionallıqlarını ehtiva edir.

---

## **Layihə Strukturu**

Bu layihə aşağıdakı modullardan ibarətdir:

- **`adam.py`**: Əsas baza sinfi. Digər siniflər bu sinfi miras alır.
- **`telebe.py`**: Tələbələrin məlumatlarını idarə edən sinf.
- **`muellim.py`**: Müəllimlərin məlumatlarını idarə edən sinf.
- **`universitet.py`**: Universitet məlumatlarını idarə edən sinf.
- **`main.py`**: Bütün modulları birləşdirən idarəetmə və interaktiv menyu.

---

## **Funksionallıqlar**

### **1. Adam Sinfi (`adam.py`)**
- **Atributlar:**
  - `ad`, `soyad`, `yas`: Şəxsi məlumatları saxlayır.
- **Metodlar:**
  - `tam_ad()`: Adamın tam adını qaytarır.
  - `__repr__()`: Adam obyektinin təsvirini qaytarır.

---

### **2. Tələbə Sinfi (`telebe.py`)**
- **Atributlar:**
  - `ixtisas`, `qrup`, `fennler`: Tələbənin oxuduğu ixtisas, qrup və fənnlər.
  - `qiymetler`: Tələbənin qiymətləri (`dictionary` formatında saxlanılır).
  - `qiymet_kateqoriyalari`: Qiymət kateqoriyaları (`tuple` formatında).
- **Metodlar:**
  - `fenn_elave_et()`: Tələbəyə yeni fənn əlavə edir.
  - `qiymet_elave_et()`: Tələbənin qiymətini qeyd edir.
  - `ortalama_qiymet()`: Tələbənin orta qiymətini qaytarır.
  - `telebe_melumatlari()`: Tələbənin bütün məlumatlarını qaytarır.

---

### **3. Müəllim Sinfi (`muellim.py`)**
- **Atributlar:**
  - `vezife`, `kafedra`, `fennler`: Müəllimin vəzifəsi, kafedrası və tədris etdiyi fənnlər.
  - `telebeler`: Müəllimin tədris etdiyi tələbələrin siyahısı.
- **Metodlar:**
  - `fenn_siyahisi()`: Tədris etdiyi fənnləri qaytarır.
  - `telebe_elave_et()`: Müəllimə tələbə təyin edir.
  - `telebeleri_goster()`: Tədris etdiyi tələbələrin siyahısını qaytarır.
  - `muellim_melumatlari()`: Müəllimin bütün məlumatlarını qaytarır.

---

### **4. Universitet Sinfi (`universitet.py`)**
- **Atributlar:**
  - `telebeler`, `muellimler`, `kafedralar`: Universitetdə tələbələr, müəllimlər və kafedralar.
  - `qruplar`, `ixtisaslar`, `vezifeler`: Sabit qruplar, ixtisaslar və vəzifələr (`tuple` formatında).
  - `budce`: Universitetin büdcəsi.
- **Metodlar:**
  - `telebe_elave_et()`: Universitetə tələbə əlavə edir.
  - `muellim_elave_et()`: Universitetə müəllim əlavə edir.
  - `butce_artir()`, `butce_azalt()`: Büdcəni idarə edir.
  - `melumatlari_goster()`: Universitetin bütün məlumatlarını qaytarır.
  - `qrup_siyahisi()`, `ixtisas_siyahisi()`, `vezife_siyahisi()`: Universitetin sabit məlumatlarını qaytarır.

---

### **5. Əsas Menyu və Funksionallıq (`main.py`)**

Menyu istifadəçiyə interaktiv idarəetmə imkanı yaradır:
- Universitet əlavə etmək, silmək və siyahısını göstərmək.
- Tələbə və müəllim əlavə etmək, silmək və siyahısını göstərmək.
- Universitetin büdcəsini artırmaq və azaltmaq.
- Universitet məlumatlarını JSON faylına yazmaq.
- Qiymət kateqoriyalarını göstərmək.

---

## **Necə İşə Salmaq Olar**

### **1. Tələblər**
Bu sistem üçün yalnız Python tələb olunur. Dəstəklənən Python versiyası:
- **Python 3.6 və ya daha yuxarı**

### **2. Layihəni Yükləyin**

#### Git vasitəsilə:
1. Terminalı açın.
2. Layihəni klonlayın:
   ```bash
   git clone https://github.com/istifadeci-adiniz/telebe-idareetme-sistemi.git
   ```
3. Layihə qovluğuna keçin:
   ```bash
   cd telebe-idareetme-sistemi
   ```

#### ZIP Faylı vasitəsilə:
1. ZIP faylını GitHub-dan yükləyin.
2. Faylları bir qovluğa çıxarın.
3. Terminalda həmin qovluğa keçin:
   ```bash
   cd /sizin/qovluq/yolu
   ```

---

### **3. Layihəni İşə Salın**

#### Addım 1: Terminalı Açın
Layihə fayllarınızın olduğu qovluğa keçin:
```bash
cd telebe-idareetme-sistemi
```

#### Addım 2: `main.py` Faylını İşə Salın
Terminalda aşağıdakı əmrlərdən birini yazın:

- **Windows** üçün:
  ```bash
  python main.py
  ```

- **MacOS/Linux** üçün:
  ```bash
  python3 main.py
  ```

---

### **4. Menyu İstifadəsi**

Proqram başladıqda əsas menyu görünəcək. Menyudan lazımi funksionallığı seçə bilərsiniz.

#### Məsələn:
```text
==== Tələbə İdarəetmə Sistemi ====
1. Universitet əlavə et
2. Universitetləri göstər
3. Universitet sil
4. Tələbə əlavə et
5. Tələbələri göstər
6. Tələbəni sil
7. Müəllim əlavə et
...
Seçiminizi daxil edin: 1
```

Hər bir əməliyyatdan sonra menyuya geri dönəcəksiniz.

---

## **Fayl Strukturu**

Layihə aşağıdakı fayl strukturuna malikdir:
```plaintext
telebe-idareetme-sistemi/
│
├── adam.py          # Adam sinfi
├── telebe.py        # Tələbə sinfi
├── muellim.py       # Müəllim sinfi
├── universitet.py   # Universitet sinfi
├── main.py          # Əsas proqram
├── data.json        # JSON formatında məlumatların saxlanması
```

---

## **Məlumatların JSON Faylına Yazılması**

Proqramdan çıxarkən bütün məlumatlar `data.json` adlı fayla yazılacaq. Bu fayl gələcəkdə proqram işə salındıqda oxunub məlumatlar bərpa olunacaq.

#### **JSON Faylının Formatı:**
```json
{
  "Universitet": "Bakı Dövlət Universiteti",
  "Tələbələr": [
      {
          "Ad": "Aysel",
          "Soyad": "Məmmədova",
          "Yaş": 20,
          "İxtisas": "İnformatika",
          "Qrup": "İN01",
          "Fənnlər": ["Riyaziyyat", "Fizika"],
          "Qiymətlər": {"Riyaziyyat": 90, "Fizika": 85},
          "Ortalama Qiymət": 87.5
      }
  ],
  "Müəllimlər": [
      {
          "Ad": "Elçin",
          "Soyad": "Quliyev",
          "Yaş": 45,
          "Vəzifə": "Professor",
          "Kafedra": "Riyaziyyat",
          "Fənnlər": ["Cəbr", "Riyazi Analiz"],
          "Tədris Etdiyi Tələbələr": ["Aysel Məmmədova"]
      }
  ],
  "Kafedralar": ["Riyaziyyat"],
  "Qruplar": ["İN01", "İN02", "FZ01", "FZ02"],
  "İxtisaslar": ["İnformatika", "Fizika", "Kimya"],
  "Vəzifələr": ["Professor", "Dosent", "Baş müəllim"],
  "Büdcə": 50000
}
```

---

## **Problem Yaranarsa**

### **Python Versiyası**
- Python versiyanızın uyğun olduğundan əmin olun:
  ```bash
  python --version
  ```

### **Doğru Fayl Yolu**
- Terminalda düzgün qovluqda olduğunuzu yoxlayın:
  ```bash
  pwd  # Linux/MacOS
  cd   # Windows
  ```

### **Əmrin Doğruluğu**
- Proqramı çalışdırmaq üçün `python main.py` əmrini istifadə etdiyinizdən əmin olun.

---

## **Mümkün Gələcək Təkmilləşdirmələr**

- **Verilənlər bazası dəstəyi:** SQLite və ya PostgreSQL istifadə edilə bilər.
- **Çoxdilli dəstək:** İngilis, Azərbaycan və digər dillər üçün.
- **GUI əlavə olunması:** Layihəyə qrafik interfeys əlavə etməklə istifadənin asanlaşdırılması.
- **Təhlükəsizlik yoxlamaları:** Məlumatların doğruluğunu və tamlığını təmin etmək.

---

Bu təlimatlar layihəni işlətmək üçün kifayət edəcəkdir. Əlavə suallarınız varsa, mənimlə əlaqə saxlamaqdan çəkinməyin! 😊

