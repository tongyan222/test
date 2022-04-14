"""
数据库的连接和处理
"""
import os
from configparser import ConfigParser


import pymysql

# --------- 读取config.ini配置文件 ---------------

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")  # 读取到本机的配置文件
print(cfgpath)
conf = ConfigParser()
cf = conf.read(cfgpath, encoding='utf-8')
class mysql_db(object):
    """
    数据库的基本操作，增删改查
    """
    def __init__(self):
        """
        数据库的连接
        """
        env = 'mysqlconf'
        try:
            self.conn = pymysql.connect(
                host = conf.get(env, 'host'),
                user = conf.get(env, 'user'),
                password =conf.get(env, 'password'),
                db = conf.get(env, 'db_name'),
                charset='utf8'

            )
        #
        except OperationalError as e:
            print('数据库连接错误')



    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
        self.conn.close()

   # 清除表数据
    def clear(self,table_name,condit):
        real_sql = "delete from " + table_name + "where" + condit + ";"
        with self.conn.cursor() as cursor:
             # 取消表的外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()
        self.conn.close()

    # 修改表数据
    def update(self,table_name,table_data,condit):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "UPDATE" + table_name + "set" + table_data + "where"+condit+";"

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(real_sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback() #修改失败回滚
        finally:
            self.conn.close()


    # 查询表的数据
    def select(self,table_name,table_data,condit):
        real_sql = "select " + table_data +" from " + table_name +" where " + condit+";"
        print(real_sql)
        with self.conn.cursor() as cursor:
            result = cursor.execute(real_sql)
            
        self.conn.commit()
        self.conn.close()
        return result

if __name__ == "__main__":
    aa =mysql_db()
    table = 'dftc_cas_client_user'
    table_data = 'use_nick_name'
    condit = 'id=1143759237769125890'
    print(aa.select(table,table_data,condit))
