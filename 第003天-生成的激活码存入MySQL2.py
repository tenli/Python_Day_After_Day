"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import random
import string
from Python日复一日.Python_Day_After_Day.MySQL_Connect import MysqlConnect


# 定义方法,code_long:激活码长度,code_num


def gen_codes(code_long, code_num):
    # code_long:激活码长度
    # code_num:激活码数量
    # 定义列表,用以存储激活码
    gen_code_list = []
    i = 1
    while i <= code_num:
        # 随机字符串
        gen_code = ''.join(random.sample(string.ascii_letters + string.digits, code_long))
        # 判断是否已经存在
        if gen_code in gen_code_list:
            continue
        else:
            gen_code_list.append(gen_code)
            i += 1
    # print(gen_code_list)
    return gen_code_list


def save_into_da():
    db = MysqlConnect('192.168.5.36', 'root', 'aa111111', 3306, 'wdd_test')
    code_list = gen_codes(10, 10)
    i = 0
    while i < len(code_list):
        # 拼接SQL
        sql = 'insert into test_user(name) values("'"{0}"'")'.format(code_list[i])
        # 执行sql语句
        db.exec(sql)
        i += 1


if __name__ == '__main__':
    save_into_da()
