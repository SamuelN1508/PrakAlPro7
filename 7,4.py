# Input
kalimat = input("Masukan kalimat : ")

# Fungsi mencari kata terpendek
def terpendek(kalimat):
    # Memisahkan kata-kata dalam kalimat
    list1 = kalimat.split()
    
    # Terpendek = kata pertama list sebagai default
    terpendek = list1[0]
    
    # Perulangan kata didalam list
    for kata in list1:
        # Jika panjang kata lebih pendek dari default
        if len(kata) < len(terpendek):
            # Kata itu menjadi default terpendek
            terpendek = kata
    return terpendek

# Fungsi mencari kata terpendek
def terpanjang(kalimat):
    # Memisahkan kata-kata dalam kalimat
    list1 = kalimat.split()
    
    # Terpanjang = kata pertama list sebagai default
    terpanjang = list1[0]
    
    # Perulangan kata didalam list
    for kata in list1:
        # Jika panjang kata lebih pendek dari default
        if len(kata) > len(terpanjang):
            # Kata itu menjadi default terpendek
            terpanjang = kata
    return terpanjang

print(f"terpendek : {terpendek(kalimat)}")
print(f"terpanjang : {terpanjang(kalimat)}")