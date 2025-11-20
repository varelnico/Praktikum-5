print("Nama : Varel Nico Ramadhan")
print("NIM : 312510156")
print()
print("-TUGAS PERULANGAN-")
print()
print("=== Program Nilai Mahasiswa ===")
print()
# Siapkan list kosong untuk menampung data

data_mahasiswa = []

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == "1":
        print("\nDaftar Nilai")
        print("="*70)
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("-"*70)

        if not data_mahasiswa:
            print("|                       TIDAK ADA DATA                      |")
        else:
            no = 1
            for m in data_mahasiswa:
                print(f"| {no:<2} | {m['nim']:<6} | {m['nama']:<8} | {m['tugas']:<5} | {m['uts']:<3} | {m['uas']:<3} | {m['akhir']:<5.2f} |")
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
    data_mahasiswa.append([nama, nim, tugas, uts, uas, nilai_akhir])

    print("Data berhasil ditambahkan!\n")


i = 1
for mhs in data_mahasiswa:
    print(f"\nData ke-{i}")
    print("Nama        :", mhs[0])
    print("NIM         :", mhs[1])
    print("Nilai Tugas :", mhs[2])
    print("Nilai UTS   :", mhs[3])
    print("Nilai UAS   :", mhs[4])
    print("Nilai Akhir :", round(mhs[5], 2))
    i += 1