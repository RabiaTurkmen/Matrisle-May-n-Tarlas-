
import random
secim = "1"
while True:
    if secim == "1":
        puan=0
        boyut = 0
        while boyut < 10: #Gecersiz boyut degerinde surekli donmesi icin yazdim.
            boyut = int(input("Kac boyutunda mayin tarlasi istersiniz->(En az 10x10)"))
            if boyut < 10:
                print("10'dan buyuk bir boyut giriniz.\n")
        mayin_sayisi = int(boyut * boyut * 0.3)
        acik_mod = []
        gizli_mod = []

        # Acik mod olusturma kismi:
        for i in range(boyut):
            acik_mod.append("*" * boyut)
        for i in range(mayin_sayisi):
            index1 = random.randint(0, boyut - 1)
            index2 = random.randint(0, boyut - 1)
            while True:
                if acik_mod[index1][index2] == "*":
                    break
                else:
                    index1 = random.randint(0, boyut - 1)
                    index2 = random.randint(0, boyut - 1)
            degisecek_yer = acik_mod[index1]
            degisecek_yer = degisecek_yer[0:index2:1] + "0" + degisecek_yer[index2 + 1:boyut:1]
            acik_mod[index1] = degisecek_yer #List icinde str kullandigim icin mayinlari dilimleme yontemiyle yerlestirdim.

        # Gızlı mod olusturma kismi:
        for i in range(boyut):
            gizli_mod.append("?" * boyut)
        print("Mayin tarlasi olusturuldu.")

        # Sadece mayinlarin oldugu tarla:
        #Bu alani mayina basildiginde goruntulemek icin yaptim.
        sadece_mayin = acik_mod.copy()
        for i in range(boyut):
            for j in range(boyut):
                if acik_mod[i][j] == "0":
                    degisecek_yer = sadece_mayin[i]
                    degisecek_yer = degisecek_yer[0:j:1] + "X" + degisecek_yer[j + 1::1]
                    sadece_mayin[i] = degisecek_yer
                else:
                    degisecek_yer = sadece_mayin[i]
                    degisecek_yer = degisecek_yer[0:j:1] + " " + degisecek_yer[j + 1::1]
                    sadece_mayin[i] = degisecek_yer

        # 5 ve 35 satir arasini oyunda sadece 1 kez yapilan kisimlar icin alttaki dongunun disinda yazdim.
        while True:
            if secim=="2":
                break
            while True: #Gecerli deger girene kadar sormasi icin dongu kullandim.
                print("Hangi modda gormek istersiniz?\n1->Gizli Mod\n2->Acik Mod")
                mod = input()
                if mod == "1":
                    for k in gizli_mod:
                        print(" ".join(k)) #Daha guzel gorunmesi icin bosluk ekledim.
                    break
                elif mod == "2":
                    print("MAYINLI YERLER-> 0")
                    for k in acik_mod:
                        print(" ".join(k)) #Daha guzel gorunmesi icin bosluk ekledim.
                    break
                else:
                    print("Lutfen gecerli bir deger giriniz.(1 veya 2)\n")

            # Acilacak hucreyi belirleme kismi
            while True: #Ayni hucreyi secmesinin onune gecmek icin dongu yazdim.
                print("Lutfen acmak istediginiz hucrenin sirasiyla satir degerini giriniz.")
                satir = int(input())
                while satir > boyut:
                    print("Lutfen gecerli bir sayi giriniz.")
                    satir = int(input())
                satir = satir - 1  # Indexleme mantigi sifirdan basladigi icin
                print("Lutfen acmak istediginiz hucrenin sirasiyla sutun degerini giriniz.")
                sutun = int(input())
                while sutun > boyut:
                    print("Lutfen gecerli bir sayi giriniz.")
                    sutun = int(input())
                sutun = sutun - 1  # Indexleme mantigi sifirdan basladigi icin
                if acik_mod[satir][sutun]!=" ": #Daha once secilmemis hucreyse cikmasi icin yazdim.
                    break
                else:
                    print("Secmis oldugunuz konumu daha once de sectiniz.Lutfen baska bir konum giriniz.\n")



            # Secilen Hucreye Gitme:
            if acik_mod[satir][sutun] == "0":
                print("Mayinli yeri sectiniz.Oyunu kaybettiniz.\nPuaniniz:{}".format(puan))
                print("Tum mayinlar asagida gosteriliyor...")
                for k in sadece_mayin:
                    print(" ".join(k))
                print("1-Oyuna devam etmek\n2-Cikis")
                print("Lutfen yukaridaki menuden secim yapiniz.")
                secim = input()
                break

            else:
                print("Mayin olmayan yeri sectiniz.Hucremiz tarladan silindi.")

                if puan==int(boyut*boyut*0.7):
                    print("Tebrikler!Oyunu kazandiniz.\nTum mayinlari buldunuz.\nPuaniniz:{}".format(puan))
                    print("1-Oyuna devam etmek\n2-Cikis")
                    print("Lutfen yukaridaki menuden secim yapiniz.")
                    secim = input()
                    break
                puan += 1
                # Acik moddan silme kismi:
                degisecek_yer = acik_mod[satir]
                degisecek_yer = degisecek_yer[0:sutun:1] + " " + degisecek_yer[sutun + 1::1]
                acik_mod[satir] = degisecek_yer

                # Gizli moddan silme kismi:
                degisecek_yer = gizli_mod[satir]
                degisecek_yer = degisecek_yer[0:sutun:1] + " " + degisecek_yer[sutun + 1::1]
                gizli_mod[satir] = degisecek_yer

                # Mayin durumu goruntuleme:
                # Kosede bulunma durumu:
                if (satir == 0 and sutun == 0) or (satir == 0 and sutun == boyut - 1) or (
                        satir == boyut - 1 and sutun == 0) or (satir == boyut - 1 and sutun == boyut - 1):
                    sayac = 0
                    # Sol ust kose olma durumu:
                    if satir == 0 and sutun == 0:
                        if acik_mod[0][1] == "0":
                            sayac += 1
                        if acik_mod[1][0] == "0":
                            sayac += 1
                        if acik_mod[1][1] == "0":
                            sayac += 1

                    # Sag ust kose olma durumu:
                    elif satir == 0 and sutun == boyut - 1:
                        if acik_mod[0][boyut - 2] == "0":
                            sayac += 1
                        if acik_mod[1][boyut - 2] == "0":
                            sayac += 1
                        if acik_mod[1][boyut - 1] == "0":
                            sayac += 1

                    # Sol alt kose olma durumu:
                    elif satir == boyut - 1 and sutun == 0:
                        if acik_mod[boyut - 2][0] == "0":
                            sayac += 1
                        if acik_mod[boyut - 1][1] == "0":
                            sayac += 1
                        if acik_mod[boyut - 2][1] == "0":
                            sayac += 1

                    # Sag alt kose olma durumu:
                    elif satir == boyut - 1 and sutun == boyut - 1:
                        if acik_mod[boyut - 2][boyut - 1] == "0":
                            sayac += 1
                        if acik_mod[boyut - 1][boyut - 2] == "0":
                            sayac += 1
                        if acik_mod[boyut - 2][boyut - 2] == "0":
                            sayac += 1

                    print("Sectiginiz hucrenin cevresinde {} tane mayin vardir.\n".format(sayac))


                # Ortada olma durumu:
                elif (satir != 0 and satir != boyut - 1) and (sutun != 0 and sutun != boyut - 1):
                    sayac = 0
                    if acik_mod[satir][sutun + 1] == "0":
                        sayac += 1
                    if acik_mod[satir][sutun - 1] == "0":
                        sayac += 1
                    for i in range(3):
                        if acik_mod[satir + 1][sutun - 1 + i] == "0":
                            sayac += 1
                        if acik_mod[satir-1][sutun-1+i]=="0":
                            sayac+=1
                    print("Sectiginiz hucrenin cevresinde {} tane mayin vardir.\n".format(sayac))


                else:
                    # Sol kenarda olma durumu:
                    sayac = 0
                    if (sutun == 0 and satir != 0) or (sutun == 0 and satir != boyut - 1):
                        if acik_mod[satir - 1][sutun] == "0":
                            sayac += 1
                        if acik_mod[satir - 1][sutun + 1] == "0":
                            sayac += 1
                        if acik_mod[satir][sutun + 1] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun + 1] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun] == "0":
                            sayac += 1

                    # Sag kenarda olma durumu:
                    elif (sutun == boyut - 1 and satir != 0) or (sutun == boyut - 1 and satir != boyut - 1):
                        sayac = 0
                        if acik_mod[satir - 1][sutun] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun] == "0":
                            sayac += 1
                        if acik_mod[satir][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir - 1][sutun - 1] == "0":
                            sayac += 1

                    # Ust kenarda olma durumu:
                    elif (satir == 0 and sutun != 0) or (satir == 0 and sutun != boyut - 1):
                        sayac = 0
                        if acik_mod[satir][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir][sutun + 1] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun] == "0":
                            sayac += 1
                        if acik_mod[satir + 1][sutun + 1] == "0":
                            sayac += 1

                    # Alt kenarda olma durumu:
                    elif (satir == boyut - 1 and sutun != boyut - 1) or (satir == boyut - 1 and sutun != 0):
                        sayac = 0
                        if acik_mod[satir][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir][sutun + 1] == "0":
                            sayac += 1
                        if acik_mod[satir - 1][sutun - 1] == "0":
                            sayac += 1
                        if acik_mod[satir - 1][sutun] == "0":
                            sayac += 1
                        if acik_mod[satir - 1][sutun + 1] == "0":
                            sayac += 1
                    print("Sectiginiz hucrenin cevresinde {} tane mayin vardir.\n".format(sayac))

    elif secim == "2":
        print("Programi kapattiniz!")
        quit()

    else:
        print("Lutfen gecerli bir sayi giriniz(1 veya 2)\n")
        secim = 0
        while secim == 0:
            print("Lutfen asagidaki menuden secim yapiniz:\n1-Oyuna devam etmek\n2-Cikis")
            secim = input("Seciminizi Giriniz:")
