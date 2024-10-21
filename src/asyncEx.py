import asyncio


async def main():
    print("main function")
    task1 =  asyncio.create_task(foo("g"))
    task2 = asyncio.create_task(foo2())


    print("before await")
   

async def foo(text):
    print("foo1")
    # await asyncio.sleep(1)
    print("after sleep")

async def foo2():
    await asyncio.sleep(2)
    print("foo2")


asyncio.run(main())
print("outside function await")