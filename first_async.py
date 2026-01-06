import asyncio


async def task_1():
    print("задача 1, начали")
    await asyncio.sleep(2)
    print("закончили задачу 1")


async def task_2():
    print("задача 2, начали")
    await asyncio.sleep(2)
    print("закончили задачу 2")


async def task_3():
    print("задача 3, начали")
    await asyncio.sleep(2)
    print("закончили задачу 3")


async def main():
    t1 = asyncio.create_task(task_1())  # планируем задачу в цикл событий
    await asyncio.sleep(0)  # уступили управление, цикл событий может начинать t1

    t3 = asyncio.create_task(task_3())  # планируем еще одну задачу
    await asyncio.sleep(0)  # снова дали управление циклу событий (t1 и t3)

    t2 = asyncio.create_task(task_2())  # планируем третью задачу
    await asyncio.sleep(0)  # опять уступили управление

    await asyncio.gather(t1, t2, t3)  # ждем завершения всех задач


asyncio.run(main())
