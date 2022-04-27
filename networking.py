import platform
import subprocess


def ping():
    host = input(str("Host: "))
    packet_number = input(str("Number of packets (default=4): "))
    param = '-n' if system_info() == 'windows' else '-c'
    command = ['ping', param, packet_number if packet_number != "" else "4", host]
    return subprocess.call(command) == 0


def traceroute():
    pass


def system_info():
    return platform.system().lower()
