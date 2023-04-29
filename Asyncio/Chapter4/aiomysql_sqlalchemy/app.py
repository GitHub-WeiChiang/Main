import asyncio
import aiomysql.sa
import sqlalchemy
import aiomysql.sa.result

# 聲明數據表結構
student = sqlalchemy.Table(
    'student', sqlalchemy.MetaData(),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('student_name', sqlalchemy.String(255)),
    sqlalchemy.Column('student_age', sqlalchemy.Integer)
)


async def print_all_data(conn):
    result: aiomysql.sa.result.ResultProxy = await conn.execute(
        student.select()
    )
    all_data = await result.fetchall()
    print(all_data)


async def main():
    engine: aiomysql.sa.Engine = await aiomysql.sa.create_engine(
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )

    conn: aiomysql.sa.SAConnection = await engine.acquire()

    # 增加一条数据
    await conn.execute(student.insert().values(
        student_name='杨阳', student_age=20
    ))
    await print_all_data(conn)

    # 修改一条数据
    await conn.execute(student.update().where(
        student.columns.student_name == '杨阳'
    ).values(student_age=10))
    await print_all_data(conn)

    # 删除一条数据
    await conn.execute(student.delete().where(student.columns.student_name == '杨阳'))
    await print_all_data(conn)
    engine.release(conn)


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
