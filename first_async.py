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

    t3 = asyncio.create_task(task_3())  # планируем еще одну задачу

    t2 = asyncio.create_task(task_2())  # планируем третью задачу

    # event loop сам переключает задачи, ведь внутри каждой
    # задачи мы прописали await - точки передачи управления event loop 

    await asyncio.gather(t1, t3, t2)  # ждем завершения всех задач


asyncio.run(main())
