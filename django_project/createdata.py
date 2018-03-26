from faker import Faker
import pymysql.cursors
import random

try:
    f = Faker()
    # print (f.name())
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='123456',
                                 db='student_infos',
                                 charset='utf8')
    # cursorclass = pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "INSERT INTO stuInfos VALUES(%d,%s,%d,%s,%d)"
    for i in range(0, 150):
        gender = random.randint(0, 1)
        # print(type(gender))
        # data = int(f.numerify()),f.name(),int(gender),f.name(),int(f.numerify())
        name = '"%s"' % f.name()
        duty = '"%s"' % f.name()
        print(name + "name")
        print(duty + "duty")
        data = (random.randint(0, 100000), name, int(gender), duty, int(f.numerify()))
        cursor.execute(sql % data)
        connection.commit()
finally:
    connection.close()
# print(f.name())
