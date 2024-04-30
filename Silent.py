import os, platform, time, sys
os.system("pip install requests && pip install rich")

def S1(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
S1('\n\x1b[1;37m[●] Checking Update........☢️');time.sleep(0.5)
os.system("git pull")
def Update():
    exit('\033[1;31m[●] Tools On Updating... Please Wait For Complete 💖 ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            S1("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🔥💥")
            S1('\x1b[1;94m[●] Follow My Page 👻')
            os.system('xdg-open https://www.facebook.com/matal.tools')
            from sex_sn import welcome
            welcome()
        elif bit == '32bit':
            S1("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 💥🔥")
            S1('\x1b[1;94m[●] Follow My Page 👻')
            os.system('xdg-open https://www.facebook.com/Sohan.143s')
            from sex_sn import welcome
            welcome()
        else:
            exit('\033[1;31m[●] Connection & Network Error ❌')
Run()
