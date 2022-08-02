"""
Time:2022/8/2 000216:57
Author:bty
连接数据库
"""
import pymysql
from common.handle_config import conf


class HandleDB:

    def __init__(self):
        self.con = pymysql.connect(host=conf.get('mysql', 'host'),
                                   user=conf.get('mysql', 'user'),
                                   password=conf.get('mysql', 'pwd'),
                                   port=conf.getint('mysql', 'port'),
                                   charset='utf8')

    def find_one(self, sql: str) -> tuple:
        """
        查询数据库后返回一条结果
        :param sql: 查询的sql语句
        :return: 返回元组类型的数据
        """
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        # 关闭游标
        cur.close()
        return res

    def find_count(self, sql) -> int:
        """
        查询数据库后，返回数据的条数
        :param sql: 查询的sql语句
        :return: 返回查询后的结果条数，类型为int
        """
        with self.con as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()


if __name__ == '__main__':
    mysql = HandleDB()
    sql = "SELECT mobile_phone FROM futureloan.member LIMIT 1"
    res = mysql.find_count(sql)
    print(res, type(res))
