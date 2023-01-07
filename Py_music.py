import random
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
import os
import re
import shutil
import eyed3
import time
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
import mutagen

dict_music = ['Hammali, Navai - Птичка.mp3',
'Disturbed_-_A_Reason_to_Fight_musmorecom.mp3',
'Rosenfeld_-_I_Want_To_(musmore.com).mp3',
'Silent Child - Fuck You - muzykaws.mp3',
'Silent_Child_PatrickReza_-_Jump_musmorecom.mp3',
'Omido_Silent_Child_-_Me_My_Demons_musmorecom.mp3',
'KALEO - Skinny.mp3',
'Elvis_Drew_Avivian_-_Where_are_you_musportalorg.mp3',
'Rosenfeld_-_Body_musmorecom.mp3',
'rosenfeld-do-it-for-me.mp3',
'Two_Feet_-_Nightmares_musmorecom.mp3',
'iwilldiehere_akiaura_-_anbu_musmorecom.mp3',
'-ravnodushie-feat_-sjuzanna.mp3',
'Kaleo - Break My Baby [vzvukenet].mp3',
'_intelligency-outlaw.mp3',
'Ваня Дмитриенко - Венера-Юпитер.mp3',
'Джарахов Markul - Я В Моменте.mp3',
'Sia_-_Unstoppable_musmorecom.mp3',
'Duncan Laurence featFLETCHER - Arcade.mp3',
'Elley_Duhe_MIDDLE_OF_THE_NIGHT.mp3',
'Мот featАртем Пивоваров - Муссоны.mp3',
'Sweater Weather .mp3',
'The Neighbourhood - Afraid.mp3',
'The Neighborhood - Sweater Weather.mp3',
'The Neighbourhood - Daddy Issues.mp3',
'The Neighborhood - The Beach.mp3',
'Charlotte Cardin - Big Boy.mp3',
'Hooverphonic - Mad About You.mp3',
'bebe-rexha-im-a-messmpgidme.mp3',
'lil_wayne_wiz_khalifa_imagine_dragons_feat_logic_ty_dolla_sign_x.mp3',
'zayn-sia-dusk-till-dawnmpgidme.mp3',
'alec-benjamin-alessia-cara-let-me-down-slowlympbitcc.mp3',
'Daniela_Ustinova_Derniere_Danse_Kaver_na_russkom.mp3',
'skryaga.mp3',
'Morgenshtern - Селяви.mp3',
'blackbear - idfc.mp3',
'MrKitty - After Dark.mp3',
'Glass Animals - Heat Waves.mp3',
'marshmello-anne-marie-friendsmpbitcc.mp3',
'Black Sea.mp3',
'Sam_Tinnesz_feat_Yacht_Money_Play_with_Fire_feat_Yacht_Money.mp3',
'The Game.mp3',
'bellyache - Billie Eilish.mp3',
'mpwait-com_bwthuktxc.mp3',
'Billie Eilish - Therefore I Am.mp3',
'Между Нами.mp3',
'Мокрые кроссы.mp3',
'Cheba - Девочке .mp3',
'Привет.mp3',
'dj-yo-ax-el-ckay-love-nwantiti-remix-mp.mp3',
'У окна.mp3',
'escape Даня Милохин - so low.mp3',
'Elman - Антигерой.mp3',
'Ooes - Зима_mphubbest.mp3',
'ooes-noch.mp3',
'Тима Белорусских - Окей.mp3',
'Алёна Швец. - Скейтер.mp3',
'two_feet-i_feel_like_im_drowning.mp3',
'The_Remedy_For_A_Broken_Heart.mp3',
'Shimoro - Верю.mp3',
'shawn-mendes-camila-cabello-senoritampnamenet.mp3',
'rixton_me-and-my-broken-heart.mp3',
'R_NIN_-_ALL_GIRLS_ARE_THE_SAME_iPleercom.mp3',
'NRD - All Good Things Come to an End.mp3',
'Lilly_Wood_amp_The_Prick_Prayer_In_C_Robin_Schulz_Rem.mp3',
'Kina_-_Can_we_kiss_forever_(feat._Adriana_Proenza).mp3',
'kaleo_-_way_down_we_go_stopmusic.net.mp3',
'josh-a-pain-josh-a.mp3',
'intelligency_-_august_muzter.net.mp3',
'Dathan_Mirror_Masa_I_Think_I_m_Falling_for_You_Tik_tok.mp3',
'blackbear-hot-girl-bummer(myzon.top).mp3',
'billie_eilish_-_lovely_(feat._khalid)_stopmusic.net.mp3',
'trevor-daniel-falling.mp3',
'Bea_Miller_-_Feel_Something_(Slowed).mp3']

if not "Music" in os.listdir("D:\\"):
    os.mkdir("D:\Music")

root = Tk()
root.geometry('400x400')
root['bg'] = 'black'
root.title('Py music')
load_finish = False
del_finish = False
y = 0
u = 1
shuff = False
start_time = 0
t = 0
all = 0
p = 0
num_rule = False
cycle = False


