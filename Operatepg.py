#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-15 15:12
# @Author : shiwandong
# @Site :
# @File : process_tweet.py
# @Description: 将项目服务器上面的数据荡下来

import psycopg2

class Operatepg(object):
    def __init__(self):
        self.conn = psycopg2.connect(dbname="postgres",
                                     user="postgres",
                                     password="root",
                                     host="10.10.2.52",
                                     port="5432")
        self.cur = self.conn.cursor()

    def updateDataOperate(self, update_sql):
        self.cur.execute(update_sql)
        self.conn.commit()