# !/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors

host = 'localhost'
user = 'admin'
password = 'admin'
database = 'kontora'
port = 3306

con = pymysql.connect(host=host,
                      user=user,
                      password='admin',
                      database=database,
                      port=port)

with con:
    cur = con.cursor()
    cur.execute("select * from k_firm")

    # version = cur.fetchone()

    rows = cur.fetchall()



    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

#    cursorclass=pymysql.cursors.DictCursor
#    for row in rows:
#         print(row["firm_num"], row["firm_name"])
