# cotoutines declared with the async/await syntax is the preffered way of writing asyncio app
# here below small hello world problem 
# yield to give output
import asyncio
async def main():
	print("hello ")
	await asyncio.sleep(10)
	print("world")

asyncio.run(main())

# To run a coroutine, asyncio provieds three mechanisms
# 1) asyncio.run() fun to run the top-level entry point "main()" fun

import asyncio
import time

async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(what)

async def main():
	print("started at {}".format(time.strftime('%X')))
	await say_after(4, "hello")
	await say_after(4, "world")

	print("finished at {}".format(time.strftime('%X')))

asyncio.run(main())

#The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
async def main():
	task1 = asyncio.create_task(
		say_after(1, 'hello'))

	task2 = asyncio.create_task(
		say_after(2, 'world'))

	print(f"started at {time.strftime('%X')}")

	# Wait until both tasks are completed (should take
	# around 2 seconds.)
	await task1
	await task2

	print(f"finished at {time.strftime('%X')}")