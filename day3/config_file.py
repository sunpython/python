#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import json
import os


def get_content(title):
    """
    根据内容找出匹配行
    :param title: www.oldboy.org
    :return: 列表
    """
    content = ""
    with open("config") as f:
        content = f.read()
    # 找不到的处理
    try:
        # 确定正则范围backend www.oldboy.org 下的节点
        find_area = re.search(r"backend %s\n(.*?)backend" % title, content, re.S).group(1)
        # 按行放进列表，方便后期append
        find_list = find_area.split("\n")
        # 删除空行
        while "" in find_list:
            find_list.remove("")
    except:
        find_list = []

    return find_list


def cf_get(a):
    """
    获取内容并格式化成字符串
    :param a: list
    :return:
    """
    get_str = get_content(a)
    if get_str:
        return "\n".join(get_str)
    else:
        return "您的内容没有找到"


def cf_add(a):
    """
    添加操作
    :param a:
    :return:
    """
    try:
        # 传入的值格式化成字典
        data_arr = json.loads(a)
        # 获取标题
        data_title = "backend %s\n" % data_arr["backend"]
        # 获取记录内容
        data_detail = "        server %s weight %d maxconn %d" % (data_arr["record"]["server"], data_arr["record"]["weight"], data_arr["record"]["maxconn"])
        # 取得文件中间部份
        data_body = get_content(data_arr["backend"])
        if data_detail not in data_body:
            # 追加内容到中间内容
            data_body.append(data_detail)
            # 格式化成字符串
            data_bodys = "\n".join(data_body)
             # 取得文件首尾
            config_body = get_file(data_arr["backend"])
            # 合成文件
            create_file(config_body[0], data_title+data_bodys+"\n", config_body[1])
            if os.path.exists("configbak"):
                os.remove("configbak")
            os.rename("config", "configbak")
            os.rename("newconfig", "config")
            return "生成成功"
        else:
             return "该内容已经存在"
    except:
        return "生成失败，请检查"


def cf_del(a):
    try:
        # 传入的值格式化成字典
        data_arr = json.loads(a)
        # 获取标题
        data_title = "backend %s\n" % data_arr["backend"]
        # 获取内容
        data_body = get_content(data_arr["backend"])
        data_detail = "        server %s weight %d maxconn %d" % (data_arr["record"]["server"], data_arr["record"]["weight"], data_arr["record"]["maxconn"])
        # 如果文件的内容存在才操作
        if data_body and data_detail in data_body:
            # 从列表删除该内容
            data_body.remove(data_detail)
            # 格式化字符串
            data_bodys = "\n".join(data_body)
            # 取得文件首尾
            config_body = get_file(data_arr["backend"])
            # 合成文件
            create_file(config_body[0], data_title+data_bodys+"\n", config_body[1])
            # 如果configbak存在，那下一步重命名会出错，所以判断一下，存在就删除
            if os.path.exists("configbak"):
                os.remove("configbak")
            # 把原文件重命名成configbak
            os.rename("config", "configbak")
            # 把合成的文件重命成config
            os.rename("newconfig", "config")
            return "删除成功"
        else:
            return "内容不存在"
    except:
        return "删除失败"


def to_quit():
    """
    退出
    :return:
    """
    exit()


def get_file(title):
    """
    获取文件首尾
    :param title:
    :return:
    """
    group_list = []
    with open("config") as f:
        content = f.read()
    find_area = re.search(r"^(.*?)backend %s\n(.*?)backend(.*?)$" % title, content, re.S)
    group_list.append(find_area.group(1))
    group_list.append("backend" + find_area.group(3))
    return group_list


def create_file(top, body, foot):
    """
    合并文件
    :param top: 文件上部
    :param body: 中部
    :param foot: 下部
    :return:
    """
    with open("newconfig", "w") as write_obj:
        write_obj.write(top)
        write_obj.write(body)
        write_obj.write(foot)


if __name__ == "__main__":
    # 定义函数字典 代替 swich case
    os_select = {"1": cf_get, "2": cf_add, "3": cf_del, "4": to_quit}
    while True:
        print("1,显示".center(20, "#"))
        print("2,添加".center(20, "#"))
        print("3,删除".center(20, "#"))
        print("4,退出".center(20, "#"))
        user_select = input("请选择您的操作:".center(30, "*"))
        # 判断定义的函数字典中是否有用户输入的对应的键
        if user_select in os_select.keys():
            if user_select == "4":
                to_quit()
            # 添加|删除{"backend":"www.oldboy.org","record":{"server":"100.1.7.9","weight":20,"maxconn":30}}
            # 获取 www.oldboy.org
            data_input = input("请输入指定的内容（单引号用双引号代替）:")
            # 根据用户选择定向到相应函数（1，获取2,添加3,删除）
            print(os_select.get(user_select)(data_input))
        else:
            print("您的操作有误！")
