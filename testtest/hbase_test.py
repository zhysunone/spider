# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/13 13:44"

import happybase
from happybase_monkey.monkey import monkey_path;monkey_path()


conn = happybase.Connection("", )
# conn.delete_table("testtest", True)
# conn.create_table('zhy', {"info":{}})

table = conn.table("")

# print conn.tables()
def write_data_to_db():

    count = 1
    for key,value in table.scan():
        print key
        print "***" * 100
        print value
        print "***"*100
        count += 1
    print(count)


# if __name__ == '__main__':
#     write_data_to_db()


# hbase测试

# print conn.tables()
#
# table.put("test2", {"info:data":"1111111"})
# table.put("test2", {"info:content":"2222222"})

# row = table.row("")
# print row["info:content"]


















