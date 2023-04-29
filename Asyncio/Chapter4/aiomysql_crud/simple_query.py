import aiomysql
import asyncio


async def print_all_data(cur):
    # 获取原始数据结果
    raw_data = await cur.fetchall()
    print("raw_data:", raw_data)
    print("raw data type:", type(raw_data))
    print()
    # raw_data: ((1, '小云', 10),)
    # raw data type: <class 'tuple'>

    # 计算字段个数
    field_range = range(len(cur.description))

    # 将字段名与原始结果映射生成对象数组
    result = [
        {cur.description[i][0]: row[i] for i in field_range}
        for row in raw_data
    ]

    print(result)
    # [{'id': 1, 'student_name': '小云', 'student_age': 10}]


async def main():
    # 创建连接池
    pool: aiomysql.Pool = await aiomysql.create_pool(
        minsize=0, maxsize=10,
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )

    # 启用一个连接
    conn: aiomysql.Connection = await pool.acquire()

    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()

    await cur.execute(
        "SELECT * FROM `student` WHERE `id` = '1';"
    )

    print(cur.description)
    print(type(cur.description))
    print()
    # (
    #     ('id', 3, None, 10, 10, 0, False),
    #     ('student_name', 253, None, 2048, 2048, 0, True),
    #     ('student_age', 3, None, 11, 11, 0, True)
    # )
    # <class 'tuple'>

    # print(await cur.fetchall())
    # # ((1, '小云', 10),)

    await print_all_data(cur)

    # 关闭 cursor 对象
    await cur.close()

    # 释放一个连接
    pool.release(conn)
    pool.close()

    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
