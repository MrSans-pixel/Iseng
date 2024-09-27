# Membuat fungsi baru bernama "introScene"
def introScene():
  operasi = ["tambah", "kurang", "kali", "bagi"] # List operasi yang dapat digunakan
  print("Apa yang ingin kau lakukan dengan angkamu?")
  userInput = ""
  while userInput not in operasi:
    print("Pilihan: tambah/kurang/kali/bagi")
    userInput = input("Masukkan pilihanmu: ")
    if userInput == "tambah": # Operasi Penjumlahan
      tambah = angka1 + angka2
      print(f"{angka1} + {angka2} = {tambah}")
      lanjutan()
    elif userInput == "kurang": # Operasi Pengurangan
      kurang = angka1 - angka2
      print(f"{angka1} - {angka2} = {kurang}")
      lanjutan()
    elif userInput == "kali": # Operasi Perkalian
      kali = angka1 * angka2
      print(f"{angka1} * {angka2} = {kali}")
      lanjutan()
    elif userInput == "bagi": # Operasi Pembagian
      if angka2 == 0: # Jika angka2 == 0, pembagian tidak dapat dijalankan.
        print("Pembagian dengan 0 tidak diperbolehkan")
      else:
        bagi = angka1 / angka2
        print(f"{angka1} / {angka2} = {bagi}")
      lanjutan()
    else:
      print("Mohon masukkan pilihan yang sudah disediakan!")

# Membuat fungsi baru bernama "lanjutan"
def lanjutan():
  pilih = ["ya", "tidak"]
  print("Apakah kau ingin melanjutkan?")
  userInput = ""
  while userInput not in pilih:
    print("ya atau tidak")
    userInput = input()
    if userInput == "ya":
      introScene()
    elif userInput == "tidak":
      exit()
    else:
      print("Masukkan pilihanmu.")

# Main Source
if __name__ == "__main__":
  while True:
    angka1 = float(input("Masukkan angka pertama: "))
    print(f"Angka pertamamu adalah {angka1}")
    angka2 = float(input("Masukkan angka kedua: "))
    print(f"Angka keduamu adalah {angka2}\n")
    introScene()