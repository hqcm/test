import scrapy
import hashlib
import base64
import re

def get_imgurl(m, r='', d=0):
        #解密获取图片链接
        e = "DECODE"
        q = 4
        r = _md5(r)
        o = _md5(r[0:0 + 16])
        n = _md5(r[16:16 + 16])
        l = m[0:q]
        c = o + _md5(o + l)
        m = m[q:]
        k = _base64_decode(m)                       
        h = list(range(256))
        b = [ord(c[g % len(c)]) for g in range(256)]

        f = 0
        for g in range(0, 256):
            f = (f + h[g] + b[g]) % 256
            tmp =  h[g]
            h[g] = h[f]
            h[f] = tmp

        t = ""
        p, f = 0, 0
        for g in range(0, len(k)):
            p = (p + 1) % 256
            f = (f + h[p]) % 256
            tmp = h[p]
            h[p] = h[f]
            h[f] = tmp
            t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
        t = t[26:]
        return t
def _md5(value):
        #md5加密
        m = hashlib.md5(value.encode('utf-8'))
        return m.hexdigest()
def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)
if __name__ == '__main__':
    m = 'e449ZjGdeQ7XK5gByQ4KKVjUgM+oybr+ESXa4OEZtVUhEi+fPI7+StsM6BDHKr8kyVDZTvmvborhd1UNE0A+iAy0xPy4Rb4zwPBhXTUtRt49wB+bCaXI5w'
    r = 'cDU6z5s1g1G2mdw3XS5P3T1ZMgNah1Bt'
    print(get_imgurl(m,r))
