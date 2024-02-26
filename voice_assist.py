
from vosk import Model, KaldiRecognizer
import ffmpeg
import os
import json
import pyaudio
import sounddevice as sd
from pygame import mixer
import pyautogui as pag
import random as ran
import time
import webbrowser as web
from keyboard import press_and_release
import cv2
import mediapipe as mp
import threading









def hand_recognizer():
    try:
        # получаем изображение с камеры (0 - порядковый номер камеры в системе)
        camera = cv2.VideoCapture(0)
        mpHands = mp.solutions.hands            # подключаем раздел распознавания рук
        hands = mpHands.Hands()                 # создаем объект класса "руки"
        mpDraw = mp.solutions.drawing_utils     # подключаем инструменты для рисования



        # создаем массив из 21 ячейки для хранения высоты каждой точки
        h = [0 for i in range(21)]
        w = [0 for i in range(21)]

        # создаем массив из 5 ячеек для хранения положения каждого пальца
        finger = [0 for i in range(5)]

        # функция, возвращающая расстояние по модулю (без знака)
        def distance(point1, point2):
            return abs(point1 - point2)

        while run:
            # получаем один кадр из видеопотока
            good, img = camera.read()
            # преобразуем кадр в RGB
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


            if cv2.waitKey(1) & 0xFF == 27:     # ждем нажатия клавиши q в течение 1 мс
                break             # если нажмут, всё закрываем

            # получаем результат распознавания
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:                            # если обнаружили точки руки
                for handLms in results.multi_hand_landmarks:            # получаем координаты каждой точки

                    # при помощи инструмента рисования проводим линии между точками
                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                    # работаем с каждой точкой по отдельности
                    # создаем список от 0 до 21 с координатами точек
                    for id, point in enumerate(handLms.landmark):
                        # получаем размеры изображения с камеры и масштабируем
                        width, height, color = img.shape
                        width, height = int(point.x * height), int(point.y * width)
                        

                        # заполняем массив высотой каждой точки
                        h[id] = height
                        w[id] = width

                        if id == 8:              # выбираем нужную точку
                            # рисуем нужного цвета кружок вокруг выбранной точки
                            cv2.circle(img, (width, height), 15,
                                    (255, 0, 255), cv2.FILLED)
                        if id == 12:
                            cv2.circle(img, (width, height), 15,
                                    (0, 0, 255), cv2.FILLED)

                    # получаем расстояние, с которым будем сравнивать каждый палец
                    distanceGoodH = distance(
                        h[0], h[3]) + (distance(h[0], h[2]) / 2)

                    distanceGoodW = distance(
                        w[0], w[3]) + (distance(w[0], w[2]) / 2)
                    # заполняем массив 1 (палец поднят) или 0 (палец сжат)
                    finger[1] = 1 if distance(h[0], h[8]) > distanceGoodH or distance(w[0], w[8]) > distanceGoodW else 0
                    finger[2] = 1 if distance(h[0], h[12]) > distanceGoodH or distance(w[0], w[12]) > distanceGoodW else 0
                    finger[3] = 1 if distance(h[0], h[16]) > distanceGoodH or distance(w[0], w[16]) > distanceGoodW else 0
                    finger[4] = 1 if distance(h[0], h[20]) > distanceGoodH or distance(w[0], w[20]) > distanceGoodW else 0
                    finger[0] = 1 if distance(h[4], h[20]) > distanceGoodH or distance(w[4], w[20]) > distanceGoodW else 0



                    # готовим сообщение для отправки
                    msg = ''
                    # 0 - большой палец, 1 - указательный, 2 - средний, 3 - безымянный, 4 - мизинец
                    # жест "коза" - 01001
                    if not (finger[0]) and finger[1] and not (finger[2]) and not (finger[3]) and finger[4]:
                        msg = '@'
                        press_and_release('volume up')
                    if finger[0] and not (finger[1]) and not (finger[2]) and not (finger[3]) and not (finger[4]):
                        msg = '^'

                    if not (finger[0]) and finger[1] and finger[2] and not (finger[3]) and not (finger[4]):
                        msg = '$' + str(width) + ';'
                    if not (finger[0]) and finger[1] and not (finger[2]) and not (finger[3]) and not (finger[4]):
                        msg = '#' + str(width) + ';'
                        
                    # greece)
                    if not (finger[0]) and not (finger[1]) and finger[2] and not (finger[3]) and not (finger[4]):
                        msg = '*' + str(width) + ';'
                        press_and_release('volume down')

                    print(msg, finger[0], finger[1],
                        finger[2], finger[3], finger[4])
            cv2.waitKey(1)
            cv2.imshow("Image", img)       # выводим окно с нашим изображением
    except:
        print('No camera')


