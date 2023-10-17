#!/usr/bin/python3

import fabric
import invoke
import sys

def make_ip_id_map(ips):
    ip_id_map = {}
    for i in range(len(ips)):
        ip_id_map[ips[i]] = i
    print(ip_id_map)
    return ip_id_map

def print_result(result, ip_id_map):
    print("\n")
    for key, value in result.items():
        id = ip_id_map[key.host]
        print(f"{id}: \n{value.stdout}")

def get_file_name():
    if len(sys.argv) < 2:
        sys.exit("main: usage: s for servers c for clients")
    if sys.argv[1] == "s":
        return "server_ips.txt"
    elif sys.argv[1] == "c":
        return "client_ips.txt"
    else:
        sys.exit("main: invalid input")

def main():
    with open(get_file_name(), "r") as file:
        ips = file.read().split()
    ip_id_map = make_ip_id_map(ips)
    group = fabric.ThreadingGroup(*ips,
                               user="ubuntu",
                               connect_kwargs={"key_filename": "../../../key_pairs/dianadb_kp.pem"})
    while 1:
        command = input("> ")
        try:
            result = group.run(command, hide=False)
            print_result(result, ip_id_map)
        except fabric.exceptions.GroupException as e:
            print(f"\nmain: command failed")

if __name__ == "__main__":
    main()
