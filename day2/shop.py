#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
author:顾伟栋
qq:77625811
"""


def shop_data():
    """
    定义商品数据字典，mysql版本中，这里改成从mysql获取数据
    :return: 返回数据
    """
    dic = {
        "苹果": [5000, "手机"],
        "小米": [3030, "手机"],
        "联想": [300, "手机"],
        "索尼": [200, "手机"],
        "华为": [4000, "手机"],
        "索爱": [800, "手机"],
        "诺基亚": [2000, "手机"]
    }
    return dic


def get_budget():
    """
    获取预算
    :return:
    """
    while True:
        my_money = input("请输入您的预算:")
        if my_money.isdigit():
            my_money = int(my_money)
            break
        else:
            print("请输入正确的数字")

    return my_money


def pd_list(dic):
    print("本店商品推荐".center(50, "#"))
    for index, k in enumerate(dic.items(), 1):
        print("%s\t\t%s\t\t%s".center(40) % (index, k[0], k[1][0]))


def get_cheap_pd(dic):
    cheap_price = []
    for v in dic.values():
        cheap_price.append(v[0])
    return min(cheap_price)


def is_min_pay(my_money,dic):
    min_money = get_cheap_pd(dic)
    if my_money > min_money:
        return True
    else:
        return False


def get_pd_info(dic):
    pd_select = []
    pid = int(input("请输入产品编号:"))
    pd_name = list(dic.keys())[pid-1]
    pd_price = dic[pd_name][0]
    pd_select.append(pd_name)
    pd_select.append(pd_price)
    return pd_select


def can_buy(pd_price, my_money):
    if my_money >= pd_price:
        return True
    else:
        return False


def is_keep_buy():
    keep_on = input("是否继续购买:Y/N?")
    keep_on = keep_on.upper()
    if keep_on == "N":
        return False
    else:
        return True


def add_cart(cart, pdinfo):
    cart.append(pd_info)


def cart_list(cart):
    print("您购买的商品如下:".center(50, "#"))
    if len(cart) > 0:
        pay_money = 0
        for k in cart:
            pay_money += k[1]
            print(k[0], k[1])
        print("您一共消费了:%s元！".center(50, "-") % pay_money)
    else:
        print("您没有购买任何产品")


def pay_money():
    print("结算中心".center(50, "#"))
    print("1：结算")
    print("2：继续购买")
    op_str = input("请选择您的操作:")
    if op_str == "1":
        return True
    else:
        return False


def op_result():
    if pay_money():
        print("结算成功，欢迎下次光临")
        exit()


if __name__ == "__main__":
    # 获取预算
    budget = get_budget()
    buy_cart = []
    dic = shop_data()
    while True:
        # 显示产品列表
        pd_list(dic)
        # 判断能否购买最便宜的产品
        if is_min_pay(budget,dic):
            # 获取用户输入的产品名称和价格
            pd_info = get_pd_info(dic)
            pd_name = pd_info[0]
            pd_price = pd_info[1]
            if can_buy(pd_price, budget):
                budget -= pd_price
                # 把产品和价格放到元组，添加到购物车
                add_cart(buy_cart, (pd_name, pd_price))
                print("您还有%s元" % budget)
                if not is_keep_buy():
                    # 打印购物车
                    cart_list(buy_cart)
                    # 结算
                    op_result()
            else:
                print("您的预算不能购买此产品")
                cart_list(buy_cart)
                # 打印购物车
                cart_list(buy_cart)
                # 结算
                op_result()

        else:
            print("你的预算余额已经不够购买最便宜的商品了，以下是您的购物清单")
            # 打印购物车
            cart_list(buy_cart)
            # 结算
            op_result()



