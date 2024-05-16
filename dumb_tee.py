#!/usr/bin/env python3
import subprocess


if __name__ == "__main__":
    process = subprocess.Popen(["bash", "-c", "./test_script.py | tee output.log"])
    print("This is a dumb tee.")