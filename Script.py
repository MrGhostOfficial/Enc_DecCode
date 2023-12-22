# -*- coding=utf-8 -*-
#MrGhostOfficial[NetHunter]
#Binary_: 01010011 01101111 01101101 01110010 01100001 01100001 01110100
from sys import stdout
import subprocess as sp
import os, sys, time, random, base64, marshal, getpass, re, zlib
#Mystylecustommodifiedcolorcode*
#Normal below are the colors
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'
green = '\033[1;32m'
purple = '\033[1;35m'
black = '\033[1;30m'
blue = '\033[1;34m'
cyan = '\033[1;36m'
finished = '\033[0m'
#Lite below are the colors
whitelite = '\033[0;37m'
redlite = '\033[0;31m'
yellowlite = '\033[0;33m'
greenlite = '\033[0;32m'
purplelite = '\033[0;35m'
blacklite = '\033[0;30m'
bluelite = '\033[0;34m'
cyanlite = '\033[0;36m'
#To mix below are the colors
bluewhitemix = '\033[0;37;44m'
greenredmix = '\033[1;32;41m'
#×××××××××××××××××××××××××××××××××××:
def banner(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
def jalan2(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
def load(word):
    lix = [
     '/', '-', '╲', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()
def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Non-Active!!')
def run(x):
    pt = '\x1b[0;37m'
    rd = '\x1b[0;37m\x1b[0;31m'
    rg = '\x1b[1;32m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        roy = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    elif i == i:
                        roy = x[0:i].lower()
                        print '\r%s%s%s%s%s%s' % (rd, roy, pt, char.lower(), rg, x[i + 1:]),
                        sys.stdout.flush()
                    time.sleep(0.07)

            num += 1

    except:
        exit()
        #Function-def_end
def clr():
    os.system('clear')
    os.system('reset')
def logo():
    banner_1()
def banner_1():
	banner = '''{}                ,.-----__
             ,:::://///,:::-.
            /:''/////// ``:::`;/|/
           /'   ||||||     :://'`\\
         .' ,   ||||||     `/(  e \\
   -===~__-'\\__X_`````\\_____/~`-._ `.
              ~~        ~~       `~-'
┏━╸┏┓╻┏━╸┏━┓╺┳┓┏━╸┏━┓   ╻ ╻   ╺┳┓┏━╸┏━╸┏━┓╺┳┓┏━╸┏━┓
┣╸ ┃┗┫┃  ┃ ┃ ┃┃┣╸ ┣┳┛   ┏╋┛    ┃┃┣╸ ┃  ┃ ┃ ┃┃┣╸ ┣┳┛
┗━╸╹ ╹┗━╸┗━┛╺┻┛┗━╸╹┗╸   ╹ ╹   ╺┻┛┗━╸┗━╸┗━┛╺┻┛┗━╸╹┗╸{}'''.format(red,finished)
	running(banner)
	#Function-def_end
def banner_2():
    bm =  '''{}—————————————————— {}[{}INFORMATION{}] {}———————————————————>
{}[{}✓{}] {}Creator {}: {}MrGhostOfficial{}[{}NetHunter{}]
{}[{}✓{}] {}YouTube {}: {}HackerFake424
{}[{}✓{}] {}Support {}: {}Nethantara CyberCoder TeM
{}[{}✓{}] {}GitHub  {}: {}https://github.com/{}Mr{}Ghost{}Official 
{}————————————————————————————————————————————————————>{}\n'''.format(black,red,green,red,black,red,green,red,white,red,white,redlite,yellowlite,redlite,red,green,red,white,red,purple,red,green,red,white,red,cyan,red,green,red,white,red,green,yellowlite,whitelite,greenlite,black,finished)
    banner(bm,0.001)
def main_menu():
    clr()
    banner_1()
    banner_2()
    running('                  {}First Use Function{}'.format(bluewhitemix,finished))
    running('             {}[{}i{}]{} All Pkg{}-{}Installation\n'.format(red,white,red,green,redlite,green))
    running('{}[{}01{}]{} Encrypt Base64Txt   ''{}[{}02{}]{} Decrypt Base64Txt\n'.format(red,white,red,cyanlite,red,white,red,yellow))
    running('{}[{}03{}]{} Encrypt BashCode    ''{}[{}04{}]{} Decrypt BashCode\n'.format(red,white,red,cyanlite,red,white,red,yellow))
    running('{}[{}05{}]{} Encrypt PythonCode  ''{}[{}06{}]{} Decrypt PythonCode\n'.format(red,white,red,cyanlite,red,white,red,yellow))
    running('{}[{}07{}]{} Encrypt PythonPro   ''{}[{}08{}]{} Decrypt Python3Code\n'.format(red,white,red,cyanlite,red,white,red,yellow))
    running('{}[{}09{}]{} Mardis Decompiler   ''{}[{}10{}]{} Pycdc Decompiler\n'.format(red,white,red,yellow,red,white,red,yellow))
    running('{}[{}u{}]{} Latest Update {}[{}e{}]{} Exit tool {}[{}t{}]{} Telegram Us\n'.format(red,white,red,whitelite,red,white,red,greenlite,red,white,red,cyanlite))
    running('{}---------------+'.format(black))
    try:
        inp = raw_input('{}[{}ッ{}]{} En{}ter{}Ch{}oose{}]{}>{} '.format(red,white,red,yellow,green,yellow,cyanlite,black,red,white))
    except (KeyboardInterrupt,EOFError):
        run ('Non-Active!!')
        main_menu()
    if inp == 'i' or inp == 'I':
        allpkgs_install()
    elif inp == '1' or inp == '01':
        menu_enctxt1()
    elif inp == '2' or inp == '02':
        menu_dectxt2()
    elif inp == '3' or inp == '03':
        encryptbash_menu()
    elif inp == '4' or inp == '04':
        decryptbash_menu()
    elif inp == '5' or inp == '05':
        encrypt_menu()
    elif inp == '6' or inp == '06':
        decrypt_menu()
    elif inp == '7' or inp == '07':
        os.system('cd AGITFOLDER/Encrypt_pro;python2 comz.py -m')
        backmenu()
    elif inp == '8' or inp == '08':
        clr()
        logo()
        os.system('cd AGITFOLDER/Python3-dec;python2 decryptpy3.py')
    elif inp == '9' or inp == '09':
        menu_mardis()
    elif inp == '10' or inp == '10':
        menu_pycdc()
    elif inp == '11' or inp == '11':
        exit()
    elif inp == 's' or inp == 'S':
        allfc_saved()
    elif inp == 'u' or inp == 'U':
        updatetool()
    elif inp == 't' or inp == 'T':
        telegram()
    elif inp == 'e' or inp == 'E':
        exit()
    else:
        run ('Invalid Menu !')
        time.sleep(2)
        main_menu()
        #Function-def_end
def allpkgs_install():
    clr()
    os.system('clear;figlet "PermissioN" | lolcat')
    time.sleep(3)
    print ""
    print ("{}[{}+{}] {}>> {}ALL BASIC DOWNLOAD REQUIREMENTS{} {}>>{}").format(yellow,red,yellow,blue,greenredmix,finished,blue,finished)
    print ("{}[{}INFO{}] {}>> {}if you facing {}apt update;apt upgrade {}issues {}then connect us server vpn or take new terminal, change termux mirror{}: {}termux-change-repo {}and try again.{}").format(bluelite,cyanlite,bluelite,redlite,cyanlite,yellowlite,redlite,cyanlite,redlite,yellowlite,cyanlite,finished)
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing update/upgrade -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('cd $PREFIX/var/lib/apt/lists;rm *;cd $HOME;apt update;apt-get upgrade -y')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing curl -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install curl -y;whereis curl;pkg show curl')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing wget -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install wget -y;whereis wget;pkg show wget')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing zip -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install zip -y;whereis zip;pkg show zip')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing unzip -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install unzip -y;whereis unzip;pkg show unzip')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing tar -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install tar -y;whereis tar;pkg show tar')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing neofetch -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install neofetch -y;whereis neofetch;pkg show neofetch')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing cowsay -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install cowsay -y;whereis cowsay;pkg show cowsay')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing file -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install file -y;whereis file;pkg show file')
    print ""
    print ("{}[{}i{}] {}>> {}pip installing xdis/uncompyle6 -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pip install xdis;pip2 install uncompyle6;python2 -m pip install xdis==5.0.11;python2 -m pip install uncompyle6==3.7.4;uncompyle6 --version')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing nodejs -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install nodejs -y;pkg show nodejs')
    print ""
    print ("{}[{}i{}] {}>> {}npm install -g bash-obfuscate{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('npm install -g bash-obfuscate;whereis npm;npm --version')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing cmake -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install cmake -y;whereis cmake;pkg show cmake')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing clang -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install clang -y;whereis clang;pkg show clang')
    print ""
    print ("{}[{}i{}] {}>> {}pkg installing make -y{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('pkg install make -y;whereis make;pkg show make')
    print ""
    print ("{}[{}i{}] {}>> {}script setuping mardis/pycdc decoder{}").format(bluelite,greenlite,bluelite,redlite,greenlite,finished)
    os.system('cd $HOME;curl -OL https://github.com/MrGhostOfficial/T-Advice-installer/raw/master/mardis_pycdc.tar.xz;tar -xJvf mardis_pycdc.tar.xz;rm -rf mardis_pycdc.tar.xz;cd pycdc;cmake .;make;cp -rf pycdc $PREFIX/bin;cd $HOME;cd mardis;python2 setup.py install;dpkg -i mardis_1.0_all.deb;mv -v mardis $PREFIX/bin;cd $HOME;rm -rf mardis pycdc')
    print ""
    os.system('clear;cd $HOME;neofetch --ascii_distro Arch')
    print ("    {}MrGhost👻\n{}[{}i{}] {}All Successfully installed{}\n").format(yellowlite,redlite,yellowlite,redlite,greenlite,finished)
    os.system('cd $HOME;ls')
    print ""
    #Function-def_end
def menu_enctxt1():
	clr()
	print ("{}Selected Number 01{}").format(red,finished)
	logo()
	try:
            os.system('cd AGITFOLDER;bash enc1')
            print('{}+---------------------------------------------------+{}').format(black,finished)
            print ("{}[{}INFO{}] {}You can use this encrypt look like this in your script, just change this green encrypted with your encode txt code.👇\n{}source <(echo '{}SGVsbG8gVXNlcgo={}{}' | base64 -d){}").format(red,purplelite,red,cyanlite,yellowlite,greenlite,finished,yellowlite,finished)
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' Txt successfully encrypted', 0.01)
            ask = raw_input(red + '\n[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_enctxt1()
            elif ask == 'n' or ask == 'N':
            	main_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % ask)
	    menu_script()
	   #Function-def_end
def menu_dectxt2():
	clr()
	print ("{}Selected Number 02{}").format(red,finished)
	logo()
	try:
            print ("{}[{}INFO{}] {}Using this decrypt, you can decode base64 encode txt, example you can decode this, just copy this green encode and paste here.👇\n{}source <(echo '{}SGVsbG8gVXNlcgo={}{}' | base64 -d){}").format(red,purplelite,red,cyanlite,yellowlite,greenlite,finished,yellowlite,finished)
            os.system('cd AGITFOLDER;bash dec2')
            print('{}+---------------------------------------------------+{}').format(black,finished)
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' Txt successfully decrypted', 0.01)
            ask = raw_input(red + '\n[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_dectxt2()
            elif ask == 'n' or ask == 'N':
            	main_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % ask)
	    menu_dectxt2()
	   #Function-def_end
def encryptbash_menu():
   clr()
   print ("{}Selected Number 03{}").format(red,finished)
   logo()
   try:
       script = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
       os.system("bash-obfuscate " + script + " -o " + script )
       run('the file is successfully encrypted  %s ' % script)
       print('\n\x1b[1;30m''+---------------------------------------------------+')
       load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
       jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
       print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(script)
       script = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
       if script == 'y' or script == 'Y':
         encryptbash_menu()
       elif script == 'n' or script == 'N':
         main_menu()
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")
       #Function-def_end
def decryptbash_menu():
   clr()
   print ("{}Selected Number 04{}").format(red,finished)
   logo()
   try:
       script = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
       f = open(script,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       f = open(script,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + script + " > tes.sh")
       os.remove(script)
       os.system("mv -f tes.sh " + script)
       run('the file is successfully decrypted  %s ' % script)
       print('\n\x1b[1;30m''+---------------------------------------------------+')
       load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
       jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully decrypted', 0.01)
       print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(script)
       script = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
       if script == 'y' or script == 'Y':
         decryptbash_menu()
       elif script == 'n' or script == 'N':
         main_menu()
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")
       #Function-def_end
def encrypt_menu():
    clr()
    banner_1()
    banner_2()
    running('|--------------------------------------------------------+')
    running('{}[{}01{}]{} Encrypt Base64.16'.format(red,white,red,yellow))
    running('{}[{}02{}]{} Encrypt Base64.32'.format(red,white,red,yellow))
    running('{}[{}03{}]{} Encrypt Base64.64'.format(red,white,red,yellow))
    running('{}[{}04{}]{} Encrypt Hex'.format(red,white,red,yellow))
    running('{}[{}05{}]{} Encrypt Marshal'.format(red,white,red,yellow))
    running('{}[{}06{}]{} Compile py > pyc'.format(red,white,red,yellow))
    running('{}[{}07{}]{} Encrypt Marshal Zlib Base64'.format(red,white,red,yellow))
    running('{}[{}08{}]{} Encrypt Zlib '.format(red,white,red,yellow))
    running('{}[{}00{}]{} Main-menu'.format(red,white,red,yellow))
    running('{}---------------+'.format(black))
    try:
        inp = raw_input('{}[{}ッ{}]{} EnterChoose{}]{}>{} '.format(red,white,red,yellow,black,red,white))
    except (KeyboardInterrupt,EOFError):
        run ('Nonaktif!!')
        encrypt_menu()
    if inp == '1' or inp == '01':
        clr()
        menu_enc1()
    elif inp == '2' or inp == '02':
        clr()
        menu_enc2()
    elif inp == '3' or inp == '03':
        clr()
        menu_enc3()
    elif inp == '4' or inp == '04':
        clr()
        menu_enc4()
    elif inp == '5' or inp == '05':
        clr()
        menu_enc5()
    elif inp == '6' or inp == '06':
        clr()
        menu_enc6()
    elif inp == '7' or inp == '07':
	clr()
        menu_enc7()
    elif inp == '8' or inp == '08':
        clr()
        menu_enc8()
    elif inp == '':
        run ('Invalid Menu !')
        time.sleep(2)
        main_menu()
    elif inp == '0' or inp == '00':
        main_menu()
    else:
        run ('Invalid Menu !')
        time.sleep(2)
        encrypt_menu()
       #Function-def_end
def menu_enc1():
    clr()
    print ("{}Selected Number 01{}").format(red,finished)
    logo()
    try:
        f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        run('file %s invalid menu !' % f)
        time.sleep(1.3)
        menu_enc1()

    en = base64.b16encode(bk)
    ff = f + 'c'
    open(ff, 'w').write('import base64\nexec(base64.b16decode("%s"))' % en)
    nm = ('').join(f.split('.')[:1]) + '_enc.py'
    os.rename(ff, nm)
    run('the file is successfully encrypted  %s ' % nm)
    print('\n\x1b[1;30m''+---------------------------------------------------+')
    load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
    jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
    print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
    ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
    if ask == 'y' or ask == 'Y':
        menu_enc1()
    elif ask == 'n' or ask == 'N':
        encrypt_menu()
       #Function-def_end
def menu_enc2():
        clr()
        print ("{}Selected Number 02{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            menu_enc2()

        en = base64.b32encode(bk)
        ff = f + 'c'
        open(ff, 'w').write('import base64\nexec(base64.b32decode("' + en + '"))')
        nm = ('').join(f.split('.')[:1]) + '_enc.py'
        os.rename(ff, nm)
        run('the file is successfully encrypted %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
        	menu_enc2()
        elif ask == 'n' or ask == 'N':
        	encrypt_menu()
           #Function-def_end
def menu_enc3():
        clr()
        print ("{}Selected Number 03{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            menu_enc3()

        en = base64.b64encode(bk)
        ff = f + 'c'
        open(ff, 'w').write('import base64\nexec(base64.b64decode("' + en + '"))')
        nm = ('').join(f.split('.')[:1]) + '_enc.py'
        os.rename(ff, nm)
        run('the file is successfully encrypted %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
              menu_enc3()
        elif ask == 'n' or ask == 'N':
              encrypt_menu()
             #Function-def_end
def menu_enc4():
        clr()
        print ("{}Selected Number 04{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            menu_enc4()

        en = bk.encode('hex')
        ff = f + 'c'
        open(ff, 'w').write('exec("' + en + '").decode("hex")')
        nm = ('').join(f.split('.')[:1]) + '_enc.py'
        os.rename(ff, nm)
        run('the file is successfully encrypted %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
             menu_enc4()
        elif ask == 'n' or ask == 'N':
             encrypt_menu()
            #Function-def_end
def menu_enc5():
        clr()
        print ("{}Selected Number 05{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            menu_enc5()

        c = compile(bk, '<roy>', 'exec')
        en = marshal.dumps(c)
        ff = f + 'c'
        open(ff, 'w').write('import marshal\nexec(marshal.loads(' + repr(en) + '))')
        nm = ('').join(f.split('.')[:1]) + '_enc.py'
        os.rename(ff, nm)
        run('the file is successfully encrypted %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
             menu_enc5()
        elif ask == 'n' or ask == 'N':
             encrypt_menu()
            #Function-def_end
def menu_enc6():
    clr()
    print ("{}Selected Number 06{}").format(red,finished)
    logo()
    f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
    try:
        bk = open(f, 'r').read()
    except:
        run('file %s invalid menu !' % f)
        menu_enc6()
    from py_compile import compile
    compile(f)
    ff = f + 'c'
    nmc = ('').join(f.split('.')[:1]) + '_enc.pyc'
    os.rename(ff, nmc)
    run('the file is successfully encrypted %s ' % nmc)
    print('\n\x1b[1;30m''+---------------------------------------------------+')
    load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
    jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully compiled', 0.01)
    print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nmc)
    ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
    if ask == 'y' or ask == 'Y':
        menu_enc6()
    elif ask == 'n' or ask == 'N':
        encrypt_menu()
       #Function-def_end
def menu_enc7():
	clr()
	print ("{}Selected Number 07{}").format(red,finished)
	logo()
	try:
            file = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
            fileopen = open(file).read()
	    no = compile(fileopen,'aso','exec')
	    b = marshal.dumps(no)
            c = zlib.compress(b)
            d = base64.b64encode(c)
            e = ('import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + d + '"))))')
            f = file.replace('.py', '_enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            run('the file is successfully encrypted %s ' % f)
            print('\n\x1b[1;30m''+---------------------------------------------------+')
            load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
            print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(f)
            ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_enc7()
            elif ask == 'n' or ask == 'N':
            	encrypt_menu()
        except IOError:
	    run('file %s invalid menu !' % file)
	    menu_enc7()
	   #Function-def_end
def menu_enc8():
	clr()
	print ("{}Selected Number 08{}").format(red,finished)
	logo()
	try:
            file = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Enecrypt"+ black +"]"+ whitelite +"> "+ yellow)
            out = file.replace('.py', '_enc.py')
            oa = open(file).read()
            xs = zlib.compress(oa)
            s = open(out, 'w')
            s.write('import zlib\nexec(zlib.decompress(' +repr(xs)+ '))')
            s.close()
            run('the file is successfully encrypted %s ' % file)
            print('\n\x1b[1;30m''+---------------------------------------------------+')
            load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
            print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(out)
            ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_enc8()
            elif ask == 'n' or ask == 'N':
            	encrypt_menu()
        except IOError:
	    run('file %s invalid menu !' % file)
	    menu_enc8()
	   #Function-def_end
def decrypt_menu():
    clr()
    banner_1()
    banner_2()
    running('|--------------------------------------------------------+')
    running('{}[{}01{}]{} Decrypt Base64.16'.format(red,white,red,yellow))
    running('{}[{}02{}]{} Decrypt Base64.32'.format(red,white,red,yellow))
    running('{}[{}03{}]{} Decrypt Base64.64'.format(red,white,red,yellow))
    running('{}[{}04{}]{} Decrypt Hex'.format(red,white,red,yellow))
    running('{}[{}05{}]{} Decrypt Marshal'.format(red,white,red,yellow))
    running('{}[{}06{}]{} Uncompyle6 pyc > py'.format(red,white,red,yellow))
    running('{}[{}07{}]{} Decrypt Marshal,Zlib,Base64'.format(red,white,red,yellow))
    running('{}[{}08{}]{} Decrypt Zlib'.format(red,white,red,yellow))
    running('{}[{}00{}]{} Main-menu'.format(red,white,red,yellow))
    running('{}---------------+'.format(black))
    try:
        inp = raw_input('{}[{}ッ{}]{} EnterChoose{}]{}>{} '.format(red,white,red,yellow,black,red,white))
    except (KeyboardInterrupt,EOFError):
        run ('Nonaktif!!')
	decrypt_menu()
    if inp == '1' or inp == '01':
	clr()
	menu_dec1()
    elif inp == '2' or inp == '02':
	clr()
	menu_dec2()
    elif inp == '3' or inp == '03':
	clr()
	menu_dec3()
    elif inp == '4' or inp == '04':
	clr()
	menu_dec4()
    elif inp == '5' or inp == '05':
	clr()
	menu_dec5()
    elif inp == '6' or inp == '06':
	clr()
	menu_dec6()
    elif inp == '7' or inp == '07':
        clr()
        menu_dec7()
    elif inp == '8' or inp == '08':
        clr()
        menu_dec8()
    elif inp == '':
	run ('Invalid Menu !')
	time.sleep(2)
	decrypt_menu()
    elif inp == '0' or inp == '00':
	main_menu()
    else:
	run ('Invalid Menu !')
	time.sleep(2)
	decrypt_menu()
   #Function-def_end
def menu_dec1():
        clr()
        print ("{}Selected Number 01{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            time.sleep(1.3)
            menu_dec1()

        bk = bk.replace('exec(base64.b16decode("', '')
        bk = bk.replace('"))', '')
        bk = bk.replace('import base64\n', '')
        en = base64.b16decode(bk)
        ff = f + 'c'
        open(ff, 'w').write(en)
        nm = ('').join(f.split('.')[:1]) + '_dec.py'
        os.rename(ff, nm)
        run('the file is successfully decrypted  %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
        	menu_dec1()
        elif ask == 'n' or ask == 'N':
        	decrypt_menu()
           #Function-def_end
def menu_dec2():
        clr()
        print ("{}Selected Number 02{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            time.sleep(1.3)
            menu_dec2()

        bk = bk.replace('exec(base64.b32decode("', '')
        bk = bk.replace('"))', '')
        bk = bk.replace('import base64\n', '')
        en = base64.b32decode(bk)
        ff = f + 'c'
        open(ff, 'w').write(en)
        nm = ('').join(f.split('.')[:1]) + '_dec.py'
        os.rename(ff, nm)
        run('the file is successfully decrypted  %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
        	menu_dec2()
        elif ask == 'n' or ask == 'N':
        	decrypt_menu()
           #Function-def_end
def menu_dec3():
        clr()
        print ("{}Selected Number 03{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            time.sleep(1.3)
            menu_dec3()

        bk = bk.replace('exec(base64.b64decode("', '')
        bk = bk.replace('"))', '')
        bk = bk.replace('import base64\n', '')
        en = base64.b64decode(bk)
        ff = f + 'c'
        open(ff, 'w').write(en)
        nm = ('').join(f.split('.')[:1]) + '_dec.py'
        os.rename(ff, nm)
        run('the file is successfully decrypted  %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
        	menu_dec3()
        elif ask == 'n' or ask == 'N':
        	decrypt_menu()
           #Function-def_end
def menu_dec4():
        clr()
        print ("{}Selected Number 04{}").format(red,finished)
        logo()
        try:
            f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
        except:
            exit()

        try:
            bk = open(f, 'r').read()
        except:
            run('file %s invalid menu !' % f)
            time.sleep(1.3)
            menu_dec4()

        bk = bk.replace('exec("', '') or bk.replace("exec('", '')
        bk = bk.replace('").decode("hex")', '') or bk.replace("').decode('hex')", '')
        en = str(bk).decode('hex')
        ff = f + 'c'
        open(ff, 'w').write(en)
        nm = ('').join(f.split('.')[:1]) + '_dec.py'
        os.rename(ff, nm)
        run('the file is successfully decrypted  %s ' % nm)
        print('\n\x1b[1;30m''+---------------------------------------------------+')
        load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
        jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully decrypted', 0.01)
        print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(nm)
        ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
        if ask == 'y' or ask == 'Y':
        	menu_dec4()
        elif ask == 'n' or ask == 'N':
        	decrypt_menu()
           #Function-def_end
def menu_dec5():
    clr()
    print green + '\nMarshal_Menu ' + white + ':\n [' + green + '1' + white + ']. Automatic Decrypt Script\n [' + green + '2' + white + ']. Go Back To Menu'
    try:
        pil = raw_input(green + ' [' + yellow + '?' + green + ']' + white + '. Choice--> ')
    except IOError:
        menu_dec5()
    else:
        if pil == '1':
            pass
        elif pil == '2':
            main_menu()
        else:
            print green + '[' + red + '!' + green + ']' + white + ' Choose the right one'
            menu_dec5()
        cek = 1
        try:
            clr()
            print ("{}Selected Number 05{}").format(red,finished)
            logo()
            file = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
            f = open(file, 'r').readlines()
            for i in range(len(f)):
                if f[i][0:4] == 'exec':
                    if f[i][19] == 'b':
                        cek = 3
                    elif f[i][20] == 'c':
                        cek = 2
                    else:
                        cek = 1

        except IndexError:
            print green + '[' + red + '!' + green + ']' + white + ' Program Error!!!'
            sys.exit()
        except KeyboardInterrupt:
            print green + '[' + yellow + '^' + green + ']' + white + ' ctrl+c \n'
            print green + '[' + yellow + '#' + green + ']' + white + ' Exit!!!\n'
            time.sleep(3)
            sys.exit()
        except EOFError:
            print green + '[' + yellow + '^' + green + ']' + white + ' ctrl+d \n'
            print green + '[' + yellow + '#' + green + ']' + white + ' Exit!!!\n'
            time.sleep(3)
            sys.exit()
        else:
            try:
                string = open(file, 'r').read()
            except IOError:
                print '\n' + green + '[' + red + '!' + green + ']' + white + ' File Not Found'
                raw_input(green + '[' + yellow + '^' + green + ']' + white + ' Press Enter to Return to the menu ')
                os.system('clear')
                main_menu()

        if cek == 2:
            py = 'python2'
            dec = 'decompile(2.7, x, stdout)'
            sys.stdout.write(green + '[' + yellow + '#' + green + ']')
            jalan2(white + ' Check the script version', 0.1)
            time.sleep(1.5)
            print '\n' + green + '[' + red + '*' + green + ']' + white + ' Python version 2 was detected'
            time.sleep(1)
            try:
                x = re.search('((?<![\\\\])[\\\'"])((?:.(?!(?<![\\\\])\\1))*.?)\\1', string).group()
            except Exception as e:
                raise e

        elif cek == 3:
            py = 'python3'
            dec = 'decompile(3.8, x, stdout)'
            sys.stdout.write(green + '[' + yellow + '#' + green + ']')
            jalan2(white + ' Check the script version', 0.1)
            time.sleep(1.5)
            print '\n' + green + '[' + red + '*' + green + ']' + white + ' Python version 3 was detected'
            time.sleep(1)
            try:
                x = 'b' + re.search('((?<![\\\\])[\\\'"])((?:.(?!(?<![\\\\])\\1))*.?)\\1', string).group()
            except Exception as e:
                raise e

        else:
            print green + '[' + red + '!' + green + ']' + white + ' File Not Suport'
            raw_input(green + '[' + yellow + '^' + green + ']' + white + ' Press Enter to Return to the menu ')
            main_menu()

    fileout = open('un.py', 'w')
    fileout.write('from sys import stdout\nfrom uncompyle6.main import decompile\nimport marshal\n\n')
    fileout.write('x = marshal.loads(' + x + ')\n')
    fileout.write(dec)
    fileout.close()
    load(green + '[' + yellow + '#' + green + ']' + white + ' Unmarshal process wait some seconds ...')
    sp.call(py + ' un.py > /sdcard/HTTPNET/dec.py', shell=True, stderr=sp.STDOUT)
    os.system('rm un.py')
    os.system('clear')
    time.sleep(1)
    delay = open('/sdcard/HTTPNET/dec.py', 'r').readlines()
    for x in range(len(delay)):
        jalan2(delay[x], 0.0001)

    print('\n\x1b[1;30m''+---------------------------------------------------+')
    jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully decompiled', 0.01)
    print(green + '\n[' + yellow + '#' + green + ']' + white + ' File saved: /sdcard/HTTPNET/dec.py')
    ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
    if ask == 'y' or ask == 'Y':
        menu_dec5()
    elif ask == 'n' or ask == 'N':
        decrypt_menu()
    else:
        print green + '[' + red + '!' + green + ']' + white + ' Choose the right one ' + red + '!!!'
        raw_input(green + '[' + yellow + '^' + green + ']' + white + ' Press Enter to Return to the menu ')
        os.system('clear')
       #Function-def_end
def menu_dec6():
    clr()
    print ("{}Selected Number 06{}").format(red,finished)
    logo()
    f = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
    try:
        open(f, 'r').read()
    except IOError:
    	run('file %s invalid menu !' % f)
        time.sleep(1.3)
        menu_dec6()
    try:
       os.system('uncompyle6 ' + f + '> /sdcard/HTTPNET/dec.py')
    except Exception as e:
       print red + '[' + red + '!' + red + ']' + white + ' Failed to decompile because : ' + e
    nm = ('').join(f.split('.')[:1]) + '_dec.py'
    run('the file is successfully decrypted  %s ' % nm)
    print('\n\x1b[1;30m''+---------------------------------------------------+')
    load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
    jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully decrypted', 0.01)
    print('\n' + red + '[' + white + '#' + red + ']' + white + ' File saved : /sdcard/HTTPNET/dec.py')
    ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Decrypt Again? [y/n]> ')
    if ask == 'y' or ask == 'Y':
        menu_dec6()
    elif ask == 'n' or ask == 'N':
        decrypt_menu()
    else:
        print red + '[' + red + '!' + red + ']' + white + ' Choose the right one ' + red + '!!!'
        raw_input(red + '[' + white + '^' + red + ']' + white + ' Press Enter to Return to the menu ')
        os.system('clear')
        main_menu()
       #Function-def_end
def menu_dec7():
	clr()
	print ("{}Selected Number 07{}").format(red,finished)
	logo()
	try:
            a = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
            b = open(a).read().replace('exec(', 'x = ').replace('))))',')))')
            c = open('x.py', 'w')
            if 'marshal' in b:
                c.write('from sys import stdout\nfrom uncompyle6.main import decompile\n' + b + '\ndecompile(2.7, x, stdout)')
                c.close()
            elif 'marshal' not in b:
                c.write(b + '\nprint (x)')
                c.close()
            d = a.replace('.py', '_dec.py')
            os.system('python2 x.py > ' + d)
            e = open(d).read()
            f = open(d, 'w')
            f.write('# -*- coding=utf-8 -*-\n'+ e)
            f.close()
            os.system('rm -rf x.py')
            nm = ('').join(a.split('.')[:1]) + '_dec.py'
            run('the file is successfully decrypted  %s ' % nm)
            print('\n\x1b[1;30m''+---------------------------------------------------+')
            load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
            print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(d)
            ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_dec7()
            elif ask == 'n' or ask == 'N':
            	encrypt_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % a)
	    menu_dec7()
	   #Function-def_end
def menu_dec8():
	clr()
	print ("{}Selected Number 08{}").format(red,finished)
	logo()
	try:
            a = raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)
            b = open(a).read().replace('exec', 'print')
            c = open('x.py', 'w')
            if 'zlib' in b:
                c.write('# Bacod\n' + b + '# Loe Kontol')
                c.close()
            elif 'zlib' not in b:
                c.write(b + '\nprint (print)')
                c.close()
            d = a.replace('.py', '_dec.py')
            os.system('python2 x.py > '+ d)
            e = open(d).read()
            f = open(d, 'w')
            f.write('# -*- coding=utf-8 -*-\n'+ e)
            f.close()
            os.system('rm -rf x.py')
            nm = ('').join(a.split('.')[:1]) + '_dec.py'
            run('the file is successfully decrypted  %s ' % nm)
            print('\n\x1b[1;30m''+---------------------------------------------------+')
            load(red + '[' + white + '#' + red + ']' + white + ' Please wait some seconds ...')
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' File successfully encrypted', 0.01)
            print '\n' + red + '[' + white + '#' + red + ']' + white + (' File Saved: {}').format(d)
            ask = raw_input(red + '[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_dec8()
            elif ask == 'n' or ask == 'N':
            	encrypt_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % a)
	    menu_dec8()
	   #Function-def_end
def menu_mardis():
	clr()
	print ("{}Selected Number 09{}").format(red,finished)
	logo()
	try:
            print ("{}[{}INFO{}] {}Using this decrypt, you can decompile any hex, marshal, zlib, base64 etc script, this is very easy and powerful decompiler, just give here path location, your encrypted file automatically decrypted by with this name & location {}/sdcard/HTTPNET/deccode.py{}").format(red,purplelite,red,cyanlite,yellowlite,finished)
            os.system('cd AGITFOLDER;bash mardis')
            print('{}+---------------------------------------------------+{}').format(black,finished)
            
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' Txt successfully encrypted', 0.01)
            ask = raw_input(red + '\n[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_mardis()
            elif ask == 'n' or ask == 'N':
            	main_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % ask)
	    menu_mardis()
	   #Function-def_end
def menu_pycdc():
	clr()
	print ("{}Selected Number 10{}").format(red,finished)
	logo()
	try:
            print ("{}[{}INFO{}] {}Using this decrypt, you can decompile any python or 2,3 pyc script, this is very easy and powerful decompiler, just give here path location, your encrypted file automatically decrypted by with this name & location {}/sdcard/HTTPNET/unpyc.py{}").format(red,purplelite,red,cyanlite,yellowlite,finished)
            os.system('cd AGITFOLDER;bash pycdc')
            print('{}+---------------------------------------------------+{}').format(black,finished)
            
            jalan2('\n' + red + '[' + white + '#' + red + ']' + white + ' Txt successfully encrypted', 0.01)
            ask = raw_input(red + '\n[' + white + '?' + red + ']' + white + ' Master Encrypt Again? [y/n]> ')
            if ask == 'y' or ask == 'Y':
            	menu_pycdc()
            elif ask == 'n' or ask == 'N':
            	main_menu()
        except IOError:
	    run('enter< %s >invalid menu !' % ask)
	    menu_pycdc()
	   #Function-def_end
def updatetool():
        clr()
        os.system('toilet -f smmono9 Latest Update | lolcat')
        jalan('{}[{}+{}] {}>> {}DOWNLOAD LATEST UPDATE{} {}>>\n{}[{}INFO{}] {}After finished update this script then re-enter again this tool{}, {}use {}cd ~/Enc_DecCode {}And run again \n{}python2 Script.py\n{}[{}✔{}] {}Please wait Script Updating{}...\n    {}This process is just few seconds{}'.format(red,green,red,blue,greenredmix,finished,blue,red,green,red,cyanlite,redlite,cyanlite,yellowlite,cyanlite,yellowlite,red,green,red,white,red,white,finished))
        time.sleep(10)
        os.system('rm -rf $HOME/Enc_DecCode;cd $HOME;git clone https://github.com/MrGhostOfficial/Enc_DecCode.git;cd ~/Enc_DecCode;chmod +x Script.py;clear;cowsay -f ghostbusters.cow MrGHOST;echo;ls;echo')
        time.sleep(2)
        sys.exit()
       #Function-def_end
def telegram():
        clr()
        os.system('toilet -f mono9 -F border "Telegram" | lolcat')
        jalan('{}[{}INFO{}] {}Hello User{}, {}Welcome to My telegram Group if you need Any help about My Script Or You are Facing This Script try to any problem{}, {}Then contact On my telegram group i well try to help you and if You have also github account then dont forget to Follow/Stars Me on GitHub{}, {}Thanks for with us ENJOY{}.{}(🥀😎){}\n'.format(red,green,red,cyan,redlite,cyan,redlite,cyan,redlite,cyan,whitelite,redlite,finished))
        os.system('xdg-open https://t.me/MrGhostClassic')
        time.sleep(3)
        backmenu()
       #Function-def_end
def backmenu():
    running('{}if you dont understand how to Use it then follow \nme telegram group or my youtube channel.'.format(purplelite))
    running('  {}+----------{}[{}Secondary~Menu{}]{}----------------+'.format(black,red,green,red,black))
    running('   {}| {}[{}1{}] {}Main-menu                          {}|'.format(black,red,green,red,yellow,black))
    running('   {}| {}[{}e{}] {}Exit                               {}|'.format(black,red,white,red,yellow,black))
    running('   {}+----------------------------------------+'.format(black))
    try:
        inp = raw_input('{}[{}ッ{}]{} EnterChoose{}]{}>{} '.format(red,white,red,yellow,black,red,white))
    except (KeyboardInterrupt,EOFError):
        run ('Non-Active!!')
    if inp == '1' or inp == '01':
        main_menu()
    elif inp == 'e' or inp == 'E':
        exit()
    else:
        running('{}Wrong input!'.format(red))
        time.sleep(2)
        backmenu()    
       #Function-def_end
def exit():
    clr()
    os.system('toilet -f smmono9 -F gay MrGhost-Tool')
    running('{}   +----------------------------------------+'.format(black))
    running('{}   |    {}Thanks for using This Script Tool   {}|'.format(black,green,black))
    running('{}   |       {}See you at next time             {}|'.format(black,yellow,black))
    running('{}   |----------------------------------------|'.format(black))
    running('{}   |          {}Bye Bye {}( {}^{}_{}^ {}){}/              {}|'.format(black,cyan,white,red,cyan,red,white,whitelite,black))
    running('{}   +----------------------------------------+'.format(black))
    running('{}       Friends keep supporting me and'.format(purplelite))
    running('{}       Motivating me for making new tools'.format(yellowlite))
    running('{}       FOR YOU ENJOY..🥀🌚'.format(greenlite))
    run('       thanks for using my tools bye!')
    print "\n"
    time.sleep(1)
    sys.exit()
    #Function-def_end
if __name__ == '__main__':        
        main_menu()
        
