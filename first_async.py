import asyncio


async def task_1():
    print("1")
    await asyncio.sleep(2)
    print("2")


def task_2():
    print("3")
    print("4")


async def main():
    t1 = asyncio.create_task(task_1())  # запуск на фоне
    await asyncio.sleep(0)  # переключили руки
    task_2()
    await t1  # дождались окончания task_1


asyncio.run(main())
