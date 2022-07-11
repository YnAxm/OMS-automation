#订单推送
import requests
import time
f = open("E:\\OMS-automation\\config\\test.txt",encoding = "utf-8")
#输出读取到的数据
# print(f.read())
orderid = f.read()
print(orderid)

def order_time():
    import datetime
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %T')
    return now_time
    # print(now_time)

def Order_push():
    # order_id = str(format_time_to_timestamp())
    order_newtime = str(order_time())
    Order_information = "data={\"ORDER\":[{\"ORDERFROM\":\"105\",\"ORDERCODE\":\""+orderid+"\",\"STORECODE\":\"K001\",\"BUYERNAME\":\"雨诺测试\",\"ORDERTYPE\":\"1\",\"ORDERSTATUS\":\"32\",\"PAYTYPE\":\"微信支付\",\"PAYTYPECODE\":\"wxpay\",\"TRANTYPE\":\"u5230u5e97u81eau63d0\",\"RECEIVEADDRESS\":\"山东省青岛市市南区宁夏路288号3号楼\",\"RECEIVERNAME\":\"雨诺\",\"RECEIVEPHONE\":\"18363229723\",\"RECEIVETEL\":\"18363229723\",\"RECEIVEPROVINCE\":\"u5c71u4e1cu7701\",\"RECEIVECITY\":\"u9752u5c9bu5e02\",\"RECEIVEAREA\":\"u9ec4u5c9bu533a\",\"LAT\":\"35.874205\",\"LNG\":\"120.049001\",\"BUYERNOTES\":\"\",\"CREATETIME\":\""+order_newtime+"\",\"PAYTIME\":\""+order_newtime+"\",\"RECEIVEBESTTIME\":\"\",\"POSTFEE\":\"0.00\",\"PACKAGEFEE\":\"0.00\",\"SERVICEFEE\":\"0.00\",\"COUPONSAMOUNT\":0,\"PRODUCTSAMOUNT\":\"1.00\",\"AMOUNT\":1,\"PAYAMOUNT\":1,\"NOTES\":\"\",\"ISPAY\":\"1\",\"ISAUDITABLE\":\"0\",\"ISNEEDINVOICE\":\"0\",\"ISFULLREFUND\":\"0\",\"ISPARTSEND\":\"1\",\"ISOTC\":\"0\",\"OTCPIC\":\"\",\"PICKUPNUMBER\":\"1111111\",\"DELIVERYORDER\":\"\",\"SENDCLASS\":\"0\",\"ORDERINDEX\":\"1\",\"POITRANSCOUPON\":\"0\",\"REALPOSTFEE\":\"0.00\",\"COUPONSAMOUNT_ORIGIN\":0,\"PRODUCTSAMOUNT_ORIGIN\":\"1.00\",\"ORDERAMOUNT\":1,\"REALPAYAMOUNT\":1,\"USEPOINTS\":\"0\",\"ISGROUP\":\"0\",\"MEMBERSHIPCODE\":\"wx000001\",\"MERCHANTID\":\"305232814203\",\"WXPAYID\":\"4200000835202101175509309204\",\"RESERVEFIELD4\":\"\"}],\"GOODS\":[{\"ORDERGUID\":\"DABDD42A-BC82-0A5E-54B6-F6248F2DC7A8\",\"ORDERCODE\":\"order_numbers\",\"GOODSGUID\":\"209-007378\",\"GOODSCODE\":\"007378\",\"GOODSNAME\":\"u8368u9ebbu75b9u4e38uff08u9f99u4ed5u5eb7uff09\",\"BUYCOUNT\":\"1\",\"GOODSPRICE\":\"1.00\",\"DISCOUNTPRICE\":\"1.0000\",\"GOODSAMOUNT\":\"1.0000\",\"ISGIFT\":\"0\",\"ISOTC\":\"0\",\"BUYERNOTES\":\"\",\"SELLERNOTES\":\"\",\"ISPART\":\"1\",\"SHOWPRICE\":\"1.00\",\"PLATPRICE\":\"1.00\"}],\"FEE_DETAIL\":[{\"ORDERGUID\":\"DABDD42A-BC82-0A5E-54B6-F6248F2DC7A8\",\"ORDERCODE\":\"202205300003\",\"FEECODE\":\"wxpay\",\"FEENAME\":\"u5faeu4fe1u652fu4ed8\",\"AMOUNT\":\"1.00\",\"FEETYPE\":\"1\",\"PAYODERENO\":\"4200000835202101175509309204\",\"PAYBATCHNO\":\"305232814203\",\"POICHARGE\":\"0.00\",\"EXTINFO\":\"\"}],\"INVOICE\":[]}"
    #!/usr/bin/python
    str_a = Order_information
    d = dict(i.split("=") for i in str_a.split("&"))
    print(d)
    #print(d.get('ORDERCODE'))

    x = sorted(d.keys())
    #print(x)
    y = sorted(d.items(),key=lambda x:x[0])
    #print(y)
    str_x = ''
    for aa ,bb in y:
        str_x = str_x + aa + bb
    #print(str_x)
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
    #print('二进制数据字符串值：', md5_base64_byte(string))
    transformation = md5_base64_byte(string)
    temp_str = transformation
    #print(temp_str.replace('=','-').replace('+','_').replace('/','|').replace('\\','|'))
    sing_in =('&Sign='+temp_str.replace('=','-').replace('+','_').replace('/','|').replace('\\','|'))
    # print(str_a + sing_in)
    # ，编码的结果中=需要替换成-，+需要替换成_，/需要替换成|，\替换成|
    headers={"ContentType":"application/x-www-form-urlencoded"}
    Order_information=Order_information+sing_in
    response = requests.post("http://oms-dev.romens.cloud/API/order/neworder/v1",Order_information.encode('utf-8'),headers = headers)
    #response = requests.post("http://oms-dev.romens.cloud/API/omsorder/omsqueryorder/v1", "orderfrom=1&appkey=4138&ordercode=2212388405000583", headers = headers)
    print(response.text)
if __name__ == '__main__':
    Order_push()