#!/usr/bin/env python3
# 定义跳出循环的开关
break_power = False
# 定义用户名输对标志避免第二次输用户名
user_power = False
err_num = 0
while err_num < 3:
    # 没有输过用户名或用户名前一次未输对的，才提示输入用户名
    if user_power is False:
        user_name = input("请输入用户名:")
        break_power = False
    # 判断是否存在该用户
    user_list = open("user.txt", "r")
    s_count = 0
    for is_user in user_list.readlines():
        db_user, db_pwd = is_user.strip().split('|')
        if user_name == db_user:
            s_count += 1
    user_list.close()
    if s_count < 1:
        print("用户名不存在，请重输:")
        continue
    else:
        user_power = True
    lock_users = open("error.log", "r")
    for err_user in lock_users:
        if user_name == err_user.strip():
            print("该用户已经被锁定了")
            user_power = False
            break_power = True
            break
    if break_power is True:
        continue
    # 关闭文件
    lock_users.close()
    user_list = open("user.txt", "r")
    is_login = False
    user_pwd = input("请输入密码：")
    for u in user_list.readlines():
        db_user, db_pwd = u.strip().split('|')
        if user_name == db_user and user_pwd == db_pwd:
            is_login = True
            break
    user_list.close()
    if is_login is False:
        print("密码错误")
        err_num += 1
    else:
        print("欢迎您进入菜单系统!")
        break
else:
    lock_add = open("error.log", "a")
    lock_add.write(user_name+"\n")
    print("该用户错误已达三次")





