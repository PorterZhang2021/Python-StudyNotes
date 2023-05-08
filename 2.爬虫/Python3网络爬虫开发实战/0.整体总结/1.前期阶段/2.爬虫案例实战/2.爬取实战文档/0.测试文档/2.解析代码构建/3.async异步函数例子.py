import asyncio
import time

def count():
    print("One")
    time.sleep(1)
    print("two")

def main():
    for _ in range(3):
        count()

main()