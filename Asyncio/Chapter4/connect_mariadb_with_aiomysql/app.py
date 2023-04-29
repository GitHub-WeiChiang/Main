import asyncio
import aiomysql


async def main():
    # 建立与数据库的连接
    conn: aiomysql.Connection = await aiomysql.connect(
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )

    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()

    # 执行一条 sql 语句，返回值是影响的数据的条数
    effected = await cur.execute(
        "INSERT INTO `student` (`student_name`, `student_age`) "
        "VALUES ('小云', 10);"
    )

    print(effected)

    # 将更改提交到数据库
    await conn.commit()

    # 关闭 cursor 对象
    await cur.close()

    # 关闭连接对象
    conn.close()


if __name__ == '__main__':
    # 若使用 PyCharm 執行，
    # 這裡會報 RuntimeError: Event loop is closed 錯誤。
    asyncio.run(main())

    # 解決方法 1
    # just delete two line of code in aiomysql/sa/result.py,
    # the code works fine! The code info:
    # 116: assert dialect.case_sensitive, \
    # 117: "Doesn't support case insensitive database connection"

    # # 解決方法 2
    # # 改用下方寫法
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
