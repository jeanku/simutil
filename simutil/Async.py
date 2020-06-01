import asyncio


class Async():
    __slots__ = []

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Async, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def run(self, tasks):
        flag = asyncio._get_running_loop()
        if flag:
            loop = asyncio.get_event_loop()
            for index in tasks:
                asyncio.run_coroutine_threadsafe(index, loop=loop)
        else:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()


if __name__ == '__main__':
    async def hello2(index):
        print("number:{}, Hello world!".format(index))
        r = await asyncio.sleep(1)
        print("end!")


    tasks = [hello2(index) for index in range(5)]
    Async.run(tasks)
