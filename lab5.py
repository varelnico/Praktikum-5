print("Nama : Varel Nico Ramadhan")
print("NIM  : 312510156\n")
print("=== PROGRAM INPUT NILAI ===\n")

data = []   # List untuk menyimpan semua data mahasiswa

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()

    # =============================== LIHAT DATA ====================================
    if pilihan == "l":
        print("\nDaftar Nilai")
        print("="*70)
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("-"*70)

        if not data:
            print("|                       TIDAK ADA DATA                      |")
        else:
            no = 1
            for m in data:
                print(f"| {no:<2} | {m['nim']:<6} | {m['nama']:<8} | {m['tugas']:<5} | {m['uts']:<3} | {m['uas']:<3} | {m['akhir']:<5.2f} |")
                no += 1
        print("-"*70, "\n")

    # =============================== TAMBAH DATA ====================================
    elif pilihan == "t":
        nim = input("NIM        : ")
        nama = input("Nama       : ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS  : "))
        uas = float(input("Nilai UAS  : "))

        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        data.append({
            "nama": nama,
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        })

        print("Data berhasil ditambahkan!\n")

    # =============================== UBAH DATA ======================================
    elif pilihan == "u":
        cari = input("Masukkan NIM yang ingin diubah: ")

        found = False
        for m in data:
            if m["nim"] == cari:
                print("Data ditemukan. Masukkan nilai baru.")
                m["nama"] = input("Nama baru     : ")
                m["tugas"] = float(input("Nilai Tugas   : "))
                m["uts"] = float(input("Nilai UTS     : "))
                m["uas"] = float(input("Nilai UAS     : "))
                m["akhir"] = (m["tugas"]*0.30) + (m["uts"]*0.35) + (m["uas"]*0.35)
                print("Data berhasil diubah!\n")
                found = True
                break
        
        if not found:
            print("Data tidak ditemukan.\n")

    # =============================== HAPUS DATA ======================================
    elif pilihan == "h":
        hapus = input("Masukkan NIM yang ingin dihapus: ")
        data = [m for m in data if m["nim"] != hapus]
        print("Data berhasil dihapus (jika ada).\n")

    # =============================== CARI DATA =======================================
    elif pilihan == "c":
        cari = input("Masukkan NIM yang dicari: ")
        print()

        ketemu = False
        for m in data:
            if m["nim"] == cari:
                print("Data Ditemukan:")
                print("Nama        :", m["nama"])
                print("NIM         :", m["nim"])
                print("Tugas       :", m["tugas"])
                print("UTS         :", m["uts"])
                print("UAS         :", m["uas"])
                print("Nilai Akhir :", round(m["akhir"], 2))
                print()
                ketemu = True
                break

        if not ketemu:
            print("Data tidak ditemukan.\n")

    # =============================== KELUAR ==========================================
    elif pilihan == "k":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia!\n")
