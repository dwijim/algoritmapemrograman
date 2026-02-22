import curses

# contoh penggunaan berbagai macam fungsi
# ── 1. FUNGSI TANPA PARAMETER ──────────────────────────────────
def hai_dunia():
    """Fungsi sederhana tanpa parameter dan tanpa nilai kembalian."""
    print("Halo, Dunia Pemrograman!")

def mencetak_tulisan_dengan_posisi(baris: int, kolom: int, tulisan: str):
    stdscr.addstr(baris+1,kolom+1, tulisan)  # indeks mulai dari 0
    stdscr.refresh()
    stdscr.getch()  # tunggu input



hai_dunia()

stdscr.getch()  # tunggu input
curses.wrapper(mencetak_tulisan_dengan_posisi(4, 9, "Halo di baris 5, kolom 10!"))

