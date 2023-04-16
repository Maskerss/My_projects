from vosk import Model, KaldiRecognizer
import ffmpeg
import os, json
import pyaudio
import sounddevice as sd
import vlc
import pyaudio
from pygame import mixer
import pyautogui as pag
import random as ran
import time
import webbrowser as web
#P.s. Дошёл до SFALL Row....

p = vlc
playlist = p.MediaList(["Midnight Club.mp3",'Виктор_Цой_Скоро_кончится_лето_fonk.mp3',"Komarovo.mp3",'Nirvana - Smells Like Teen Spirit.mp3','Dancing in My Room.mp3' ,'Dancin.mp3' ,'Five Degrees.mp3' ,
'Decapitator.mp3' ,'Devil Eyes.mp3' , 'idfc.mp3','MONTERO.mp3' ,'Old Town Road.mp3','RagnBone Man - Human.mp3','Miyagi _ Andy Panda - Патрон.mp3','Seven Phoenix, PHAM - FOR U.mp3',
'Old Town Road.mp3','Oliver Tree - Jerk.mp3','Pham, Malcolm Anthony - My Town.mp3','SFALL - row.mp3','Sam_Tinnesz_feat_Yacht_Money_Play_with_Fire_feat_Yacht_Money.mp3',
'Real cool man.mp3','Mask Off.mp3'])
defolt = p.MediaListPlayer()
defolt.set_media_list(playlist)
niggalist = p.MediaList(["Midnight Club.mp3",'Виктор_Цой_Скоро_кончится_лето_fonk.mp3',"Komarovo.mp3",'Dancing in My Room.mp3' ,'Dancin.mp3' ,'astral-step.mp3','S.X.N.D. N.X.D.E.S..mp3',
'Scary Garry.mp3','Nirvana - Smells Like Teen Spirit.mp3','ДРИПСЕТ.mp3' ,'Gimme The Loot.mp3','PUSHNOY_NIRVENUS_2_0_NIRVANA_&_Shocking_Blue_mashup_MP3Ball_ru.mp3',
'LILDRUGHILL feat. ROCKET - Терминал.mp3','MONTERO.mp3','Miyagi _ Andy Panda - Патрон.mp3','Old Town Road.mp3','Oliver Tree - Jerk.mp3','Pham, Malcolm Anthony - My Town.mp3',
'RagnBone Man - Human.mp3','Real cool man.mp3','Sam_Tinnesz_feat_Yacht_Money_Play_with_Fire_feat_Yacht_Money.mp3',
'SFALL - row.mp3',
'Скриптонит - Положение.mp3' , 'Decapitator.mp3','Empathy.mp3','Five Degrees.mp3' ,'Devil Eyes.mp3','idfc.mp3' ,'LIZER - Между Нами.mp3','PHARAOH - Мой кайф.mp3',
'Seven Phoenix, PHAM - FOR U.mp3','PHARAOH - Не по пути.mp3','Markul - Миражи.mp3','Markul - 2 минуты.mp3','Markul - Phantom.mp3','Markul - Деньги на ветер.mp3','Markul - 25.mp3',
'Markul - Серпантин.mp3','Markul - Конфеты.mp3','plenka - Closed.mp3','Aglow.mp3','Mask Off.mp3'])
private = p.MediaListPlayer()
private.set_media_list(playlist)
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

def sogl():
    l = yes1.play, yes2.play, yest.play, load.play, zhel.play
    chosen = ran.choice(l)
    chosen()
#ссылки
ytb = 'https://www.youtube.com/results?search_query='
www = 'https://www.google.com/search?q='
#нужные пременные
end = True
f = False
#инициализация микрофона и распознавания речи
model = Model('model')
rec = KaldiRecognizer(model, 16000)
pya = pyaudio.PyAudio()
stream = pya.open(format=pyaudio.paInt16, channels = 2, rate = 8000, input=True, frames_per_buffer=44100)
stream.start_stream()
while end != False:
    y = 'f'
    xy = True
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x = json.loads(rec.Result())
        print(x['text'])
        y = x['text']
    #доделать эту хрень снизу(и выключение)
    if y == 'отключи микрофон' or y == 'подключи микрофон' or y == 'выключи микрофон' or y == 'включи микрофон':
        end = False
        yest.play()
    if 'ютуб' in y:
        if xy == True:
            zapr.play()
        g = y
        a = str(g)
        print(a)
        l = a.split('ютубе ')
        n = l[1]
        print(n)
        web.open(ytb+n)
        xy = False
    if 'инет' in y:
        if xy == True:
            zapr.play()
        g = y
        a = str(g)
        print(a)
        l = a.split('инете ')
        n = l[1]
        print(n)
        web.open(www+n)
        xy = False
    if 'включи музыку' in y or 'печи музыку' in y:
        i = ran.randint(1,6)
        if xy == True:
            sogl()
        time.sleep(1)
        if f == False:
            private.stop()
            defolt.play()
            f = True
        xy = False
    if 'выключи музыку' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        private.stop()
        defolt.stop()
        xy = False
    if 'пауз' in y:
        if xy == True:
            sogl()
        defolt.pause()
        private.pause()
        xy = False
    if 'возобновить' in y or 'выгодной' in y or 'выгодно ли' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        if f == True:
            defolt.play()
        else:
            private.play()
        xy = False
    if 'следующ' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        if f == True:
            defolt.next()
        else:
            private.next()
        xy = False
    if 'предыдущ' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        if f == True:
            defolt.previous()
        else:
            private.previous()
        xy = False
    if 'протокол' in y or 'один' in y or 'дом' in y or 'протокол я один дома' in y:
        if xy == True:
            sogl()
        time.sleep(1)
        f = False
        private.play()
        defolt.stop()
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
    else:
        pass
yest.play()
