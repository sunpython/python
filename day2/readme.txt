###老男孩python学员###
qq群昵称：71-sungwd-顾伟栋
svn用户名:stu107411
博客：http://www.cnblogs.com/sunface/
github:https://github.com/sunpython/python
qq:77625811
邮箱:77625811@qq.com
#######################

    flowchart 流程图文件夹
    shop_mysql.py mysql版本(整核了用户登陆)
    shop.py       基础版本（重在实践字典操作）
    tree.py       三层菜单作业
    环境          数据库脚本及数据库客户端
    readme 第1天的文件说明

    shop_mysql.py

        1，数据库
            我使用了mysql5.5 现在放在我单位服务器上
            用户测试数据
                sungwd	123	111	1	7570
                moongwd	123	0	1	1000
                test	321	0	1	10000
        2,使用说明
             本程序在python3.5环境中测试通过
            （1）需要安装mysql-connector-python-2.0.4，下载并解压，把lib中的内容中复制到site-packages中才可以运行
            （2）mysql-connector-python-2.0.4和sql文件，我会一起上传至svn
             (3) 基本流程：
                    A 用户登陆  用户和密码都存在数据中，用户成功验证才能进行下一步
                    B 获取用户信息，获取用户的余额并以此来当作预算，来限制加入购物车的中产品数量
                    C 打印产品列表
                    D 判断用户的余额是否能购买最低价的产品，如果不可以了，打印购物车，并提示进入结算流程
                    E 选择产品进行购买，并判断用户的余额，是否可以购买此产品，如果不行，让用户重新选择
                    F 把产品和用户关联在一起加入购物车，并从预算中减掉价格，若购物车已经存在此商品，则把数量+1
                    G 购买成功后让用户选择是否继续购买，否则打印购物车，进入结算流程,选是继续购买
                    H 打印购物车时统计出自己的消费
                    I 结算是清空用户的购物车，并从数据库扣除所花费金额（实现真正下单）
					
	本周发现：字典并非完全无序  我的博文 http://www.cnblogs.com/sunface/p/5163996.html




