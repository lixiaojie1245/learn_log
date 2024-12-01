import mysql.connector

# 创建数据库连接
db = mysql.connector.connect(
    host="localhost",  # MySQL服务器地址
    user="root",   # 用户名
    password="asdfasdf",  # 密码
    database="mydatabase"  # 数据库名称
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()


try:
    # 创建一个名为"customers"的数据表
    cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
except:
    print("customers is exists")

# 插入一条记录到"customers"表中
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = ("John Smith", "123 Main St")
cursor.execute(sql, values)

# 提交更改到数据库
db.commit()

print(f"插入了 {cursor.rowcount} 条记录")

# 查询所有记录
cursor.execute("SELECT * FROM customers")

# 获取查询结果
results = cursor.fetchall()

for row in results:
    print(row)

# 更新"customers"表中id为1的记录
sql = "UPDATE customers SET address = %s WHERE id = %s"
values = ("456 Elm St", 1)
cursor.execute(sql, values)

# 提交更改到数据库
db.commit()

print(f"更新了 {cursor.rowcount} 条记录")


# 删除"customers"表中id为1的记录
sql = "DELETE FROM customers WHERE id = %s"
values = (1,)
cursor.execute(sql, values)

# 提交更改到数据库
db.commit()

print(f"删除了 {cursor.rowcount} 条记录")


try:
    db.start_transaction()
    # 执行一系列SQL操作
    cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Alice", "789 Oak St"))
    cursor.execute("UPDATE customers SET address = %s WHERE id = %s", ("789 Elm St", 2))
    db.commit()  # 提交事务
except:
    db.rollback()  # 事务回滚，撤销之前的操作


cursor.close()  # 关闭游标
db.close()  # 关闭数据库连接


