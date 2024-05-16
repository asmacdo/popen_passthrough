import subprocess
import sys
import threading
import selectors
import os


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


def stream_output(proc, selector, tee):
    while True:
        # Select file descriptors that are ready for reading
        for key, _ in selector.select():
            data = os.read(key.fd, 4096)
            if not data:
                # If no data is read, unregister the file descriptor
                selector.unregister(key.fd)
                continue
            tee.write(data)

        # Check if the process has terminated
        if proc.poll() is not None:
            # If the process has terminated, check if there is any more data to read
            if not any(selector.get_map()):
                break


def execute_command(command, output_file):
    with open(output_file, 'wb') as file:  # Open in binary mode
        tee = Tee(sys.stdout.buffer, file)

        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, bufsize=0
        )

        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ)
        selector.register(process.stderr, selectors.EVENT_READ)

        # Single thread handles both stdout and stderr
        output_thread = threading.Thread(target=stream_output, args=(process, selector, tee))
        output_thread.start()

        process.wait()
        output_thread.join()


if __name__ == "__main__":
    command = "./test_script.py"  # Replace with your shell command
    output_file = "output.log"  # Replace with your desired output file path
    execute_command(command, output_file)
