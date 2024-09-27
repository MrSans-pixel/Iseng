# Global Variabel
senjata = False
arah = []

# Intro Scene
def introScene():
    arah = ["kiri", "kanan", "maju"]    
    print("Kau menemukan empat jalan ke ruangan yang berbeda-beda, sekarang pilih kemana kau ingin pergi.")
    userInput = ""
    while userInput not in arah:
        print("Pilihan: kiri/kanan/mundur/maju")
        userInput = input()
        if userInput == "kiri":
            showShadowFigure()
        elif userInput == "kanan":
            showSkeletons()
        elif userInput == "maju":
            hauntedRoom()
        elif userInput == "mundur":
            print("Kau menemukan sebuah pintu. Kau membukanya dan hanya menemukan tembok dibaliknya")
        else:
            print("Masukkan pilihan yang benar sialan.")

# Neutral Creature
def showShadowFigure():
    arah = ["kanan", "mundur"]
    print("Kau melihat sesosok makhluk hitam yang memperhatikanmu dari kejauhan. Kau ketakutan.")
    print("Kemana kau ingin pergi?")
    userInput = ""
    while userInput not in arah:
        print("Pilihan: kanan/kiri/mundur")
        userInput = input()
        if userInput == "kanan":
            cameraScene()
        elif userInput == "kiri":
            print("kau menemukan pintu yang mengarahkanmu ke ruang kosong.")
        elif userInput == "mundur":
            introScene()
        else:
            print("Masukkan pilihan yang benar sialan.")

# Safest Way
def cameraScene():
    arah = ["maju", "mundur"]
    print("Kau menemukan sebuah kamera tergeletak di tanah. Seseorang baru saja dari ruangan ini!")
    print("Kemana kau ingin pergi?")
    userInput = ""
    while userInput not in arah:
        print("Pilihan: maju/mundur")
        userInput = input()
        if userInput == "maju":
            print("Kau melihat sebuah cahaya di ujung ruangan.\nKau berlari kearah cahaya itu dan akhirnya keluar dari dungeon itu.")
            print("Selamat! Kau berhasil keluar.")
            quit()
        elif userInput == "mundur":
            showShadowFigure()
        else:
            print("Masukkan pilihan yang benar sialan.")

# Haunted Room
def hauntedRoom():
    arah = ["kanan", "kiri", "mundur"]
    print("Kau tiba-tiba mendengar suara. Kau berpikir kalau kau membangunkan yang telah mati.")
    print("Kemana kau ingin pergi?")
    userInput = ""
    while userInput not in arah:
        print("Pilihan: kanan/kiri/mundur")
        userInput = input()
        if userInput == "kanan":
            print("Muncul banyak hantu marah didepanmu. Mereka menyerangmu tanpa ampun.")
            print("Kau Mati!")
            quit()
        elif userInput == "kiri":
            print("Kau memutuskan mengambil jalan yang sangat gelap.\nTanpa tau arah kau terus maju dan tanpa kau sadari kau telah keluar dari dungeon itu.")
            print("Selamat! Kau berhasil keluar.")
            quit()
        elif userInput == "mundur":
            introScene()
        else:
            print("Masukkan pilihan yang benar sialan.")

# Enemy Encounter
def showSkeletons():
    arah = ["mundur", "maju"]
    global senjata
    print("Kau melihat sekumpulan tulang dan tengkorak berserakan saat memasuki ruangan.\nKau merasa seperti diawasi oleh seseorang.")
    print("Kemana kau ingin pergi?")
    userInput = ""
    while userInput not in arah:
        print("Pilihan: kiri/mundur/maju")
        userInput = input()
        if userInput == "kiri":
            print("Kau menemukan sebuah ruangan dengan kotak ditengahnya.\nSaat kau membukanya, kau menemukan sebuah pedang.")
            senjata = True
        elif userInput == "mundur":
            introScene()
        elif userInput == "maju":
            strangeCreature()
        else:
            print("Masukkan pilihan yang benar sialan.")

# Strange Creature
def strangeCreature():
    tindakan = ["serang", "kabur"]
    global senjata
    print("Seekor monter yang terlihat ganas tiba-tiba menampakkan diri dihadapanmu.\nMonster itu tampaknya ingin menyerangmu. kau bisa menyerang ataupun kabur darinya.")
    print("Apa yang akan kau lakukan?")
    userInput = ""
    while userInput not in tindakan:
        print("Pilihan: serang/kabur")
        userInput = input()
        if userInput == "serang":
            if senjata:
                print("Kau membunuh monster itu dengan pedang yang kau dapatkan di tempat sebelumnya.\nSetelah melanjutkan perjalanan, kau menemukan jalan keluar dari dungeon.")
                print("Selamat! Kau berhasil keluar.")
            else:
                print("Monster itu membunuhmu dengan mudahnya karena kau tidak memiliki apa-apa untuk melindungi dirimu sendiri.")
            quit()
        elif userInput == "kabur":
            showSkeletons()
        else:
            print("Masukkan pilihan yang benar sialan.")

# Main Function
if __name__ == "__main__":
    while True:
        print("Selamat datang di game petualangan ini!")
        print("Sebagai seorang adventurer, dengan berani kau memutuskan untuk pergi berpetualang menjelajahi dunia.")
        print("Namun sayangnya, saat dalam petualanganmu, kau tak sengaja tersesat kedalam dungeon.")
        print("Kau harus mencari jalan untuk keluar dari dungeon tersebut.")
        name = input("Mari mulai dengan namamu: ")
        print(f"Semoga beruntung, {name}.")
        introScene()
