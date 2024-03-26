# Input kalimat
kalimat = input("Masukan kalimat : ")

def hapus_spasi(kalimat):
    # Memisahkan kata satu per satu menggunakan split
    kalimat = kalimat.split()
    
    # Menggabungkan kata yang dipisah dengan " " 
    kalimat = ' '.join(kalimat)
    return kalimat

print(f'"{hapus_spasi(kalimat)}"')
