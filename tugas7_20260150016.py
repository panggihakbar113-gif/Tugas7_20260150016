import modul_evaluasi

def input_angka_valid(prompt, min_val, max_val):
    while True:
        try:
            angka = float(input(prompt))

            if angka < min_val or angka > max_val:
                print(f"Warning: Input harus antara {min_val} " f"hingga {max_val}.")
            else:
                return angka

        except ValueError:
            print("Error: Input harus berupa angka! Silakan coba lagi.")

def main():
    while True:
        print("\n====================================")
        print(" SISTEM EVALUASI KELAYAKAN ASISTEN LAB AI ")
        print("====================================")
        print("1. Hitung Kelayakan")
        print("2. Keluar")
        print("====================================")

        try:
            pilihan = int(input("Pilih menu (1/2): "))

            if pilihan == 1:
                print("\n--- INPUT DATA MAHASISWA ---")
                nama = input("Masukkan Nama: ")
                nim = input("Masukkan NIM: ")
                hadir = input_angka_valid("Jumlah Kehadiran (0-14): ", 0, 14)
                tugas = input_angka_valid("Nilai Tugas (0-100): ", 0, 100)
                ucp1 = input_angka_valid("Nilai UCP 1 (0-100): ", 0, 100)
                ucp2 = input_angka_valid("Nilai UCP 2 (0-100): ", 0, 100)

                # Menghitung persentase kehadiran
                persentase = modul_evaluasi.hitung_persentase_presensi(hadir)

                # Menghitung nilai akhir
                nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)

                # Menentukan status kelayakan
                status = modul_evaluasi.cek_kelayakan_asisten_lab_AI(persentase, nilai_akhir)

                # Hasil evaluasi
                print("\n===============================")
                print("       HASIL EVALUASI ASISTEN LAB AI")
                print("====================================")
                print(f"Nama                 : {nama}")
                print(f"NIM                  : {nim}")
                print(f"Jumlah Kehadiran     : {hadir:g}/14")
                print(f"Persentase Kehadiran : {persentase:.2f}%")
                print(f"Nilai Tugas          : {tugas:.2f}")
                print(f"Nilai UCP 1          : {ucp1:.2f}")
                print(f"Nilai UCP 2          : {ucp2:.2f}")
                print(f"Nilai Akhir          : {nilai_akhir:.2f}")
                print("====================================")
                print(f"STATUS               : {status}")
                print("====================================")

            elif pilihan == 2:
                print("\nTerima kasih. Program selesai.")
                break

            else:
                print("Warning: Pilihan menu hanya 1 atau 2.")

        except ValueError:
            print("Error: Menu harus diisi dengan angka 1 atau 2.")

if __name__ == "__main__":
    main()