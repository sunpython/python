#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tool

"""
author:顾伟栋
qq:77625811
blog:http://www.cnblogs.com/sunface/
"""


def shop_data():
    """
    从mysql获取数据
    :return: 返回数据
    """
    pd_data = tool.GetUser().get_pdlist()
    return pd_data


def get_budget(username):
    """
    从数据中取得用户可用金额
    :param username: 用户名
    :return:
    """
    return tool.GetUser().get_user_money(username)


def pd_list(dic):
    """
    打用商品列表
    :param dic: 数据中返回的是列表，每天记录是一个元组
    :return:
    """
    print("本店商品推荐".center(50, "#"))
    for pd in dic:
        print("%s\t\t%s\t\t%s" % (pd[0], pd[1], str(pd[2])))


def get_cheap_pd(dic):
    """
    获取便宜的商品价格
    :param dic: 数据源
    :return:
    """
    cheap_price = []
    for v in dic:
        cheap_price.append(v[2])
    return min(cheap_price)


def is_min_pay(my_money, dic):
    """
    判断是否可以买最便宜的商品
    :param my_money: 余下的预算
    :param dic: 数据源
    :return:
    """
    min_money = get_cheap_pd(dic)
    if my_money > min_money:
        return True
    else:
        return False


def get_pd_info():
    """
    从数据库中获取用户选择的商品信息
    :return:
    """
    pid = int(input("请输入产品编号:"))
    pd_info = tool.GetUser().get_byid(pid)
    return pd_info


def can_buy(pd_price, my_money):
    """
    判断用户是否够钱买该商品
    :param pd_price: 产品价格
    :param my_money: 我的余额
    :return:
    """
    if my_money >= pd_price:
        return True
    else:
        return False


def is_keep_buy():
    """
    是否继续购买，把输入的值转成大写后返回
    :return:
    """
    keep_on = input("是否继续购买:Y/N?")
    keep_on = keep_on.upper()
    if keep_on == "N":
        return False
    else:
        return True


def add_cart(username, pdinfo):
    """
    加入购物车
    :param username: 用户名
    :param pdinfo: 产品信息
    :return:
    """
    tool.GetUser().add_cart(username, pdinfo)


def cart_list(username):
    """
    打印购物车
    :param username: 用户名
    :return:
    """
    print("您购买的商品如下:".center(50, "#"))
    cart = tool.GetUser().get_cart_list(username)
    pay_money = 0
    if len(cart) > 0:
        for k in cart:
            pay_money += k[1]*k[3]
            print(pay_money)
            print("名称：%s\t价格：%s\t数量：%s" % (k[0],k[1],k[3]))
        print("您一共消费了:%s元！".center(50, "-") % pay_money)
    else:
        print("您没有购买任何产品")
    return pay_money


def pay_money():
    """
    结算中心，显示几个菜单
    :return:
    """
    print("结算中心".center(50, "#"))
    print("1：结算")
    print("2：继续购买")
    op_str = input("请选择您的操作:")
    if op_str == "1":
        return True
    else:
        return False


def op_result(money, username):
    """
    结算：1，清空购物车 2,根据消费，从数据库用户表中扣除消费
    :param money:
    :param username:
    :return:
    """
    if pay_money():
        tool.GetUser().clear_cart(money, username)
        # 真正从数据库中扣除金额 并清空购物车
        print("结算成功，欢迎下次光临")
        print("已经从你的账户中扣除金额，现在您的账户中还有:" + str(tool.GetUser().get_user_money(username)))
        exit()


def user_login():
    """
    用户登陆操作
    :return:
    """
    err_limit = 0
    err_flag = True
    while True:
        user_name = input("请输入用户名:")
        # 判断是否注册
        if tool.GetUser().is_user(user_name):
            while err_flag:
                user_pwd = input("请输入密码:")
                # 判断是否正确
                if tool.GetUser().login(user_name, user_pwd):
                    print("登陆成功".center(50, "_"))
                    print("成功")
                    return "%s|%s" % (True, user_name)
                else:
                    err_limit += 1
                    if err_limit >= 3:
                        print("错误达三次")
                        break
                    print("密码错误")
        else:
            print("用户名不存在".center(50, "#"))


if __name__ == "__main__":
    # 用户信息
    login_info, username = user_login().split("|")
    # 判断是否正确登陆
    if login_info:
        # 从数据中获取用户余额，并以此做为预算
        budget = get_budget(username)
        # 获取商品数据
        dic = shop_data()
        while True:
            # 显示产品列表
            pd_list(dic)
            # 判断能否购买最便宜的产品
            if is_min_pay(budget, dic):
                # 获取用户输入的产品的价格和相关信息
                pd_info = get_pd_info()
                pd_price = float(pd_info[0][2])
                # 产品id
                pid = int(pd_info[0][0])
                # 判断是否能购买此产品
                if can_buy(pd_price, budget):
                    # 扣除金额（并非从实际账户中扣，把是把余额当成一种预算，待结算时才从数据库中扣除）
                    budget = (float(budget)) - pd_price
                    # 把用户和所买产品关联在一此加到购物车
                    add_cart(username, pd_info)
                    print("您还有%s元" % budget)
                    # 判断是否继续购买
                    if not is_keep_buy():
                        # 打印购物车
                        pay_my = cart_list(username)
                        # 结算
                        op_result(pay_my, username)
                else:
                    print("您的预算不能购买此产品")
                    cart_list(username)
                    # 打印购物车
                    cart_list(username)
                    # 结算
                    op_result(username)

            else:
                print("你的预算余额已经不够购买最便宜的商品了，以下是您的购物清单")
                # 打印购物车
                cart_list(username)
                # 结算
                op_result(username)



