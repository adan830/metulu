# _*_ coding: utf-8 _*_
__author__ = 'StudentDream'
import hashlib

def get_md5(url):
    if isinstance(url,str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
if __name__ == "__main__":
   pass