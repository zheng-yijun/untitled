#-*-coding:utf-8-*-
__aothor__ = "zhengyj"
import pymysql

#创建连接
conn = pymysql.connect(host='192.168.50.201',user='admin',password='makecook',port=3306)
#创建游标
cursor = conn.cursor()
#执行语句
effect_row = cursor.execute("select * from zyj.student")



print(cursor.fetchmany(3))


