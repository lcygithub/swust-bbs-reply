脚本使用python语言编写，只要用到了requests、bs4等模块，在写脚本前看了HTTP权威指南这本书，很受益。

用法： python swust-bbs-reply.py start(起始帖子id) end(结束贴子id) content(发帖内容)

    eg： python swust-bbs-reply.py 50 60 顶起！
    
     默认情况下，帖子从3050开始，一直发170000，内容默认为 "顶起"。
     
    eg:  python swust-bbs-reply.py 
    


声明：此脚本是近期学习HTTP协议的练习作品，clone者可共享源代码学习，但不可用于非法用途。否则，造成一切后果自己承担。
