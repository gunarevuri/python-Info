# single thread
# to run all these commands you must have python version 3.7++
import asyncio
import aiohttp
import time

async def waiter(n):
	await asyncio.sleep(n)
	print(f"waited for {n} seconds")

async def main():
	task1 = asyncio.create_task(waiter(2))
	task12 = asyncio.create_task(waiter(3))

	print(time.strftime('%X'))
	await task1
	await task12

	print(time.strftime('%X'))

# to run a coroutine as a list must include in await asyncio.gather method

async def fun():
	url =   'http://www.google.com'
	session = aiohttp.ClientSession()
	rep = await session.get(url)
	print(await rep.content.read())
	await session.close()

	
async def fetchfromgoogle():
	print(time.strftime('%X'))
	await asyncio.gather(
		*[
			fetchfromgoogle() for _ in range(100)
]
		)

#-------To get response in synchronous way ------#
async def fetchfromgoogle():
	for i in range(20):
		fun()

if __name__=='__main__':
	asyncio.run(main())
	# asyncio.run(fetchfromgoogle())