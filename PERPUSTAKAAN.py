import os
import math
import pwinput

admin = {"Username" : ["ADMIN"],
        "Password" : ["111"]}
pengunjung = {"Username" : ["MUTI", "ALLYYA", "RIZANI"],
        "Password" : ["001", "030", "039"]}

def registrasi_pengunjung():
    while True:
        try:
            Username = input("Masukkan Username Baru : ")
            if len(Username) > 15:
                os.system("cls")
                print("Maksimal Memasukkan 15 Karakter Pada Username!")
            else:
                huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                user = ""
                for i in Username:
                    if i in huruf:
                        user = user + i
                    else:
                        user = ""
                        os.system("cls")
                        print("Username dan Password Hanya Dapat Berupa Huruf Kapital dan Angka")
                        break
                if user != "":
                    user = user
                    if Username in pengunjung.get("Username"):
                        os.system("cls")
                        print("Username Telah Digunakan")
                    else:
                        Password = pwinput.pwinput("Masukkan Password Baru : ")
                        if len(Password) > 15:
                            os.system("cls")
                            print("Maksimal Memasukkan 15 Karakter Pada Password!")
                        else:
                            pw = ""
                            for i in Password:
                                if i in huruf:
                                    pw = pw + i
                                else:
                                    pw = ""
                                    os.system("cls")
                                    print("Username dan Password Hanya Dapat Berupa Huruf Kapital dan Angka")
                                    break
                            if pw != "":
                                pw = pw
                                pengunjung.get("Username").append(Username)
                                pengunjung.get("Password").append(Password)
                                break
        except KeyboardInterrupt:
            os.system("cls")
            print("Masukkan Inputan Yang Benar!")

def login_admin():
    while True:
        try:
            Username = input("Masukkan Username : ")
            Password = pwinput.pwinput("Masukkan Password : ")
            try:
                login = admin.get("Username").index(Username)
                if Username == admin.get("Username")[login] and Password == admin.get("Password")[login]:
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("Password Anda Salah! ")
            except ValueError:
                os.system("cls")
                print("Username Anda Salah! ")
        except KeyboardInterrupt:
            os.system("cls")
            print("Masukkan Inputan Yang Benar!")

def login_pangunjung():
    while True:
        try:
            Username = input("Masukkan Username : ")
            Password = pwinput.pwinput("Masukkan Password : ")
            try:
                login = pengunjung.get("Username").index(Username)
                if Username == pengunjung.get("Username")[login] and Password == pengunjung.get("Password")[login]:
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("Password Anda Salah! ")
            except ValueError:
                os.system("cls")
                print("Username Anda Salah! ")
        except KeyboardInterrupt:
            os.system("cls")
            print("Masukkan Inputan Yang Benar!")

 class NodeBuku:
    def __init__(self, Judul, Pengarang, Penerbit, Genre, Tahun, Status):
        self.Judul = Judul
        self.Pengarang = Pengarang
        self.Penerbit = Penerbit
        self.Genre = Genre
        self.Tahun = Tahun
        self.Status = Status
        self.next = None    
        
