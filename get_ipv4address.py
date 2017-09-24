# -*- coding: utf-8 -*-
import socket

'''
https://algorithm.joho.info/programming/python/socket-get-local-ip-address/#comment-279
'''

def main():
    # ローカルIPアドレスを取得
    ip = socket.gethostbyname(socket.gethostname())
    print(ip) # 192.168.○○○.○○○
    
if __name__ == "__main__":
    main()
