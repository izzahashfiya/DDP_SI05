import math

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi * sisi * sisi * sisi
    print(f'hasil luas persegi adalah {sisi} * {sisi} = {luas}')
    print(f'keliling persegi adalah {keliling}')

def l_persegipanjang(panjang, lebar):
    luas = panjang * lebar
    print(f'hasil luas persegi panjang adalah {panjang } * {lebar} = {luas}')

def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'hasil luas segitiga adalah {0.5} * {alas} * {tinggi} = {alas}')

def l_lingkaran(phi, r1, r2):
    luas = phi * r1 * r2
    print(f'hasil luas lingkaran adalah {phi} * {r1} * {r2} = {luas}')

def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi 
    print(f'hasil luas jajargenjang adalah {alas} * {tinggi} = {alas}')
