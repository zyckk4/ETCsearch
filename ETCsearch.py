# -*- coding: utf-8 -*-
'''
ETC search
@author: zyckk4  https://github.com/zyckk4
Created on Mar 25 2022
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def load_chrome(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    wd = webdriver.Chrome(options=chrome_options)
    wd.implicitly_wait(10)
    return wd

def search(mode,a):
    wd=load_chrome()
    url=['https://faculty.evansville.edu/ck6/encyclopedia/Search_6_9_13.html',
         'https://faculty.evansville.edu/ck6/encyclopedia/Search_9_13_6.html',
         'https://faculty.evansville.edu/ck6/encyclopedia/Search_13_6_9.html']
    wd.get(url[mode-1])
    try:
        element=wd.find_element(By.XPATH,f'//tr[td[2]-{a}<0.0000001 and td[2]-{a}>-0.0000001]/td[1]')
    except NoSuchElementException:
        print("Element doesn't exist!")
        return
    mesg=f'The triangle center you want is X({element.text})'
    return mesg
    
def main():
    print('mode1:search center by (6,9,13) coordinate')
    print('mode2:search center by (9,13,6) coordinate')
    print('mode3:search center by (13,6,9) coordinate')
    try:
        mode=int(input('Choose the mode:'))
    except:
        print('invalid input!')
        return
    a=input('enter the coord:')
    try:
        a=float(a)
    except:
        print('invalid input!')
        return
    mesg=search(mode,a)
    if mesg is None:
        return
    print(mesg)
    
main()
    