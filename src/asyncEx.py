import asyncio


async def main():
    print("main function")
    task1 = asyncio.create_task(foo("one",1))
    print("between")
    task2 =  asyncio.create_task(foo("two",2))
    # await task1
    # await task2
    print("before await")
   

async def foo(text:str,delay:int):
    print(text)
    await asyncio.sleep(delay)
    print(f"after {text}")

asyncio.run(main())
