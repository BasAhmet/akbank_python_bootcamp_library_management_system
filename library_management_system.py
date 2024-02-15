import time
class Library:
    
    def __init__(self):
        self.books_file_create() #Program çalıştığında books.txt dosyası yoksa oluşturur
    
    def books_file_create(self): #books.txt dosyası oluşturma fonksiyonu
        file = open("books.txt","a+",encoding="utf-8")
        file.close()

    def book_add(self): #kitap ekleme fonksiyonu
        print("Kitap ekleme ekranına hoşgeldiniz.")         #Kullanıcı karşılama metni
        book_name   = input("Lütfen Kitap Adını Giriniz    : ") #Kullanıcıdan kitap ismi alır
        book_author = input("Lütfen Yazar Adını Giriniz    : ") #Kullanıcıdan yazar adı alır
        book_year   = input("Lütfen Yayın Tarihini Giriniz : ") #Kullanıcıdan yayın tarihi alır
        book_page   = input("Lütfen Sayfa Sayısını Giriniz : ") #Kullanıcıdan sayfa sayısı alır

        
    #Kullanıcıdan onay alma ekranı başlangıcı

        #Kullanıcı hangi kitabı girdi bilgisi
        print(f"""
    Kitap Adı    : {book_name}
    Yazarı       : {book_author}
    Yayın yılı   : {book_year}
    Sayfa sayısı : {book_page}""")
        
        #Kullanıcıdan onay döngüsü
        while True:
            choice_add = input(f"'{book_name}' kitabı kaydedilecek onaylıyormusunuz e/h : ") #Onay alır

            if choice_add == "e":

                # e onayı alınca a modunda açıp kayıt yapıyoruz
                file = open("books.txt","a",encoding="utf-8")
                file.write(book_name + "," + book_author + "," + book_year + "," + book_page + "\n")
                file.close

                #Kullanıcıya eklendi bilgisi veriyor
                print(f"\n'{book_name}' kitabı kütüphaneye eklendi.")
                time.sleep(0.5)
                break

            elif choice_add == "h":

                # h yazıldığında kayıt ekranından çıkar
                print(f"\n'{book_name}' kitabı kütüphaneye kayıt edilmedi.")
                break

            else:
                print("Yanlış seçenek!!!")

    #Kullanıcıdan onay alma ekranı bitişi
        
    def books_list_print(self): #Kitap listeleme fonksiyonu
        file = open("books.txt","r",encoding="utf-8") # r modunda dosyayı açar
        books_list = file.readlines() #Bütün satırları okuyup listeye atar
        file.close()

        #liste boş ise kullanıcıya bilgi verir
        if len(books_list) == 0:
            print("Kütüphanede Kitap Yok.")
            time.sleep(0.5)

        count = 1 #Kitapları saymak için
        for i in books_list: #Liste içindeki kitapları tek tek döner
            book_attribute = i.split(",") #virgül ile ayrılmış olan kitap özelliklerini listeye atar
            time.sleep(0.2)

            #Kitapları ekrana basar
            print(f"""
**************   {count}. kitap  *********
Kitap adı      : {book_attribute[0]}
Kitabın yazarı : {book_attribute[1]}""")
            
            count += 1 #Kitap numarasını 1 arttırır

    def book_delete(self): #kitap silme fonksiyonu

        book_delete = input("Lütfen silmek istediğiniz kitabın adını giriniz : ") #Kullanıcıdan silmek istediği kitap adı alınır
        file = open("books.txt","r",encoding="utf-8") # r modunda dosya açılır
        books_list = file.readlines() # kitaplar listeye atılır
        file.close

        #silinecek kitabın indeksini bulduracak döngü
        index_no = 0 #İndeksi buradan alacağız
        for i in books_list: #Liste içindeki kitapları tek tek döner
            find_book = i.startswith(book_delete) #Kullanıcının girdiği kitapla başlıyormu True yada False döner

            if find_book:
                books_list.pop(index_no) # True ise indeks numarası ile silecek döngü bitecek
                break
            index_no += 1 # False ise indeks bir artar bir sonraki döngü için

        #Girilen kitabı sildiğimiz listeyi dosyaya tekrar yazarız
        file = open("books.txt","w",encoding="utf-8") # w modunda açıp dosya boşaltılır
        #Döngü ile liste elemanları dosyaya tekrar yazdırılır
        for i in books_list:
            file.write(i)
        file.close
        
        #Kullanıcıya silindi bilgisi
        print(f"'{book_delete}' kitabı silindi.")
        time.sleep(0.2)

class Menu():
        
        def __init__(self):
            self.menu()
        
        # Menü ekran
        def menu(self):
            #Kullanıcıya seçenekler sunulur
            while True:
                print("""
        ****** Menü *****
        1) Kitap Listesi
        2) Kitap Ekleme
        3) Kitap Silme
        q) Çıkış
        *****************
        """)
                choice = input("Lütfen Bir Seçenek (1-2-3-q) Giriniz : ") #Kullanıcıdan yapmak istediği işlem bilgisi alınır
                if choice == "1":
                    lib.books_list_print() #Kitap listelemesi yapar

                elif choice == "2":
                    lib.book_add() #Kitap eklemesi yapar

                elif choice == "3":
                    lib.book_delete() #Kitap siler

                elif choice == "q":
                    time.sleep(0.3)
                    print(f"Uygulamadan Çıkılıyor") # break ile uygulamadan çıkılır
                    time.sleep(0.3)
                    break

                else:
                    print("Lütfen geçerli bir seçenek giriniz") #Farklı girişte uyarı verir döngü başa döner
                    time.sleep(0.5)

# run ettiğimizde Library() ve Menu() class ları çalışır
if __name__ == '__main__':
    lib = Library()
    menu = Menu()
     



