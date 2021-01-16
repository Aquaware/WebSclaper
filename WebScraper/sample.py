#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:58:49 2018

@author: iku
"""
import sys
sys.path.append("../common")
sys.path.append("../private")

import ChromeHandler as Chrome

chrome1 = Chrome.ChromeHandler()

def action():
    chrome1.clickButtonByName('reloadButton')
    try:
        chrome1.selectListByName('targetDeliveryMonth', '1234')
        chrome1.executeJS("changeDeliveryMonth('0')", [])
    except:
        print('error')
   
def close():
    chrome1.close()
    pass

def login():
    url = 'https://xxx.xxxx.xxxx.xxx.xxx'
    userid = 'id'
    password = 'pass'
    chrome1.connect(url)
    chrome1.inputElement('j_username', userid)
    chrome1.inputElement('j_password', password)
    chrome1.clickButtonByName('LoginForm')
    chrome1.linkByClassName('js-fuop')
    chrome1.linkByText('注文')
    return

def test():
    login()
    action()
    close()

if __name__ == "__main__":
    test()