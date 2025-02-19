import mysql.connector
    
db =mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_warung'
    
)

# print(db.is_connected()) check apakah connect dengan database

def insert_item(kodeBrg, namaBrg, hargaBrg, stokBrg): # function Add
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kodeBrg, namaBrg, hargaBrg, stokBrg) VALUES (%s, %s, %s, %s)", (kodeBrg, namaBrg, hargaBrg, stokBrg)) #query
    db.commit()
    
    if cursor.rowcount > 0:
        print("\nData berhasil ditambahkan\n")
    else:
        print("\nData gagal ditambahkan\n")
        
def fetch_item(): # function Get
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()

def delete_item():
    cursor = db.cursor()
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")

    sql = "DELETE FROM tbl_barang WHERE kodeBrg = %s"
    val = (kode_barang,)

    cursor.execute(sql, val)
    db.commit()
    if cursor.rowcount > 0:
        print("\nData berhasil dihapus\n")
    else:
        print("\nData gagal dihapus\n")
    
    