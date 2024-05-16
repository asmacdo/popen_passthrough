#!/usr/bin/env python
import os
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
    fast_stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)
    fast_stderr = os.fdopen(sys.stderr.fileno(), 'wb', 0)
    while True:
        out = process.stdout.read()
        err = process.stderr.read()
        if out:
            print("HI")
            fast_stdout.write(out)
            fast_stdout.flush()
        if err:
            fast_stderr.write(err)
            fast_stderr.flush()
        if process.poll() is not None:
            break
    fast_stdout.close()
    fast_stdout.close()

    # Capture any remaining output after the process has exited
    # for out_line in process.stdout:
    #     fast_stdout.write(out)
    #     fast_stderr.flush()
    # for err_line in process.stderr:
    #     fast_stderr.write(err_line)
    #     fast_stderr.flush()


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
