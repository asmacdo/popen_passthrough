#!/usr/bin/env python
import subprocess
import sys


def stream_and_capture_output(args):
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,  # No internal buffering
    )

    # Read stdout and stderr in real-time
    while True:
        out_line = process.stdout.readline()
        err_line = process.stderr.readline()
        if out_line:
            sys.stdout.buffer.write(out_line)
            sys.stdout.buffer.flush()
        if err_line:
            sys.stderr.buffer.write(err_line)
            sys.stderr.buffer.flush()
        if process.poll() is not None:
            break

    # Capture any remaining output after the process has exited
    for out_line in process.stdout:
        sys.stdout.buffer.write(out_line)
        sys.stdout.buffer.flush()
    for err_line in process.stderr:
        sys.stderr.buffer.write(err_line)
        sys.stderr.buffer.flush()


if __name__ == '__main__':
    print("============= python -u (unbuffered)")
    stream_and_capture_output(
        ["python3", "-u", "./test_script.py", "--duration", "5"],
    )
    print("=============")
    print("---------------  direct execution ---------------")
    stream_and_capture_output(
        ["./test_script.py", "--duration", "5"],
    )
    print("------------------------------")
