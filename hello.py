# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     debug_bot.py
   Description：
   Author :       stephen
   date：          2018/10/11
-------------------------------------------------
   Change Activity:
                   2018/10/11:
-------------------------------------------------
"""
import logging

import os
import argparse
import webdriverwrapper
from pyvirtualdisplay import Display



class DebugBot(object):

    def __init_screen(self):
        self.display = Display(visible=0, size=(1920, 1080))
        if not os.getenv('DISPLAY'):
            self.display.start()
            logging.info('Started virtual display at %s', os.getenv('DISPLAY'))

    def __close_screen(self):
        if self.display.is_started:
            self.display.stop()

    def init_driver(self, proxy, user_agent):
        options = webdriverwrapper.ChromeOptions()
        options.add_argument('--proxy-server=%s' % proxy)
        options.add_argument("--no-sandbox")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        if user_agent:
            options.add_argument('--user-agent={}'.format(user_agent) )
        cd = webdriverwrapper.Chrome(chrome_options=options)
        cd.set_window_size(1920, 1080)
        return cd

    def __init__(self, proxy, user_agent, url):
        self.__init_screen()
        self.driver = self.init_driver(proxy=proxy, user_agent=user_agent)
        self.driver.get(url)
        print(self.driver.page_source)

    def __del__(self):
        self.__close_screen()


ap = argparse.ArgumentParser()
ap.add_argument('-u', '--url', type=str, required=True, help='test url')
ap.add_argument('-p', '--proxy', type=str, required=None, help='proxy')
ap.add_argument('-a', '--userAgent', type=str, default=None, required=False, help='user agent')
args = ap.parse_args()
url = args.url
if __name__ == '__main__':
    testbot = DebugBot(proxy=args.url, user_agent=args.userAgent, url=url)

