# KELOMPOK 13
# MUTHMAINNAH AISYAH (2209116001)
# ALLYYA NUR AZIZAH (2209116030)
# RIZANI RUPA MADAUN (2209116039)

import os
import math
import pwinput
import mysql.connector

db_perpus = mysql.connector.connect(
    host="db4free.net",
    user="muthmainnah",
    password="perpus13",
    database="perpustakaan")

try:
    cursor = db_perpus.cursor()
except mysql.connector.Error as err:
    print("Error Code : ", err.errno)
    print("Error Message : ", err.msg)
    exit()

def login_admin():
    while True:
        try:
            Username = input("Masukkan Username: ")
            Password = pwinput.pwinput("Masukkan Password: ")
            try:
                query = "SELECT * FROM ADMIN WHERE Username = %s AND Password = %s"
                values = (Username, Password)
                cursor = db_perpus.cursor()
                cursor.execute(query, values)
                User = cursor.fetchone()
                if User:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Username Atau Password Anda Salah!")
            except ValueError:
                os.system("cls")
                print("Username Atau Password Anda Salah!")
        except KeyboardInterrupt:
            os.system("cls")
            print("Masukkan Inputan Yang Benar!")

def login_pengunjung():
    while True:
        try:
            Username = input("Masukkan Username: ")
            Password = pwinput.pwinput("Masukkan Password: ")
            try:
                query = "SELECT * FROM USER WHERE Username = %s AND Password = %s"
                values = (Username, Password)
                cursor = db_perpus.cursor()
                cursor.execute(query, values)
                User = cursor.fetchone()
                if User:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Username Atau Password Anda Salah!")
            except ValueError:
                os.system("cls")
                print("Username Atau Password Anda Salah!")
        except KeyboardInterrupt:
            os.system("cls")
            print("Masukkan Inputan Yang Benar!")

