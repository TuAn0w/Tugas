import random
import os, sys
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
print ""

print B+"Permainan : CAK-CIK-BOOM"
print G+"pembuat permainan BY : TuAn. 0w"
print "-cara nya adalah dgn menemukan CAK & CIK"
print "-selain mencari CAK & CIK ada banyak hadiah lainnya bossque"
print O+"Pilihlah  nomor jika mau anda boleh tanya ama mbah dukun!!!:"
print ""
print G+"nomor 1"
print R+"nomor 2"
print O+"nomor 3"
print W+"nomor 4"
print G+"nomor 5"
print R+"nomor 6"
print O+"nomor 7"
print W+"nomor 8"
print G+"nomor 9"
print R+"nomor 10"
print O+"nomor 11"
print W+"Jika sudah menemukan CAK & CIK kalian pilih nomor 11"
print W+"jika kamu belum menemukan CAK & CIK kamu belum bisa mendapat kan hadiah nya"
def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)
def permainan ():
    kamu = int(input("masukan pilihanmu: "))
    kom = random.choice(["Selamat anda mendapat Janda!!!", "pilih yg bener Boedjank", "Boom bosque", "\SELAMAT ANDA MENDAPAT *CAK* SEKARANG TINGGAL MENCARI *CIK*", "Selamat anda mendapat sabun untuk coli"])
    if kamu == 1:
        print G+"nomor 1 "
        print("komputer :", kom)
        if kom == "CAK..":
            print B+"\tSELAMAT ANDA MENDAPAT *CAK* SEKARANG TINGGAL MENCARI *CIK*"
    if kamu == 2:
        print G+"nomor 2 "
        print("komputer :", kom)
    if kamu == 3:
        print G+"nomor 3 "
        print("komputer :", kom)
    if kamu == 4:
        print G+"nomor 4 "
        print("komputer :", kom)
        if kom == "CAK":
            print G+"\tSELAMAT ANDA MENDAPAT *CAK* SEKARANG TINGGAL MENCARI *CIK*"
        if kom == "CAK":
            print R+"\tSELAMAT ANDA MENDAPAT *CAK* SEKARANG TINGGAL MENCARI *CIK*"
        if kom == "CAK":
            print B+"\tSELAMAT ANDA MENDAPAT *CAK* SEKARANG TINGGAL MENCARI *CIK*"
    if kamu == 5:
        print G+"nomor 5 "
        print("komputer :", kom)
    if kamu == 6:
        print G+"nomor 6 "
        print("komputer :", kom)
    if kamu == 7:
        print G+"nomor 7 "
        print("komputer :", kom)
    if kamu == 8:
        print G+"nomor 8 "
        print("komputer :", kom)
    if kamu == 9:
        print G+"nomor 9 "
        print("komputer :", kom)
    if kamu == 10:
        print G+"nomor 10 "
        print("komputer :", kom)
        restart()
permainan()
restart()
try:
        permainan()
except KeyboardInterrupt:
        os.system('clear')
        restart()
