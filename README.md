## Nama : Varel Nico Ramadhan
## Nim  : 312510156

📘 PENJELASAN PROGRAM SECARA LENGKAP

Program ini digunakan untuk mengelola daftar nilai mahasiswa menggunakan dictionary di Python.
Pengguna dapat menambah, mengubah, menghapus, menampilkan, dan mencari data mahasiswa.

🔹 1. Dictionary Data Mahasiswa
data_mahasiswa = {}


Semua data mahasiswa akan disimpan dalam dictionary dengan format:

data_mahasiswa[nama] = {
    "tugas": nilai,
    "uts": nilai,
    "uas": nilai,
    "akhir": nilai_akhir
}

🔹 2. Fungsi hitung_nilai_akhir()
def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)


Fungsi ini menghitung nilai akhir berdasarkan bobot:

Tugas : 30%

UTS : 35%

UAS : 35%

🔹 3. Menu Utama (Looping while True)

Program menampilkan menu dan meminta pengguna memilih salah satu:

1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
0. Keluar


Proses berlangsung terus sampai pengguna memilih 0.

🔹 4. Tambah Data (Menu 1)

Program meminta input:

nama

nim

nilai tugas

nilai UTS

nilai UAS

Lalu menghitung nilai akhir, kemudian menyimpan data ke dictionary.

🔹 5. Ubah Data (Menu 2)

Pengguna memasukkan nama mahasiswa yang akan diubah.

Jika ditemukan, data diperbarui dengan input nilai baru.

Jika tidak ditemukan → tampil pesan "Data tidak ditemukan!"

🔹 6. Hapus Data (Menu 3)

Pengguna memasukkan nama mahasiswa yang ingin dihapus.

Jika ada → data dihapus.

Jika tidak → muncul pesan.

🔹 7. Tampilkan Semua Data (Menu 4)

Menampilkan semua mahasiswa dalam dictionary.

Jika data kosong → tampil "Belum ada data."

🔹 8. Cari Data (Menu 5)

Pengguna memasukkan nama.
Jika ada, tampil data mahasiswa.

🔹 9. Keluar (Menu 0)

Mengakhiri program.
