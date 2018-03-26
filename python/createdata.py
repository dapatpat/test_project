from faker import Faker
from pymysql import install_as_MySQLdb
install_as_MySQLdb()
f = Faker("zh-CN")
print(f.name())