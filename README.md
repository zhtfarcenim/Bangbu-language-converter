# Bangbu-language-converter
**_引言:_** _在绝区零这款游戏中,邦布是一个很神奇的玩意,它们只会嗯呢嗯呢.虽然有汉字字幕翻译,但是有些物种还是不满足于这样的形式,他们(我同学)希望有一款软件,可以帮我们转换和翻译邦布语,于是......我就发明了这款软件.(~~看在我为了让你们阅读代码是不那么困难,写了一堆很长的变量/函数名的份上给我一个赞吧~~.)_
### 为了正确地说出邦布语，我们首先要了解邦布语的构成（~~这不是废话~~）。  
很显然我们的邦布语由”嗯“和”呢“构成，恰好有两种形式，于是我们就可以考虑将汉字转换成二进制字符串，并分别将这些字符串使用嗯呢代替。  

这样我们就可以科学地说邦布语了。

#### 那么如何实现呢？
众嗦粥汁，我们计算机中的汉字编码形式一般使用$Unicode$中的$utf-n$编码。
而$utf-8$可以表示成16进制的形式，我们再将16进制转换为2进制，最后将$0、1$替换为"嗯"、"呢".

##### 理论存在，实践开始#Python

首先我们需要将汉字转换为16进制的字符串：
```python
def string_to_hex_binary(unicode_string):
    hex_binary_string = ""
    for char in unicode_string:
        unicode_code = ord(char)
        hex_binary_string += f"{unicode_code:04x} "
    return hex_binary_string.strip()
user_input = input()
hex_binary_result = string_to_hex_binary(user_input)
print( hex_binary_result)
```
16进制转2进制：
```python
def hex_to_bin(hex_str):
    return format(int(hex_str, 16), '04b')
def convert_hex_to_bin_spaced(hex_str):
    hex_numbers = hex_str.split()
    binary_str = ' '.join(hex_to_bin(num) for num in hex_numbers)
    return binary_str
hex_str = input()
binary_str = convert_hex_to_bin_spaced(hex_str)
print(binary_str)
```
2进制转"嗯""呢"：
```python
binary_str = input()
translated_str = binary_str.replace("1", "嗯").replace("0", "呢")
print(translated_str)
```
综合一下：
```python
def string_to_hex_binary(unicode_string):
    hex_binary_string = ""
    for char in unicode_string:
        unicode_code = ord(char)
        hex_binary_string += f"{unicode_code:04x} "
    return hex_binary_string.strip()
user_input = input()
hex_binary_result = string_to_hex_binary(user_input)
def hex_to_bin(hex_str):
    return format(int(hex_str, 16), '04b')
def convert_hex_to_bin_spaced(hex_str):
    hex_numbers = hex_str.split()
    binary_str = ' '.join(hex_to_bin(num) for num in hex_numbers)
    return binary_str
hex_str = hex_binary_result
binary_str = convert_hex_to_bin_spaced(hex_str)
translated_str = binary_str.replace("1", "嗯").replace("0", "呢")
print(translated_str)
input()
```
#### 代码解释(~~我爱AI~~)
\--------------------------------------------------------------------
##### string_to_hex_binary(unicode_string) 函数：

这个函数接收一个Unicode字符串作为参数。
它遍历字符串中的每个字符，使用内置的ord()函数获取每个字符的Unicode编码。
然后将每个编码转换为十六进制格式，并格式化为4位数，如果不足4位则前面补零。
将格式化后的十六进制数拼接成字符串，每个数之间用空格隔开。
最后使用strip()方法去除字符串末尾的空格，并返回结果。
##### hex_to_bin(hex_str) 函数：

这个函数接收一个十六进制字符串作为参数。
使用内置的int()函数将十六进制字符串转换为整数，基数为16。
然后使用format()函数将整数转换为4位的二进制格式，如果不足4位则前面补零。
##### convert_hex_to_bin_spaced(hex_str) 函数：

这个函数接收一个由十六进制数组成的字符串，这些数之间由空格隔开。
使用split()方法将字符串分割成一个列表，列表中的每个元素都是一个十六进制数。
使用列表推导式和join()方法将列表中的每个十六进制数转换为二进制数，并将这些二进制数用空格连接成一个字符串。
返回转换后的二进制字符串。
代码中的input()函数用于接收用户输入的字符串，然后存储在user_input变量中。

