# -*- coding: utf-8 -*-
import datetime


def word_parse(data):
    if parse_calculator(data):
        return parse_calculator(data)
    # parse_song support fuzzy search
    if parse_song(data):
        return parse_song(data)
    if parse_weather(data):
        return parse_weather(data)


def parse_song(data):
    # play music or download music

    # key word that storage
    key_play = ["放一首", "来一首", "放"]
    key_dl = ["下一首", "下载"]

    for item in key_play:
        if item in data:
            index = data.find(item) + len(item)
            songname = data[index:]

            return ("qqmusic", (songname,))
    for item in key_dl:
        if item in data:
            index = data.find(item) + len(item)
            songname = data[index:]
            return ("qqmusicdl", (songname,))
    return ()


def parse_weather(data):
    key = ["天气"]

    flag = False
    l = []

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    after_tomorrow = today + datetime.timedelta(days=2)
    # parse_weather(today)

    days = {"今": today.strftime("%Y-%m-%d"), "明": tomorrow.strftime("%Y-%m-%d"),
            "后": after_tomorrow.strftime("%Y-%m-%d")}
    for item in key:
        if item in data:
            flag = True
            break
    if flag:
        for day in days.keys():
            if day in data:
                l.append(days[day])

    # l example: ('2019-03-16', '2019-03-18')
    if not l:
        return ()
    else:
        return ("weather", tuple(l))


def parse_calculator(data):
    key = ["+", "-", "*", "/", "加", "减", "乘", "除"]
    flag = False
    for item in key:
        if item in data:
            flag = True
            break
    if not flag:
        return ()

    data = data.replace("加", "+").replace("减", "-").replace("乘", "*").replace("除", "/")
    data = data.replace("一", "1").replace("二", "2").replace("三", "3").replace("四", "4").replace("五", "5")
    data = data.replace("六", "6").replace("七", "7").replace("八", "8").replace("九", "9").replace("零", "0")
    return ("calculator",(data,))