def start():
    global load_finish, del_finish
    load_finish = False
    del_finish = False

    def q():
        root.quit()
        quit()

    def append_playlist():
        playlist.destroy()
        #backup.destroy()
        playlist_.destroy()
        listen.destroy()
        name_main.destroy()
        main.destroy()
        #q1.destroy()

        def left():
            if create.get() == '':
                back.destroy()
                create_text.destroy()
                create.destroy()
                root.unbind('<Return>')
                start()

        back = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09', command=left)
        create_text = Label(root, text='Enter playlist name and press enter: ', width=30, font=('Times', 12),
                            bg='#24ad09', fg='black')
        create = Entry(root, width=20, font=('Times', 12), bg='#24ad09', fg='black',
                       takefocus=True)
        back.pack(expand=1, anchor=NW)
        create_text.pack(expand=1)
        create.pack(expand=1)
        create.focus_set()

        def append_music(event):
            if create.get() == '':
                pass
            else:
                files = "D:\Music"
                files = os.listdir(files)
                if create.get() in files:
                    path = f"D:\Music\{create.get()}"
                else:
                    os.mkdir(f"D:\Music\{create.get()}")
                    path = f"D:\Music\{create.get()}"
                print(path)
                back.destroy()
                create_text.destroy()
                create.destroy()

                def left_2():
                    if load_finish:
                        back_2.destroy()
                        load_text.destroy()
                        load.destroy()
                        root.unbind('<Return>')
                        start()

                back_2 = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                    command=left_2)
                back_2.pack(expand=1, anchor=NW)
                load_text = Label(root, text='Select music for playlist: ', width=20, font=('Times', 12),
                                      bg='#24ad09', fg='black')
                load_text.pack(expand=1)

                def load():
                    global load_finish, num_rule
                    old_music_files = list(filedialog.askopenfilenames())
                    print(old_music_files)
                    list_music = os.listdir(path)

                    try:
                        def filter(lst):
                            old_path = lst[0][:lst[0].index(lst[0].split('/')[-1][0])]
                            news = [i.split('/')[-1] for i in lst]
                            news = [i.split('.mp3')[0] for i in news]
                            for i in range(len(news)):
                                news[i] = re.sub(r'[^А-яA-zА-я- ]', '', news[i])
                            for i in range(len(news)):
                                if news[i].endswith('.mp3'):
                                    pass
                                else:
                                    news[i] += '.mp3'
                            news = [old_path + str(i) for i in news]
                            return news

                        if len(old_music_files) == []:
                            print(1)
                            raise ValueError

                        for i in range(len(old_music_files)):
                            for j in range(len(list_music)):
                                if old_music_files[i].split('/')[-1] == list_music[j][4:]:
                                    print(old_music_files[i].split('/')[-1])
                                    print(list_music[j][4:])
                                    print(2)
                                    raise ValueError

                        news = filter(old_music_files)
                        if len(news) > 1:
                            for i in range(len(news)):
                                if news[i - 1].split('/')[-1] == news[i].split('/')[-1]:
                                    print(3)
                                    raise ValueError

                        for i in zip(old_music_files, news):
                            os.rename(i[0], i[1])
                        old_music_files = news

                        def last_4chars(x):
                            return (x[:4])

                        list_music = sorted(list_music, key=last_4chars)
                        print(list_music)
                        if list_music != []:
                            # num - позиция трека
                            num = len(list_music) + 1  # в конец
                            if num_rule:
                                print(num_rule)
                                # в начало + переименовка уже имееющихся файлов
                                num = 1
                                old_list_name = os.listdir(path)

                                def last_4chars(x):
                                    return (x[:4])

                                old_list_name = sorted(old_list_name, key=last_4chars)
                                num_plus = len(old_music_files)
                                print(num_plus)
                                new_list_name = []
                                for i in range(len(old_list_name)):
                                    old = str(old_list_name[i][:4])
                                    print(old)
                                    try:
                                        old = int(old)
                                    except:
                                        try:
                                            old = int(old[1:])
                                        except:
                                            try:
                                                old = int(old[2:])
                                            except:
                                                old = int(old[3])

                                    n = old + num_plus
                                    if 0 <= n <= 9:
                                        new_name = old_list_name[i][:3] + str(n) + old_list_name[i][4:]
                                        new_list_name.append(new_name)
                                    elif 10 <= n <= 99:
                                        new_name = old_list_name[i][:2] + str(n) + old_list_name[i][4:]
                                        new_list_name.append(new_name)
                                    elif 100 <= n <= 999:
                                        new_name = old_list_name[i][:1] + str(n) + old_list_name[i][4:]
                                        new_list_name.append(new_name)
                                    elif 1000 <= n <= 9999:
                                        new_name = old_list_name[i] + str(n) + old_list_name[i][4:]
                                        new_list_name.append(new_name)
                                new_list_name = [f"{path}\{i}".replace('\\', '/') for i in new_list_name]
                                old_list_name = [f"{path}\{i}".replace('\\', '/') for i in old_list_name]
                                for i in zip(old_list_name, new_list_name):
                                    os.rename(i[0], i[1])

                            old_namel = [f"{path}\{i.split('/')[-1]}".replace('\\', '/') for i in old_music_files]
                            new_namel = [f"{i.split('/')[-1]}".replace('\\', '/') for i in old_music_files]
                            n1 = 0
                            for i in range(len(new_namel)):
                                if 0 <= num <= 9:
                                    new_namel[n1] = path + '\\' + '000' + str(num) + new_namel[n1]
                                elif 10 <= num <= 99:
                                    new_namel[n1] = path + '\\' + '00' + str(num) + new_namel[n1]
                                elif 100 <= num <= 999:
                                    new_namel[n1] = path + '\\' + '0' + str(num) + new_namel[n1]
                                elif 1000 <= num <= 9999:
                                    new_namel[n1] = path + '\\' + str(num) + new_namel[n1]
                                n1 += 1
                                num += 1

                            new_namel = [i.replace('\\', '/') for i in new_namel]
                            for i in old_music_files:
                                shutil.copy(i, path)
                            for i in zip(old_namel, new_namel):
                                os.rename(i[0], i[1])
                            if os.listdir(path) != []:
                                num_rule = False
                                load_finish = True
                        else:
                            num = 1
                            old_namel = [f"{path}\{i.split('/')[-1]}".replace('\\', '/') for i in old_music_files]
                            new_namel = [f"{i.split('/')[-1]}".replace('\\', '/') for i in old_music_files]
                            n1 = 0
                            for i in range(len(new_namel)):
                                if 0 <= num <= 9:
                                    new_namel[n1] = path + '\\' + '000' + str(num) + new_namel[n1]
                                elif 10 <= num <= 99:
                                    new_namel[n1] = path + '\\' + '00' + str(num) + new_namel[n1]
                                elif 100 <= num <= 999:
                                    new_namel[n1] = path + '\\' + '0' + str(num) + new_namel[n1]
                                elif 1000 <= num <= 9999:
                                    new_namel[n1] = path + '\\' + str(num) + new_namel[n1]
                                n1 += 1
                                num += 1

                            new_namel = [i.replace('\\', '/') for i in new_namel]
                            for i in old_music_files:
                                shutil.copy(i, path)

                            for i in zip(old_namel, new_namel):
                                os.rename(i[0], i[1])

                            if os.listdir(path) != []:
                                load_finish = True
                    except:
                        load_finish = True
                        left_2()

                load = Button(root, text='Load', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                  command=load)

                def in_start():
                    global num_rule
                    num_rule = True
                    in_start.destroy()
                    in_end.destroy()
                    to_pos.destroy()
                    load.pack(expand=1)

                def in_end():
                    global num_rule
                    num_rule = False
                    in_start.destroy()
                    in_end.destroy()
                    to_pos.destroy()
                    load.pack(expand=1)

                def to_pos():
                    in_start.destroy()
                    in_end.destroy()
                    to_pos.destroy()
                    back_2.destroy()

                    def left_3():
                        global load_finish
                        if load_finish:
                            load_text.destroy()
                            back_3.destroy()
                            to_pos_text.destroy()
                            to_pos_t.destroy()
                            root.unbind('<Return>')
                            start()
                    back_3 = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                    command=left_3)
                    back_3.pack(expand=1, anchor=NW)
                    load_text.pack(expand=1, side=BOTTOM)
                    to_pos_text.pack(expand=1, side=LEFT)
                    to_pos_t.pack(expand=1, side=LEFT)
                    to_pos_t.focus_set()
                    load_text.config(text='Select 1 track: ')

                    def load_track(event):
                        if to_pos_t.get() == '':
                            pass
                        else:
                            global load_finish
                            old_music_files = list(filedialog.askopenfilenames())
                            if len(old_music_files) > 1:
                                pass
                            else:
                                try:
                                    num = int(to_pos_t.get())
                                    print(old_music_files)
                                    list_music = os.listdir(path)
                                    if list_music == []:
                                        num = 0
                                    if num > len(list_music):
                                        raise ValueError
                                    else:
                                        print(len(list_music))
                                        if num != len(list_music):
                                            # если num = 1 то как выше
                                            # если нет, то следующим после num  +1
                                            print(num)
                                            if num == 1:
                                                def filter(lst):
                                                    old_path = lst[0][:lst[0].index(lst[0].split('/')[-1][0])]
                                                    news = [i.split('/')[-1] for i in lst]
                                                    news = [i.split('.mp3')[0] for i in news]
                                                    for i in range(len(news)):
                                                        news[i] = re.sub(r'[^А-яA-zА-я- ]', '', news[i])
                                                    for i in range(len(news)):
                                                        if news[i].endswith('.mp3'):
                                                            pass
                                                        else:
                                                            news[i] += '.mp3'
                                                    news = [old_path + str(i) for i in news]
                                                    return news

                                                old_namel = f"{path}\{old_music_files[0].split('/')[-1]}".replace('\\',
                                                                                                                  '/')
                                                new_music_files = filter(old_music_files)
                                                print(new_music_files)
                                                new_namel = new_music_files[0].split('/')[-1]
                                                if 0 <= num <= 9:
                                                    new_namel = path + '\\' + '000' + str(num) + new_namel
                                                elif 10 <= num <= 99:
                                                    new_namel = path + '\\' + '00' + str(num) + new_namel
                                                elif 100 <= num <= 999:
                                                    new_namel = path + '\\' + '0' + str(num) + new_namel
                                                elif 1000 <= num <= 9999:
                                                    new_namel = path + '\\' + str(num) + new_namel

                                                new_namel = new_namel.replace('\\', '/')
                                                print(old_namel, new_namel)
                                                old_list_name = os.listdir(path)

                                                def last_4chars(x):
                                                    return (x[:4])

                                                old_list_name = sorted(old_list_name, key=last_4chars)
                                                num_plus = len(old_music_files)
                                                new_list_name = []
                                                for i in range(len(old_list_name)):
                                                    old = str(old_list_name[i][:4])
                                                    print(old)
                                                    try:
                                                        old = int(old)
                                                    except:
                                                        try:
                                                            old = int(old[1:])
                                                        except:
                                                            try:
                                                                old = int(old[2:])
                                                            except:
                                                                old = int(old[3])

                                                    n = old + num_plus
                                                    if 0 <= n <= 9:
                                                        new_name = old_list_name[i][:3] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 10 <= n <= 99:
                                                        new_name = old_list_name[i][:2] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 100 <= n <= 999:
                                                        new_name = old_list_name[i][:1] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 1000 <= n <= 9999:
                                                        new_name = old_list_name[i] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                new_list_name = [f"{path}\{i}".replace('\\', '/') for i in
                                                                 new_list_name]
                                                old_list_name = [f"{path}\{i}".replace('\\', '/') for i in
                                                                 old_list_name]
                                                for i in zip(old_list_name, new_list_name):
                                                    os.rename(i[0], i[1])

                                                for i in old_music_files:
                                                    shutil.copy(i, path)

                                                os.rename(old_namel, new_namel)
                                                if os.listdir(path) != []:
                                                    load_finish = True
                                            else:
                                                def filter(lst):
                                                    old_path = lst[0][:lst[0].index(lst[0].split('/')[-1][0])]
                                                    news = [i.split('/')[-1] for i in lst]
                                                    news = [i.split('.mp3')[0] for i in news]
                                                    for i in range(len(news)):
                                                        news[i] = re.sub(r'[^А-яA-zА-я- ]', '', news[i])
                                                    for i in range(len(news)):
                                                        if news[i].endswith('.mp3'):
                                                            pass
                                                        else:
                                                            news[i] += '.mp3'
                                                    news = [old_path + str(i) for i in news]
                                                    return news

                                                old_namel = f"{path}\{old_music_files[0].split('/')[-1]}".replace('\\',
                                                                                                                  '/')
                                                new_music_files = filter(old_music_files)
                                                print(new_music_files)
                                                new_namel = new_music_files[0].split('/')[-1]
                                                if 0 <= num <= 9:
                                                    new_namel = path + '\\' + '000' + str(num) + new_namel
                                                elif 10 <= num <= 99:
                                                    new_namel = path + '\\' + '00' + str(num) + new_namel
                                                elif 100 <= num <= 999:
                                                    new_namel = path + '\\' + '0' + str(num) + new_namel
                                                elif 1000 <= num <= 9999:
                                                    new_namel = path + '\\' + str(num) + new_namel

                                                new_namel = new_namel.replace('\\', '/')
                                                print(old_namel, new_namel)
                                                old_list_name = list_music[num - 1:]

                                                def last_4chars(x):
                                                    return (x[:4])

                                                old_list_name = sorted(old_list_name, key=last_4chars)
                                                num_plus = len(old_music_files)
                                                new_list_name = []
                                                for i in range(len(old_list_name)):
                                                    old = str(old_list_name[i][:4])
                                                    print(old)
                                                    try:
                                                        old = int(old)
                                                    except:
                                                        try:
                                                            old = int(old[1:])
                                                        except:
                                                            try:
                                                                old = int(old[2:])
                                                            except:
                                                                old = int(old[3])

                                                    n = old + num_plus
                                                    if 0 <= n <= 9:
                                                        new_name = old_list_name[i][:3] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 10 <= n <= 99:
                                                        new_name = old_list_name[i][:2] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 100 <= n <= 999:
                                                        new_name = old_list_name[i][:1] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                    elif 1000 <= n <= 9999:
                                                        new_name = old_list_name[i] + str(n) + old_list_name[i][4:]
                                                        new_list_name.append(new_name)
                                                new_list_name = [f"{path}\{i}".replace('\\', '/') for i in
                                                                 new_list_name]
                                                old_list_name = [f"{path}\{i}".replace('\\', '/') for i in
                                                                 old_list_name]
                                                for i in zip(old_list_name, new_list_name):
                                                    os.rename(i[0], i[1])

                                                for i in old_music_files:
                                                    shutil.copy(i, path)

                                                os.rename(old_namel, new_namel)
                                                if os.listdir(path) != []:
                                                    load_finish = True

                                        else:
                                            # последнему елементу даем num +1 а новому num
                                            print(num)

                                            def filter(lst):
                                                old_path = lst[0][:lst[0].index(lst[0].split('/')[-1][0])]
                                                news = [i.split('/')[-1] for i in lst]
                                                news = [i.split('.mp3')[0] for i in news]
                                                for i in range(len(news)):
                                                    news[i] = re.sub(r'[^А-яA-zА-я- ]', '', news[i])
                                                for i in range(len(news)):
                                                    if news[i].endswith('.mp3'):
                                                        pass
                                                    else:
                                                        news[i] += '.mp3'
                                                news = [old_path + str(i) for i in news]
                                                return news

                                            old_namel = f"{path}\{old_music_files[0].split('/')[-1]}".replace('\\', '/')
                                            new_music_files = filter(old_music_files)
                                            print(new_music_files)
                                            new_namel = new_music_files[0].split('/')[-1]
                                            if 0 <= num <= 9:
                                                new_namel = path + '\\' + '000' + str(num) + new_namel
                                            elif 10 <= num <= 99:
                                                new_namel = path + '\\' + '00' + str(num) + new_namel
                                            elif 100 <= num <= 999:
                                                new_namel = path + '\\' + '0' + str(num) + new_namel
                                            elif 1000 <= num <= 9999:
                                                new_namel = path + '\\' + str(num) + new_namel

                                            new_namel = new_namel.replace('\\', '/')
                                            print(old_namel, new_namel)
                                            old_namet = list_music[-1]
                                            new_namet = list_music[-1][:4]
                                            num += 1
                                            if 0 <= num <= 9:
                                                new_namet = path + '\\' + '000' + str(num) + old_namet[4:]
                                            elif 10 <= num <= 99:
                                                new_namet = path + '\\' + '00' + str(num) + old_namet[4:]
                                            elif 100 <= num <= 999:
                                                new_namet = path + '\\' + '0' + str(num) + old_namet[4:]
                                            elif 1000 <= num <= 9999:
                                                new_namet = path + '\\' + str(num) + old_namet[4:]
                                            old_namet = path + '\\' + old_namet
                                            new_namet = new_namet.replace('\\', '/')
                                            old_namet = old_namet.replace('\\', '/')
                                            print(old_namet, new_namet)

                                            for i in old_music_files:
                                                shutil.copy(i, path)

                                            os.rename(old_namel, new_namel)
                                            os.rename(old_namet, new_namet)
                                            if os.listdir(path) != []:
                                                load_finish = True
                                except:
                                    to_pos_text.config(text='Enter the right position:')

                    root.bind('<Return>', load_track)
                in_start = Button(root, text='Copy to the beginning', width=20, font=('Times', 10), bg='black',
                                  fg='#24ad09',
                                  command=in_start)
                in_start.pack(expand=1)
                to_pos = Button(root, text='Copy to position 1 track', width=20, font=('Times', 10), bg='black',
                                fg='#24ad09',
                                command=to_pos)
                to_pos_text = Label(root, text='Position:', width=20, font=('Times', 10), bg='black',
                                fg='#24ad09')
                to_pos_t = Entry(root, width=20, font=('Times', 10), bg='#24ad09',
                                    fg='black')
                to_pos.pack(expand=1)
                in_end = Button(root, text='Copy to end of playlist', width=20, font=('Times', 10), bg='black',
                                  fg='#24ad09',
                                  command=in_end)
                in_end.pack(expand=1)

        root.bind('<Return>', append_music)

    def listen_playlist():
        global y, u, p
        files = "D:\Music"
        files = os.listdir(files)
        list_playlists = files
        playlist.destroy()
        playlist_.destroy()
        #backup.destroy()
        listen.destroy()
        name_main.destroy()
        main.destroy()
        #q1.destroy()
        if len(list_playlists) != 0:
            def play(nam):
                global shuff, y, u, start_time
                path = f"D:\Music\{nam}"
                print(path)
                print(' ')
                list_tracks = os.listdir(path)

                def last_4chars(x):
                    return (x[:4])

                list_tracks = sorted(list_tracks, key=last_4chars)
                list = root.pack_slaves()
                for l in list:
                    l.destroy()
                if list_tracks == []:

                    def left_2():
                        if load_finish:
                            back_2.destroy()
                            load_text.destroy()
                            load.destroy()

                            start()

                    back_2 = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                    command=left_2)
                    back_2.pack(expand=1, anchor=NW)
                    load_text = Label(root, text='Select music for playlist: ', width=20, font=('Times', 12),
                                      bg='#24ad09', fg='black')
                    load_text.pack(expand=1)

                    def load():
                        global load_finish
                        music_files = filedialog.askopenfilenames()
                        for i in music_files:
                            shutil.copy(i, path)
                        if os.listdir(path) != []:
                            load_finish = True

                    load = Button(root, text='Load', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                  command=load)
                    load.pack(expand=1)
                else:
                    mixer.init()
                    pygame.init()

                    class Track:
                        playing_state = False
                        name = ''
                        time_s = 0

                        def __init__(self, _job):
                            self._job = _job

                        def cancel(self):
                            if self._job is not None:
                                root.after_cancel(self._job)
                                self._job = None

                        def play_track(self, name):
                            self.name = name
                            mixer.music.load(name)
                            mixer.music.play()

                        def pause(self):
                            if not self.playing_state:
                                mixer.music.pause()
                                self.playing_state = True
                            else:
                                mixer.music.unpause()
                                self.playing_state = False

                        def volume(self, v=0.5):
                            # 0 => 1
                            mixer.music.set_volume(v)

                        def stop(self):
                            mixer.music.stop()

                        def next(self, name_next):
                            mixer.music.queue(name_next)

                        def time_song(self, n):
                            self.time_s = round((MP3(n).info.length+1))
                            return self.time_s

                    def left():
                        global y
                        y = 0
                        list = root.pack_slaves()
                        for l in list:
                            l.destroy()
                        root.unbind('<KeyPress>')
                        now_song.stop()
                        now_song.cancel()
                        start()

                    back = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                  command=left)
                    back.pack(expand=1, anchor=NW)

                    now_song = Track(None)
                    normal_list_tracks = []

                    for i in range(len(list_tracks)):
                        path_song = path + '\\' + list_tracks[i]
                        normal_list_tracks.append(path_song)

                    shuff_list_tracks = sorted(normal_list_tracks, key=lambda k: random.random())
                    shuff_list_tracks = sorted(shuff_list_tracks, key=lambda k: random.random())

                    print(list_tracks)
                    print(normal_list_tracks)
                    print(shuff_list_tracks)
                    print(' ')
                    tl = ''
                    m = Frame(root)
                    song = Label(m, text=tl, width=30, font=('Times', 12), bg='#20fc03', fg='black', relief=SUNKEN)

                    def viev(l):
                        print(l)
                        audio = eyed3.load(f"{l}")
                        try:
                            tl = str(audio.tag.artist) + ' - ' + str(audio.tag.title)
                        except AttributeError:
                            tl = l[13:]
                        song.config(text=tl)

                    def img(filename):
                        mp3 = mutagen.File(filename)
                        allpix = []
                        for tag in mp3.items():
                            if tag[0][:4] == 'APIC':
                                pic = tag[1]
                                new_name = "D:\\Projects\\Python\\Py music\\Images\\" + f'img.' + str(
                                    pic.mime.split('/')[1])
                                file = open(new_name, "wb")
                                file.write(pic.data)
                                file.close()
                                allpix.append(new_name)
                        return allpix

                    print(normal_list_tracks[y])
                    viev(normal_list_tracks[y])

                    now_song.play_track(normal_list_tracks[y])

                    m1 = Frame(root)
                    viev_img = Label(root, bg='#24ad09',
                                image=ImageTk.PhotoImage(Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png')))
                    viev_img.pack(expand=1)
                    var = 0.1

                    def vol(val):
                        v = float(val)
                        var = v
                        now_song.volume(var)

                    volume = Scale(m1, orient=HORIZONTAL, from_=0, resolution=0.02, to=1, command=vol)
                    volume.set(0.1)
                    now_song.volume(0.1)

                    size_img = (200, 200)

                    im = img(normal_list_tracks[y])
                    if im != []:
                        album = Image.open(im[0])
                        album.thumbnail(size_img, Image.ANTIALIAS)
                        album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                        album = ImageTk.PhotoImage(Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                        viev_img.config(image=album)

                    global t
                    t = now_song.time_song(normal_list_tracks[y])
                    start_time = time.time()

                    def shf():
                        global shuff
                        shuff = True

                    def nrm():
                        global shuff
                        shuff = False

                    def up():
                        global y, u, shuff, start_time, t
                        if shuff:
                            y = y + 1
                            if y > len(shuff_list_tracks) - 1:
                                y = len(shuff_list_tracks) - y
                            viev(shuff_list_tracks[y])
                            now_song.stop()
                            now_song.play_track(shuff_list_tracks[y])
                            t = now_song.time_song(shuff_list_tracks[y])
                            start_time = time.time()
                            #now_song.volume(var)
                            
                            im = img(shuff_list_tracks[y])
                            if im != []:
                                album = Image.open(im[0])
                                album.thumbnail(size_img, Image.ANTIALIAS)
                                album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                album = ImageTk.PhotoImage(
                                    Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                viev_img.config(image=album)

                        else:
                            y = y + 1
                            if y > len(normal_list_tracks) - 1:
                                y = len(normal_list_tracks) - y
                            viev(normal_list_tracks[y])
                            now_song.stop()
                            now_song.play_track(normal_list_tracks[y])
                            t = now_song.time_song(normal_list_tracks[y])
                            start_time = time.time()
                            #now_song.volume(var)
                            
                            im = img(normal_list_tracks[y])
                            if im != []:
                                album = Image.open(im[0])
                                album.thumbnail(size_img, Image.ANTIALIAS)
                                album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                album = ImageTk.PhotoImage(
                                    Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                viev_img.config(image=album)

                    def down():
                        global y, u, shuff, start_time, t
                        if shuff:
                            y = y - 1
                            if y < 0:
                                y = len(shuff_list_tracks) + y
                            viev(shuff_list_tracks[y])
                            now_song.stop()
                            t = now_song.time_song(shuff_list_tracks[y])
                            now_song.play_track(shuff_list_tracks[y])
                            start_time = time.time()
                            #now_song.volume(var)
                            
                            im = img(shuff_list_tracks[y])
                            if im != []:
                                album = Image.open(im[0])
                                album.thumbnail(size_img, Image.ANTIALIAS)
                                album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                album = ImageTk.PhotoImage(
                                    Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                viev_img.config(image=album)
                        else:
                            y = y - 1
                            if y < 0:
                                y = len(normal_list_tracks) + y
                            viev(normal_list_tracks[y])
                            now_song.stop()
                            t = now_song.time_song(normal_list_tracks[y])
                            now_song.play_track(normal_list_tracks[y])
                            start_time = time.time()
                            #now_song.volume(var)
                            
                            im = img(normal_list_tracks[y])
                            if im != []:
                                album = Image.open(im[0])
                                album.thumbnail(size_img, Image.ANTIALIAS)
                                album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                album = ImageTk.PhotoImage(
                                    Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                viev_img.config(image=album)

                    def pause():
                        global all, start_time, t
                        now_song.pause()
                        all = time.time() - start_time
                        t = t - all
                        if now_song.playing_state:
                            pe.config(text='play')
                        else:
                            pe.config(text='pause')

                    def choose(event):
                        if event.keysym == 'Left':
                            down()
                        elif event.keysym == 'Right':
                            up()
                        elif event.keysym == 'space':
                            pause()
                        elif event.keysym == 'Escape':
                            left()
                        elif event.keysym == 'Up':
                            if volume.get() != 1:
                                volume.set(volume.get() + 0.02)
                        elif event.keysym == 'Down':
                            if volume.get() != 0.02:
                                volume.set(volume.get() - 0.02)

                    def check():
                        global start_time, shuff, y, t, all, cycle
                        print(y)
                        if shuff:
                            if now_song.playing_state:
                                start_time = time.time()
                                print(time.time()-start_time, t)
                            else:
                                all = time.time() - start_time
                                print(all, t)
                                if all > t:
                                    if cycle:
                                        y = y
                                        viev(shuff_list_tracks[y])
                                        now_song.stop()
                                        now_song.play_track(shuff_list_tracks[y])

                                        im = img(shuff_list_tracks[y])
                                        if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)

                                        t = now_song.time_song(shuff_list_tracks[y])
                                        start_time = time.time()
                                        #now_song.volume(var)
                                    else:
                                        y = y + 1
                                        if y > len(shuff_list_tracks) - 1:
                                            y = len(shuff_list_tracks) - y
                                        viev(shuff_list_tracks[y])
                                        now_song.stop()
                                        now_song.play_track(shuff_list_tracks[y])

                                        im = img(shuff_list_tracks[y])
                                        if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)

                                        t = now_song.time_song(shuff_list_tracks[y])
                                        start_time = time.time()
                                        #now_song.volume(var)
                        else:
                            if now_song.playing_state:
                                start_time = time.time()
                                print(time.time() - start_time, t)
                            else:
                                all = time.time() - start_time
                                print(all, t)
                                if all > t:
                                    if cycle:
                                        y = y
                                        viev(normal_list_tracks[y])
                                        now_song.stop()
                                        now_song.play_track(normal_list_tracks[y])

                                        im = img(normal_list_tracks[y])
                                        if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)

                                        t = now_song.time_song(normal_list_tracks[y])
                                        start_time = time.time()
                                        #now_song.volume(var)
                                    else:
                                        y = y + 1
                                        if y > len(normal_list_tracks) - 1:
                                            y = len(normal_list_tracks) - y
                                        viev(normal_list_tracks[y])
                                        now_song.stop()
                                        now_song.play_track(normal_list_tracks[y])

                                        im = img(normal_list_tracks[y])
                                        if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)

                                        t = now_song.time_song(normal_list_tracks[y])
                                        start_time = time.time()
                                        #now_song.volume(var)
                        now_song.__init__(_job=root.after(500, check))

                    def c():
                        global cycle
                        if cycle:
                            cycle = False
                            circle.config(text='=>')
                        else:
                            cycle = True
                            circle.config(text='<=>')

                    root.bind('<KeyPress>', choose)
                    STOPPED_PLAYING = pygame.USEREVENT + 1
                    pygame.mixer.music.set_endevent(STOPPED_PLAYING)

                    sh = Button(root, text='Shuffle', width=10, font=('Times', 10), bg='black',
                                fg='#24ad09', command=shf)
                    sh.pack(expand=1, anchor=NE)
                    normal = Button(root, text='In order', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                    command=nrm)
                    normal.pack(expand=1, anchor=NE)
                    
                    def choose_track():
                        global shuff, y
                        root1 = Tk()
                        root1.title('Choose track:')

                        def show(ls):
                            path_list = ls[0].split('\\')[:-1]
                            path = path_list[0]
                            for i in path_list[1:]:
                                path = path + '\\' + i
                            path += '\\'
                            print(path)

                            if len(ls) > 3:

                                def playit1():
                                    global t, start_time, y
                                    y = ls.index(path+p1.cget('text'))
                                    now_song.stop()
                                    now_song.play_track(ls[y])
                                    if now_song.playing_state:
                                        now_song.pause()
                                    t = now_song.time_song(ls[y])
                                    start_time = time.time()
                                    viev(ls[y])
                                    im = img(ls[y])
                                    if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)
                                    print(y)

                                def playit2():
                                    global t, start_time, y
                                    y = ls.index(path+p2.cget('text'))
                                    now_song.stop()
                                    now_song.play_track(ls[y])
                                    if now_song.playing_state:
                                        now_song.pause()
                                    t = now_song.time_song(ls[y])
                                    start_time = time.time()
                                    viev(ls[y])
                                    im = img(ls[y])
                                    if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)
                                    print(y)

                                def playit3():
                                    global t, start_time, y
                                    y = ls.index(path+p3.cget('text'))
                                    now_song.stop()
                                    now_song.play_track(ls[y])
                                    if now_song.playing_state:
                                        now_song.pause()
                                    t = now_song.time_song(ls[y])
                                    start_time = time.time()
                                    viev(ls[y])
                                    im = img(ls[y])
                                    if im != []:
                                            album = Image.open(im[0])
                                            album.thumbnail(size_img, Image.ANTIALIAS)
                                            album.save('D:\\Projects\\Python\\Py music\\Images\\img.png')
                                            album = ImageTk.PhotoImage(
                                                Image.open('D:\\Projects\\Python\\Py music\\Images\\img.png'))
                                            viev_img.config(image=album)
                                    print(y)

                                def down_p():
                                    i = ls.index(path+p3.cget('text')) + 1
                                    if i > len(ls) - 1:
                                        i = len(ls) - i
                                    p1.config(text=ls[i].split('\\')[-1])
                                    i += 1
                                    if i > len(ls) - 1:
                                        i = len(ls) - i
                                    p2.config(text=ls[i].split('\\')[-1])
                                    i = i + 1
                                    if i > len(ls) - 1:
                                        i = len(ls) - i
                                    p3.config(text=ls[i].split('\\')[-1])

                                def up_p():
                                    i = ls.index(path+p1.cget('text')) - 1
                                    if i < 0:
                                        i = len(ls) + i
                                    p1.config(text=ls[i].split('\\')[-1])

                                    i = i - 1
                                    if i < 0:
                                        i = len(ls) + i
                                    p2.config(text=ls[i].split('\\')[-1])

                                    i = i - 1
                                    if i < 0:
                                        i = len(ls) + i
                                    p3.config(text=ls[i].split('\\')[-1])

                                up_p = Button(root1, text='up', width=5, font=('Times', 12), bg='#24ad09', fg='black',
                                              command=up_p)
                                up_p.pack(expand=1, side=TOP)
                                p1 = Button(root1, text=ls[0].split('\\')[-1], width=50, font=('Times', 12), bg='#24ad09', fg='black',
                                            command=playit1)
                                p1.pack(expand=1)
                                p2 = Button(root1, text=ls[1].split('\\')[-1], width=50, font=('Times', 12), bg='#24ad09', fg='black',
                                            command=playit2)
                                p2.pack(expand=1)
                                p3 = Button(root1, text=ls[2].split('\\')[-1], width=50, font=('Times', 12), bg='#24ad09', fg='black',
                                            command=playit3)
                                p3.pack(expand=1)
                                down_p = Button(root1, text='down', width=5, font=('Times', 12), bg='#24ad09',
                                                fg='black',
                                                command=down_p)
                                down_p.pack(expand=1, side=BOTTOM)
                            else:
                                def playit(nnn):
                                    global t, start_time
                                    list = root.pack_slaves()
                                    for l in list:
                                        l.destroy()
                                    y = ls.index(path + nnn)
                                    now_song.stop()
                                    now_song.play_track(ls[y])
                                    if now_song.playing_state:
                                        now_song.pause()
                                    t = now_song.time_song(ls[y])
                                    start_time = time.time()
                                    viev(ls[y])

                                for i in range(len(ls)):
                                    p = Button(root, text=ls[i].split('\\')[-1], width=10, font=('Times', 12), bg='#24ad09',
                                               fg='black',
                                               command=lambda i=i: playit(ls[i]))
                                    p.pack(expand=1, side=BOTTOM)
                            
                        if shuff:
                            show(shuff_list_tracks)
                        else:
                            show(normal_list_tracks)
                        root1.mainloop()
                        
                    choose_track = Button(root, text='Choose track', width=10, font=('Times', 10), bg='black',
                                          fg='#24ad09',
                                    command=choose_track)
                    choose_track.pack(expand=1, anchor=NE)
                    m1.pack(expand=1, anchor=S)
                    m.pack(expand=1, anchor=S)
                    pe = Button(m1, text='pause', width=5, font=('Times', 12), bg='#20fc03',
                                fg='black', command=pause)
                    pe.pack(expand=1, side=LEFT, padx=10)

                    circle = Button(m1, text='=>', width=3, font=('Times', 10), bg='black', fg='#20fc03',
                                    command=c)
                    circle.pack(expand=1, side=LEFT, padx=10)

                    v_text = Label(m1, text='volume:', width=5, font=('Times', 12), bg='black', fg='#20fc03')
                    v_text.pack(expand=1, side=LEFT, padx=10)
                    volume.pack(expand=1, side=RIGHT)
                    down1 = Button(m, text='<', width=2, font=('Times', 12), bg='black', fg='#24ad09', command=down)
                    down1.pack(expand=1, side=LEFT)
                    song.pack(expand=1, side=LEFT, padx=5)
                    up1 = Button(m, text='>', width=2, font=('Times', 12), bg='black', fg='#24ad09', command=up)
                    up1.pack(expand=1, side=LEFT)
                    mixer.music.set_endevent(pygame.USEREVENT)
                    check()

            def left():
                global p
                p = 0
                list = root.pack_slaves()
                for l in list:
                    l.destroy()
                start()
            back = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09', command=left)
            back.pack(expand=1, anchor=NW)
            for i in range(len(list_playlists)):
                p = Button(root, text=list_playlists[i], width=10, font=('Times', 12), bg='#24ad09', fg='black',
                           command=lambda i=i: play(list_playlists[i]))
                p.pack(expand=1, side=BOTTOM)
        else:
            no_playlist = Label(root, text='Please add playlists.', width=20, font=('Times', 12), bg='#24ad09',
                                fg='black')
            no_playlist.pack(expand=1, side=BOTTOM)

            def q():
                no_playlist.destroy()
                rtn.destroy()
                start()
            rtn = Button(root, text='Back', width=10, font=('Times', 12), bg='black', fg='#24ad09', command=q)
            rtn.pack(expand=1, side=BOTTOM)

    def del_playlist():
        playlist.destroy()
        playlist_.destroy()
        #backup.destroy()
        listen.destroy()
        name_main.destroy()
        main.destroy()
        #q1.destroy()

        def left():
            if del1.get() == '':
                back1.destroy()
                del_text1.destroy()
                del1.destroy()
                root.unbind('<Return>')
                start()

        back1 = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09', command=left)
        del_text1 = Label(root, text='Enter playlist name and press enter: ', width=30, font=('Times', 12),
                             bg='#24ad09', fg='black')
        del1 = Entry(root, width=20, font=('Times', 12), bg='#24ad09', fg='black', takefocus=True)
        back1.pack(expand=1, anchor=NW)
        del_text1.pack(expand=1)
        del1.pack(expand=1)
        del1.focus_set()

        def del_music(event):
            if del1.get() == '':
                pass
            else:
                files = "D:\Music"
                files = os.listdir(files)
                if del1.get() in files:
                    path = f"D:\Music\{del1.get()}"
                    back1.destroy()
                    del_text1.destroy()
                    del1.destroy()

                    def d_p():
                        del_p.destroy()
                        del_m.destroy()
                        shutil.rmtree(path)
                        time.sleep(1)
                        start()

                    def d_m():
                        del_p.destroy()
                        del_m.destroy()

                        def left_2():
                            global del_finish
                            if del_finish:
                                back_2.destroy()
                                del_text.destroy()
                                delete.destroy()
                                root.unbind('<Return>')
                                start()

                        back_2 = Button(root, text='Back', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                        command=left_2)
                        back_2.pack(expand=1, anchor=NW)
                        del_text = Label(root, text='Select music from playlist: ', width=20, font=('Times', 12),
                                         bg='#24ad09', fg='black')
                        del_text.pack(expand=1)

                        def d():
                            global del_finish
                            music_files = list(filedialog.askopenfilenames())
                            f = [f"{path}\{j[-1]}".replace('\\', '/') for j in [i.split('/') for i in music_files]]
                            print(music_files)
                            last_music_clone = os.listdir(path)

                            def last_4chars(x):
                                return (x[:4])

                            last_music_clone = sorted(last_music_clone, key=last_4chars)
                            music_files = sorted(music_files, key=last_4chars)

                            if music_files != []:
                                change = False
                                for o in music_files:
                                    for j in f:
                                        if o == j:
                                            change = True
                                if change:
                                    if len(music_files) != 1:
                                        print(music_files)
                                        num_rate1 = str(music_files[0].split('/')[-1][:4])
                                        try:
                                            num_rate1 = int(num_rate1)
                                        except:
                                            try:
                                                num_rate1 = int(num_rate1[1:])
                                            except:
                                                try:
                                                    num_rate1 = int(num_rate1[2:])
                                                except:
                                                    num_rate1 = int(num_rate1[3])
                                        num_rate = str(music_files[len(music_files) - 1].split('/')[-1][:4])
                                        try:
                                            num_rate = int(num_rate)
                                        except:
                                            try:
                                                num_rate = int(num_rate[1:])
                                            except:
                                                try:
                                                    num_rate = int(num_rate[2:])
                                                except:
                                                    num_rate = int(num_rate[3])
                                        print(num_rate1, num_rate)
                                        if num_rate == len(last_music_clone):
                                            print(2)
                                            pass
                                        else:
                                            last_music = os.listdir(path)
                                            last_music = sorted(last_music, key=last_4chars)
                                            last_music = last_music[num_rate:]
                                            new_music = []
                                            print(last_music)
                                            for i in range(len(last_music)):
                                                old_num = last_music[i][:4]
                                                try:
                                                    old_num = int(old_num)
                                                except:
                                                    try:
                                                        old_num = int(old_num[1:])
                                                    except:
                                                        try:
                                                            old_num = int(old_num[2:])
                                                        except:
                                                            old_num = int(old_num[3])
                                                nn = old_num - len(music_files)
                                                if 0 <= nn <= 9:
                                                    mmm = last_music[i] + '000' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    new_music.append(mmm)
                                                elif 10 <= nn <= 99:
                                                    mmm = last_music[i] + '00' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    new_music.append(mmm)
                                                elif 100 <= nn <= 999:
                                                    mmm = last_music[i] + '0' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    new_music.append(mmm)
                                                elif 1000 <= nn <= 9999:
                                                    mmm = last_music[i] + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    new_music.append(mmm)
                                            new_music = [f"{path}\{i}".replace('\\', '/') for i in new_music]
                                            last_music = [f"{path}\{i}".replace('\\', '/') for i in last_music]
                                            for i in zip(last_music, new_music):
                                                print(i[0], i[1])
                                                os.rename(i[0], i[1])
                                    else:
                                        num_rate = str(music_files[0].split('/')[-1][:4])
                                        try:
                                            num_rate = int(num_rate)
                                        except:
                                            try:
                                                num_rate = int(num_rate[1:])
                                            except:
                                                try:
                                                    num_rate = int(num_rate[2:])
                                                except:
                                                    num_rate = int(num_rate[3])
                                        print(num_rate)
                                        if num_rate == 1:
                                            last_music = os.listdir(path)
                                            last_music = sorted(last_music, key=last_4chars)
                                            last_music = last_music[num_rate:]
                                            print(last_music)
                                            new_music = []

                                            for i in range(len(last_music)):
                                                old_num = last_music[i][:4]
                                                try:
                                                    old_num = int(old_num)
                                                except:
                                                    try:
                                                        old_num = int(old_num[1:])
                                                    except:
                                                        try:
                                                            old_num = int(old_num[2:])
                                                        except:
                                                            old_num = int(old_num[3])
                                                nn = old_num - num_rate
                                                print(nn)
                                                if 0 <= nn <= 9:
                                                    mmm = last_music[i] + '000' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1]+'.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 10 <= nn <= 99:
                                                    mmm = last_music[i] + '00' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1]+'.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 100 <= nn <= 999:
                                                    mmm = last_music[i] + '0' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1]+'.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 1000 <= nn <= 9999:
                                                    mmm = last_music[i] + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1]+'.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                            new_music = [f"{path}\{i}".replace('\\', '/') for i in new_music]
                                            last_music = [f"{path}\{i}".replace('\\', '/') for i in last_music]
                                            for i in zip(last_music, new_music):
                                                os.rename(i[0], i[1])
                                        elif num_rate != 1 and num_rate != len(last_music_clone):
                                            last_music = os.listdir(path)
                                            last_music = sorted(last_music, key=last_4chars)
                                            last_music = last_music[num_rate:]
                                            new_music = []
                                            print(last_music)
                                            for i in range(len(last_music)):
                                                old_num = last_music[i][:4]
                                                try:
                                                    old_num = int(old_num)
                                                except:
                                                    try:
                                                        old_num = int(old_num[1:])
                                                    except:
                                                        try:
                                                            old_num = int(old_num[2:])
                                                        except:
                                                            old_num = int(old_num[3])
                                                nn = old_num - 1
                                                print(nn)
                                                if 0 <= nn <= 9:
                                                    mmm = last_music[i] + '000' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 10 <= nn <= 99:
                                                    mmm = last_music[i] + '00' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 100 <= nn <= 999:
                                                    mmm = last_music[i] + '0' + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                                elif 1000 <= nn <= 9999:
                                                    mmm = last_music[i] + str(nn) + last_music[i][4:]
                                                    mmm = mmm.split('.mp3')[1] + '.mp3'
                                                    print(mmm)
                                                    new_music.append(mmm)
                                            new_music = [f"{path}\{i}".replace('\\', '/') for i in new_music]
                                            last_music = [f"{path}\{i}".replace('\\', '/') for i in last_music]
                                            for i in zip(last_music, new_music):
                                                os.rename(i[0], i[1])
                                        else:
                                            pass
                                    for o in music_files:
                                        for j in f:
                                            if o == j:
                                                os.remove(o)
                            del_finish = True

                        delete = Button(root, text='Delete', width=10, font=('Times', 10), bg='black', fg='#24ad09',
                                        command=d)
                        delete.pack(expand=1)

                    del_p = Button(root, text='Delete playlist', width=30, font=('Times', 12), bg='#24ad09', fg='black',
                                   command=d_p)
                    del_p.pack(expand=1)
                    del_m = Button(root, text='Delete music in playlist', width=30, font=('Times', 12), bg='#24ad09',
                                   fg='black', command=d_m)
                    del_m.pack(expand=1)
                else:
                    del_text1.config(text="Enter a real playlist's name: ")

        root.bind('<Return>', del_music)

    def back_up():
        #backup.config(text='Load back up')
        if 'relax' in os.listdir("D:/Music"):
            if os.listdir("D:/Music/relax") != []:
                for i in os.listdir("D:/Music/relax"):
                    os.remove("D:/Music/relax/" + str(i))
            os.rmdir("D:/Music/relax")

        os.mkdir("D:/Music/relax")
        path_from = "D:/Telegram download/"
        path_to = "D:/Music/relax/"
        file_list = os.listdir(path_from)
        dict_find = {i: i for i in range(74)}
        #l = []
        #with open('D:\Projects\Python\hide.txt', 'r') as f:
        #    text = f.read()
        #l = text.split('\n')
        for i in range(len(dict_music)):
            if dict_music[i] in file_list:
                dict_find[i] = dict_music[i]
        for i in list(dict_find.values()):
            print(i)
        l = [path_from + i for i in dict_find.values()]
        l_old = [path_to + i for i in dict_find.values()]
        num = 1
        print(len(l))
        for i in l:
            print(i)
        print(' ')

        for i in l_old:
            print(i)
        print(' ')

        def filter(lst, num):
            news = [i.split('/')[-1] for i in lst]
            for i in news:
                print(i)
            print(' ')

            news = [i.split('.mp3')[0] for i in news]
            for i in news:
                print(i)
            print(' ')
            for i in range(len(news)):
                news[i] = re.sub(r'[^A-zА-яА-я- ]', '', news[i])
            for i in news:
                print(i)
            print(' ')
            for i in range(len(news)):
                if news[i].endswith('.mp3'):
                    pass
                else:
                    news[i] += '.mp3'
            for i in news:
                print(i)
            print(' ')
            for i in range(len(news)):
                if num >= 10:
                    news[i] = '00' + str(num) + news[i]
                else:
                    news[i] = '000' + str(num) + news[i]
                num += 1
            for i in news:
                print(i)
            print(' ')
            news = [path_to + str(i) for i in news]
            for i in news:
                print(i)
            print(' ')
            return news

        l_new = filter(l_old, num)

        for i in l:
            shutil.copy(i, path_to)
        for i in zip(l_old, l_new):
            os.rename(i[0], i[1])

        #backup.config(text='Done')

    name_main = Label(root, text='Py music', width=20, height=2, font=('Helvetica', 20), bg='#24ad09', fg='black',
                      relief=SUNKEN)
    name_main.pack(expand=1, anchor=CENTER, fill=X, padx=20, pady=10)
    main = Frame(root)
    main.pack(expand=1, anchor=N)
    playlist = Button(main, text='+ Music', width=10, font=('Times', 12), command=append_playlist, bg='#24ad09',
                      fg='black')
    playlist.pack(expand=1, side=LEFT, anchor=W, padx=20, pady=10)
    playlist_ = Button(main, text='- Music', width=10, font=('Times', 12), command=del_playlist, bg='#24ad09',
                       fg='black')
    playlist_.pack(expand=1, side=RIGHT, anchor=E, padx=20, pady=10)
    #q1 = Button(main, text='Quit', width=10, font=('Times', 12), command=q, bg='#24ad09', fg='black')
    #backup = Button(main, text='Load back up', width=40, font=('Times', 12), command=back_up, bg='#24ad09',
    #                fg='black')
    listen = Button(main, text='Listen', width=10, font=('Times', 15), bg='#24ad09', fg='black',
                    command=listen_playlist)
    listen.pack(expand=1, side=TOP, anchor=S, padx=20, pady=10)
    #q1.pack(expand=1, side=BOTTOM, padx=20, pady=10)
    #backup.pack(expand=1, anchor=W, side=BOTTOM, padx=5, pady=5)

    def esc(event):
        if event.keysym == 'Escape':
            exit()

    root.bind('<KeyPress>', esc)


if __name__ == '__main__':
    start()
    root.mainloop()
