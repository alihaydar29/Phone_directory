rehber = [["ahmet", "celik", "23456"], ["seda", "nur", "77889"],["ali", "sagir", "12345"],["ekrem", "sever", "31141"]]


def kayit_ekle(rehber):
    while True:
        isim = input("isim giriniz: ")
        soyad = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        if emin_misin():
            rehber += [[isim, soyad, numara]]

        if devam_mi():
            continue
        else:
            break


def emin_misin():
    a = input("emin misin (evet,hayır): ")
    if a.lower().startswith("e"):
        return True
    else:
        False


def devam_mi():
    a = input("devam etmek istiyor musun (evet,hayır): ")
    if a.lower().startswith("e"):
        return True
    else:
        False


def kayıt_listele(rehber):
    for i, j, k in rehber:
        print("isim---> {}    soyad---> {}    numara---> {}".format(i, j, k))


def kayit_ara(rehber):
    while True:
        isim = input("bulmak istediğiniz kişinin adını veya soyadını giriniz: ")
        for i in rehber:
            if isim in i:
                print("isim--> {}  soyad--> {}    numara--> {}".format(i[0], i[1], i[2]))
        if devam_mi():
            continue
        else:
            break


def kayit_sil(rehber):
    while True:
        for i in rehber:
            print(*i)
        isim = input("silmek istediğiniz kişinin ismini giriniz: ")
        if emin_misin():
            for i in rehber:
                if isim in i:
                    rehber.remove(i)
        if devam_mi():
            continue
        else:
            break
#######################

while True:
    a = int(input(
        """
    1) kayıt ekle
    2) kayıtları listele
    3) kayıt ara
    4) kayıt sil
    5) çıkış
    
    """
    ))
    #################
    if a == 1:
        kayit_ekle(rehber)
    elif a == 2:
        kayıt_listele(rehber)
    elif a == 3:
        kayit_ara(rehber)
    elif a == 4:
        kayit_sil(rehber)
    elif a == 5:
        print(" iyi günler :) ")
        break