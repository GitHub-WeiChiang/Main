import asyncio
import aiomysql


async def print_all_data(cur):
    await cur.execute(
        "SELECT * FROM `student` WHERE id>0;"
    )

    # 获取原始数据结果
    raw_data = await cur.fetchall()

    # 计算字段个数
    field_range = range(len(cur.description))

    # 将字段名与原始结果映射生成对象数组
    result = [
        {cur.description[i][0]: row[i] for i in field_range}
        for row in raw_data
    ]

    print(result)


async def main():
    # 创建连接池
    pool: aiomysql.Pool = await aiomysql.create_pool(
        minsize=0, maxsize=10,
        host='127.0.0.1', port=3306, user='root', password='pwd', db='mydb'
    )

    # 启用一个连接
    conn: aiomysql.Connection = await pool.acquire()
    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()

    await print_all_data(cur)

    await cur.execute(
        "UPDATE `student` SET "
        "`student_name` = '小云加', "
        "`student_age` = '22' "
        "WHERE `id` = '1';"
    )

    await print_all_data(cur)

    await cur.execute(
        "DELETE FROM `student` WHERE `id` = '1';"
    )
    await print_all_data(cur)

    # 将更改提交到数据库
    await conn.commit()
    # 关闭 cursor 对象
    await cur.close()
    # 释放一个连接
    pool.release(conn)

    pool.close()

    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
