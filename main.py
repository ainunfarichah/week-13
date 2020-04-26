import function

loopmaster=True
while loopmaster:
    print ("MENU")
    print ("1. Melihat Data Siswa 2. Menghitung Volume Prisma dan Limas")
    pilihan = int (input ("Masukkan pilihan: "))
    if pilihan == 1 :
        if __name__ == "__main__":

          listNama = ("Ainun", "Linda", "Karin", "Santi", "Dian")
          listKELAS = [ 8, 8, 8, 8, 8 ]

        listfunction = []

        for i in range(len(listKELAS)):
            listfunction.append(function.function(listNama[i], listKELAS[i]))


        for j in range(len(listfunction)):
            print(" NAMA: {} ".format(listfunction[j].show_NAMA()))
            print(" KELAS: {} ".format(listfunction[j].show_KELAS()))
    elif pilihan == 2 :
      print("Menghitung Volume Prisma Segitiga dan Limas Segitiga")
      t = int(input("Masukkan tinggi Prisma: "))
      ts = int(input("Masukkan tinggi segitiga (alas): "))
      ss = int(input("Masukkan alas segitiga (alas): "))

      print ("Volume Prisma Segitiga = {}". format(function.prisma().add(t, ts, ss)))

      t = int(input("Masukkan tinggi Prisma: "))
      ts = int(input("Masukkan tinggi segitiga (alas): "))
      ss = int(input("Masukkan alas segitiga (alas): "))

      print ("Volume Limas Segitiga = {}". format(function.limas().add(t, ts, ss)))

      print ("Asal kalian tahu, Volume Limas adalah 1/3 dari Volume Prisma (jika tinggi dan luas alasnya sama)")

    print ("")
    lagi = input ("Mau kembali ke menu ? (y/n) : ")
    if lagi == 'n' :
        loopmaster = False



