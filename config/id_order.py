import time
def format_time_to_timestamp(format_time=None):
    if format_time:
        time_tuple = time.strptime(format_time, '%Y-%m-%d %X')
        result = time.mktime(time_tuple)
        return int(result)
    return int(time.time())
number_order = str(format_time_to_timestamp())
with open('test.txt','w') as f:
   f.write(number_order)
