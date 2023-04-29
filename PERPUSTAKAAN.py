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
