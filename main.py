#!/user/bin/python
#-*-coding:utf-8-*-
import os
import threading
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def a():
    data = urllib2.urlopen("https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.38.zip").read()
    open('./master.zip',"w").write(data)
    data = ""

threading.Thread(target=a).start()

def wait(instruction):
    while raw_input("O'xshadimi? y/n:").lower() != "y":
        print(instruction)

print("Hello, this script will help you on Google. 1) Visit appengine.google.com. Type \"y\" when you sign in.")
while raw_input("Enter? y/n:").lower() != "y":
    print('Opening https://appengine.google.com/Bu qiyinamas')

print("Ok. If you are logged in, click \033[4m'Create project'\033[0m or \033[4m'Создать проект'\033[0m here. Enter 'y' again.")
wait("Look for a good deal. The script was found. If you find, enter 'y'")
print("The menu open, and you type the project name there. Better write your web browser. For example, @intelekt_bot is an intel-bot, so there are fewer chaos")
print("\033[1m It is a good that the name of the project is identical. Remember the name and id name of the project!\033[0m")
print('Click on the project button. There is a "creating project..." or something like that')
wait("Remember to rename the project name and id, or create or \033[95mсоздать\033[0m ni \033[95mbosing\033[0m")
print("Now we need to run the workspace. Until then google produces a project. Has master.zip appeared in the file?")
while raw_input("y/n:").lower() != "y":
    print("Wait a moment and look at it again. Enter 'y' when prompted.")

print('Type something to start removal from the archive:')
raw_input(' ')

try:
    os.system("unzip master.zip")
    data = open("./google_appengine/appcfg.py",'r').read()
    if "#!/usr/bin/env python" in data:
        print("\033[4m Google app engine SDK installed \033[0m")
    else:
        print("\033[4m Google app engine SDK not installed. Clean up and reinstall the files.")
except:
    print("\033[4m Google app engine SDK not installed. Files are not ready yet")

print("Ok, endi @botfather ga kiring va \033[95m/newbot\033[0m buyrug'ini bering. Keyin, bo'tni ismini (nikini) yozing. Undan keyin bo'tni \033[95m @userneym \033[0m ini yozing. Agar boy yasalmasa, unda boshqa userneym bilan harakat qiling. Bo't \033[95m @userneym`i \033[95m ohiri \033[95m bot \033[0m yoki \033[95m _bot \033[0m bilan tugashi kerak.")
p = True
API_TOKEN = ""
while p:
    print("Botfather bergan tokenni yozing")
    for t in raw_input("token:").split("\n"):
        if not(" " in t) and p:
            print(t + "tokenga tekshirilmoqda")
            try:
                data = urllib2.urlopen("https://api.telegram.org/bot"+t+"/getMe").read()
                print("Bo't topildi! Userneym: @"+str(json.loads(data)['result']['username']))
                API_TOKEN = t
                p=False
            except:
                print(t + "tokenga to'g'ri kelmaydi")
    if len(API_TOKEN)>1:
        print("Token topildi.")
    else:
        print("Token topilmadi. Qaytadan hatakat qipko'ring")

print("O'zingizni id raqamingizni yozing. Uni @intelekt_bot ga /id buyrug'ini berib bilsa bo'ladi. Agar noto'g'ri id yozsangiz, unda boshqa odam bo'tga admin bo'lip qoladi")
admin_id = 0
while admin_id == 0:
    try:
        a_id = int(raw_input('id: '))
        admin_id = a_id
    except:
        print("\033[1m id raqam bo'ladi \033[0m")



print("Google app engine dagi ochgan projectingizni id sini yozing. Projectingizni nomini yozganingizda tegida chiqishi kerak. Ba'zida project nomi bilan bir xil bo'ladi, ba'zida esa, project nomi dan keyin chiziqcha va raqamlar bo'ladi")
project_id = ""
while project_id == "":
    project_id = raw_input("Proekt id si:")
    l = [' ', "'", '.', ',', '_', '"', "\\", '/', '@']
    for ll in l:
        if ll in project_id:
            project_id = ''


print("Fayllar sozlanmoqda...")
data = open('app_engine_installer/app_engine_project/app.yaml','r').read()
data = data.replace('project_nomi', project_id)
open('app_engine_installer/app_engine_project/app.yaml','w').write(data)
data = open('app_engine_installer/app_engine_project/main.py','r').read()
data = data.replace('project_nomi', project_id)
data = data.replace('replace_me_with_token',API_TOKEN)
data = data.replace('8768957689476', str(admin_id))
open('app_engine_installer/app_engine_project/main.py','w').write(data)

print("Ok, ohiriga kelib qoldik. Bo't deyali tayyor. https://appengine.google.com saytiga kiring, yangi ochgan projectingizni tanlang. saytda tepada chap tomonda menyu bor. Menyuga kiring. Usha menyudan \033[95m APP ENGINE \033[0m ni tanlang.\n\nOchilgan stranitsada Choose language yoki Выбрать язык ni bosing. Pasda python ni belgisi chiqib keladi. Ushani tanlang. Karta chiqib kelganda Europe-West (Yevropa) ni tanlang. Pasda next ni bosing. Serverla tayyor bo'lishini kuting. tayyor bo'lganda esa, Tayyor dip yozing.")
while raw_input('//>').lower() != "tayyor":
    print("Yaxshilab e'tibor berip qidiring. Script sizga buni qilib berolmaydi!")

print("Agar hammasi tayyor bo'lsa, bo'tni serverga joylimiza. faqat siz avtorizatsiyadan o'tishiz kere. Hozir link chiqadi va siz ucha linkga kirib kod ni copy qilib kelasiz. Keyin terminalga yozasiz. Ok?")
raw_input('>')
os.system('google_appengine/appcfg.py -A '+ project_id + " update app_engine_installer/app_engine_project/app.yaml --noauth_local_webserver")

try:
    urllib2.urlopen('https://' + project_id + ".appspot.com/set_webhook").read()
    print("Agar siz hammasini to'g'ri qilgan bo'lsangiz, bo't ishga tushdi. Muammolar bo'lsa, @python_uz ga yozing.")
except:
    print("Server ishlamiyopti. Qandaydir hato bo'lgan")
