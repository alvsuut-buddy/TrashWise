import alamat, os

def main_donasi():
    while True :
        os.system("cls")
        print("================================================================")
        print("| $$$$$$$                                            $$$$$$$$  |")
        print("|                      Selamat Datang                          |")
        print("|                    Silahkan berdonasi                        |")
        print("|                                                              |")
        print("|           Bantuan kalian akan sangat berguna untuk           |")
        print("|              keberlangsungan bumi tercinta kita              |")
        print("| $$$$                                                   $$$$  |")
        print("================================================================")
        print("")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      Metode Berdonasi                        ║")
        print("║                                                              ║")
        print("║ 1. Tunai                                                     ║")
        print("║ 2. Transfer bank                                             ║")
        print("║ 3. Kembali ke menu utama                                     ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        pilihan_donasi = input("Pilih cara berdonasi : ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        if pilihan_donasi == "1" :
            print("################################################################")
            print("#    Silahkan datang langsung ke kantor TrashWise terdekat     #")
            print("#                    😁 Terima Kasih 😁                        #")
            print("################################################################")
            print("")
            print("================================================================")        
            print("           >>>  Tekan enter untuk melihat alamat  <<<          ")
            print("================================================================")
            back = input(" ")
            alamat.main_alamat()

        elif pilihan_donasi == "2" :
            os.system("cls")
            print("╔══════════════════════════════════════════════════════════════╗")
            print("║                    Daftar Bank TrashWise                     ║")
            print("║                                                              ║")
            print("║ 1. Bank BCA                                                  ║")
            print("║    7927201155 (a.n. Kantor TrashWise)                        ║")
            print("║                                                              ║")
            print("║ 2. Bank BNI                                                  ║")
            print("║    42838524 (a.n. Kantor TrashWise)                          ║")
            print("║                                                              ║")
            print("║ 3. Bank Mandiri                                              ║")
            print("║    1350019686773 (a.n. Kantor TrashWise)                     ║")
            print("║                                                              ║")
            print("╚══════════════════════════════════════════════════════════════╝")
            print("\n\n================================================================")        
            print("           >>>  Tekan enter untuk kembali ke menu  <<<          ")
            print("================================================================")
            back = input(" ")

        elif pilihan_donasi == "3" :
            os.system("cls")
            print("================================================================")
            print("|                                                              |")
            print("|            Terima kasih banyak atas dukungan Anda            |")
            print("|                      kepada TrashWise!                       |")
            print("|                                                              |")
            print("|                  Dengan kebaikan hati Anda,                  |")
            print("|              kami bisa terus menjaga lingkungan              |")
            print("|                 dan memberdayakan komunitas.                 |")
            print("|                                                              |")
            print("|  Teruslah bersama kami dalam menciptakan perubahan positif!  |")
            print("|                           😁😁                               |")
            print("|                                                              |")
            print("================================================================")  
            print("\n\n================================================================")        
            print("         >>>  Tekan enter untuk kembali ke menu utama  <<<          ")
            print("================================================================")
            back = input(" ")    
            break 

        else :
            print("\n================================================================")
            print("      >>>  Input salah! Masukkan kode input yang benar  <<<   ")
            print("================================================================\n")
            print("\n================================================================")
            print("        >>>  tekan enter untuk kembai ke menu donasi  <<<        ")
            q = input("================================================================\n")







