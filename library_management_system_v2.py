import time # Terminalden takip etmek için time.sleep kullanılarak bazı işlemler yavaşlatıldı
class Library:
    
    def __init__(self):
        self.books_file_create() #Program çalıştığında books.txt dosyası yoksa oluşturur
    
    def books_file_create(self): #books.txt dosyası oluşturma fonksiyonu
        file = open("books.txt","a+",encoding="utf-8")
        file.close()

    def book_add(self,message): #kitap ekleme fonksiyonu
        print(message[0])         #Kullanıcı karşılama metni "Kitap ekleme ekranına hoşgeldiniz."
        book_name   = input(message[1]) #Kullanıcıdan kitap ismi alır
        book_author = input(message[2]) #Kullanıcıdan yazar adı alır
        book_year   = input(message[3]) #Kullanıcıdan yayın tarihi alır
        book_page   = input(message[4]) #Kullanıcıdan sayfa sayısı alır

        
    #Kullanıcıdan onay alma ekranı başlangıcı

        #Kullanıcı hangi kitabı girdi bilgisi
        print(f"""
    {message[5]}{book_name}
    {message[6]}{book_author}
    {message[7]}{book_year}
    {message[8]}{book_page}""")
        
        #Kullanıcıdan onay döngüsü
        while True:
            choice_add = input(f"'{book_name}'{message[9]}") #Onay alır

            if choice_add == message[21]: #Türkçe için "e" İngilizce için "y"

                # e onayı alınca a modunda açıp kayıt yapıyoruz
                file = open("books.txt","a",encoding="utf-8")
                file.write(book_name + "," + book_author + "," + book_year + "," + book_page + "\n")
                file.close

                #Kullanıcıya eklendi bilgisi veriyor
                print(f"\n'{book_name}'{message[10]}")
                time.sleep(0.5)
                break

            elif choice_add == message[22]: #Türkçe için "h" İngilizce için "n"

                # h yazıldığında kayıt ekranından çıkar kullanıcıya kayıt edilmedi bilgisi verir
                print(f"\n'{book_name}'{message[11]}")
                break

            else:
                print(message[12]) #"Yanlış seçenek!!!"

    #Kullanıcıdan onay alma ekranı bitişi
        
    def books_list_print(self,message): #Kitap listeleme fonksiyonu
        file = open("books.txt","r",encoding="utf-8") # r modunda dosyayı açar
        books_list = file.readlines() #Bütün satırları okuyup listeye atar
        file.close()

        #liste boş ise kullanıcıya bilgi verir
        if len(books_list) == 0:
            print(message[13]) # "Kütüphanede Kitap Yok."
            time.sleep(0.5)

        count = 1 #Kitapları saymak için
        for i in books_list: #Liste içindeki kitapları tek tek döner
            book_attribute = i.split(",") #virgül ile ayrılmış olan kitap özelliklerini listeye atar
            time.sleep(0.2)

            #Kitapları ekrana basar
            print(f"""
**************   {count}. {message[14]}  *********
{message[5]}{book_attribute[0]}
{message[6]}{book_attribute[1]}""")
            
            count += 1 #Kitap numarasını 1 arttırır

    def book_delete(self,message): #kitap silme fonksiyonu

        book_delete = input(message[15]) #Kullanıcıdan silmek istediği kitap adı alınır
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
        print(f"'{book_delete}'{message[16]}")
        time.sleep(0.2)

class Menu():
        
        def __init__(self):
            self.language_choice_menu()

        def language_choice_menu(self):
            
            t_mesaj = [
                "Kitap ekleme ekranına hoşgeldiniz."
                ,"Lütfen Kitap Adını Giriniz    : "
                ,"Lütfen Yazar Adını Giriniz    : "
                ,"Lütfen Yayın Tarihini Giriniz : "
                ,"Lütfen Sayfa Sayısını Giriniz : "
                ,"Kitap Adı    : "
                ,"Yazarı       : "
                ,"Yayın yılı   : "
                ,"Sayfa sayısı : "
                ," kitabı kaydedilecek onaylıyormusunuz e/h : "
                ," kitabı kütüphaneye eklendi."
                ," kitabı kütüphaneye kayıt edilmedi."
                ,"Yanlış seçenek!!!"
                ,"Kütüphanede Kitap Yok."
                ,"kitap"
                ,"Lütfen silmek istediğiniz kitabın adını giriniz : "
                ," kitabı silindi."
                ,"""
        ****** Menü *****
        1) Kitap Listesi
        2) Kitap Ekleme
        3) Kitap Silme
        q) Çıkış
        *****************
        """
        ,"Lütfen Bir Seçenek (1-2-3-q) Giriniz : "
        ,"Uygulamadan Çıkılıyor"
        ,"Lütfen geçerli bir seçenek giriniz"
        ,"e","h"]
            e_message = [
                "Welcome to the book adding screen."
                 ,"Please Enter Book Name: "
                 ,"Please Enter Author Name: "
                 ,"Please Enter Publication Date: "
                 ,"Please Enter the Number of Pages: "
                 ,"Book Name: "
                 ,"Author: "
                 ,"Publication year: "
                 ,"Number of pages : "
                 ," do you approve the book to be saved y/n : "
                 ," added the book to the library."
                 ," his book was not registered in the library."
                 ,"Wrong option!!!"
                 ,"No Books in the Library."
                 ,"book"
                 ,"Please enter the name of the book you want to delete: "
                 ," his book was deleted."
                 ,"""
        ****** Menu *****
        1) Book List
        2) Adding Books
        3) Deleting a Book
        q) Exit
        *****************
        """
        ,"Please Enter an Option (1-2-3-q): "
        ,"Quitting Application"
        ,"Please enter a valid option"
        ,"y","n"]
            while True:
                lang_choice = input("""
    Türkçe menü için 't'
    For English menu press 'e' : """)
            
                if lang_choice == "t":
                    self.message = t_mesaj
                    self.menu(self.message)
                    break
                elif lang_choice == "e":
                    self.message = e_message
                    self.menu(self.message)
                    break
        
        # Menü ekran
        def menu(self,message):
            #Kullanıcıya seçenekler sunulur
            while True:
                print(message[17])
                choice = input(message[18]) #Kullanıcıdan yapmak istediği işlem bilgisi alınır
                if choice == "1":
                    lib.books_list_print(self.message) #Kitap listelemesi yapar

                elif choice == "2":
                    lib.book_add(self.message) #Kitap eklemesi yapar

                elif choice == "3":
                    lib.book_delete(self.message) #Kitap siler

                elif choice == "q":
                    time.sleep(0.3)
                    print(message[19]) # break ile uygulamadan çıkılır
                    time.sleep(0.3)
                    break

                else:
                    print(message[20]) #Farklı girişte uyarı verir döngü başa döner
                    time.sleep(0.5)

# run ettiğimizde Library() ve Menu() class ları çalışır
if __name__ == '__main__':
    lib = Library()
    menu = Menu()
     



