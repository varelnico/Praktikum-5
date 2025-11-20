print("Nama : Varel Nico Ramadhan")
print("NIM : 312510156\n")
print("-TUGAS DICTIONARY-\n")
print("=== Program Nilai Mahasiswa ===\n")

# Siapkan list kosong untuk menampung data
data_mahasiswa = []

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == "l":
        print("\nDaftar Nilai")
        print("="*70)
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("-"*70)

        if not data_mahasiswa:
            print("|                       TIDAK ADA DATA                      |")
        else:
            no = 1
            for m in data_mahasiswa:
                print(f"| {no:<2} | {m['nim']:<6} | {m['nama']:<8} | {m['tugas']:<5} | {m['uts']:<3} | {m['uas']:<3} | {m['nilai_akhir']:<5.2f} |")
                no += 1
        print("-"*70, "\n")

    elif pilihan == "t":
        nama = input("Nama Mahasiswa : ")
        nim = input("NIM Mahasiswa  : ")
        tugas = float(input("Nilai Tugas    : "))
        uts = float(input("Nilai UTS      : "))
        uas = float(input("Nilai UAS      : "))

        nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Simpan sebagai list biasa
        data_mahasiswa.append({"nama": nama, "nim": nim, "tugas": tugas, "uts": uts, "uas": uas, "nilai_akhir": nilai_akhir})

        print("Data berhasil ditambahkan!\n")

    elif pilihan == "u":
        cari = input("Masukan Nama yang ingin di ubah: ")

        found = False
        for m in data_mahasiswa:
            if m ["nama"] == cari:
                print("Data ditemukan, Masukan nilai baru.")
                m["tugas"] = float(input("Nilai Tugas     : "))
                m["uts"] = float(input("Nilai UTS     : "))
                m["uas"] = float(input("Nilai UTS     : "))
                m["nilai_akhir"] = (m["tugas"]*0.30) + (m["uts"]*0.35) + (m["uas"]*0.35)
                print("Data berhasi diubah\n")
                found = True
                break

        if not found:
            print("Data tidak ditemukan\n")

    elif pilihan == "h":
        hapus = input("Masukan Nama yang ingin dihapus: ")
        data_mahasiswa = [m for m in data_mahasiswa if m["nama"] != hapus]
        print("Data berhasil dihapus (jika ada).\n")

    elif pilihan == "c":
        cari = input("Masukan Nama yang dicari: ")
        print()

        Ketemu = False
        for m in data_mahasiswa:
            if m["nama"] == cari:
                print("Data ditemukan:")
                print("Nama         :", m["nama"])
                print("NIM          :", m["nim"])
                print("Tugas        :", m["tugas"])
                print("UTS          :", m["uts"])
                print("UAS          :", m["uas"])
                print("Nilai Akhir  :", m["nilai_akhir"])
                print()
                Ketemu = False
                break
        
        if not Ketemu:
            print("Data tidak ditemukan.\n")

    elif pilihan == "k":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia!\n")