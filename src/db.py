#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# https://docs.sqlalchemy.org/en/14/orm/quickstart.html
# SQLAlchemy
import re
from src.config import *
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Date, Time, DECIMAL, Text, create_engine, and_, or_, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
import json
import os,sys
import datetime
# 创建对象的基类:
Base = declarative_base()

# 创建表对象:


class Weather(Base):
    # 表的名字:
    __tablename__ = 'weather'
    # 表的结构:
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)  # 自增、主键、不为空
    city = Column(String(100), nullable=False)  # 字符串、不为空
    weather = Column(String(100), nullable=False)  # 字符串、不为空
    day = Column(String(100), nullable=False)  # 字符串、不为空

    # sqlalchemy转json，方式一
    def to_json(self):
        return {
            'id': self.id,
            'city': self.city,
            'day': self.day,
        }
    # sqlalchemy转dict，方式二

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'day': self.day,
        }


'''
CREATE TABLE IF NOT EXISTS `weather`(
`id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'ID',
`city` VARCHAR(100) NOT NULL COMMENT '城市',
`weather` INT(100) NOT NULL COMMENT '天气',
`day` VARCHAR(100) NOT NULL COMMENT '日期'
PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''



# 初始化数据库连接: TODO 参数化
engine = create_engine(
    f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()

'''
    # [用户表插入数据-创建用户]
    param: city string
    param: weather string
    param: day string
'''


def insert_db_table(city, weather, day):
    try:
        # 创建对象:
        w = Weather(city=city, weather=weather, day=day)  # 插入数据表成功后，返回的是一个对象，具有id属性
        # 添加到session
        session.add(w)
        print("w:", w)
        # 提交即保存到数据库
        session.commit()
        # 判断是否插入成功
        if w.id:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        session.rollback()# 回滚
    finally:
        session.close()# 关闭session

