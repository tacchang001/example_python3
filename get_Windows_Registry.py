# -*- coding: utf-8 -*-
from winreg import *

'''
http://d.hatena.ne.jp/itasuke/20110730/winreg_dword
https://automationlabo.com/wat/enc/des/screensaveactive/
'''

def main():
    try:
        with OpenKey(HKEY_CURRENT_USER, r'Control Panel\Desktop') as key:
            # スクリーン セーバー 有効／無効
            _val = 'ScreenSaveActive'
            data, typ = QueryValueEx(key, _val)
            print(_val, ":", data)
            # スクリーン セーバーの種類
            _val = 'SCRNSAVE.EXE'
            data, typ = QueryValueEx(key, _val)
            print(_val, ":", data)
            # スクリーン セーバーの待ち時間
            _val = 'ScreenSaveTimeOut'
            data, typ = QueryValueEx(key, _val)
            print(_val, ":", data)
            # スクリーン セーバーの待ち時間
            _val = 'ScreenSaverIsSecure'
            data, typ = QueryValueEx(key, _val)
            print(_val, ":", data)
    except FileNotFoundError:
        print('スクリーンセーバーが設定されていません')

if __name__ == "__main__":
    main()
