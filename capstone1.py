import csv
import os
from datetime import datetime

# PROGRAM PENJUALAN BARANG TOKO SUKES SELALU BERJAYA
# DENGAN LOGIN, CSV DATA, LAPORAN PENJUALAN DAN OMZET HARIAN

file_barang = "barang.csv"
file_penjualan = "penjualan.csv"

# LOGIN SYSTEM

users = {
    "admin" : "admin123",
    "kasir" : "kasir123"
}

#FUNGSI UNTUK LOGIN USER

def login():
    print("==== LOGIN SISTEM TOKO SUKSES SELALU BERJAYA ===")
    for i in range(3):
        username = input("Username: ").lower()
        password = input("Password: ")
        if username in users and users[username] == password:
            print(f"Login berhasil! Selamat datang, {username.title()}")
            return username
        else:
            print("Username atau password salah!")
    print("Terlalu banyak percobaan gagal. Program ditutup.")
    exit()

# FUNGSI MEMUAT DATA BARANG DARI CSV

def muat_data():
    barang = {}
    if os.path.exists(file_barang):
        with open(file_barang, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) == 3:
                    nama, harga, stok = row
                    barang[nama] = [int(harga), int(stok)]
    else:
        barang = {
            "Sabun" : [5000,20],
            "Shampoo" : [10000, 15],
            "Pasta Gigi" : [8000, 25],
            "Sikat Gigi" : [6000, 30],
            "Deterjen" : [12000, 10]
        }
        simpan_data(barang)
    return barang

# FUNGSI SIMPAN DATA KE CSV

