import asyncio

async def nested():
    print(2)
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    print(1)
    task = asyncio.create_task(nested())
    print(3)

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await asyncio.sleep(1)
    await task

    print(4)

# asyncio.run(main())

if __name__ == '__main__':
    print(0)
    asyncio.run(main())