import asyncio
import sys

async def _print_stream(stream):
    while True:
        line = await sys.stdout.buffer.read()
        if line:
            print(line.decode(), end="")
        else:
            break



async def _stream_subprocess():
    process = await asyncio.create_subprocess_exec("./test_script.py")

    await asyncio.gather(
        _print_stream(sys.stdout.buffer),
        _print_stream(sys.stdout.buffer)
    )
    return await process.wait()


def execute():
    loop = asyncio.get_event_loop()
    rc = loop.run_until_complete(_stream_subprocess())
    loop.close()
    return rc

if __name__ == '__main__':
   execute()
