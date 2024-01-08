from vosk import Model, KaldiRecognizer
import ffmpeg
import os, json
import pyaudio
import sounddevice as sd
from pygame import mixer
import pyautogui as pag
import random as ran
import time
import webbrowser as web
from keyboard import *

# import vlc
# import pyaudio
# from collections.abc import Set
# from collections.abc import Mapping

# from sound import *

# p = vlc
# playlist = p.MediaList(["Midnight Club.mp3",'Виктор_Цой_Скоро_кончится_лето_fonk.mp3', 'Nirvana - Smells Like Teen Spirit.mp3','Dancing in My Room.mp3' ,'Dancin.mp3' ,'Five Degrees.mp3' ,
# 'Decapitator.mp3' ,'Devil Eyes.mp3' , 'idfc.mp3','MONTERO.mp3' ,'Old Town Road.mp3','RagnBone Man - Human.mp3','Miyagi _ Andy Panda - Патрон.mp3','Seven Phoenix, PHAM - FOR U.mp3',
# 'Old Town Road.mp3','Oliver Tree - Jerk.mp3','Pham, Malcolm Anthony - My Town.mp3','SFALL - row.mp3','Sam_Tinnesz_feat_Yacht_Money_Play_with_Fire_feat_Yacht_Money.mp3',
# 'Real cool man.mp3','Mask Off.mp3'])
# defolt = p.MediaListPlayer()
# defolt.set_media_list(playlist)
# niggalist = p.MediaList(["Midnight Club.mp3",'Виктор_Цой_Скоро_кончится_лето_fonk.mp3','Dancing in My Room.mp3' ,'Dancin.mp3' ,'astral-step.mp3','S.X.N.D. N.X.D.E.S..mp3',
# 'Scary Garry.mp3','Nirvana - Smells Like Teen Spirit.mp3','ДРИПСЕТ.mp3' ,'Gimme The Loot.mp3','PUSHNOY_NIRVENUS_2_0_NIRVANA_&_Shocking_Blue_mashup_MP3Ball_ru.mp3',
# 'LILDRUGHILL feat. ROCKET - Терминал.mp3','MONTERO.mp3','Miyagi _ Andy Panda - Патрон.mp3','Old Town Road.mp3','Oliver Tree - Jerk.mp3','Pham, Malcolm Anthony - My Town.mp3',
# 'RagnBone Man - Human.mp3','Real cool man.mp3','Sam_Tinnesz_feat_Yacht_Money_Play_with_Fire_feat_Yacht_Money.mp3',
# 'SFALL - row.mp3',
# 'Скриптонит - Положение.mp3' , 'Decapitator.mp3','Empathy.mp3','Five Degrees.mp3' ,'Devil Eyes.mp3','idfc.mp3' ,'LIZER - Между Нами.mp3','PHARAOH - Мой кайф.mp3',
# 'Seven Phoenix, PHAM - FOR U.mp3','PHARAOH - Не по пути.mp3','Markul - Миражи.mp3','Markul - 2 минуты.mp3','Markul - Phantom.mp3','Markul - Деньги на ветер.mp3','Markul - 25.mp3',
# 'Markul - Серпантин.mp3','Markul - Конфеты.mp3','plenka - Closed.mp3','Aglow.mp3','Mask Off.mp3'])
# private = p.MediaListPlayer()
# private.set_media_list(niggalist)

# defolt.play()
# private.play()
# defolt.pause()
# private.pause()
# private.stop()
# defolt.stop()







#Ответы Джарвиса
mixer.init()
yes1 = mixer.Sound('Да сэр.wav')
yes2 = mixer.Sound('Да сэр(второй).wav')
yest = mixer.Sound('Есть.wav')
load = mixer.Sound('Загружаю сэр.wav')
zhel = mixer.Sound('Как пожелаете .wav')
yslyg = mixer.Sound('К вашим услугам сэр.wav')
zapr = mixer.Sound('Запрос выполнен сэр.wav')
re = mixer.Sound('Я перезагрузился сэр.wav')
diag1 = mixer.Sound('Начинаю диагностику системы.wav')
diag2 = mixer.Sound('Начинаю диагностику системы (второй).wav')
check_end = mixer.Sound('Проверка завершена.wav')

def diag():
    s = diag1.play, diag2.play, zhel.play, yes1.play, yes2.play, yest.play
    chosen = ran.choice(s)
    chosen()
def come():
    r = yslyg.play, re.play, check_end.play
    chosen = ran.choice(r)
    chosen()
def yes():
    l = yes1.play, yes2.play, yslyg.play
    chosen = ran.choice(l)
    chosen()
def sogl():
    l = yes1.play, yes2.play, yest.play, load.play, zhel.play
    chosen = ran.choice(l)
    chosen()
#ссылки
gsm = 'https://www.gismeteo.ru/weather-stary-oskol-5024/'
ytb = 'https://www.youtube.com'
www = 'https://www.google.com/search?q='
#нужные пременные
run = True
f = False

#инициализация микрофона и распознавания речи
model = Model('model')
rec = KaldiRecognizer(model, 16000)
pya = pyaudio.PyAudio()
stream = pya.open(format=pyaudio.paInt16, channels = 2, rate = 8000, input=True, frames_per_buffer=44100)
stream.start_stream()

re.play()

