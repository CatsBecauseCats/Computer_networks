import sys
import subprocess


def print_cmd(cmd):
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode("utf-8"))


def active_connection(os_name):
    print(os_name)
    if os_name == "darwin":
        print_cmd("arp -a")
        print_cmd("ndp -an")
    elif os_name == "win32":
        print_cmd("arp -a inet_addr")


def stats(os_name):
    if os_name == "darwin":
        print_cmd("netstat -s")
    elif os_name == "win32":
        print_cmd("netsh interface ipv4 show ipstats")
        print_cmd("netsh interface ipv6 show ipstats")


def main():
    active_connection(sys.platform)
    stats(sys.platform)


if __name__ == "__main__":
    main()