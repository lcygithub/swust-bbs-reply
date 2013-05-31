#!/usr/bin/env python
#coding:utf8
'''
Copyright (c) 2013, lcyang/Liu Chongyang
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import requests
from bs4 import BeautifulSoup
import time
import random
import sys

login_url = "http://bbs.swust.edu.cn/login.php"
index_url = "http://bbs.swust.edu.cn/index.php"
# my_page = 14069

def login(username, password):
    login_data = {"jumpurl": "http://bbs.swust.edu.cn/index.php","step": "2","pwuser":username,"pwpwd":password}
    client = requests.session()
    direct = client.post(login_url, data=login_data)
    index = client.get(index_url)
    check = index.text.encode(index.encoding).find(username)
    print check
    return client

def judge_err(text, markup):
    return text.find(username)

def make_url(i):
    base_url = "http://bbs.swust.edu.cn/read-htm-tid-"
    post_url = base_url + str(i) + ".html"
    return post_url

def make_page(i, clinet):
    page = client.get(make_url(i))
    return page.text.encode(page.encoding)

def make_content(content):
    return content + str(random.uniform(0,100)) + "!"

def reply(contents,start,end, username, client):
    for i in range(start,end):
        if judge_err(make_page(i, client), username) != -1:
            print make_url(i)
            content = make_page(i, client)
            start = content.find('<form name="FORM" method="post"')
            end = content.find("</form>",content.find('<form name="FORM" method="post"'))
            content = BeautifulSoup(content[start: end+len("</form>")])
            post_data = {}
            try:
                post_url = index_url.replace("index.php",content.form.attrs["action"])
                for input in content.find_all("input"):
                    post_data[input.attrs["name"]] = input.attrs["value"]
                post_data["atc_content"] = make_content(contents)
                rep = client.post(post_url,data=post_data)
                print rep.text.encode(rep.encoding)
            except AttributeError as e:
                print e
        time.sleep(5)

def ToReply(contents, username, client):
    time.sleep(4)
    print make_url(my_page)
    content = make_page(i, client)
    start = content.find('<form name="FORM" method="post"')
    end = content.find("</form>",content.find('<form name="FORM" method="post"'))
    content = BeautifulSoup(content[start: end+len("</form>")])
    post_data = {}
    try:
        post_url = index_url.replace("index.php",content.form.attrs["action"])
        for input in content.find_all("input"):
            post_data[input.attrs["name"]] = input.attrs["value"]
        post_data["atc_content"] = make_content(contents)
        rep = client.post(post_url,data=post_data)
        print rep.text.encode(rep.encoding)
    except AttributeError as e:
        print e
    
if __name__ == '__main__':
    print sys.argv
    try:
        start = int(sys.agrs[1])
        end = int(sys.argv[2])
    except:
        start = 3050
        end = 170000
    try:
        content = sys.argv[3]
    except:
        content = "顶起 "
    print start,end,content
    username = raw_input("username:")
    password = raw_input("password:")
    client = login(username, password)
    reply(content, start, end, username, client)
    # while(True):
    #     ToReply("pythoner ")
    