import os

def tampilkan_faq():
    faq = {
        "1": "Tidak ada batasan minimal berat sampah yang bisa dijual melaluiprogram kami. "
           "Kami menghapus batasan tersebut untuk mendorong partisipasi yang lebih luas.",  
        "2": "Aplikasi pengolahan sampah kami hanya untuk jenis sampah anorganik, termasuk plastik, kertas, kaleng, dan kardus. "
            "Jika ada sampah yang tidak masuk ke dalam kategori tersebut, hubungi dukungan pelanggan kami.",
        "3": "Pengguna memilih jenis sampah, memasukkan berat sampah, dan mengonfirmasi transaksi. Sampah kemudian diantarkan "
            "ke lokasi yang ditentukan, diproses, dan didaur ulang sesuai standar lingkungan yang berlaku.",
        "4": "Sampah plastik, kertas, kaleng, dan kardus yang diserahkan akan didaur ulang. Kami akan memberikan konfirmasi "
            "dan laporan dampak lingkungan kepada pengguna setelah proses daur ulang selesai.",
        "5": "Sebagian dari pendapatan penjualan sampah didaur ulang akan didonasikan untuk mendukung proyek-proyek lingkungan, "
            "seperti penanaman pohon dan kampanye daur ulang. Laporan transparansi penggunaan dana donasi dapat diakses oleh pengguna.",
        "6": "Sampah organik memerlukan proses pengelolaan yang berbeda dan tidak dapat dijual melalui aplikasi kami. "
            "Kami mendorong pengguna untuk mengelola sampah organik dengan cara komposting di rumah.",
        "7": "Jika pertanyaan Anda tidak terdaftar di FAQ atau ingin memberikan kritik dan saran, silakan hubungi kami di nomor kontak: +62 813-3566-9787."
    }

    while True:
        os.system("cls")
        print('█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█')
        print("█ FAQ seputar program pengelolaan sampah:                          █")
        print("█ ============================================================     █")
        print("█ 1. Berapa minimal kuantiti sampah yang bisa dijual?              █")
        print("█ 2. Bagaimana jika ada jenis sampah yang tidak masuk ke           █")
        print("█    dalam kategori?                                               █")
        print("█ 3. Bagaimana cara kerja dari program ini?                        █")
        print("█ 4. Apa proses selanjutnya jika sampah sudah diserahkan           █")
        print("█    kepada pengelola?                                             █")
        print("█ 5. Bagaimana sistem penyaluran donasi pada program ini?          █")
        print("█ 6. Mengapa jenis sampah organik tidak dapat dijual melalui       █")
        print("█    program ini?                                                  █")
        print("█ 7. Jika pertanyaan tidak ada di daftar FAQ, silakan              █")
        print("█    menghubungi contact person.                                   █")
        print("█ 8. Kembali ke menu                                               █ ")
        print("█ ============================================================     █")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        pertanyaan = input("Pilih pertanyaan (1-7, atau 8 untuk keluar): ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        if pertanyaan == "8":
            os.system("cls")
            print("====================================================================")
            print("|                                                                  |")
            print("|           Terima kasih telah menggunakan layanan kami            |")
            print("|    Teruslah bersama kami dalam menciptakan perubahan positif!    |")
            print("|                               😁😁                               |")
            print("|                                                                  |")
            print("|                       Sampai jumpa lagi!                         |")
            print("|                                                                  |")
            print("====================================================================")  
            print("")
            print("\n====================================================================")        
            print("          >>>  Tekan enter untuk kembali ke menu utama  <<<       ")
            print("====================================================================")
            back = input(" ")
            break
            
        elif pertanyaan in faq:
            jawaban = faq[pertanyaan]
            baris_jawaban = [jawaban[j:j+63] for j in range(0, len(jawaban), 63)]
            print("Jawaban:")
            print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
            for baris in baris_jawaban:
                print(f"{'█ ' + baris.ljust(64) + ' █'}")
            print('█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')
            print("")
            print("====================================================================")        
            print("              >>>  Tekan enter untuk kembali ke FAQ  <<<          ")
            print("====================================================================")
            back = input(" ")   

        else:
            print("\n===================================================================")
            print("       >>>  Input salah! Masukkan kode input yang benar  <<<   ")
            print("===================================================================\n")
            print("\n====================================================================")
            print("            >>>  tekan enter untuk kembai ke menu faq  <<<        ")
            q = input("====================================================================\n")