调用string_to_hex_binary(user_input)函数，将用户输入的字符串转换为十六进制字符串，并存储在hex_binary_result变量中。

使用变量hex_str存储hex_binary_result的值。

调用convert_hex_to_bin_spaced(hex_str)函数，将十六进制字符串转换为二进制字符串，并存储在binary_str变量中。

使用replace()方法将binary_str中的“1”替换为“嗯”，将“0”替换为“呢”，存储在translated_str变量中。

使用print()函数打印出转换后的字符串。
\-----------------------------------------------------------------

##### 现在我们会说邦布语了，但是别人有可能听不懂，所以还需要一个解码程序：

一样的，先把嗯呢转化为二进制：
```python
original_str = input()
converted_str = original_str.replace("嗯", "1").replace("呢", "0")
print(converted_str)
```
然后就是转16进制，再转成汉字：
```python
#转16进制
def bin_to_hex(bin_str):
    bin_parts = bin_str.split()
    hex_str = ""
    for bin_part in bin_parts:
        decimal_value = int(bin_part, 2)
        hex_str += format(decimal_value, '02X') + " "
    return hex_str.strip()
bin_str = input()
hex_str = bin_to_hex(bin_str)
print(hex_str)
```
```python
#转汉字
def hex_binary_to_string(hex_binary_string):
    hex_groups = hex_binary_string.split()
    unicode_string = ""
    for hex_group in hex_groups:
        unicode_code = int(hex_group, 16)
        unicode_string += chr(unicode_code)
    return unicode_string
hex_binary_result=input()
recovered_string = hex_binary_to_string(hex_binary_result)
print(recovered_string)
```
合并后的代码：
```python
#嗯呢转二进制
original_str = input()
converted_str = original_str.replace("嗯", "1").replace("呢", "0")
#二进制转十六进制
def bin_to_hex(bin_str):
    bin_parts = bin_str.split()
    hex_str = ""
    for bin_part in bin_parts:
        decimal_value = int(bin_part, 2)
        hex_str += format(decimal_value, '02X') + " "
    return hex_str.strip()
bin_str = converted_str
hex_str = bin_to_hex(bin_str)
#16转汉字
def hex_binary_to_string(hex_binary_string):
    hex_groups = hex_binary_string.split()
    unicode_string = ""
    for hex_group in hex_groups:
        unicode_code = int(hex_group, 16)
        unicode_string += chr(unicode_code)
    return unicode_string
hex_binary_result = hex_str
recovered_string = hex_binary_to_string(hex_binary_result)
print(recovered_string)
input()
```
代码解释就是上面的解释反过来,没啥好说的.

#### 效果:
```
C:\Users\Administrator\Desktop>汉字转邦布语.exe
原神启动!11
嗯呢嗯呢呢嗯嗯嗯呢呢嗯嗯嗯嗯嗯 嗯嗯嗯嗯呢呢嗯呢嗯呢嗯嗯嗯嗯呢 嗯呢嗯呢嗯呢呢呢呢嗯呢嗯嗯嗯嗯 嗯呢嗯呢呢嗯呢嗯呢嗯呢嗯呢 呢呢 嗯呢呢呢呢嗯 嗯嗯呢呢呢嗯 嗯嗯呢呢呢嗯

C:\Users\Administrator\Desktop>邦布语转汉字.exe
嗯嗯嗯嗯嗯嗯呢嗯嗯呢嗯嗯呢呢嗯 嗯呢呢嗯嗯嗯呢呢呢嗯呢嗯呢嗯呢 嗯呢呢呢嗯嗯呢嗯呢嗯呢嗯嗯嗯嗯呢 嗯呢嗯呢嗯呢呢呢呢嗯呢呢 嗯嗯嗯 嗯呢嗯呢呢呢 嗯嗯嗯呢呢呢嗯 嗯嗯嗯呢嗯嗯嗯 嗯嗯嗯呢呢呢嗯
给个赞吧(qwq
```

**绝区零启动11111111**
# 完
**_~~代码送你们啦/~~_**
