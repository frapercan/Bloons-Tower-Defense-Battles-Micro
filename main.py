# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key,KeyCode
import time


tower_buy_coords = None

tower_power_coords = None

tower_build_coords = None

left_upgrade = False



def set_up_tower_buy_coords():
    global tower_buy_coords
    tower_buy_coords= pyautogui.position()
    
    print(f'buy towers in coords {tower_buy_coords}')

def set_up_tower_power_coords():
    global tower_power_coords
    tower_power_coords= pyautogui.position()
    print(f'tower power coords: {tower_power_coords}')
    
def set_up_tower_build_coords():
    global tower_build_coords
    tower_build_coords= pyautogui.position()
    print(f'tower build coords: {tower_build_coords}')

def toggle_left_upgrade():
    global left_upgrade
    left_upgrade = not left_upgrade 

    
def use_power():
    time.sleep(0.05)
    pyautogui.click(tower_buy_coords)
    time.sleep(0.05)
    pyautogui.moveTo(tower_build_coords,duration=0.05 )
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.press('.')
    pyautogui.press('.')
    pyautogui.press('.')
    pyautogui.press('.')
    pyautogui.press('.')
    if left_upgrade:
        pyautogui.press(',')
        pyautogui.press(',')
    time.sleep(0.05).....,
    pyautogui.moveTo(tower_power_coords,duration=0.05 )
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.moveTo(tower_build_coords,duration=0.05 )
    pyautogui.click()
    pyautogui.press('backspace')
    print(left_upgrade()) 
    

    

def on_press(key):
    
    if key == KeyCode(char='c'):
        toggle_left_upgrade()
    if key == KeyCode(char='b'):
        set_up_tower_buy_coords()
    if key == KeyCode(char='n'):
        set_up_tower_power_coords()
    if key == KeyCode(char='m'):
        set_up_tower_build_coords()
    if key == Key.space:
        use_power()
    
    
    




with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
