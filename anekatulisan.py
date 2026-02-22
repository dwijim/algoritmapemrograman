import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    
    def cetak_di(x, y, teks):
        """Cetak teks di kolom x, baris y (mengikuti konvensi manusia: mulai dari 1)"""
        # Ubah ke indeks 0-based: y-1, x-1
        try:
            stdscr.addstr(y - 1, x - 1, teks)
        except curses.error:
            # Hindari error jika teks keluar layar
            pass
    
    # Gunakan fungsi dengan koordinat mulai dari 1
    cetak_di(1, 1, "Header")
    cetak_di(20, 5, "Tengah atas")
    cetak_di(1, 24, "Footer di baris 24")
    
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)