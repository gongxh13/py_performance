import asyncio
import websockets
import time
import threading

async def send_data(uri, interval, message_size, num_messages):
    async with websockets.connect(uri) as websocket:
        message = "x" * message_size  # 创建一个指定大小的消息
        for i in range(num_messages):
            await websocket.send(message)
            print(f"Sent message {i+1}/{num_messages}")
            await asyncio.sleep(interval / 1000)  # 间隔是以毫秒为单位的，所以除以1000转换成秒

def start_send_data(uri, interval, message_size, num_messages): 
    asyncio.run(send_data(uri, interval, message_size, num_messages))

async def main():
    uri = "ws://localhost:8765"
    interval = 1  # 每隔20毫秒
    message_size = 1024  # 每条消息1KB
    num_messages = 1000  # 发送70条消息
    concurrent_number = 10
    start_time = time.time()

    threads = []
    for _ in range(concurrent_number):
        thread = threading.Thread(target=start_send_data, args=(uri, interval, message_size, num_messages))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    total_time = time.time() - start_time
    print(f"Total time to send {num_messages} messages: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
    start_time = time.time()
    for _ in range(1000):
        time.sleep(1/1000)
    print(f"Total cost {time.time() - start_time} seconds.")