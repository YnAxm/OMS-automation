# 订单推送
import requests
import time

f = open("E:\\OMS-automation\\config\\test.txt", encoding="utf-8")
# 输出读取到的数据
order_newid = f.read()
tk = 'TK'
Chargeback_No = (tk + order_newid)
print(Chargeback_No)


def order_time():
    import datetime
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %T')
    return now_time


def Order_tuidan():
    Chargeback = "data={\"FEE_DETAIL\":[{\"AMOUNT\":\"2.50\",\"FEECODE\":\"JDJKPAY\",\"FEENAME\":\"微信支付\",\"FEETYPE\":\"1\",\"PAYBATCHNO\":\"\",\"PAYODERENO\":\"\",\"RETURNCODE\":\"" + Chargeback_No + "\"}],\"RETURNGOODS\":[{\"BUYERNOTES\":\"\",\"DISCOUNTPRICE\":\"0\",\"GOODSAMOUNT\":\"2.50\",\"GOODSCODE\":\"144595\",\"GOODSNAME\":\"\",\"GOODSPRICE\":\"2.50\",\"GOODSSTATUS\":\"8\",\"ISGIFT\":0,\"RETURNCODE\":\""+ Chargeback_No +"\",\"RETURNCOUNT\":\"1\",\"SELLERNOTES\":\"\"}],\"RETURNORDER\":[{\"APPLYNAME\":\"雨诺\",\"APPLYPHONE\":\"18363229723\",\"CREATETIME\":\"" + order_time() + "\",\"ISFULLREFUND\":\"1\",\"LAT\":\"0\",\"LNG\":\"0\",\"ORDERCODE\":\"" + order_newid + "\",\"ORDERFROM\":\"105\",\"ORDERTYPE\":\"1\",\"PACKAGEFEE\":\"0\",\"POSTFEE\":\"0\",\"PRODUCTSAMOUNT\":\"2.50\",\"RETURNADDRESS\":\"云南昆明市呈贡区洛羊街道一心堂药业集团股份有限公司\",\"RETURNAMOUNT\":\"2.50\",\"RETURNCODE\":\"" + Chargeback_No + "\",\"RETURNPICTURE\":\"\",\"RETURNREASON\":\"不想要了\",\"RETURNSTATUS\":\"120\",\"RETURNTYPE\":\"0\",\"STORECODE\":\"K001\"}]}"
    # !/usr/bin/python
    str_a = Chargeback
    d = dict(i.split("=") for i in str_a.split("&"))
    print(d)
    # print(d.get('ORDERCODE'))

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
    temp_str = transformation
    # print(temp_str.replace('=','-').replace('+','_').replace('/','|').replace('\\','|'))
    sing_in = ('&Sign=' + temp_str.replace('=', '-').replace('+', '_').replace('/', '|').replace('\\', '|'))
    # print(str_a + sing_in)
    # ，编码的结果中=需要替换成-，+需要替换成_，/需要替换成|，\替换成|
    headers = {"ContentType": "application/x-www-form-urlencoded"}
    Transmittal_parameter = Chargeback + sing_in
    response = requests.post("http://oms-dev.romens.cloud/API/order/refund/v1", Transmittal_parameter.encode('utf-8'),
                             headers=headers)
    # response = requests.post("http://oms-dev.romens.cloud/API/omsorder/omsqueryorder/v1", "orderfrom=1&appkey=4138&ordercode=2212388405000583", headers = headers)
    print(response.text)


if __name__ == '__main__':
    Order_tuidan()
