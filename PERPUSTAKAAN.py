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
