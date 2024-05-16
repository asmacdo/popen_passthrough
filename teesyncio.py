#!/usr/bin/env -S python3 -u
import asyncio
import sys

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, data):
        for f in self.files:
            f.write(data)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

async def stream_subprocess_output(stream, tee):
    while True:
        line = await stream.readline()
        if not line:
            break
        tee.write(line)

async def execute_command(command, output_file):
    process = await asyncio.create_subprocess_exec(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    with open(output_file, 'wb') as file:
        tee_stdout = Tee(sys.stdout.buffer, file)
        tee_stderr = Tee(sys.stderr.buffer, file)

        await asyncio.gather(
            stream_subprocess_output(process.stdout, tee_stdout),
            stream_subprocess_output(process.stderr, tee_stderr)
        )

    await process.wait()


command = "./test_script.py"  # Replace with your shell command
output_file = "output.log"  # Replace with your desired output file path

asyncio.run(execute_command(command, output_file))