while run != False:
    y = 'f'
    xy = True
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x = json.loads(rec.Result())
        print(x['text'])
        y = x['text']


    if 'джар' in y:
        if xy == True:
            yes()
        xy = False
    if y == 'отключи микрофон' or y == 'подключи микрофон' or y == 'выключи микрофон' or y == 'включи микрофон':
        yest.play()
        time.sleep(1)
        run = False
    if 'ютуб' in y:
        if xy == True:
            zapr.play()
        g = y
        a = str(g)
        print(a)
        try:
            l = a.split('ютубе ')
            n = l[1]
            print(n)
            web.open(f'{ytb}/results?search_query={n}')
        except:
            web.open(ytb)
        xy = False
    if 'инет' in y or 'интернет' in y:
        if xy == True:
            zapr.play()
        g = y
        a = str(g)
        print(a)
        if 'инете' in a:
            l = a.split('инете')
        else:
            l = a.split('интернете')
        n = l[-1]
        web.open(www+n)
        xy = False
        
    if 'погод' in y:
        if xy == True:
            zapr.play()
        if 'завтра' in y:
            web.open(gsm + 'tomorrow')
        else:
            web.open(gsm)
        xy = False
    if 'разверни' in y:
        if xy == True:
            sogl()
        press_and_release('f')
        xy = False

    if 'открой' in y:
        if xy == True:
            sogl()
        if 'вконтакт' in y or 'быка' in y or 'лука' in y or 'вака' in y:
            web.open('https://vk.com/feed')
        if 'телег' in y: 
            os.startfile(r"C:\Progs\Telegram\Telegram Desktop\Telegram.exe")
        if 'декор' in y or 'корт' in y: 
            os.startfile(r'C:\Users\PCMan\AppData\Local\Discord\Update.exe --processStart Discord.exe')
        xy = False

    if 'закрой' in y:
        if xy == True:
            sogl()
        if 'телег' in y: 
            os.system('TASKKILL /IM Telegram.exe /T')
        if 'декор' in y or 'корт' in y: 
            os.system('TASKKILL /IM Discord.exe /T')
        xy = False

    #Всё, связанное с громкостью
    if 'громче' in y:
        if xy == True:
            sogl()
        press_and_release('volume up')
        press_and_release('volume up')
        press_and_release('volume up')
        xy = False

    if 'тише' in y:
        if xy == True:
            sogl()
        press_and_release('volume down')
        press_and_release('volume down')
        press_and_release('volume down')
        xy = False

    if 'громко'in y and 'минимум' in y:
        for i in range(100):
            press_and_release('volume down')
        press_and_release('volume up')    
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' ноль' in y or 'выключи звук' in y:
        for i in range(100):
            press_and_release('volume down')        
        if xy == True:
            sogl()
        xy = False
        
    if 'громко' in y and ' десять':
        for i in range(100):
            press_and_release('volume down')
        for i in range(5):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' два' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(10):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' три' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(15):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' сорок' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(20):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if ('громко' in y and ' пять' in y) or ('громко' in y and ' наполовин' in y):
        for i in range(100):
            press_and_release('volume down')
        for i in range(25):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' шесть' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(30):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' семь' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(35):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' восемь' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(40):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if 'громко' in y and ' девяносто' in y:
        for i in range(100):
            press_and_release('volume down')
        for i in range(45):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False

    if ('громко'in y and 'максимум' in y) or ('громко' in y and ' сто' in y):
        for i in range(100):
            press_and_release('volume up')
        if xy == True:
            sogl()
        xy = False


    #Конец всего, связанного со звуком=)

    #Музыка 
    if 'включи музыку' in y or 'печи музыку' in y:
        if xy == True:
            sogl()
        web.open('https://vk.com/feed')
        time.sleep(3)
        press_and_release('play/pause media')
        xy = False

    if 'выключи музыку' in y:
        if xy == True:
            sogl()
        press_and_release('stop media')
        xy = False

    if 'пауз' in y:
        if xy == True:
            sogl()
        press_and_release('play/pause media')
        xy = False

    if 'возобновить' in y or 'выгодной' in y or 'выгодно ли' in y:
        if xy == True:
            sogl()
        press_and_release('play/pause media')
        xy = False

    if 'следующ' in y:
        if xy == True:
            sogl()
            press_and_release('next track')
        xy = False

    if 'предыдущ' in y:
        if xy == True:
            sogl()
        press_and_release('previous track')
        xy = False
#Протоколы
    if 'один дома' in y or 'протокол я один дома' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        web.open('https://www.youtube.com')
        web.open('https://vk.com/feed')
        os.startfile(r"C:\Progs\Telegram\Telegram Desktop\Telegram.exe")
        os.startfile(r"C:\Program Files\Algoritmika\vscode\Code.exe")
        os.startfile(r"C:\Progs\Steam\steam.exe")
        xy = False

    if 'атмосферн' in y and ('фронт' in y or 'фон' in y or 'пан' in y or 'он' in y):
        if xy == True:
            sogl()
        web.open('https://www.youtube.com/watch?v=_VTtXA2Cy-o')
        xy = False
        
    if 'жди' in y:
        if xy == True:
            diag()
        while not 'джар' in y:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                x = json.loads(rec.Result())
                print(x['text'])
                y = x['text']
        come()
        xy = False

    if 'выключи компьютер' in y or 'выключи компьютер' in y:
        sogl()
        time.sleep(2)
        os.system('shutdown -s -t 0')
    else:
        pass
