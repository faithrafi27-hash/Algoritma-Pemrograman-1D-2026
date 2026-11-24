tugas = {}

while True:
    nama = input("Masukkan nama tugas (ketik selesai untuk berhenti): ")

    if nama == "selesai":
        break

    if nama in tugas:
        print("Tugas sudah ada.")
    else:
        tugas[nama] = "Belum selesai"
        print("Tugas berhasil ditambahkan.")
print()
print("1. Tandai Tugas Selesai")
print("2. Hapus Tugas")
print("3. Tampilkan Tugas")
print("4. Jumlah Tugas")
print("5. Keluar")

jalan = True

while jalan:
    pilih = input("\nPilih menu: ")

    if pilih == "1":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "2":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "3":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama, status in tugas.items():
                print(nama, ":", status)

    elif pilih == "4":
        selesai = 0
        belum = 0

        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    elif pilih == "5":
        print("Program selesai.")
        jalan = False

    else:
        print("Pilihan tidak tersedia.")
