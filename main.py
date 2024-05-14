#!/usr/bin/env python
import subprocess
from pathlib import Path
import sys
import threading
import time

OUTFILE = "stdout"
ERRFILE = "stderr"


def tail_file(file, buffer, stop_event):
    while not stop_event.is_set():
        line = file.read()
        if not line:
            time.sleep(0.01)
            continue
        buffer.write(line)
        buffer.flush()
    buffer.flush()


def main():
    out_file_path = Path(OUTFILE)
    err_file_path = Path(ERRFILE)
    if out_file_path.exists():
        out_file_path.unlink()
    out_file_path.touch()
    if err_file_path.exists():
        err_file_path.unlink()
    err_file_path.touch()

    with open(OUTFILE, "rb") as out_readfile, open(ERRFILE, "rb") as err_readfile:
        out_stop = threading.Event()
        out_thread = threading.Thread(target=tail_file, args=(out_readfile, sys.stdout.buffer, out_stop))
        out_thread.start()
        err_stop = threading.Event()
        err_thread = threading.Thread(target=tail_file, args=(err_readfile, sys.stderr.buffer, err_stop))
        err_thread.start()

        with open(OUTFILE, "wb") as out_writefile, open(ERRFILE, "wb") as err_writefile:
            process = subprocess.Popen(
                ["./test_script.py"],
                stdout=out_writefile,
                stderr=err_writefile,
                bufsize=0,
            )
            process.wait()
            out_stop.set()
            err_stop.set()
            out_thread.join()
            err_thread.join()



if __name__ == '__main__':
    main()
