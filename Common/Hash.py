# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 下午2:13
# @Author  : WangJuan
# @File    : Hash.py
"""
封装各种加密方法

"""

from hashlib import sha1
from hashlib import md5
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import binascii, hashlib


def double_md5(self):
    '''
    一生约正式环境登录接口的签名规则-双重加密
    现在加密算法和java的MD5值不匹配
    :return:
    '''
    key = 'MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALe39vUUq6T1NBMg4QoEyl96WKYdHrGUvYIMRDIIaHZbu1eLeYEiesV/XNMwLyzXVZwmy9WpyNBTdDpQ'
    rand8 = self.randint_8()
    cur_ti = self.get_current_timestamp()
    str_sum = str(rand8) + key + str(cur_ti)
    str_re = str_sum.encode(encoding='utf-8')
    m = hashlib.md5()
    m.update(str_re)  # 和java端切换为一致的编码格式，也不一样
    n = hashlib.md5()  # 再次定义一个hash对象，因为重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖
    str_rb = m.hexdigest().encode(encoding='utf-8')
    n.update(str_rb)
    k = n.hexdigest()
    return rand8, cur_ti, k

def my_md5(msg):
    """
    md5 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    hl = md5()
    hl.update(msg.encode('utf-8'))
    return hl.hexdigest()


def my_sha1(msg):
    """
    sha1 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_sha256(msg):
    """
    sha256 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = SHA256.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_des(msg, key):
    """
    DES 算法加密
    :param msg: 需加密的字符串,长度必须为8的倍数，不足添加'='
    :param key: 8个字符
    :return: 加密后的字符
    """
    de = DES.new(key, DES.MODE_ECB)
    mss = msg + (8 - (len(msg) % 8)) * '='
    text = de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()


def my_aes_encrypt(msg, key, vi):
    """
    AES 算法的加密
    :param msg: 需加密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return: 加密后的字符
    """
    obj = AES.new(key, AES.MODE_CBC, vi)
    txt = obj.encrypt(msg.encode())
    return binascii.b2a_hex(txt).decode()


def my_aes_decrypt(msg, key, vi):
    """
    AES 算法的解密
    :param msg: 需解密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return: 加密后的字符
    """
    msg = binascii.a2b_hex(msg)
    obj = AES.new(key, AES.MODE_CBC, vi)
    return obj.decrypt(msg).decode()



print(my_md5('wj123456'))