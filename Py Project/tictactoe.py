# Import Module
import pygame
from pygame.locals import *

pygame.init()

# Konstanta
LEBAR_SCR = 300
TINGGI_SCR = 300
LEBAR_GARIS = 6
PLAYER_X = 1
PLAYER_O = -1
KOSONG = 0
GRID = 100

# Variabel
penanda = []
pos = []
player = 1
pemenang = 0
game_over = False

# Warna
hijau = (0, 255, 0)
merah = (255, 0, 0)
biru = (0, 0, 255)
putih = (255, 255, 255)
bg = (255, 255, 200)
garis = (50, 50, 50)

# Layar Game
screen = pygame.display.set_mode((LEBAR_SCR, TINGGI_SCR))
pygame.display.set_caption('TicTacToe')

# Font
font = pygame.font.SysFont(None, 40)

# Buat Persegi
rect_ulang = Rect(LEBAR_SCR // 2 - 88, TINGGI_SCR // 2, 160, 50)
rect_keluar = Rect(LEBAR_SCR // 2 - 88, TINGGI_SCR // 2 + 60, 160, 50)

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((LEBAR_SCR, TINGGI_SCR))
    pygame.display.set_caption('TicTacToe')
    return screen

# Fungsi untuk keluar dari game
def quit_game():
    pygame.quit()

# Fungsi Grid ntuk permainan Tic Tac Toe
def draw_grid():
    screen.fill(bg)
    for i in  range(1,3):
        pygame.draw.line(screen, garis, (i * GRID, 0), (i * GRID, TINGGI_SCR), LEBAR_GARIS)
        pygame.draw.line(screen, garis, (0, i * GRID), (LEBAR_SCR, i * GRID), LEBAR_GARIS)

# Fungsi untuk menggambar penanda
def draw_penanda(papan):
    for baris in range(3):
        for kolom in range(3):
            if papan[baris][kolom] == PLAYER_X:
                draw_x(kolom, baris)
            elif papan[baris][kolom] == PLAYER_O:
                draw_o(kolom, baris)

# Fungsi X atau Player1
def draw_x(kolom, baris):
    padding = 15
    x_awal = kolom * GRID + padding
    x_akhir = (kolom + 1) * GRID - padding
    y_awal = baris * GRID + padding
    y_akhir = (baris + 1) * GRID - padding
    pygame.draw.line(screen, hijau, (x_awal, y_awal), (x_akhir, y_akhir), LEBAR_GARIS)
    pygame.draw.line(screen, hijau, (x_awal, y_akhir), (x_akhir, y_awal), LEBAR_GARIS)

# Fungsi O atau Player2
def draw_o(kolom, baris):
    tengah = (kolom * GRID + GRID // 2, baris * GRID + GRID // 2)
    radius = GRID // 2 - 15
    pygame.draw.circle(screen, merah, tengah, radius, LEBAR_GARIS)

def cek_menang(papan, player):
    for baris in range(3):
        if all([papan[baris][kolom] == player for kolom in range(3)]):
            return True
    for kolom in range(3):
        if all([papan[baris][kolom] == player for baris in range(3)]):
            return True
    if papan[0][0] == papan[1][1] == papan[2][2] == player:
        return True
    if papan[0][2] == papan[1][1] == papan[2][0] == player:
        return True
    return False

def tombol(teks, x, y, lebar, tinggi, warna, hover, aksi=None):
    mouse = pygame.mouse.get_pos()
    klik = pygame.mouse.get_pressed()

    if x + lebar > mouse[0] > x and y + tinggi > mouse[1] > y:
        pygame.draw.rect(screen, hover, (x, y, lebar, tinggi))
        if klik[0] == 1 and aksi is not None:
            aksi()
    else:
        pygame.draw.rect(screen, warna, (x, y, lebar, tinggi))

    teks_dasar = font.render(teks, True, putih)
    screen.blit(teks_dasar, (x + (lebar // 2 - teks_dasar.get_width() // 2), y + (tinggi // 2 - teks_dasar.get_height() // 2)))

def menu():
    running = True
    while running:
        screen.fill(biru)
        judul = font.render("TicTacToe", True, putih)
        screen.blit(judul, (LEBAR_SCR // 2 - judul.get_width() // 2, TINGGI_SCR // 4))

        tombol("Main", 100, 150, 100, 50, hijau, (0, 200, 0), main)
        tombol("Keluar", 100, 220, 100, 50, merah, (200, 0, 0), exit)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

def menu_akhir(pemenang):
    end_running = True
    while end_running:
        screen.fill(biru)
        if pemenang == PLAYER_X:
            teks_menang = "Player X Menang!"
        elif pemenang == PLAYER_O:
            teks_menang = "Player O Menang!"
        else:
            teks_menang = "Seri!"

        dasar_menang = font.render(teks_menang, True, putih)
        screen.blit(dasar_menang, (LEBAR_SCR // 2 - dasar_menang.get_width() // 2, TINGGI_SCR // 4))

        tombol("Main Lagi", 70, 160, 160, 50, hijau, (0, 200, 0), main)
        tombol("Keluar", 100, 220, 100, 50, merah, (200, 0, 0), exit)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

# Main game loop
def main():
    init_game()
    game_running = True
    papan = [[KOSONG, KOSONG, KOSONG], [KOSONG, KOSONG, KOSONG], [KOSONG, KOSONG, KOSONG]]
    player_skr = PLAYER_X
    game_over = False

    while game_running:
        draw_grid()
        draw_penanda(papan)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mousex, mousey = event.pos
                klik_baris = mousey // GRID
                klik_kolom = mousex // GRID
                if papan[klik_baris][klik_kolom] == KOSONG:
                    papan[klik_baris][klik_kolom] = player_skr
                    if cek_menang(papan, player_skr):
                        game_over = True
                        menu_akhir(player_skr)
                    player_skr = PLAYER_O if player_skr == PLAYER_X else PLAYER_X

        pygame.display.update()

if __name__ == "__main__":
    screen = init_game()
    menu()