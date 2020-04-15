# -*- coding:utf-8 -*-
import pygame
import sys
import random
import os

class Bird(object):
        '''定义一个鸟类'''
        def __init__(self):
                '''定义初始化方法'''
                pass

        def birUpdate(self):
                pass

class Pipeline(object):
        '''定义一个管道类'''
        def __init__(self):
                '''定义初始化方法'''
                pass

        def updatePipeline(self):
                '''水平移动'''
                pass

def createMap():
        '''定义创建地图的方法'''
        screen.fill((255,255,255))                        #填充颜色
        screen.blit(background,(0,0))                #填入到背景
        pygame.display.update()                                #更新显示

if __name__ == '__main__':
        pygame.init()                                                        #初始化pygame
        os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (800, 200)  
        size = width,height = 400,650                        #设置窗口
        screen = pygame.display.set_mode(size)        #显示窗口
        clock = pygame.time.Clock()                                #设置时钟
        Pipeline = Pipeline()                                        #实例化管道类
        Bird = Bird()                                                        #实例化鸟类
        while True:
                clock.tick(50)                                                #每秒执行50次
                # 轮询事件
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()

                background = pygame.image.load('assets/background.png')        #加载背景图片
                createMap()                                                        #绘制地图
        pygame.quit()                                                        #退出
