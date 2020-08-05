alphabet_src = 'abcdefghijklmnopqrstuvwxyz'


def cryptIt(src_str: str, if_decrypt: bool = False) -> str:
    '''用于对字符串进行简单替换加密/解密
    输入参数：
    src__str: 原始文本内容
    if_decrypt: True表示解密过程，False表示加密过程
    返回结果：加密文本
    '''
    global alphabet_src
    result = ''
    for single_char in src_str:
        if single_char in alphabet_src:
            old_index = alphabet_src.index(single_char)
            if if_decrypt == True:
                new_index = (old_index - 3) % 26 
                # if old_index + 3 < 26 else old_index + 3 - 26
            else:
                new_index = (old_index + 3) % 26
            result += alphabet_src[new_index]
        else:
            result += single_char
    return result

# 测试代码
assert('abcdefghijklmnopqrstuvwxyz!' == cryptIt(cryptIt('abcdefghijklmnopqrstuvwxyz!', False), True))
a=input("请输入字符串: ")
print(cryptIt(a))
print(cryptIt('I love you!'))
print(cryptIt('I oryh brx', True))

