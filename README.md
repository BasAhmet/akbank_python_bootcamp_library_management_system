# Akbank Python Bootcamp Library Management System
Akbank Python Bootcamp kapsamı içinde yapmış olduğum kütüphane yönetim sistemi

# Versiyon
- **_library_management_system.py versiyonunda Türkçe menu var_**
- **_library_management_system_v2.py versiyonunda Türkçe ve İngilizce menü kondu_**

# Uygulamanın çalışması
```python
if __name__ == '__main__':
    lib = Library()
    menu = Menu()
```  
Kod bloğu ile uygulama başlatılıyor.

Oluşturulan "lib" nesnesi ile 
1. books.txt dosyası oluşuyor
2. Library() class ındaki fonksiyonlar çağrılıyor

Oluşturulan "menu" nesnesi "Menu()" class ının çaışması için

# Kullanıcı karşılama ekranı
Türkçe Menü
```python
****** Menü *****
1) Kitap Listesi
2) Kitap Ekleme
3) Kitap Silme
q) Çıkış
*****************
```
İngilizce Menü
```python
****** Menu *****
1) Book List
2) Adding Books
3) Deleting a Book
q) Exit
*****************
```
Kullanıcı buradan yapmak istediği işlemi seçerek uygulamayı kullanmakta.

# Versiyon 2 karşılama ekranı
```python
*** Dil Menüsü / Language Menu ***
Türkçe menü için 't'
For English menu press 'e'
**********************************
```
Kullanıcı bu menüden istediği dilde devam eder






