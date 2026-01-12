#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
屏幕监控模块
负责实时监控电脑屏幕，捕获屏幕内容，分析屏幕元素
"""

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time

class ScreenMonitor:
    """屏幕监控类"""
    
    def __init__(self):
        """初始化屏幕监控"""
        self.screen_width, self.screen_height = pyautogui.size()
        self.last_screenshot = None
        self.monitoring = False
        
    def get_screen_size(self):
        """获取屏幕尺寸"""
        return self.screen_width, self.screen_height
    
    def capture_screen(self, region=None):
        """
        捕获屏幕截图
        :param region: 捕获区域 (left, top, width, height)
        :return: 截图图像 (numpy数组)
        """
        try:
            if region:
                left, top, width, height = region
                screenshot = ImageGrab.grab(bbox=(left, top, left+width, top+height))
            else:
                screenshot = ImageGrab.grab()
            
            # 转换为numpy数组
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            self.last_screenshot = screenshot
            return screenshot
        except Exception as e:
            print(f"捕获屏幕失败: {e}")
            return None
    
    def save_screenshot(self, filename, region=None):
        """
        保存屏幕截图
        :param filename: 保存路径
        :param region: 捕获区域
        :return: 是否保存成功
        """
        screenshot = self.capture_screen(region)
        if screenshot is not None:
            cv2.imwrite(filename, screenshot)
            return True
        return False
    
    def start_monitoring(self, interval=1.0):
        """
        开始监控屏幕
        :param interval: 监控间隔（秒）
        """
        self.monitoring = True
        while self.monitoring:
            screenshot = self.capture_screen()
            # 这里可以添加屏幕变化检测逻辑
            time.sleep(interval)
    
    def stop_monitoring(self):
        """停止监控屏幕"""
        self.monitoring = False
    
    def detect_screen_change(self, threshold=1000):
        """
        检测屏幕是否变化
        :param threshold: 变化阈值
        :return: 是否变化
        """
        current_screenshot = self.capture_screen()
        if self.last_screenshot is None:
            self.last_screenshot = current_screenshot
            return True
        
        # 计算差异
        diff = cv2.absdiff(self.last_screenshot, current_screenshot)
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        non_zero_count = np.count_nonzero(gray_diff)
        
        self.last_screenshot = current_screenshot
        return non_zero_count > threshold
    
    def get_screen_element(self, element_name):
        """
        获取屏幕元素位置
        :param element_name: 元素名称
        :return: 元素位置 (x, y, width, height)
        """
        # 这里可以集成阶跃星辰的GELab-Zero模型进行元素识别
        # 暂时返回None，后续集成模型后实现
        return None
    
    def analyze_screen_content(self, screenshot=None):
        """
        分析屏幕内容
        :param screenshot: 截图图像
        :return: 分析结果
        """
        # 这里可以集成阶跃星辰的GELab-Zero模型进行内容分析
        # 暂时返回空字典，后续集成模型后实现
        return {}

# 示例用法
if __name__ == "__main__":
    monitor = ScreenMonitor()
    print(f"屏幕尺寸: {monitor.get_screen_size()}")
    
    # 捕获全屏
    screenshot = monitor.capture_screen()
    if screenshot is not None:
        print(f"截图尺寸: {screenshot.shape[:2]}")
        monitor.save_screenshot("test_screenshot.png")
        print("截图已保存")
    
    # 捕获指定区域
    region_screenshot = monitor.capture_screen((100, 100, 400, 300))
    if region_screenshot is not None:
        monitor.save_screenshot("test_region_screenshot.png")
        print("区域截图已保存")