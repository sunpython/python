#!/usr/bin/env python3
tree_menu = {
    "数码": {
            "笔记本": ['联想', '索尼'],
            "台式机": ['惠普', '清华同方']
    },
    '图书': {

            '程序': ['iphone', 'python'],
            '前端': ['html', 'css']
    },
     '教育': {
            '初中': ['中考', '体育', '英语'],
            '高中': ['高考', '文科']
    }
}
# 定义跳出标志
tab_power=False
# 为真的时候循环
while not tab_power:
    # 索引计数器遍历出一级菜单
    for index, key in enumerate(tree_menu.keys()):
        # 以1,2,3的方式排列
        print(index+1, key)
    menu1 = input("欢迎来到阳光小超市，选择对应编号进入分类,按q退出:").strip()
    # 如果是数字 就转为int并判断分类是否存在，不存在，就显示继续执行
    if menu1.isdigit():
        menu1 = int(menu1)
        if(menu1 > len(tree_menu.keys())):
            print("无此分类")
            continue
        key_1 = list(tree_menu.keys())[menu1-1]
        while not tab_power:
            # 索引计数器遍历出二级菜单
            for index, key in enumerate(tree_menu[key_1]):
                print(index+1, key)
            menu2 = input("选择对应编号进入分类,按q退出,按b返回上一层").strip()
            if menu2.isdigit():
                menu2 = int(menu2)
                if(menu2 > len(list(tree_menu[key_1].keys()))):
                    print("无此分类")
                    continue
                key_2 = list(tree_menu[key_1].keys())[menu2-1]
                while not tab_power:
                    # 索引计数器遍历出三级菜单
                    for index, key in enumerate(tree_menu[key_1][key_2]):
                        print(index+1, key)
                    menu3 = input("选择对应编号进入分类,按q退出，按b返回上一层").strip()
                    if menu3.isdigit():
                       input("这是最后一层了，按q退出").strip()
                     # 以下都是每一级b返回 按q 退出的功能
                    elif menu3 == "q":
                        tab_power = True
                    elif menu3 == "b":
                        break
            elif menu2 == "q":
                tab_power = True
            elif menu2 == "b":
                break
    elif menu1 == "q":
        tab_power = True
else:
    print("退出成功")








