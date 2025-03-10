import libs
from services import db

def add():
    kodeBrg = input("kode barang: ")
    namaBrg = input("nama barang: ")
    hargaBrg = int(input("Harga barang: "))
    stokBrg = int(input("stok barang: "))
    
    db.insert_item(kodeBrg, namaBrg, hargaBrg, stokBrg)
    
def check():
    items = db.fetch_item()
    style = "============================"
    for item in items:
        #print(item)
        
        # Re-format data yang dimunculkan dari database
        kodeBrg = item[1]
        namaBrg = item[2]
        hargaBrg = item[3]
        stokBrg = item[4]
        print(f"{style}\n\nKode Barang: {kodeBrg}\nNama Barang: {namaBrg}\nHarga Barang: Rp. {hargaBrg}\nStok Barang: {stokBrg}\n{style}")
        
def deleted():
    db.delete_item()
    
    
def start():
    while True:
        menus = int(input("\n\nmenu pilihan:\n1. Tambah Barang\n2. Cek Barang\n3. hapus Barang\n4. Menu\n5. Keluar Program\n\nSilahkan pilih: "))
        
        if menus == 1:
            while True:
                add()
                inputAdd = input(f"Lanjut Input Barang lagi?: ")
                inputAddKecil = inputAdd.lower()
                if inputAdd == "n":
                    break                    
        elif menus == 2:
            check()
        elif menus == 3:
            deleted()
        elif menus == 4:
            libs.menu()
        elif menus == 5:
            libs.exit_program()
        else:
            break

if __name__ == "__main__":
    start()