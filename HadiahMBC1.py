def luas_kubus():
    print ("hitung luas permukaan kubus")
    sisi = float(input("masukan sisi :"))
    luas = 6 * sisi * sisi
    print ("luas permukaan kubus adalah :", luas, "\n")

def luas_balok():
    print ("hitung luas permukaan balok")
    panjang = float(input("masukan panjang :"))
    lebar = float(input("masukan lebar :"))
    tinggi = float(input("masukan tinggi :"))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*tinggi*lebar)
    print ("luas permukaan balok adalah :", luas, "\n")

def luas_tabung():
    print ("hitung luas permukaan tabung")
    r = float(input("masukan jari-jari :"))
    tinggi = float(input("masukan tinggi :"))
    luas = 2 * 3.14 * r * (r + tinggi)
    print ("luas permukaan tabung adalah :", luas, "\n")

def luas_bola():
    print ("hitung luas permukaan bola")
    r = float(input("masukan jari-jari :"))
    luas = 4 * 3.14 * (r**2)
    print ("luas permukaan bola adalah :", luas, "\n")


while True:
    userInput = int(input(
        "pilih rumus yang akan digunakan: \n\n1.luas permukaan kubus\n2.luas permukaan balok\n3.luas permukaan tabung\n4.luas permukaan bola\n\n0.keluar program\n\npilih nomer berapa: "))
    if (userInput == 1):
        luas_kubus()
    elif (userInput == 2):
        luas_balok()
    elif (userInput == 3):
        luas_tabung()
    elif (userInput == 4):
        luas_bola()
    else:
        break