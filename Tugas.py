print("FAKTUR")
print("---------------------------------------")
no_invoice = input("Nomor Inv : ")
nama_pelanggan = input("Kepada : ")
nama_up = input("UP :")
nama_alamat = input("Alamat :")
tanggal = input("Tanggal (DD/MM/YYYY/) : ")
uang = input("Mata Uang : ")
term = input("Cash/Tunai :")
gudang = input("Gudang : ")


print("No |Kode    |Nama Barang  |Harga  ")
print("1. |PRD-003 |Product C    |600.000")
print("2. |PRD-004 |Product D    |500.000")
print("3. |PRD-005 |Product E    |400.000")
print("4. |PRD-006 |Product F    |300.000")

total =int(input("masukan total barang :"))

kode_barang = []
jumlah_barang = []
harga = []
jumlah_harga = []

for i in range (total):
    print("barang ke - ", i+1)
    kode_barang.append(input("Masukan kode barang : "))
    jumlah_barang.append(int(input("Masukan jumlah barang : ")))

    if kode_barang == "PRD-003" : 
        harga = 600000
        nama_produk = "Product C"
    elif kode_barang == "PRD-004" :
        harga = 500000
        nama_produk = "Product D"
    elif kode_barang ==  "PRD-005" : 
        harga = 400000
        nama_produk = "Product E"
    elif kode_barang ==  "PRD-006" : 
        harga = 300000
        nama_produk = "Product F"
    else : 
        harga = 0
        nama_produk = "Produk menghilang"


print(kode_barang)
print(harga)
print(jumlah_barang)
print(nama_produk)