def microphone():
    # Ответы Джарвиса
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
    # ссылки
    gsm = 'https://www.gismeteo.ru/weather-stary-oskol-5024/'
    ytb = 'https://www.youtube.com'
    www = 'https://www.google.com/search?q='
    # нужные пременные
    global run
    run = True
    f = False
    # инициализация микрофона и распознавания речи
    model = Model('model')
    rec = KaldiRecognizer(model, 16000)
    pya = pyaudio.PyAudio()
    stream = pya.open(format=pyaudio.paInt16, channels=2,
                      rate=8000, input=True, frames_per_buffer=44100)
    stream.start_stream()

    re.play()

    while run != False:
        y = 'f'
        xy = True
        data = stream.read(4000)
        try:
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
                if 'вконтакт' in y or 'быка' in y or 'лука' in y or 'вака' in y:
                    if xy == True:
                        sogl()
                    web.open('https://vk.com/feed')
                if 'телег' in y:
                    if xy == True:
                        sogl()
                    # path to telegram
                    os.startfile(
                        r"C:\Progs\Telegram\Telegram Desktop\Telegram.exe")
                if 'декор' in y or 'корт' in y:
                    if xy == True:
                        sogl()
                    # path to discord
                    os.startfile(r'C:\Users\PCMan\AppData\Local\Discord\app-1.0.9032\Discord.exe')
                xy = False

            if 'закрой' in y:
                if xy == True:
                    sogl()
                if 'телег' in y:
                    os.system('TASKKILL /IM Telegram.exe /T')
                if 'декор' in y or 'корт' in y:
                    os.system('TASKKILL /IM Discord.exe /T')
                xy = False

            # Всё, связанное с громкостью
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


            if 'громко' in y:
                try:
                    # Подготовка входных данных
                    try:
                        vol = y.split('громкость ')[-1]
                    except:
                        vol = y.split('громко ')[-1]
                    if 'на ' in y:
                        vol = vol.split('на ')[-1]
                    # условия
                    match vol:
                        case 'ноль' | 'выключи звук':
                            for i in range(100):
                                press_and_release('volume down')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'минимум':
                            for i in range(100):
                                press_and_release('volume down')
                            press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False
                            
                        case 'десять':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(5):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'два' | 'двадцать':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(10):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'три' | 'тридцать':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(15):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'сорок':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(20):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'пять' | 'пятьдесят' | 'наполовин':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(25):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'шесть' | 'шестьдесят':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(30):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'семь' | 'семьдесят':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(35):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'восемь' | 'восемьдесят':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(40):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'девяносто' | 'девять':
                            for i in range(100):
                                press_and_release('volume down')
                            for i in range(45):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False

                        case 'максимум' | 'сто':
                            for i in range(100):
                                press_and_release('volume up')
                            if xy == True:
                                sogl()
                            xy = False
                except:
                    pass
            # Конец всего, связанного с громкостью=)


            # Музыка
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
        # Протоколы
            if 'один дома' in y or 'протокол я один дома' in y:
                if xy == True:
                    sogl()
                time.sleep(1)
                web.open('https://www.youtube.com')
                web.open('https://vk.com/feed')
                os.startfile(r"C:\Progs\Telegram\Telegram Desktop\Telegram.exe")
                os.startfile(r"C:\Program Files\Algoritmika\vscode\Code.exe")
                os.startfile(r"C:\Progs\Steam\steam.exe")
                time.sleep(3)
                press_and_release('play/pause media')   
                xy = False

            if 'за работу' in y or 'на работу' in y or 'протокол за работу' in y:
                if xy == True:
                    sogl()
                time.sleep(1)
                web.open('https://vk.com/feed')
                os.startfile(r"C:\Progs\Telegram\Telegram Desktop\Telegram.exe")
                os.startfile(r"C:\Program Files\Algoritmika\vscode\Code.exe")
                time.sleep(3)
                press_and_release('play/pause media')   
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
        except:
            run = False


thread = threading.Thread(target=microphone)
thread2 = threading.Thread(target=hand_recognizer)
thread.start()
thread2.start()
