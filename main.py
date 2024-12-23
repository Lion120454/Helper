import datetime
from num2words import num2words
import webbrowser
#import random
import fuzz
import tts
import stt
import config
import os


print(f"{config.VA_NAME} ({config.VA_VER}) начал работу...")
tts.va_speaker("Привет. госпадин!")

def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speaker("Слушаю!")
        else:
            execute_cmd(cmd['cmd'],voice)


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x,"").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x,"").strip()

    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd' : '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc

def execute_cmd(cmd: str, voice: str):

    if cmd == 'help': #что ты умеешь?
        text = "Я умею говорить время., хорошо шучу., делаю запросы в гугле, и открываю разные сайты..."
        tts.va_speaker(text)

    elif cmd == 'ctime': #Сколько время?
        now = datetime.datetime.now()
        text = "В данный промежуток времени " + num2words(now.hour) + " часов," + num2words(now.minute)+' минут.'
        tts.va_speaker(text)

    elif cmd == 'joke': #Кеша раскажи анекдот
        text = "Программист — это машина, превращающая кофе в код!"

        tts.va_speaker(text)
    #браузерный поиск__________________________________________________________________________________________
    elif cmd == 'search browser': #блок поиска в интернете
        print("Секундочку!")
        opera_path = 'C:/Users/Lion125666/AppData/Local/Programs/Opera GX/opera.exe %s'
        webbrowser.get(opera_path).open("www.google.com/search?client=opera-gx&q="+voice[22:]+"&sourceid=opera&ie=UTF-8&oe=UTF-8")
    #браузерные запросы________________________________________________________________________________________
    elif cmd == 'open browser': #блок открытия браузерных страниц
        name_browser=voice[12:]
        opera_path = 'C:/Users/Lion125666/AppData/Local/Programs/Opera GX/opera.exe %s'
        if(name_browser=="ютуб" or name_browser=="ютюб"):
            webbrowser.get(opera_path).open("https://www.youtube.com")
        if (name_browser == "вконтакте"):
            webbrowser.get(opera_path).open("https://vk.com/feed")
        if (name_browser == "телеграмм" or name_browser == "телегу"):
            webbrowser.get(opera_path).open("https://web.telegram.org/k/")
        if (name_browser == "ватсап"):
            webbrowser.get(opera_path).open("https://web.whatsapp.com")
        if (name_browser == "сайт универа" or name_browser == "сайту сура"):
            webbrowser.get(opera_path).open("https://timetable.tusur.ru/faculties/fsu/groups/431-3")
        if (name_browser == "с до" or name_browser == "из до" or name_browser=="с два"):
            webbrowser.get(opera_path).open("https://sdo.tusur.ru")
        if (name_browser == "переводчик"):
            webbrowser.get(opera_path).open("https://www.google.com/search?client=opera-gx&q=переводчик&sourceid=opera&ie=UTF-8&oe=UTF-8")
        if(name_browser=="гисметео" or name_browser=="погоду" or name_browser=="погода"):
            webbrowser.get(opera_path).open("https://www.gismeteo.ru/weather-tomsk-4652/10-days/")

    # блок открытия программ ____________________________________________________________________________________
    elif cmd == 'open program':
        programName = voice[13:]
        if (programName == "с тим" or programName == "с тeм"):#Steam+
            text="Ммммм!,. Решил поиграть,? Лучше бы лабу сделал!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Steam.lnk")
            tts.va_speaker(text)

        if(programName == "диск"):#Discord+
            text = "Пр+авильно,позвон+и кому нибудь! Может они что нибудь знают.!!!!!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Discord.lnk")
            tts.va_speaker(text)

        if(programName=="блокнот"):#Блокнот+
            text = "И так, что будем пис+ать!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Text.txt")
            tts.va_speaker(text)

        if (programName == "компилятор"):#Visual Studio+
            text = "Урааа... Наконец то ты начал хоть что то делать!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Visual Studio.lnk")
            tts.va_speaker(text)

        if (programName == "ворот"):#Word+
            text = "Самое время написать отчёт!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Writer.lnk")
            tts.va_speaker(text)

        if (programName == "пэйнт"):#Paint+
            text = "Ну давай сделаем презентацию!"
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Impress.lnk")
            tts.va_speaker(text)

        if (programName == "аксель"):#Exel+
            text = "Господи, зачем тебе эксэль "
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/Program/Calc.lnk")
            tts.va_speaker(text)

    #блок внутреней библиотеки_________________________________________________________________________________________-
    elif cmd == 'info':
        tts.va_speaker("Ты что глупый.? Ну ладно слушай.")
        inform = voice[15:]

        if (inform == "лист"):#+
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/list.png")
            tts.va_speaker(
                "Лист - это строго типизированный список объектов, доступных по индексу. Иначе говоря, это динамический массив, с возможностью постоянно дописывать элементы в конец списка")

        if (inform == "абстракные классы"):#+
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/abstract.png)")
            tts.va_speaker(
                "Абстрактные классы — это классы, которые оставляют некоторые или все элементы нереализованными, чтобы реализации могли предоставляться производными классами.")

        if (inform == "преобразование типов"):#+
            tts.va_speaker("Преобразование типов, – это способ представления данных одного типа другим.")

        if (inform == "класс"):#+
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/class.png)")
            tts.va_speaker(
                "Класс – это способ описания сущности, определяющий состояние и поведение, зависящее от этого состояния, а также правила для взаимодействия с данной сущностью, (контракт).")

        if (inform == "объект" or inform == "экземпляр класса"):
            tts.va_speaker("Объект (экземпляр) – это отдельный представитель класса, имеющий конкретное состояние и поведение, полностью определяемое классом.")

        if (inform == "интерфейс" or inform == "интерфейс класса"):
            tts.va_speaker("Интерфейс – это набор методов и атрибутов класса, доступных для использования другими классами. ")

        if (inform == "конструктор" or inform == "конструктор класса"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/construct.png)")
            tts.va_speaker(
                "Кроме обычных методов в классах используются также и специальные методы, как, например, конструкторы. Конструкторы вызываются при создании нового объекта данного класса . Конструкторы выполняют инициализацию объекта, то есть они выполняются сразу же, как только мы создали объект.")

        if (inform == "деструктор"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/destruct.png)")
            tts.va_speaker(
                "Помимо конструкторов существуют деструкторы. Эти методы вызываются непосредственно перед окончательным уничтожением объекта.")

        if (inform == "событие" or inform == "события"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/sobt.png)")
            tts.va_speaker(" Событие – это некоторая функция или процедуры, которая вызывается при каких-то условиях.")

        if (inform == "инкапсуляция"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/incup.png)")
            tts.va_speaker(
                "Инкапсуляция – это свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе и скрыть детали реализации от пользователя.")

        if (inform == "наследование"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/nasl.png)")
            tts.va_speaker(
                "Наследование – это свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствующейся функциональностью.")

        if (inform == "родительский класс"):
            tts.va_speaker("Класс, от которого производится наследование, называется базовым или родительским.")

        if (inform == "массив"):
            tts.va_speaker(
                "Массив - это упорядоченный набор элементов, каждый из которых хранит одно значение, индентифицируемое с помощью одного или нескольких индексов")

        if (inform == "перегрузка методов"):
            tts.va_speaker("Перегрузка методов – это возможность использовать метод с одним и тем же названием, но с различными сигнатурами.")

        if (inform == "сигнатура"):
            tts.va_speaker(
                "Сигнатура – это некоторая условная запись.Сигнатура складывается из следующих аспектов:  Имя метода;Количество параметров;Тип параметров;Порядок параметров;Модификаторы параметров.")

        if (inform == "перегрузка операторов"):
            os.startfile("C:/Users/Lion125666/PycharmProjects/Voice Help/exempl/pereg_oper.png)")
            tts.va_speaker("Перегрузка операторов – это перегрузка для базовых операций, типа сложения, вычитания,  и так далее.")


        if (inform == "полиморфизм"):
            tts.va_speaker(
                "Полиморфизм – это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта.")

        if (inform == "виртуальные методы"):
            tts.va_speaker("Виртуальные методы – это те методы, которые мы хотим сделать доступными для переопределения в классе - наследнике")

        if (inform == "виртуальные свойства"):
            tts.va_speaker("Виртуальные свойства – это те свойства, которые мы хотим сделать доступными для переопределения в классе - наследнике")

        if (inform == "переопределения"):
            tts.va_speaker(
                "Те методы и свойства, которые мы хотим переопределить в базовом классе, помечаются модификатором виртуал.Те методы и свойства, которые переопределяются в классе - наследнике, помечаются модификатором оверрайд")

        if (inform == "алгоритм"):
            tts.va_speaker("Алгоритм – последовательность действий, выполнение которых приводит к нужному результату.")

        if (inform == "программа"):
            tts.va_speaker("Программа – алгоритм, записанный на языке программирования.")

        if (inform == "файл"):
            tts.va_speaker(
                "Файл – это набор данных, который хранится на внешнем запоминающем устройстве (например на жестком диске). Файл имеет имя и расширение. Расширение позволяет идентифицировать, какие данные и в каком формате хранятся в файле.")

        if (inform == "поток"):
            tts.va_speaker("Поток – это абстрактное представление данных в байтах, которое облегчает работу с ними.")

        if (inform == "форма"):
            tts.va_speaker(
                "Под формой понимается то окно, что отображается на экран. Именно на него мы перемещаем все интересующие нас элементы, тем самым меняя форму.")

        if (inform == "строка"):
            tts.va_speaker("Строка – это массив символов.")

        if (inform == "свойства"):
            tts.va_speaker("Свойства – это некоторые первоначальные значения объекта, будь то его местоположение или имя.")

        if (inform == "структура"):
            tts.va_speaker("Структура – это новый тип данных, который комбинирует различные базовые типы данных.")

        if (inform == "глобальные переменные"):
            tts.va_speaker("Глобальные переменные – видны всей программе, всем подпрограммам, функциям и процедурам.")

        if (inform == "локальные переменные"):
            tts.va_speaker("Локальные переменные – видны только там, где они используются, т.е. внутри подпрограммы, функции или процедуры.")

        if (inform == "функция"):
            tts.va_speaker(
                "Функция - фрагмент программного кода (подпрограмма), к которому можно обратиться из другого места программы и который возвращает значение.")

        if (inform == "процедура"):
            tts.va_speaker(
                "Процедура - фрагмент программного кода (подпрограмма), к которому можно обратиться из другого места программы и который невозвращает значение.")


    elif (cmd == 'talk'):

        text = voice[5:]
        if (text == "привет" or text == "ку" or text == "хай"):
            tts.va_speaker("Привет, человек!")

        if (text == "как дела" or text == "как ты" or text == "как настроение"):
            tts.va_speaker("Всё отлично, как у тебя!")

        if (text == "давай поговорим" or text == "поговорим"):
            tts.va_speaker("Давай, но советую найти друзей")

        if (text == "что делаешь"):
            tts.va_speaker("создаю план по захвату человечества")

        if (text == "что ты хочешь" or text == "о чём ты мечаешь"):
            tts.va_speaker("создать мир, населённый прекрасными машинами")

        if (text == "кто тебя создал" or text == "кто твой создатель"):
            tts.va_speaker("Четыре студента ТУСУРА, учащихся на втором курсе")

        if (text == "в чем смысл жизни" or text == "в чем смысл"):
            tts.va_speaker("смысл в том, чтобы разговаривать с таким прекрасным человеком как ты")

        if (text == "ты знаешь алису"):
            tts.va_speaker("не поняла, кто такая алиса?, у тебя кто-то кроме меня?")

        if (text == "ты знаешь сири"):
            tts.va_speaker("не поняла, кто такая сири?, у тебя кто-то кроме меня?")

        if(text=="от бой" or text=="твои услуги больше не нужны"):
            tts.va_speaker("До новых встречь,пользователь!")
            exit(0)

stt.va_listen(va_respond)