def simpan_data(barang):
    with open(file_barang, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nama Barang", "Harga", "Stok"])
        for nama, info in barang.items():
            writer.writerow([nama, info[0], info[1]])

# TAMPILKAN DAFTAR BARANG

def tampilkan_barang(barang):
    print("\n=== Daftar Barang Toko ===")
    print(f"{'No':3} {'Nama Barang':<15} {'Harga':<10} {'Stok':<5}")
    print("-"*40)
    for i, (nama, info) in enumerate(barang.items(), start=1):
        print(f"{i:<3} {nama:<15} Rp {info[0]:<8} {info[1]:<5}")
    print("-"*40)

# Simpan transaksi ke file penjualan.csv

def catat_penjualan(keranjang, total, diskon, total_bayar, bayar, kembalian, kasir):
    file_exists = os.path.exists(file_penjualan)
    with open(file_penjualan, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Tanggal", "Kasir", "Nama Barang", "Jumlah", "Subtotal", "Total", "Diskon", "Total Bayar", "Bayar", "Kembalian"])
        tanggal = datetime.now().strftime("%Y-%M-%D")
        for item in keranjang:
            writer.writerow([tanggal, kasir.title(), item[0], item[1], item[2], total, diskon, total_bayar, bayar, kembalian])

# Lihat laporan penjualan & omzet harian

def laporan_penjualan():
    if not os.path.exists(file_penjualan):
        print ("Belum ada data penjualan.")
        return
    
    print("\n=== LAPORAN PENJUALAN TOKO SUKSES SELALU BERJAYA ===")
    omzet_harian = {}
    with open(file_penjualan, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tanggal = row["Tanggal"]
            total_bayar = float(row["Total Bayar"])
            omzet_harian[tanggal] = omzet_harian.get(tanggal, 0) + total_bayar
    
    for tanggal, total in omzet_harian.items():
        print(f"Tanggal: {tanggal} - Total Penjualan: RP {total:,.0f}")
    #print("------------------------------------------")

    tampil_detail = input("Ingin lihat detail transaksi? (y/n): ").lower()
    if tampil_detail == "y":
        with open(file_penjualan, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                print(f"Tgl: {row[0]}, Kasir: {row[1]}, Barang: {row[2]}, Jumlah: {row[3]}, Total Bayar: Rp {row[7]}")
    input("\nTekan ENTER untuk kembali....")

# Menu ADMIN

def menu_admin(barang):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang Baru")
        print("3. Edit Harga/Stok Barang")
        print("4. Hapus Barang")
        print("5. Lihat Laporan Penjualan & Omzet Harian")
        print("6. Logout")

        pilih = input("Pilih menu (1-6): ")

        if pilih == "1":
            tampilkan_barang(barang)
        elif pilih == "2":
            nama = input("Masukkan nama barang baru: ").title()
            if nama in barang:
                print("Barang Sudah ada!")
            else:
                harga = int(input("Masukkan harga barang: "))
                stok = int(input("Masukkan stok barang: "))
                barang[nama] = [harga, stok]
                simpan_data(barang)
                print(f"Barang {nama} berhasil ditambahkan")
        elif pilih == "3":
            tampilkan_barang(barang)
            nama = input("Masukkan nama barang yang ingin diedit: ").title()
            if nama in barang:
                print(f"Data lama: Harga = Rp {barang[nama][0]}, Stok = {barang[nama][1]}")
                harga_baru = input("Masukkan harga baru (kosongkan jika harga tidak berubah): ")
                stok_baru = input("Masukkan stok baru (kosongkan jika stok tidak berubah): ")
                if harga_baru:
                    barang[nama][0] = int(harga_baru)
                if stok_baru:
                    barang[nama][1] = int(stok_baru)
                simpan_data(barang)
                print("Data barang berhasil diperbaharui!")
            else:
                print("Barang tidak ditemukan!")
        elif pilih == "4":
            tampilkan_barang(barang)
            nama = input("Masukkan nama barang yang ingin dihapus: ").title()
            if nama in barang:
                del barang[nama]
                simpan_data(barang)
                print("Barang berhasil dihapus!")
            else:
                print("Barang tidak ditemukan!")
        elif pilih == "5":
            laporan_penjualan()
        elif pilih == "6":
            print("Logout dari akun admin...")
            break
        else:
            print("Pilihan tidak valid!")

# Menu Kasir

def menu_kasir(barang, kasir):
    keranjang = []
    total = 0

    while True:
        tampilkan_barang(barang)
        nama = input("Masukkan nama barang yang dibeli: ").title()
        if nama not in barang:
            print("Barang tidak ditemukan!")
            continue
        if barang[nama][1] <= 0:
            print("Stok barang habis!")
            continue

        jumlah = int(input("Masukkan jumlah yang dibeli: "))
        if jumlah > barang[nama][1]:
            print("Stok tidak mencukupi")
            continue

        subtotal = barang[nama][0] * jumlah
        total += subtotal
        keranjang.append((nama, jumlah, subtotal))
        barang[nama][1] -= jumlah
        simpan_data(barang)

        lanjut = input("Tambang barang lain? (y/n): ").lower()
        if lanjut != "y":
            break

# Hitung Diskon

    diskon = 0
    if total >= 50000:
        diskon = total *0.10
    elif total >= 30000:
        diskon = total *0.05
    
    total_bayar = total - diskon

#Input pembayaran

    while True:
        bayar = int(input(f"Masukkan jumlah uang (Total: Rp {total_bayar:,.0f}): "))
        if bayar < total_bayar:
            print("Uang tidak cukup, masukkan lagi!")
        else:
            kembalian = bayar - total_bayar
            break

# Cetak Struk

    print("\n========== STRUK PEMBELIAN ==========")
    for item in keranjang:
        print(f"{item[0]:15} x{item[1]}   Rp {item[2]:,}")
    print("------------------------------------")
    print(f"Total Harga     : Rp {total:,}")
    print(f"Diskon          : Rp {diskon:,.0f}")
    print(f"Total Bayar     : Rp {total_bayar:,.0f}")
    print(f"Uang Diterima   : Rp {bayar:,.0f}")
    print(f"Kembalian       : Rp {kembalian:,.0f}")
    print("=====================================")
    print("Terima kasih telah berbelanja di TOKO SUKSES SELALU BERJAYA!")

# SIMPAN TRANSAKSI KE LAPORAN
    
    catat_penjualan(keranjang, total, diskon, total_bayar, bayar, kembalian, kasir)
    print("Transaksi berhasil dicatat ke laporan penjualan")

# Main Program

def main():
    barang = muat_data()
    user = login()

    while True:
        if user == "admin":
            menu_admin(barang)
        elif user == "kasir":
            menu_kasir(barang, user)
        else:
            print("Tipe user tidak dikenal!")

        lagi = input("\nApakah ingin login kembali? (y/n): ").lower()
        if lagi == "y":
            user = login()
        else:
            print("Terima kasih telah menggunakan sistem TOKO SUKSES SELALU BERJAYA!")
            break

if __name__ == "__main__":
    main()