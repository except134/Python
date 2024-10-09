import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(5):
        print(f"Силач {name} поднял шар {i+1}")
        await asyncio.sleep(1 / power)
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    s1 = asyncio.create_task(start_strongman('Pasha', 3))
    s2 = asyncio.create_task(start_strongman('Denis', 4))
    s3 = asyncio.create_task(start_strongman('Apollon', 5))
    await s1
    await s2
    await s3

asyncio.run(start_tournament())

