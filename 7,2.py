# Masukan input
kalimat = input("Masukan kalimat : ")
kata = input("Kata yang dicari : ")

# Fungsi menghitung jumlah
def jumlah_kata(kalimat, kata):
    # Mengecilkan kalimat dan kata
    kalimat = kalimat.lower()
    kata = kata.lower()
    
    # Menggunakan kalimat.count(kata) untuk menghitung jumlah kata dalam kalimat
    jml = kalimat.count(kata)
    return jml

print(jumlah_kata(kalimat, kata))