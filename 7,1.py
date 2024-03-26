# Input kata 1 dan 2
kata1 = input("Masukan kata 1 : ")
kata2 = input("Masukan kata 2 : ")

# Fungsi anagram
def anagram(kata1, kata2):
    # Mengecilkan semua huruf
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    # Memasukan kata1 dan kata2 ke list1 dan list2
    list1 = list(kata1)
    list2 = list(kata2)
    # Diurutkan menggunakan .sort()
    list1.sort()
    list2.sort()
    
    # Jika list yang diurutkan sama maka kata1 dan kata2 anagram
    if list1 == list2:
        print(f"{kata1} adalah anagram dari {kata2}")
    else:
        print(f"{kata1} bukan anagram dari {kata2}")

anagram(kata1, kata2)