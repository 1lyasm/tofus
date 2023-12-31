#!/usr/bin/python3

import subprocess
import select

def main():
    addr_list = [
            "127.0.0.1:6789",
            "127.0.0.2:6789",
            "127.0.0.3:6789",
            "127.0.0.4:6789",
            "127.0.0.5:6789",
            "127.0.0.6:6789"
            ]
    i = 0
    for addr in addr_list:
        cmd_str = f"../target/debug/diserver {addr} ... > S{i}.log &"
        # print(f"cmd_str: {cmd_str}")
        subprocess.run(cmd_str, shell=True)
        i += 1
    subprocess.run(["wait"], shell=True)

if __name__ == "__main__":
    main()