class LinkedBuku:
    def __init__(self):
        self.head = None
        self.count = 0
        self.riwayatPinjam = []
        self.datarBacaan = []

    def getData(self, index):
        if index < 0 or index > self.count-1:
            os.system("cls")
            print(">>> Data Tersebut Tidak Tersedia! <<<")
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            LinkedBuku.printData(nodeTampil)

    def getStatus(self, index):
        if index < 0 or index > self.count-1:
            os.system("cls")
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            return nodeTampil.Status
    
    def ubahStatus(self, index):
        nodeUpdate = self.head
        for i in range(index):
            nodeUpdate = nodeUpdate.next
        nodeUpdate.Status = "Out Of Stock"

       def insertData(self, Judul, Pengarang, Penerbit, Genre, Tahun, Status):
        if self.head is None:
            self.head = NodeBuku(Judul, Pengarang, Penerbit, Genre, Tahun, Status)
            self.count += 1
        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = NodeBuku(Judul, Pengarang, Penerbit, Genre, Tahun, Status)
            self.count += 1
    
    def newData(self, JudulBaru, PengarangBaru, PenerbitBaru, GenreBaru, TahunBaru, StatusBaru):
        try:
            LinkedBuku.insertData(JudulBaru, PengarangBaru, PenerbitBaru, GenreBaru, TahunBaru, StatusBaru)
            print()
            print(">>> Data Baru Berhasil Ditambakan! <<<")
            print()
            return True
        except ValueError:
            print("Input Dengan Benar!")
            return False
        
    def duplicateData(self, judul):
        current = self.head
        while current is not None:
            if current.Judul.lower() == judul:
                return True
            current = current.next
        return False
    
    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.Judul == key:
                self.head = temp.next
                temp = None
                return
            while temp is not None:
                if temp.Judul == key:
                    break
                prev = temp
                temp = temp.next
            if temp == None:
                return
            prev.next = temp.next
            temp = None
        
    def printList(self):
        if self.head is None:
            print("Data Masih Kosong!")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                     List Buku")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            number = 1
            nodeTampil = self.head
            while nodeTampil is not None:
                print(number, nodeTampil.Judul)
                number += 1
                nodeTampil = nodeTampil.next

    def printData(self, node):
        print("                            DETAIL BUKU")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Judul        : {}".format(node.Judul))
        print("Pengarang    : {}".format(node.Pengarang))
        print("Penerbit     : {}".format(node.Penerbit))
        print("Genre        : {}".format(node.Genre))
        print("Tahun Terbit : {}".format(node.Tahun))
        print("Status       : {}".format(node.Status))
        
    def sortMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.Judul < b.Judul:
            result = a
            result.next = self.sortMerge(a.next, b)
        else:
            result = b
            result.next = self.sortMerge(a, b.next)
        return result

    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow    

    def mergeSort(self, c):
        if c == None or c.next == None:
            return c
        middle = self.getMiddle(c)
        next_middle = middle.next
        middle.next = None
        left = self.mergeSort(c)
        right = self.mergeSort(next_middle)
        sortedlist = self.sortMerge(left, right)
        return sortedlist

    def searchKey(self, index):
        if index < 0 or index > self.count-1:
            print()
            print(">>> Data Tersebut Tidak Tersedia! <<<")
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            return nodeTampil.Judul
        
    def makeList(self):
        values = []
        current = self.head
        while current is not None:
            values.append({"Judul":(current.Judul), "Pengarang":(current.Pengarang), "Penerbit":(current.Penerbit),
                           "Genre":(current.Genre), "Tahun Terbit":(current.Tahun), "Status":(current.Status)})
            current = current.next
        return values      

    def jumpSearch(self, arr, nama_buku, n):
        x = nama_buku
        step = math.sqrt(n)  
        prev = 0
        while arr[int(min(step, n) - 1)]["Judul"].lower() < x.lower():
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1
        while arr[int(prev)]["Judul"].lower() < x.lower():
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[int(prev)]["Judul"].lower() == x.lower():
            return prev
        return -1
    
    def printDict(self, arr, index_buku):
        print("                            DETAIL BUKU")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Judul        : {}".format(arr[index_buku]["Judul"]))
        print("Pengarang    : {}".format(arr[index_buku]["Pengarang"]))
        print("Penerbit     : {}".format(arr[index_buku]["Penerbit"]))
        print("Genre        : {}".format(arr[index_buku]["Genre"]))
        print("Tahun Terbit : {}".format(arr[index_buku]["Tahun Terbit"]))
        print("Status       : {}".format(arr[index_buku]["Status"]))
        
buku = LinkedBuku()

class Admin:
    def lihat_buku(self):
        buku.head = buku.mergeSort(buku.head)
        buku.printList()
    
    def cari_buku(self):
        cari = input("Masukkan Judul Buku: ")
        print()
        buku.head = buku.mergeSort(buku.head)
        listArray = buku.makeList()
        n = len(listArray)
        search = buku.jumpSearch(listArray, cari, n)
        index = int(search)
        if index == -1:
            print(">>> Buku {} Tidak Ditemukan! <<<".format(cari))
        else:
            buku.printDict(listArray, index)

    def tambah_buku(self):
        tambah = True
        print("Lengkapi Data Berikut: ")
        while tambah == True:
            buku_baru = input("Judul: ")
            pengarang = input("Pengarang: ")
            penerbit = input("Penerbit: ")
            genre = input("Genre: ")
            tahun = int(input("Tahun Terbit: "))
            status = ("Available")
            input("Status: Available")
            check = buku.duplicateData(buku_baru.lower())
            if check == True:
                print(">>> Buku Sudah Ada, Silahkan Tambahkan Judul Buku Yang Lain! <<<")
            elif check == False:
                buku_baru = buku_baru.capitalize()
                buku.newData(buku_baru, pengarang, penerbit, genre, tahun, status)
                tambah = False

    def hapus_buku(self):
        buku.head = buku.mergeSort(buku.head)
        buku.printList()
        try:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            hapus_buku = int(input("Masukkan Nomor Yang Ingin Dihapus: "))
            index = hapus_buku - 1
            key = buku.searchKey(index)
            if key != None:
                print()
                tanya = input("Apakah Anda Ingin Menghapus {} (y/n)? ".format(key))
                print()
                if tanya.lower() == "y":
                    buku.deleteNode(key)
                    print(">>> Buku Berhasil Dihapus! <<<")
                elif tanya.lower() == "n":
                    print(">>> Penghapusan Buku Dibatalkan! <<<")
                else:
                    print(">>> Masukkan Dengan Benar! <<<")
        except ValueError:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                Pilihan tidak tersedia               ")

