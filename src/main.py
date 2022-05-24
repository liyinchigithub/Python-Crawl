#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from re import search# 正则表达式
from src.common.get_json import config # 解析json函数
from src.common.send_email import *# 发送邮件函数
import pytest  # 单元测试模块
from selenium import webdriver# selenium库
import json,sys,os,time
from pyecharts.charts import Bar # echarts
from pyecharts import options as opts# echarts
from pyecharts.options.global_options import AxisOpts# echarts
import src.webdriver_init as webdriver_init  # 导入封装selenium初始化自定义模块
import logging  # 日志模块
import src.logging_init as logging_init  # 导入封装logging初始化自定义模块
from src.db import * # 数据库
T = time.strftime("%Y-%m-%d %X")# 时间戳
driver = webdriver_init.DriverConfig.driver_config(webdriver)# selenium初始化
logger = logging_init.LoggingConfig(logging, f"./log/{T}.txt").logging_config()# 日志初始化
Config = config(f"{os.getcwd()}/config/config.json").get_config_from_json()# 读取配置文件
logger.info(os.getcwd())# 当前项目路径


city_name = [
    "福州",
    "上海",
    "北京",
    "天津",
    "重庆",
    "南宁",
    "广州",
    "贵阳",
    "杭州",
    "南京",
    "合肥",
    "济南",
    "太原",
    "西安",
    "银川",
    "拉萨",
    "乌鲁木齐",
    "呼和浩特",
    "哈尔滨",
    "长春",
    "沈阳",
    "长沙",
    "成都",
    "昆明"
]


'''
    天气网站全国省会城市天气预报
'''


@pytest.mark.test
def test_table():
    driver.get("http://www.weather.com.cn/weather/101010100.shtml")# 打开网站
    # 遍历爬取城市
    for city in city_name:
        try:
            # 查找结果
            logger.info("打开网页")
            driver.set_window_size(800, 800)# 设置窗口大小
            driver.set_window_position(0, 0)# 设置窗口位置
            logger.info(f"当前是:{city}")
            input=driver.find_element_by_xpath('//*[@id="txtZip"]')# 查找输入框
            input.send_keys(city)# 输入城市
            search_button=driver.find_element_by_class_name('input-btn')# 查找按钮
            search_button.click()# 点击按钮
            search_result=driver.find_element_by_xpath('//*[@id="show"]/ul/li[1]')
            search_result.click()# 点击查找结果
            # 获取最近七天气温
            driver.find_elements_by_xpath('.//*[contains(text(),"7天")]')[1].click()# 点击7天
            # 
            day_list=driver.find_element_by_xpath('//*[@id="7d"]/ul')
            weather_list=day_list.find_elements_by_tag_name('li')
            x=[]
            y1=[]
            for weather in weather_list:
                weather_info=weather.find_element_by_tag_name('h1').text# 
                x.append(weather_info)# 放入列表 
                weather_temp=weather.find_element_by_class_name('tem').text# 获取温度
                m = re.findall("\d+", weather_temp)# 正则表达式
                y1.append(int(m[0]))# 放入列表
                logger.info(f"weather_info:{weather_info}")#  
                logger.info(f"weather_temp:{m[0]}")# 温度
                insert_db_table(city=city, weather=m[0], day=weather_info)# 写入数据库表
            echarts_make(x = x,y1= y1,title=city)# 生成图表
          
           
        except Exception as e:
            logger.info(e)
            # 判断监控方式
            if "email" in Config["monitor_mode"]:
                # 触达通知-qq邮箱
                SendEmail(mail_host=Config["email"]["mail_host"], mail_user=Config["email"]["mail_user"], mail_pass=Config["email"]["mail_pass"], sender=Config["email"]
                          ["sender"], receivers=Config["email"]["receivers"], subject=Config["email"]["subject"], send_content=f"当前数据:{city}条数据出现异常，请检查！！！").send_qq_email()
            time.sleep(3) # 等待
            driver.refresh()  # 刷新页面
            save_screenshot()
            continue

    driver.quit()# 退出浏览器
'''
    截图保存本地
'''


def save_screenshot():
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    if driver.get_screenshot_as_file('./save_images/%s.png' % now_time):
        logger.info('保存成功')
    else:
        logger.info('保存失败')

def echarts_make(x,y1,title):


    bar = Bar()
    bar.add_xaxis(xaxis_data = x)
    #第一个参数是图例的名称
    bar.add_yaxis(series_name = '天气',y_axis = y1)
    # bar.add_yaxis(series_name = '天气',y_axis = y2)

    #添加options
    bar.set_global_opts(title_opts=opts.TitleOpts(title = f'{title}天气预报'))

    #生成HTML文件
    bar.render(f'echarts图-{title}.html')
    
 