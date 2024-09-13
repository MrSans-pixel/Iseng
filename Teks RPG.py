# Global Variabel
senjata = False
arah = []
import random 

# Intro
def introScene():
	arah = ["kiri", "kanan", "maju"]
	print("Akhirnya aku sampai didalam dungeon yang dirumorkan itu.\nSudah saatnya aku bersinar.")
	print("\"Kemana aku harus pergi?\"")
	userInput = ""
	while userInput not in arah:
		print("Pilihan: kanan/kiri/maju/mundur")
		userInput = input()
		if userInput == "kiri":
			makhlukHytam()
		elif userInput == "kanan":
			ruangTulang()
		elif userInput == "maju":
			ruangBerhantu()
		elif userInput == "mundur":
			print("Hah! Pintu dungeonnya tertutup?\nSepertinya aku harus mencari jalan lain.")
		else:
			print("Woy! Kemana aku harus pergi sialan.")
	
# Sosok Hytam
def makhlukHytam():
	arah = ["kanan"]
	print("Makhluk apa itu? Hytam banget njir. Waspadalah sosok hytam!!!")
	print("\"Kemana aku harus pergi?\"")
	userInput = ""
	while userInput not in arah:
		print("Pilihan: kanan/kiri")
		userInput = input()
		if userInput == "kiri":
			secretScene()
		elif userInput == "kanan":
			print("Lah? Jalan buntu njir.")
		else:
			print("Woy! Kemana aku harus pergi sialan.")
			
# Ending Rahasia
def secretScene():
	arah = ["maju"]
	print("Apaan tuh? Kamera? Punya siapa nih?\nPasti ada orang lain yang baru saja dari sini.")
	print("\"Kemana aku harus pergi?\"")
	userInput = ""
	while userInput not in arah:
		print("Pilihan: MAJU")
		userInput = input()
		if userInput == "maju":
			print("Apakah itu cahaya? Hore!!!\nAkhirnya, aku bisa keluar dari dungeon ini.")
			print("\"Selamat!! Kamu berhasil keluar dan menamatkan dungeon.\"")
			exit()
		else:
			print("Woy! Kemana aku harus pergi sialan.")
			
# Ruang Penuh Tulang
def ruangTulang():
	arah = ["maju"]
	global senjata
	print("Kenapa ada banyak sekali tulang diruangan ini?\nPasti ini adalah sarang dari monster penguasa dungeon ini.")
	print("\"Kemana aku harus pergi?\"")
	userInput = ""
	while userInput not in arah:
		print("Pilihan: kiri/kanan/maju")
		userInput = input()
		if userInput == "kanan":
			senjata = True
			print("Apa itu? Sebilah pedang?\nMungkin aku bisa menggunakan ini untuk membunuh monster itu.")
		elif userInput == "maju":
			munculMonster()
		elif userInput == "kiri":
			print("Aduhai, jalan buntu cik.")
		else:
			print("Woy! Kemana aku harus pergi sialan.")

# Kemunculan Penguasa Dungeon
def munculMonster():
	tindakan = ["serang"]
	global senjata
	print("\"Saat kau memasuki ruangan, monster dengan mulut yang dipenuhi darah itu seperti sudah mengetahui kedatanganmu.\"")
	print("Jadi selama ini kau berada disini. Sungguh sosok monster yang menjijikkan.")
	print("\"Apa yang harus kulakukan?\"")
	userInput = ""
	while userInput not in tindakan:
		print("Pilihan: serang/kabur")
		userInput = input()
		if userInput == "serang":
			if senjata:
				print("Kau tidak beruntung karena aku punya pedang ini.")
				print("Akan kuakhiri kau dengan pedang ini.\nRasakan ini!!!\n•••••")
				print("Kau cukup tangguh. Sayangnya kau bertemu denganku.\nSekarang, setelah monster ini mati ditanganku, dungeon ini telah kukuasai.")
				print("Selamat!! Kau berhasil menjadi penguasa dari dungeon ini.")
				exit()
			else:
				print("Sial! Aku tidak punya senjata untuk melawannya.\nSepertinya ini adalah akhir dari journeyku.")
				print("\"Kau mati dibunuh monster penguasa dungeon.\"")
		elif userInput == "kabur":
			print("Sebaiknya aku kabur selagi aku bisa.")
			print("\"Sayangnya, saat kau mencoba kabur,\nkau terjatuh dan pada akhirnya dilahap oleh monster itu.\"")
			print("\"Kau mati dilahap monster penguasa dungeon.\"")
		else:
			print("Woy! Apa yang harus kulakukan sialan.")
			
# Ruang Berhantu
def ruangBerhantu():
	arah = ["kanan", "kiri"]
	print("Kenapa tiba-tiba terasa dingin di dalam ruangan ini?\nNampaknya ada yang tidak beres.")
	print("Sebaiknya aku lebih berhati-hati")
	print("\"Kemana aku harus pergi?\"")
	userInput = ""
	while userInput not in arah:
		print("Pilihan: kanan/kiri/maju")
		userInput = input()
		if userInput == "kiri":
			print("APA INI? Ada kuburan didalam dungeon? Sebaiknya aku segera pergi.")
			print("\"Saat kau berusaha pergi. Tanpa kau sadari, kau telah dikepung segerombolan hantu yang marah.\"")
			print("\"Jiwamu mati diseret para hantu ke alam kubur.\"")
			exit()
		elif userInput == "maju":
			print("Bagaimana caraku maju? Menghancurkan tembok didepan sana? Yang bener aja.")
		elif userInput == "kanan":
			print("Instingku mengatakan kalau aku harus pergi ke tempat yang sangat gelap itu.\nSemoga intingku tidak menghianatiku.")
			print("\"Kau masuk kedalam ruangan yang sangat gelap.\nKau terus berjalan tanpa tau harus kemana.\nDisaat kau menyadarinya, kau sudah berada diluar dungeon.\"")
			print("Selamat!! Kau berhasil keluar dari dungeon tanpa disengaja.")
			exit()
		else:
			print("Woy! Kemana aku harus pergi sialan.")
	
# Main Source
if __name__ == "__main__":
	while True:
		print('Halo dunia!')
		name = input("Namaku: ")
		print(f"Aku adalah si hebat {name}.")
		print("Aku akan menaklukkan dungeon yang dirumorkan itu dengan tanganku sendiri.\n•••••")
		introScene()