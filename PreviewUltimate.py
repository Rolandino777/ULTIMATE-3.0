import os
import time

# Pastikan neofetch terinstal (1x saja saat awal)
if os.system("command -v neofetch > /dev/null") != 0:
    os.system("pkg install neofetch -y")

# Link beli lisensi
BELI_LINK = "https://wa.me/6281243587205?text=Bang%20Roland%20Mau%20Beli%20Lisensi%20Script%20Nya%20Bang"

# Efek ketik
def type_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()

# Fungsi untuk beli lisensi
def beli_lisensi():
    print("\n Menghubungi Owner Script...")
    time.sleep(2)
    os.system(f'termux-open-url "{BELI_LINK}" || xdg-open "{BELI_LINK}"')
    time.sleep(2)
    menu_awal()

# Preview menu tools
def preview_script():
    os.system('clear')
    os.system('neofetch --ascii_distro Ubuntu || echo "[!] neofetch belum terinstall"')
    print("""
 - Version       : Ultimate 3.0
 - Developer     : Rolandino
 - Github        : github.com/Rolandino23
 - WhatsApp      : +6281243587205
 - Telegram      : t.me/rolandino28
 - Facebook      : Roland Cod
 - Support Team  : Crackers Community

╭─[ MENU ]
""")
    print("""
[01] ADMIND FINDER                [21] FOLOWERS FACEBOOK  
[02] CEK NIK EKTP                 [22] INFORMATION FACEBOOK UID
[03] CRACK WIFI                   [23] CEK OPSI FACEBOOK  
[04] DDOS WIFI (root)             [24] TERMUX STYLE         
[05] WPBRUTE/BRUTEWP              [25] AUTO DEFACER WEB     
[06] SERVEO DDOSNET               [26] IP TRACKER       
[07] BRUTE FACEBOOK TARGETV1      [27] LEAKER DB      
[08] TEMBAK/KOUTA TRI GRATIS      [28] GEO PHONE       
[09] DEMO ACCESS OSIND            [29] TELEGRAM SCRAPING 
[10] CCTV HACKERS                 [30] GPT BOT AI CYBERV1  
[11] PEMINDAI XSS TERCANGGIH      [31] TEMBAK/KUOTA AXIS GRATIS
[12] MY FRIEND MXT QUEST          [32] WIFI CLONE HACK     
[13] HACK BLUETOOTH AUDIO         [33] TOR SEACHER
[14] PRIVATE DOXING TRACKERV1     [34] SOSIAL OSIND 
[15] SPAM BOT TELEGRAM            [35] WIFI TROLL
[16] PRIVATE DOXING TRACKERV2     [36] SUBDOMAINS HACK
[17] WEB SCANING PENETRATIONV1    [37] SOSIAL FAKE LOGV1
[18] WEB SCANING PENETRATIONV2    [38] SPOOFING DNS
[19] FACEBOOK CRACKV1             [39] WEBKIT TRACKERS
[20] FACEBOOK CRACKV2             [40] HEAD MAIL

[41] BRUTE FACEBOOK TARGETV2      [61] OLD SCRIPT RLNDYNO 0.0
[42] PHPSPLOIT BACKDOR REDIRECT   [62] IMEI LOCATION
[43] EXPLOITASI XSRF TOKEN        [63] INSTAGRAM REPORT
[44] MAWARE & BACKDOOR            [64] XPLOITASI CVE
[45] BRUTE ADMIND LOGIN           [65] PEMINDAI LFI & RFI
[46] CREATE IMAIL FRESH           [66] PRIVATE DOXING TRACKERV5
[47] ANDROID EXPLOIT              [67] HACK CAMERA
[48] GPT BOT AI CYBERV2           [68] HACK DRONE PENGINTAI (esiylap)
[49] DDOS SEDERHANA               [69] XPLOITASI/CONTROL PERANGKAT JAUH
[50] ANTARMUKA MY CODE            [70] INSTAGRAM INFORMATION
[51] WEB SCANING PENETRATIONV3    [71] BOTNET SERVER 100% PLANT ONLINE
[52] OLD SCRIPT RLNDYNO 1.0       [72] WEB SCANING PENETRATIONV4
[53] PRIVATE DOXING TRACKERV3     [73] SOSIAL FAKE LOGV2
[54] WHATSAPP REPORT              [74] WEB SCANING PENETRATIONV5
[55] PRIVATE DOXING TRACKERV4     [75] XMLRPC ATACK
[56] OLD SCRIPT RLNDYNO 2.0       [76] WEB SCANING PENETRIONV6
[57] FACEBOOK REPORT              [77] DRACOS LINUX TESTING
[58] CSRF & XSRF                  [78] INSTAGRAM OSIND INFORMATION
[59] EXUCUTOR DDOSV1              [79] LAPOR BUG
[60] EXUCUTOR DDOSV2              [80] EXIT/KELUAR
    """)
    input("\n[!] Tekan Enter Untuk Kembali...")
    menu_awal()

# Menu utama
def menu_awal():
    os.system('clear')
    print("\n \n")
    print("1. Beli Lisensi ")
    print("2. Preview Script ")
    print("0. Keluar \n")
    opsi = input(" Pilih: ")
    if opsi == "1":
        beli_lisensi()
    elif opsi == "2":
        preview_script()
    elif opsi == "0":
        print("\nJangan Pernah Ragu Untul Mencoba :) ")
        time.sleep(1)
        exit()
    else:
        print("\nGoblok! ")
        time.sleep(1)
        menu_awal()

# Jalankan program
if __name__ == "__main__":
    os.system('clear')
    type_effect("Ultimate 3.0? Ngak Cuma Program Tapi Ini Mindset !")
    type_effect("Bukan Buat Pamer? Tapi Buat Lo Yang Main Di Balik Layar !")
    type_effect("Biarpun Cuma Program Tools Script? Asal Impact Dan Suspension Bekerja 100% !")
    type_effect("Hacking Bukan Cuman Seni Tapi Cara Lo Merusak Batas !\n")
    menu_awal()
