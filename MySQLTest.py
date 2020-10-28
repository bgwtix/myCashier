# coding=utf-8
import MySQLdb


def test():
    myDb = MySQLdb.connect(
        host='localhost',
        user='Skyrim',
        passwd='123456789',
        database="myCashier",
        charset='utf8'
    )
    myCursor = myDb.cursor()
    try:
        # # 删除数据表
        # sql = "DROP TABLE cashier"
        # myCursor.execute(sql)
        # # 创建数据表
        # sql = ("CREATE TABLE cashier (goodsID INT"  # 序号
        #        ", price FLOAT"  # 售价
        #        ", Discount FLOAT"  # 折扣-保留参数
        #        ", purchasePrice FLOAT"  # 进价-仅管理员可见
        #        ", remarks VARCHAR(255))"  # 货物说明
        #        )
        # myCursor.execute(sql)
        # 插入一条数据
        sql = """INSERT INTO cashier(goodsID, price, Discount, purchasePrice, remarks)
               VALUES (%s, %s, %s, %s, %s)"""
        val = ("2", "100", "1.0", "90", "第一条数据")
        print(sql % val)
        myCursor.execute(sql, val)


        # 删除查询条件的数据
        # sql = "DELETE FROM cashier WHERE remarks LIKE '%二%数据'"
        # myCursor.execute(sql)

        sql = "SELECT * FROM cashier LIMIT 5 OFFSET 0"
        myCursor.execute(sql)
        myResult = myCursor.fetchone()              # 查询单条
        while myResult is not None:
            print(myResult)
            myResult = myCursor.fetchone()

        # sql = "UPDATE cashier SET remarks = %s WHERE price = %s "       # 更新内容
        # val = ("说明更新测试1", "500.00")
        # myCursor.execute(sql, val)
        #
        # sql = "SELECT * FROM cashier LIMIT 5 OFFSET 0"
        # myCursor.execute(sql)
        # print("当前数据库内容")
        # myResult = myCursor.fetchall()              # 查询全部
        # for r in myResult:
        #     print(r)




        # myCursor.execute("CREATE TABLE customers (goodsID VARCHAR(20), price VARCHAR(10))")
        # 插入一条数据
        # myCursor.execute("insert into customers values('2','Tom','3 year 2 class','9')")

        # 修改查询条件的数据
        # cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

        # 删除查询条件的数据
        # cur.execute("delete from student where age='9'")
        print('创建成功')
    except Exception as e:
        print('创建失败')
        print(e)
    myCursor.close()
    myDb.commit()
    myDb.close()


if __name__ == "__main__":
    test()
