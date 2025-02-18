import libs
from services import db

def add():
    kodeBrg = input("kode barang: ")
    namaBrg = input("nama barang: ")
    hargaBrg = int(input("Harga barang: "))
    stokBrg = int(input("stok barang: "))
    
    db.insert_item(kodeBrg, namaBrg, hargaBrg, stokBrg)
    
def check():
    print("check")

def start():
    while True:
        menus = int(input("\n\nmenu pilihan:\n1. Tambah barang\n2. check barang\n3. kembali\n\nSilahkan pilih: "))
        
        if menus == 1:
            add()
        elif menus == 2:
            check()
        elif menus == 3:
            libs.menu()
        else:
            break

if __name__ == "__main__":
    start()