import re

def is_correct_ip_format(ip):
    if re.match("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",ip):
        return True
    else:
        return False

print(is_correct_ip_format("192.168.0.1"))
print(is_correct_ip_format("192.168.0.1."))
print(is_correct_ip_format("192.168.0.1000"))
print(is_correct_ip_format("192.168.1"))
print(is_correct_ip_format("192.168.0.0.1"))
