# import os 

# def konversi_sampah() :
#     sampah = {   
#         1: "plastik",
#         2: "kertas",
#         3: "kardus",
#         4: "kaca",
#         5: "logam"
#     }
#     harga = {
#         1: 3, 
#         2: 2,
#         3: 2,
#         4: 4,
#         5: 7
#     }

#     daftar_rincian = {}
#     daftar_berat = []
#     total = 0
#     while True :
#         os.system("cls")
#         print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█") 
#         print("█                                                              █")
#         print("█                    \033[1;1mSilahkan setor sampahmu\033[0m                   █")
#         print("█                                                              █")
#         print("█  1. Plastik                                                  █")
#         print("█  2. Kertas                                                   █")
#         print("█  3. Kardus                                                   █")
#         print("█  4. Kaca                                                     █")
#         print("█  5. Logam                                                    █")
#         print("█  6. Cetak struk                                              █")
#         print("█  7. kembali ke menu                                          █")
#         print("█                                                              █")
#         print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         x = int(input("Silahkan pilih jenis sampah yang akan disetor (1-5): "))
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         if x == 1 :
#             os.system("cls")
#             print("\n################################################################")
#             print("#                        SAMPAH PLASTIK                        #")                          
#             print("#       harga dari sampah plastik sebesar Rp3 per gram         #")
#             print("################################################################\n")            
#             print("================================================================")        
#             a = int(input("Masukkan berat sampah : "))
#             print("================================================================\n")
#             daftar_berat.append(a)
#             b = a * 3
#             total += b
#             daftar_rincian.update({x : a}) 
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print(f"{a:,.0f} gram plastik menjadi Rp{b:,.0f}".replace(',', '.'))
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("\n================================================================")
#             print(f"total dari sampah yang telah disetorkan sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("================================================================\n")
#             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
#         elif x == 2 :
#             os.system("cls")
#             print("\n################################################################")
#             print("#                        SAMPAH KERTAS                         #")                          
#             print("#        harga dari sampah kertas sebesar Rp. 2 per gram       #")
#             print("################################################################\n")            
#             print("================================================================")        
#             a = int(input("Masukkan berat sampah : "))
#             print("================================================================\n")
#             daftar_berat.append(a)
#             b = a * 2
#             total += b
#             daftar_rincian.update({x : a}) 
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print(f"{a:,.0f} gram kertas menjadi Rp{b:,.0f}".replace(',', '.'))
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("\n================================================================")
#             print(f"total dari sampah yang telah disetorkan sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("================================================================\n")
#             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#         elif x == 3 :
#             os.system("cls")
#             print("\n################################################################")
#             print("#                         SAMPAH KARDUS                        #")                          
#             print("#       harga dari sampah kardus sebesar Rp. 2 per gram        #")
#             print("################################################################\n")            
#             print("================================================================")        
#             a = int(input("Masukkan berat sampah : "))
#             print("================================================================\n")
#             daftar_berat.append(a)
#             b = a * 2
#             total += b
#             daftar_rincian.update({x : a}) 
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print(f"{a:,.0f} gram kardus menjadi Rp{b:,.0f}".replace(',', '.'))
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("\n================================================================")
#             print(f"total dari sampah yang telah disetorkan sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("================================================================\n")
#             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
#         elif x == 4 :
#             os.system("cls")
#             print("\n################################################################")
#             print("#                         SAMPAH KACA                          #")                          
#             print("#        harga dari sampah kaca sebesar Rp. 4 per gram         #")
#             print("################################################################\n")            
#             print("================================================================")        
#             a = int(input("Masukkan berat sampah : "))
#             print("================================================================\n")
#             daftar_berat.append(a)
#             b = a * 4
#             total += b
#             daftar_rincian.update({x : a}) 
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print(f"{a:,.0f} gram kaca menjadi Rp{b:,.0f}".replace(',', '.'))
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("\n================================================================")
#             print(f"total dari sampah yang telah disetorkan sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("================================================================\n")
#             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#         elif x == 5 :
#             os.system("cls")
#             print("\n################################################################")
#             print("#                         SAMPAH LOGAM                         #")                          
#             print("#        harga dari sampah logam sebesar Rp. 7 per gram        #")
#             print("################################################################\n")            
#             print("================================================================")        
#             a = int(input("Masukkan berat sampah : "))
#             print("================================================================\n")
#             daftar_berat.append(a)
#             b = a * 7
#             total += b
#             daftar_rincian.update({x : a}) 
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print(f"{a:,.0f} gram logam menjadi Rp{b:,.0f}".replace(',', '.'))
#             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("\n================================================================")
#             print(f"total dari sampah yang telah disetorkan sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("================================================================\n")
#             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#         elif x == 6 :
#             os.system("cls")
#             print("\n\n================================================================")
#             print("---------------------- STRUK PEMBAYARAN ------------------------")
#             print("================================================================") 
#             print("                                                              ")            
#             print("     Rincian total penyetoran :                                    ")
#             print("                                                              ")
#             for kode, a in daftar_rincian.items():
#                 if kode in harga :
#                     print(f"     {a:,.0f} gram {sampah[kode]} x Rp{harga[kode]:,.0f}  = Rp{harga[kode]*a:,.0f}".replace(',', '.'))
#             print("                                                              ")
#             print("----------------------------------------------------------------")
#             print(f" Sampah anda telah menjadi uang sebesar Rp{total:,.0f}".replace(',', '.'))
#             print("----------------------------------------------------------------")
#             print("                                                              ")            
#             print("================================================================ ")
#             print("        Terimakasih sudah menggunakan jasa layanan kami         ")
#             print("          Kepedulian anda sangat berarti dalam menjaga          ")
#             print("         kebersihan dan keberlanjutan bumi kita bersama         ")
#             print("================================================================ ")
#             print("              \033[1;3m>>>  HARUS DATANG KEMBALI YAA  <<<\033[0m               ")
#             print("================================================================ ")
#             print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             print("          >>>  tekan enter untuk kembali ke menu  <<<          ")
#             q = input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#             konversi_sampah()

#         elif x == 7 :
#             os.system("cls")
#             print("================================================================")
#             print("|                                                              |")
#             print("|                         terima kasih                         |")
#             print("|                             😁😁                             |")
#             print("|                                                              |")
#             print("|                      Sampai jumpa lagi!                      |")
#             print("|                                                              |")
#             print("================================================================")
#             print("\n================================================================")        
#             print("        >>>  Tekan enter untuk kembali ke menu utama  <<<       ")
#             print("================================================================")
#             back = input(" ")
#             break
            
#         else :
#             print("\n================================================================")
#             print("      >>>  Input salah! Masukkan kode input yang benar  <<<   ")
#             print("================================================================\n")
#             print("\n================================================================")
#             print("     >>>  tekan enter untuk kembai ke menu konversi sampah  <<<     ")
#             q = input("================================================================\n")


# konversi_sampah()


