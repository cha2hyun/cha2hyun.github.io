# requests 테스트

def request_test():
    import requests
    import time
    start = time.time()
    cnt = 50
    for i in range(1, cnt + 1):
        url = f"http://127.0.0.1:8002/test/{i}"
        res = requests.get(url)        
        print(f"{i}] status code -> {res.status_code}")
    total = round(time.time() - start, 4)
    average = round(total/cnt, 4)
    print(f"Total -> {total}sec")
    print(f"Avg -> {average}sec")

def grequest_test():
    import grequests
    import time
    cnt = 100
    urls = [f"http://127.0.0.1:8002/test/{i}" for i in range(1, cnt+1)]
    start = time.time()
    rs = (grequests.get(u) for u in urls)
    print(grequests.map(rs))    
    total = round(time.time() - start, 4)
    average = round(total/cnt, 4)
    print(f"Total -> {total}sec")
    print(f"Avg -> {average}sec")



import asyncio
import time
from aiohttp import ClientSession

async def aiohttp_test(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

cnt = 100
start = time.time()
loop = asyncio.get_event_loop()
coroutines = [aiohttp_test(f'http://127.0.0.1:8002/test/{i}') for i in range(cnt)]
result = loop.run_until_complete(asyncio.gather(*coroutines))
# print(result)
total = round(time.time() - start, 4)
average = round(total/cnt, 4)
print(f"Total -> {total}sec")
print(f"Avg -> {average}sec")

