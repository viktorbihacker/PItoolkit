import platform
import subprocess


def ping():
    host = input(str("Host: "))
    packet_number = input(str("Number of packets (default=4): "))
    param = '-n' if system_info() == 'windows' else '-c'
    command = ['ping', param, packet_number if packet_number != "" else "4", host]
    return call_command(command)


def traceroute():
    host = input(str("Host: "))
    command = ['tracert', host] if system_info() == 'windows' else ['traceroute', host]
    return call_command(command)


def dns_lookup():
    dns = input(str("DNS: "))
    command = ['nslookup', dns]
    return call_command(command)


def system_info():
    return platform.system().lower()


def call_command(command):
    return subprocess.call(command) == 0
