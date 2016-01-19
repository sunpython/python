#!/usr/bin/env python3
tree_menu = {
    "数码": {
        "电脑": {
            "笔记本": ['联想', '索尼'],
            "台式机": ['惠普', '清华同方']
        },
        "手机": {
            "苹果": ['iphone6s', 'iphone6s plus', 'iphone5s'],
            "小米": ['米4', '小米note']
        },
        "娱乐": {
            "音响": ['电脑音响', '笔记本音箱', 'wifi音箱'],
            "耳麦": ['无线', '有线']
        },
            },
    '图书': {
        '计算机': {
            '程序': ['iphone', 'python'],
            '前端': ['html', 'css']
        },
        '教育': {
            '初中': ['中考', '体育', '英语'],
            '高中': ['高考', '文科']
        },
    },
}

for index, key in enumerate(tree_menu.keys()):
    print(index, key)
menu1 = input("欢迎来到阳光小超市，选择对应编号进入分类,按q退出").strip()
if menu1.isdigit():
    menu1 = int(menu1)
    key_1 = list(tree_menu.keys())[menu1]
    for index, key in enumerate(tree_menu[key_1]):
        print(index, key)
    menu2 = input("选择对应编号进入分类,按q退出").strip()
    if menu2.isdigit():
        menu2 = int(menu2)
        key_2 = list(tree_menu[key_1].keys())[menu2]
        for index, key in enumerate(tree_menu[key_1][key_2]):
            print(index, key)
        menu3 = input("选择对应编号进入分类,按q退出").strip()
        if menu3.isdigit():
            menu3 = int(menu3)
            key_3 = list(tree_menu[key_1][key_2].keys())[menu3]
            for index, key in enumerate(tree_menu[key_1][key_2][key_3]):
                print(index, key)
            menu4 = input("这是最后一层了，按q退出").strip()








