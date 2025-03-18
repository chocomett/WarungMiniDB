# WarungMiniDB 🛒🛒

A Python-based CRUD program designed to help manage market stock and uses MySQL to store goods data.

## reference

Youtube: [Dea Afrizal](https://youtu.be/eKruXIX6LZk?si=GdqNiw2ZRq2CgSEM)

## feature

* Tambah barang (Create)
* Lihat daftar barang (Read)
* Ubah data barang (Update)
* Hapus barang (Delete)



## Documentation

1.  Pastikan Python dan MySQL sudah terinstall.
2.  Clone repositori ini: `git clone <URL_repositori_Anda>`
3. Create Database MySQL
* Open Laragon and Download MySQL
* Open via GUI phpmyadmin
* Create new database: `mini_warung`
* Create new tabel: `tbl_barang`
* Create Columns
    * `id => Primary Key | Auto Increment | Int`
    * `kodeBrg => Secondary Key | Unique | Varchar 255`
    * `namaBrg => Varchar 255`
    * `stokBrg => Int`
    * `hargaBrg => Int`

4. Install dependencies Python:
* Install pip ( Source From [Youtube](https://youtu.be/fJKdIf11GcI?si=LuIf1dFa2FslHPml) )
    ```bash
    Command to Download get-pip.py:
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

    python get-pip.py

* Install connector mysql ke python
    ```bash
    pip install mysql-connector
    ```

5. Jalankan aplikasi:

* `py mian.py`
    