def registrasi_pengunjung():
    while True:
        try:
            Username = input("Masukkan Username Baru: ")
            Password = pwinput.pwinput("Masukkan Password Baru: ")
            cursor = db_perpus.cursor()
            query = "SELECT * FROM USER WHERE Username = %s"
            values = [(Username)]
            cursor.execute(query, values)
            User = cursor.fetchone()
            if User:
                os.system("cls")
                print("Username Sudah Ada!")
            else:
                query = "INSERT INTO USER (Username, Password) VALUES (%s, %s)"
                values = (Username, Password)
                cursor.execute(query, values)
                db_perpus.commit()
                break
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

    def getData(self, index):
        if index < 0 or index > self.count-1:
            os.system("cls")
            print(">>> Data Tersebut Tidak Tersedia! <<<")
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            buku.printData(nodeTampil)

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

    def ubahStatus2(self, index):
        nodeUpdate = self.head
        for i in range(index):
            nodeUpdate = nodeUpdate.next
        nodeUpdate.Status = "Available"

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
            buku.insertData(JudulBaru, PengarangBaru, PenerbitBaru, GenreBaru, TahunBaru, StatusBaru)
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

    def pinjam_buku(self):
        while True:
            buku.head = buku.mergeSort(buku.head)
            buku.printList()
            try:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                pinjam = int(input("Masukkan Nomor Pilihan: "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                os.system("cls")
                index = pinjam - 1
                buku.getData(index)
                status_pinjam = buku.getStatus(index)
                if status_pinjam == "Available":
                    key = buku.searchKey(index)
                    print()
                    pinjam_buku = input("Ingin Menambahkan {} Ke Daftar Bacaan (y/n)? ".format(key))
                    if pinjam_buku.lower() == "y":
                        acc = input("Apakah Setuju Dengan Syarat Dan Ketentuan (y/n)? ")
                        if acc.lower() == "y":
                            buku.ubahStatus(index)
                            self.historyBuku.append(key)
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(">>> Buku Berhasil Ditambahkan ke Daftar Bacaan! <<<  ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            break
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("        >>> Pengajuan peminjaman buku dibatalkan <<<")
                            break
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Tambahkan buku ke dalam daftar bacaan jika anda bersedia ^_^ ")
                        break
                elif status_pinjam == "Out of Stock" or "out of stock":
                    key = buku.searchKey(index)
                    os.system("cls")
                    print()
                    print("{} saat ini tidak tersedia untuk dipinjam".format(key))
            except ValueError:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("                Pilihan tidak tersedia               ")

    def kembalikan_buku(self):
        buku.head = buku.mergeSort(buku.head)
        while True:
            try:
                if len (self.historyBuku) == 0:
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    print("                Tidak Ada Catatan Peminjaman            ")
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    break
                else:
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
                    if hapusBaca > 0:
                        hapusBaca -= 1
                        self.historyBuku[hapusBaca]
                        confirm = input("Apakah Anda ingin Mengembalikan {} (y/t)? ".format(self.historyBuku[hapusBaca]))
                        print()
                        if confirm.lower() == "y":
                            buku.ubahStatus2(index)
                            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                            print("Berhasil Mengembalikan",self.historyBuku[hapusBaca])
                            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈") 
                            if self.historyBuku[hapusBaca] in self.historyBuku:
                                self.historyBuku.pop(hapusBaca)
                            break
                        else:
                            print("\n",">>> Pengembalian Buku Dibatalkan! <<<") 
                            break
                    else:
                        print("\n>>> Mohon Input Yang Benar! <<<")
                        break
            except ValueError:
                print("\n>>> Mohon Input Yang Benar! <<<")
            except IndexError:
                print("\n>>> Mohon Input Yang Benar! <<<")
    
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

user = User()

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

buku.insertData("Laskar Pelangi", "Andrea Hirata", "Bentang Pustaka", "Roman", "2005", "Available")
buku.insertData("Cantik Itu Luka", "Eka Kurniawan", "Gramedia Pustaka Utama", "Fiksi", "2022", "Available")
buku.insertData("Bibi Gill", "Tere Liye", "Penerbit Sabak GRIP", "Fantasi", "2022", "Available")
buku.insertData("Hujan", "Tere Liye", "Gramedia Pustaka Utama", "Romansa", "2016", "Available")
buku.insertData("Mariposa", "Luluk HF", "Coconat Books", "Romance", "2018", "Available")
buku.insertData("Dikta dan Hukum", "Dhiaan Farah", "Asoka Aksara", "Romansa", "2021", "Available")
buku.insertData("Tentang Kamu", "Tere Liye", "Republika", "Fiksi/Romansa", "2016", "Available")
buku.insertData("Laut Bercerita", "Leila Salikha Chudori", "Kepustakaan Populer Gramedia", "Historical Fiction", "2017", "Available")
buku.insertData("Filosofi Teras", "Henry Manampiring", "Kompas", "Non-Fiksi", "2018", "Available")
buku.insertData("Garis Batas", "Agustinus Wibowo", "Gramedia Pustaka Utama", "Non-Fiksi", "2020", "Available")

while True:
    try:
        menu_utama()
        opsi = input("Masukkan Pilihan: ")
        if opsi == "1":
            os.system("cls")
            login_admin()
            while True:
                try:
                    os.system("cls")
                    menu_admin()
                    tanya = input("Masukkan Pilihan: ")
                    if tanya == "1":
                        os.system("cls")
                        admin.lihat_buku()
                        print("")
                        ulang()
                    elif tanya == "2":
                        os.system("cls")
                        admin.cari_buku()
                        print("")
                        ulang()
                    elif tanya == "3":
                        os.system("cls")
                        admin.tambah_buku()
                        print("")
                        ulang()
                    elif tanya == "4":
                        os.system("cls")
                        admin.hapus_buku()
                        print("")
                        ulang()
                    elif tanya == "5":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print(">>> Pilihan Tidak Tersedia! <<<".center(80))
                except ValueError:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
                except KeyboardInterrupt:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
        elif opsi == "2":
            os.system("cls")
            login_pengunjung()
            while True:
                try:
                    os.system("cls")
                    menu_pengunjung()
                    tanya = input("Masukkan Pilihan: ")
                    if tanya == "1":
                        os.system("cls")
                        user.lihat_buku()
                        print("")
                        ulang()
                    elif tanya == "2":
                        os.system("cls")
                        user.cari_buku()
                        print("")
                        ulang()
                    elif tanya == "3":
                        os.system("cls")
                        user.pinjam_buku()
                        print("")
                        ulang()
                    elif tanya == "4":
                        os.system("cls")
                        user.kembalikan_buku()
                        print("")
                        ulang()
                    elif tanya == "5":
                        os.system("cls")
                        user.history()
                        print("")
                        ulang()
                    elif tanya == "6":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print(">>> Pilihan Tidak Tersedia! <<<".center(80))
                except ValueError:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
                except KeyboardInterrupt:
                    os.system("cls")
                    print(">>> Pilihan tidak tersedia! <<<".center(80))
        elif opsi == "3":
            os.system("cls")
            registrasi_pengunjung()
            while True:
                os.system("cls")
                print(">>> Registrasi Berhasil, Silahkan Login! <<<".center(80))
                break
        elif opsi == "4":
            os.system("cls")
            print("Terima Kasih Telah Berkunjung ^_^".center(80))
            exit()
        else:
            os.system("cls")
            print(">>> Pilihan Tidak Tersedia! <<<".center(80))
    except ValueError:
        os.system("cls")
        print(">>> Pilihan tidak tersedia! <<<".center(80))
    except KeyboardInterrupt:
        os.system("cls")
        print(">>> Pilihan tidak tersedia! <<<".center(80))
        
