import mysql.connector
    
db =mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_warung'
    
)

# print(db.is_connected()) check apakah connect dengan database

def insert_item(kodeBrg, namaBrg, hargaBrg, stokBrg):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kodeBrg, namaBrg, hargaBrg, stokBrg) VALUES (%s, %s, %s, %s)", (kodeBrg, namaBrg, hargaBrg, stokBrg)) #query
    db.commit()
    
    if cursor.rowcount > 0:
        print("\nData berhasil ditambahkan\n")
    else:
        print("\nData gagal ditambahkan\n")
    