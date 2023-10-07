'''
project:声源定位系统
version:0.0
date:2023/10/7 13:14
author:丁易杰
explain：仅实现说话角度读取功能
'''

#导入串口模块
from pyb import UART
import json

uart_voice = UART(3,115200) #设置语音识别模块串口号3和波特率115200，TX--B10  RX--B11

uart_voice.write('sys start!\r\n') #初始化系统结束

while True:
 
    #判断有无收到信息
    if uart_voice.any():
        voice = uart_voice.read(300) #默认单次最多接收64字节
        voice_utf8 = voice.decode('utf-8') #将字节对象解码为字符串
        voice_json = json.loads(voice_utf8) #解析JSON字符串
        voice_info = json.loads(voice_json['content']['info'])
        voice_angle = voice_info['ivw']['angle']
        voice_angle_int = round(voice_angle) #保留整数
        
        print(voice_angle_int)
    