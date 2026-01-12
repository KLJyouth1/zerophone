#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
动作执行模块
负责执行智能体的决策结果，包括鼠标操作、键盘操作等
"""

import pyautogui
import time
import subprocess
import os

class ActionExecutor:
    """动作执行类"""
    
    def __init__(self):
        """初始化动作执行器"""
        # 设置pyautogui的安全设置
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
        
    def move_mouse(self, x, y, duration=0.2):
        """
        移动鼠标到指定位置
        :param x: 目标x坐标
        :param y: 目标y坐标
        :param duration: 移动持续时间
        """
        try:
            pyautogui.moveTo(x, y, duration=duration)
            return True
        except Exception as e:
            print(f"移动鼠标失败: {e}")
            return False
    
    def click_mouse(self, x=None, y=None, button='left', clicks=1, interval=0.2):
        """
        点击鼠标
        :param x: 点击x坐标（None表示当前位置）
        :param y: 点击y坐标（None表示当前位置）
        :param button: 按钮类型 ('left', 'right', 'middle')
        :param clicks: 点击次数
        :param interval: 点击间隔
        """
        try:
            if x is not None and y is not None:
                pyautogui.click(x, y, clicks=clicks, interval=interval, button=button)
            else:
                pyautogui.click(clicks=clicks, interval=interval, button=button)
            return True
        except Exception as e:
            print(f"点击鼠标失败: {e}")
            return False
    
    def double_click(self, x=None, y=None, button='left'):
        """
        双击鼠标
        :param x: 点击x坐标
        :param y: 点击y坐标
        :param button: 按钮类型
        """
        return self.click_mouse(x, y, button, clicks=2, interval=0.1)
    
    def right_click(self, x=None, y=None):
        """
        右键点击
        :param x: 点击x坐标
        :param y: 点击y坐标
        """
        return self.click_mouse(x, y, button='right')
    
    def drag_mouse(self, start_x, start_y, end_x, end_y, duration=0.5, button='left'):
        """
        拖拽鼠标
        :param start_x: 起始x坐标
        :param start_y: 起始y坐标
        :param end_x: 结束x坐标
        :param end_y: 结束y坐标
        :param duration: 拖拽持续时间
        :param button: 按钮类型
        """
        try:
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown(button=button)
            pyautogui.moveTo(end_x, end_y, duration=duration)
            pyautogui.mouseUp(button=button)
            return True
        except Exception as e:
            print(f"拖拽鼠标失败: {e}")
            return False
    
    def scroll_mouse(self, amount, x=None, y=None):
        """
        滚动鼠标
        :param amount: 滚动量（正数向上，负数向下）
        :param x: 滚动位置x坐标
        :param y: 滚动位置y坐标
        """
        try:
            if x is not None and y is not None:
                pyautogui.moveTo(x, y)
            pyautogui.scroll(amount)
            return True
        except Exception as e:
            print(f"滚动鼠标失败: {e}")
            return False
    
    def press_key(self, key, presses=1, interval=0.1):
        """
        按下键盘按键
        :param key: 按键名称
        :param presses: 按下次数
        :param interval: 按下间隔
        """
        try:
            pyautogui.press(key, presses=presses, interval=interval)
            return True
        except Exception as e:
            print(f"按下按键失败: {e}")
            return False
    
    def type_text(self, text, interval=0.05):
        """
        输入文本
        :param text: 要输入的文本
        :param interval: 字符间隔
        """
        try:
            pyautogui.typewrite(text, interval=interval)
            return True
        except Exception as e:
            print(f"输入文本失败: {e}")
            return False
    
    def hotkey(self, *keys):
        """
        按下组合键
        :param keys: 键名列表
        """
        try:
            pyautogui.hotkey(*keys)
            return True
        except Exception as e:
            print(f"按下组合键失败: {e}")
            return False
    
    def launch_application(self, path):
        """
        启动应用程序
        :param path: 应用程序路径
        """
        try:
            if os.path.exists(path):
                subprocess.Popen(path)
                return True
            else:
                print(f"应用程序路径不存在: {path}")
                return False
        except Exception as e:
            print(f"启动应用程序失败: {e}")
            return False
    
    def close_application(self, application_name):
        """
        关闭应用程序
        :param application_name: 应用程序名称
        """
        try:
            # 这里使用任务管理器关闭应用程序
            # 注意：这种方式可能不太安全，建议使用更优雅的方式
            subprocess.run(['taskkill', '/F', '/IM', application_name], check=True)
            return True
        except Exception as e:
            print(f"关闭应用程序失败: {e}")
            return False
    
    def get_mouse_position(self):
        """
        获取当前鼠标位置
        :return: 当前鼠标坐标 (x, y)
        """
        return pyautogui.position()
    
    def execute_action(self, action_type, **kwargs):
        """
        执行指定类型的动作
        :param action_type: 动作类型
        :param kwargs: 动作参数
        :return: 是否执行成功
        """
        action_map = {
            'move_mouse': self.move_mouse,
            'click': self.click_mouse,
            'double_click': self.double_click,
            'right_click': self.right_click,
            'drag': self.drag_mouse,
            'scroll': self.scroll_mouse,
            'press_key': self.press_key,
            'type_text': self.type_text,
            'hotkey': self.hotkey,
            'launch_application': self.launch_application,
            'close_application': self.close_application
        }
        
        if action_type in action_map:
            return action_map[action_type](**kwargs)
        else:
            print(f"未知的动作类型: {action_type}")
            return False

# 示例用法
if __name__ == "__main__":
    executor = ActionExecutor()
    
    # 测试鼠标移动和点击
    print("测试鼠标移动和点击...")
    executor.move_mouse(100, 100)
    time.sleep(1)
    executor.click_mouse()
    
    # 测试键盘输入
    print("测试键盘输入...")
    executor.type_text("Hello, World!")
    time.sleep(1)
    executor.hotkey('ctrl', 'a')
    executor.press_key('backspace')
    
    # 测试获取鼠标位置
    print(f"当前鼠标位置: {executor.get_mouse_position()}")