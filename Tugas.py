print("FAKTUR")
print("---------------------------------------")
no_invoice = input("Nomor Inv : ")
nama_pelanggan = input("Kepada : ")
nama_up = input("UP : ")
nama_alamat = input("Alamat : ")
tanggal = input("Tanggal (DD/MM/YYYY/) : ")
uang = input("Mata Uang : ")
term = input("Cash/Tunai : ")
gudang = input("Gudang : ")
print(" ")
print("DAFTAR HARGA BARANG")
print("No |Kode    |Nama Barang  |Harga  ")
print("1. |PRD-003 |Product C    |600.000")
print("2. |PRD-004 |Product D    |500.000")
print("3. |PRD-005 |Product E    |400.000")
print("4. |PRD-006 |Product F    |300.000")
print(" ")
total =int(input("Masukan total barang :"))

kode_barang = []
jumlah_barang = []
harga = []
jumlah_harga = []

for i in range (total):
    print("barang ke - ", i+1)
    kode_barang.append(input("Masukan kode barang : "))
    jumlah_barang.append(int(input("Masukan jumlah barang : ")))

    if kode_barang[i] == "PRD-003" : 
        harga = 600000
        nama_produk = "Product C"
        jumlah_harga.append(harga * jumlah_barang[i])
    elif kode_barang[i] == "PRD-004" :
        harga = 500000
        nama_produk = "Product D"
        jumlah_harga.append(harga * jumlah_barang[i])
    elif kode_barang[i] ==  "PRD-005" : 
        harga = 400000
        nama_produk = "Product E"
        jumlah_harga.append(harga * jumlah_barang[i])
    elif kode_barang[i] ==  "PRD-006" : 
        harga = 300000
        nama_produk = "Product F"
        jumlah_harga.append(harga * jumlah_barang[i])
    else : 
        harga = 0
        nama_produk = "Produk menghilang"
        jumlah_harga.append(harga * jumlah_barang[i])

print(" ")
print("FAKTUR")
print("-----------------------------------------------------------------------------------")
print("Nomor Inv : %-4s Tanggal   : %-2s" % (no_invoice, tanggal))
print("Kepada    : %-4s Mata Uang : %-2s" % (nama_pelanggan, uang))
print("UP        : %-4s Term      : %-2s" % (nama_up, term))
print("Alamat    : %-4s Gudang    : %-2s" % (nama_alamat, gudang))
print("NO  | Kode     | Nama Barang   | Jumlah | Unit | Harga  | Disc | Sub Total | Pajak ")
for i in range (total): 
    print("%-4i| %-8s | %-13s | %-6i | %-4s | %-5d | %-4s | %-9i | %-5s" % (i+1, kode_barang[i], nama_produk, jumlah_barang[i], "pcs", harga, "0%", jumlah_harga[i], "10%"))

total = sum(jumlah_harga)
pajak = total * 0.1
print(" ")
print(" ")
print(" ")
print("-----------------------------------------------------------------------------------")
print("Discount Final    : %63s" % ("0"))
print("Pajak             : %63i" % (pajak))
print("Biaya Pengantaran : %63s" % ("0"))
print("Total             : Rp.%60i" % (total + pajak))
print("Dibayar           : Rp.%60s" % ("0"))
print("Saldo             : Rp.%60i" % (total + pajak))