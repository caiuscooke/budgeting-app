import asyncio
import time

async def make_toast():
    print("starting make_toast()")
    await asyncio.sleep(2)
    print("ending make_toast()")
    return "Bagel toasted"

async def make_coffee():
    print("starting make_cofee()")
    await asyncio.sleep(3)
    print("ending make_coffee()")
    return "Cofee brewed"

async def main():
    start_time = time.time()

    coffee_task = asyncio.create_task(make_coffee())
    toast_task = asyncio.create_task(make_toast())

    result_coffee = await coffee_task
    result_toast = await toast_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"result of make_coffee: {result_coffee}")
    print(f"result of make_toast: {result_toast}")
    print(f"total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())