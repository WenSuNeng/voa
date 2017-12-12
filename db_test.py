#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sqlite3
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("voa.db")

# 创建表
'''
con.execute("""
CREATE TABLE voa
(
    id INTEGER,
    title TEXT PRIMARY KEY
);""")
'''
# 创建表：效果相同
'''
con.execute("""
CREATE TABLE todo
(
    id INTEGER PRIMARY KEY NOT NULL,
    title TEXT
);""")
'''

# 插入记录：shopping
#con.execute("INSERT INTO voa (title) VALUES ('shopping');")


# 插入记录：working
#con.execute("INSERT INTO voa (id, title) VALUES (NULL, 'working');")


str = "bbbqsssst"
#con.execute("INSERT INTO voa (id, title) VALUES (NULL,  '"+ str + "');")

# 查询记录
for row in con.execute("SELECT * FROM voa"):
    
    print (row[1].__str__())

con.commit()

con.close()

