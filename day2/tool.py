#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import mysql.connector


class GetUser(object):
    """
    定义数据库配置
    """
    config = {
            'user': 'python',
            'password': '123456',
            'host': '115.238.96.146',
            'port': 3306,
            'database': 'py_db'
         }

    def __init__(self):
        self.config = self.config

    def db_conn(self):
        """
        连接数据库
        :return:
        """
        _conn = mysql.connector.connect(**self.config)
        return _conn

    def reg(self, _username, _userpwd):
        """
        注册用户
        :param username: 用户名
        :param userpwd: 密码
        :return:成功返true，失败返回false
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "insert into py_user(username,passwd,groupid)VALUES ('%s','%s',%s)" % (_username, _userpwd, '1')
        if not self.is_exist(_username):
            cursor.execute(sql)
            if cursor.rowcount > 0:
                t = 1
            else:
                t = -1
            conn.commit()
        else:
            t = -2
        cursor.close()
        conn.close()
        return t

    def get_cart_list(self, _username):
        """
        根据用户打印购物车
        :param _username:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select title,price,pid,sl from py_cart where uid='%s'" % _username
        cursor.execute(sql)
        return cursor.fetchall()
        cursor.close()
        conn.close()

    def add_cart(self, _username, _pdinfo):
        """
        加入购物车
        :param _username: 用户名
        :param _pdinfo: 产品信息
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "insert into py_cart(title,price,pid,uid)VALUES ('%s','%s','%s','%s')" % (_pdinfo[0][1], float(_pdinfo[0][2]), _pdinfo[0][0], _username)
        if not self.is_exist(_pdinfo[0][0], _username):
            cursor.execute(sql)
            conn.commit()
        else:
            sql = "update py_cart set sl= sl+1 where pid='%s' and uid='%s' " % (_pdinfo[0][0], _username)
            cursor.execute(sql)
            conn.commit()
        cursor.close()
        conn.close()

    def sub_money(self, _money, _username):
        """
        从用户金额中扣除消费，结算
        :param _money: 所花费金额
        :param _username: 用户名
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "update py_user set my_money=(my_money-'%s') where username='%s'" % (float(_money), _username)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def clear_cart(self, _money, _username):
        """
        清空购物车
        :param _money:
        :param _username:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "delete from py_cart where uid='%s'" % _username
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        self.sub_money(_money, _username)

    def is_exist(self, _pid, _username):
        """
        判断购物国是否有相同商品
        :param _pid:
        :param _username:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select * from py_cart where pid='%s' and uid='%s' " % (_pid, _username)
        cursor.execute(sql)
        t = len(cursor.fetchall())
        if t > 0:
            return True
        else:
            return False
        cursor.close()
        conn.close()

    def is_user(self, _username):
        """
        用户是否注册
        :param _username:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select * from py_user where username='%s' " % _username
        cursor.execute(sql)
        t = len(cursor.fetchall())
        if t > 0:
            return True
        else:
            return False
        cursor.close()
        conn.close()

    def get_byid(self, pid):
        """
        获取产品信息
        :param pid: 产品编号
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select * from py_product where id=%s " % pid
        cursor.execute(sql)
        return cursor.fetchall()

        cursor.close()
        conn.close()

    def get_pdlist(self):
        """
        产品列表
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select id,title,price from py_product"
        cursor.execute(sql)
        return cursor.fetchall()
        cursor.close()
        conn.close()

    def login(self, _username, _passwd):
        """
        用户登陆功能
        :param _username:
        :param _passwd:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select * from py_user where username='%s' and passwd='%s' " % (_username, _passwd)
        cursor.execute(sql)
        t = len(cursor.fetchall())
        if t > 0:
            return True
        else:
            return False
        cursor.close()
        conn.close()

    def get_user_money(self, _username):
        """
        获取用户账户中的金额
        :param _username:
        :return:
        """
        conn = self.db_conn()
        cursor = conn.cursor()
        sql = "select my_money from py_user where username='%s' " % _username
        cursor.execute(sql)
        info = cursor.fetchall()
        return info[0][0]
        cursor.close()
        conn.close()



