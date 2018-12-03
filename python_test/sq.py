import pymysql

# 初始化连接配置
ConnectConfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'Zh13102030032',
    'charset': 'utf8',
}

# 创建连接对象
db = pymysql.connect(
    host=ConnectConfig['host'],
    port=ConnectConfig['port'],
    user=ConnectConfig['user'],
    passwd=ConnectConfig['passwd'],
    charset=ConnectConfig['charset'],
)

# 创建游标对象
cursor = db.cursor()
cursor.execute('show databases')
rows = cursor.fetchall()
flag = False
name = "test"
'''
for row in rows:
    tmp = ''.join(row)
# 判断数据库是否存在
    if name == tmp:
        flag=True
        break
if flag:
'''
cursor.execute('create database if not exists ' + name)
# 如果没有数据库则创建
cursor.execute('use ' + name)
# 创建数据表
cursor.execute("create table people(name char(30),job char(10),pay int(4));")
# 添加记录
cursor.execute('insert into people values(%s,%s,%s);',
               ('Bob', 'dev', 50000))  # 或者也可以一次性添加多条记录
rows = [('Sue', 'mus', 70000), ('Ann', 'adm', 60000)]
cursor.executemany('insert into people values(%s,%s,%s);', rows)
# 查询people表中所有记录
cursor.execute('select * from people')
result = cursor.fetchall()
for row in result:
    print(row)
# 更新people表中职务为adm的人员工资增加12000
cursor.execute('update people set pay=pay+12000 where job="adm"')
cursor.execute('select * from people where job="adm"')
result = cursor.fetchall()
print(result)
# 删除people表中姓名为Bob的记录
cursor.execute('delete from people where name="Bob"')
cursor.execute('select * from people')
result = cursor.fetchall()
for row in result:
    print(row)
# 操作完成后还需要进行事务提交以便数据库保存
db.commit()
# 此外连接对象还有事务回滚操作：db.rollback()
# 最后关闭游标对象和连接对象
cursor.close()
db.close()
