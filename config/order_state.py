import requests
f = open("E:\\OMS-automation\\config\\test.txt",encoding = "utf-8")
#输出读取到的数据
# print(f.read())
orderid = f.read()
print(orderid)

def Order_status():
    Order_information = "STATUS=58&ORDERCODE=abc&ORDERFROM=105&ORDERTYPE=order&NAME=骑手姓名&PHONE=15022220000"
    new_order_information = Order_information.replace('abc', orderid)
    # !/usr/bin/python
    str_a = new_order_information
    # str_a = Order_information
    d = dict(i.split("=") for i in str_a.split("&"))
    print(d)
    x = sorted(d.keys())
    # print(x)
    y = sorted(d.items(), key=lambda x: x[0])
    # print(y)
    str_x = ''
    for aa, bb in y:
        str_x = str_x + aa + bb
    # print(str_x)
    import hashlib
    import base64
    def md5_base64_byte(string):
        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        # 二进制数据字符串值
        md5_str = m.digest()
        b64_str = base64.b64encode(md5_str)
        return b64_str.decode('utf-8')

    def md5_base64_hex(string):
        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        # 十六进制数据字符串值
        md5_str = m.hexdigest()
        b64_str = base64.b64encode(md5_str.encode('utf-8'))
        return md5_str, b64_str.decode('utf-8')

    string = str_x
    # print('二进制数据字符串值：', md5_base64_byte(string))
    transformation = md5_base64_byte(string)
    """
    str.replace(old, new[, max])
    old -- 将被替换的子字符串。
    new -- 新字符串，用于替换old子字符串。
    max -- 可选字符串, 替换不超过 max 次
    """
    temp_str = transformation
    # print(temp_str.replace('=','-').replace('+','_').replace('/','|').replace('\\','|'))
    sing_in = ('&Sign=' + temp_str.replace('=', '-').replace('+', '_').replace('/', '|').replace('\\', '|'))
    print(new_order_information + sing_in)
    # ，编码的结果中=需要替换成-，+需要替换成_，/需要替换成|，\替换成|
    headers = {"ContentType": "application/x-www-form-urlencoded"}
    Order_information = new_order_information + sing_in
    response = requests.post("http://oms-dev.romens.cloud/API/open/syncstatus/v1", Order_information.encode('utf-8'),
                             headers=headers)
    # response = requests.post("http://oms-dev.romens.cloud/API/omsorder/omsqueryorder/v1", "orderfrom=1&appkey=4138&ordercode=2212388405000583", headers = headers)
    print(response.text)


if __name__ == '__main__':
    Order_status()