admin = Admin()
                class User:
    def __init__(self):
        self.historyBuku = []
        
    def lihat_buku(self):
        LinkedBuku.head = LinkedBuku.mergeSort(LinkedBuku.head)
        LinkedBuku.printList()

    def cari_buku(self):
        cari = input("Masukkan Judul Buku: ")
        print()
        LinkedBuku.head = LinkedBuku.mergeSort(LinkedBuku.head)
        listArray = LinkedBuku.makeList()
        n = len(listArray)
        search = LinkedBuku.jumpSearch(listArray, cari, n)
        index = int(search)
        if index == -1:
            print(">>> Buku {} Tidak Ditemukan! <<<".format(cari))
        else:
            LinkedBuku.printDict(listArray, index)

    def pinjam_buku(self):
        while True:
            LinkedBuku.head = LinkedBuku.mergeSort(LinkedBuku.head)
            LinkedBuku.printList()
            try:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                pinjam = int(input("Masukkan Nomor Pilihan: "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                os.system("cls")
                index = pinjam - 1
                LinkedBuku.getData(index)
                status_pinjam = LinkedBuku.getStatus(index)
                if status_pinjam == "Available":
                    key = LinkedBuku.searchKey(index)
                    print()
                    pinjam_buku = input("Ingin Menambahkan {} Ke Daftar Bacaan (y/n)? ".format(key))
                    if pinjam_buku.lower() == "y":
                        acc = input("Apakah Setuju Dengan Syarat Dan Ketentuan (y/n)? ")
                        if acc.lower() == "y":
                            LinkedBuku.ubahStatus(index)
                            self.historyBuku.append(key)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(">>> Buku Berhasil Ditambahkan ke Daftar Bacaan! <<<  ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            break
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(">>> Pengajuan peminjaman buku dibatalkan <<<".center(80))
                            break
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Tambahkan buku ke dalam daftar bacaan jika anda bersedia ^_^ ")
                        break
                elif status_pinjam == "Out of Stock" or "out of stock":
                    key = LinkedBuku.searchKey(index)
                    os.system("cls")
                    print()
                    print("{} saat ini tidak tersedia untuk dipinjam".format(key))
            except ValueError:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                Pilihan tidak tersedia               ")

    def kembalikan_buku(self):
        LinkedBuku.head = LinkedBuku.mergeSort(LinkedBuku.head)
        while True:
            try:
                if len(self.historyBuku) >= 1:
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    print("                  Daftar Peminjaman             ")
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    nomor = 1
                    for i in self.historyBuku:
                        print(" {}. {}".format(nomor, i))
                        nomor += 1
                print()
                hapusBaca=int(input("Pilih Nomor Buku yang Ingin Dikembalikan>> "))
                print()
                index = hapusBaca - 1
                if hapusBaca>0:
                        hapusBaca-=1
                        self.historyBuku[hapusBaca]
                        break
                else:
                    print("\nmohon input yang benar") 
            except ValueError:
                print("\nmohon input yang benar")
            except IndexError:
                print("\nmohon input yang benar")
        try:
            confirm = input("Apakah Anda ingin Mengembalikan {} (y/t)? ".format(self.historyBuku[hapusBaca]))
            print()
            if confirm.lower() == "y":  
                LinkedBuku.ubahStatus2(index)
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("Berhasil Mengembalikan",self.historyBuku[hapusBaca])
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈") 
                print()
                if self.historyBuku[hapusBaca] in self.historyBuku:
                    self.historyBuku.pop(hapusBaca)
            else:
                print("\n",">>> Pengembalian Buku dibatalkan <<<")  
        except ValueError:
                print("—————————————————————————————————————————————————————")
                print("                Pilihan tidak tersedia               ")
    
    def history(self):
        if len (self.historyBuku) == 0:
             print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
             print("                Tidak Ada Catatan Peminjaman            ")
             print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

        else:
            if len(self.historyBuku) >= 1:
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("                  Riwayat Peminjaman             ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                nomor = 1
                for i in self.historyBuku:
                    print(" {}. {}".format(nomor, i))
                    nomor += 1
                print()

                def menu_utama():
    print("========================================".center(80))
    print("|                Menu Utama             |".center(80))
    print("========================================".center(80))
    print("1. Login Admin".center(80))
    print("2. Login User".center(80))
    print("3. Registrasi User".center(80))
    print("4. Exit".center(80))
    print("========================================".center(80))

def menu_admin():
    print("========================================".center(80))
    print("|                 Menu Admin            |".center(80))
    print("========================================".center(80))
    print("1. Lihat Data Buku".center(80))
    print("2. Cari Data Buku".center(80))
    print("3. Tambah Buku Baru".center(80))
    print("4. Hapus Buku".center(80))
    print("5. Exit".center(80))
    print("========================================".center(80))

def menu_pengunjung():
    print("========================================".center(80))
    print("|                Menu User              |".center(80))
    print("========================================".center(80))
    print("1. Lihat Data Buku".center(80))
    print("2. Cari Data Buku".center(80))
    print("3. Pinjam Buku".center(80))
    print("4. Kembalikan Buku".center(80))
    print("5. History".center(80))
    print("6. Exit".center(80))
    print("========================================".center(80))

def ulang():
    while True:
        tanya = input("Kembali Ke Menu (y/n)? ")
        if tanya == "y" or tanya == "Y":
            break
        elif tanya == "n" or tanya == "N":
            os.system("cls")
            print("Terima Kasih Telah Berkunjung ^_^".center(80))
            exit()
        else:
            print(">>> Masukkan Dengan Benar! <<<")

Admin = Admin()
User = User()

LinkedBuku.insertData("Laskar Pelangi", "Andrea Hirata", "Bentang Pustaka", "Roman", "2005", "Available")
LinkedBuku.insertData("Cantik Itu Luka", "Eka Kurniawan", "Gramedia Pustaka Utama", "Fiksi", "2022", "Available")
LinkedBuku.insertData("Bibi Gill", "Tere Liye", "Penerbit Sabak GRIP", "Fantasi", "2022", "Available")
LinkedBuku.insertData("Hujan", "Tere Liye", "Gramedia Pustaka Utama", "Romansa", "2016", "Available")
LinkedBuku.insertData("Mariposa", "Luluk HF", "Coconat Books", "Romance", "2018", "Available")
LinkedBuku.insertData("Dikta dan Hukum", "Dhiaan Farah", "Asoka Aksara", "Romansa", "2021", "Available")
LinkedBuku.insertData("Tentang Kamu", "Tere Liye", "Republika", "Fiksi/Romansa", "2016", "Available")
LinkedBuku.insertData("Laut Bercerita", "Leila Salikha Chudori", "Kepustakaan Populer Gramedia", "Historical Fiction", "2017", "Available")
LinkedBuku.insertData("Filosofi Teras", "Henry Manampiring", "Kompas", "Non-Fiksi", "2018", "Available")
LinkedBuku.insertData("Garis Batas", "Agustinus Wibowo", "Gramedia Pustaka Utama", "Non-Fiksi", "2020", "Available")


while True:
    try:
        menu_utama()
        opsi = int(input("Masukkan Pilihan: "))
        if opsi == 1:
            os.system("cls")
            login_admin()
            while True:
                try:
                    os.system("cls")
                    menu_admin()
                    tanya = int(input("Masukkan Pilihan: "))
                    if tanya == 1:
                        os.system("cls")
                        Admin.lihat_buku()
                        print("")
                        ulang()
                    elif tanya == 2:
                        os.system("cls")
                        Admin.cari_buku()
                        print("")
                        ulang()
                    elif tanya == 3:
                        os.system("cls")
                        Admin.tambah_buku()
                        print("")
                        ulang()
                    elif tanya == 4:
                        os.system("cls")
                        Admin.hapus_buku()
                        print("")
                        ulang()
                    elif tanya == 5:
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print(">>> Pilihan Tidak Tersedia! <<<".center(80))
                except KeyboardInterrupt:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
        elif opsi == 2:
            os.system("cls")
            login_pengunjung()
            while True:
                try:
                    os.system("cls")
                    menu_pengunjung()
                    tanya = int(input("Masukkan Pilihan: "))
                    if tanya == 1:
                        os.system("cls")
                        User.lihat_buku()
                        ulang()
                    elif tanya == 2:
                        os.system("cls")
                        User.cari_buku()
                        ulang()
                    elif tanya == 3:
                        os.system("cls")
                        User.pinjam_buku()
                        ulang()
                    elif tanya == 4:
                        os.system("cls")
                        User.kembalikan_buku()
                        ulang()
                    elif tanya == 5:
                        os.system("cls")
                        User.history()
                        ulang()
                    elif tanya == 6:
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print(">>> Pilihan Tidak Tersedia! <<<".center(80))
                except KeyboardInterrupt:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
        elif opsi == 3:
            os.system("cls")
            registrasi_pengunjung()
            while True:
                os.system("cls")
                print(">>> Registrasi Berhasil, Silahkan Login! <<<".center(80))
                break
        elif opsi == 4:
            os.system("cls")
            print("Terima Kasih Telah Berkunjung ^_^".center(80))
            exit()
        else:
            os.system("cls")
            print(">>> Pilihan Tidak Tersedia! <<<".center(80))
    except KeyboardInterrupt:
        os.system("cls")
        print(">>> Pilihan tidak tersedia! <<<".center(80))
