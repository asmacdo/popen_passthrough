#!/usr/bin/env python3
import argparse
import sys
import time


def main(duration):
    print("Printing something to STDOUT at start")
    print("Printing something to STDERR at start", file=sys.stderr)
    for i in range(duration):
        print(f"out: {i}")
        print(f"err: {i}", file=sys.stderr)
        time.sleep(1)
    print("Printing something to STDOUT at finish")
    print("Printing something to STDERR at finish", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--duration", type=int, default=5, help="Duration to run the test in seconds."
    )

    args = parser.parse_args()
    main(args.duration)
