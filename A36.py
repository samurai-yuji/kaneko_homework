def is_ip_number(ips):
    if len(ips) == 4:
        for ip in ips:
            try:
                int(ip) 
            except e:
                return False
    else:
        return False

    return True

def is_ip_range(ips):
    for ip in ips:
        if 0 <= int(ip) and int(ip) <= 255:
            pass
        else:
            return False
    return True

def is_correct_ip_format(ip):

    ips = ip.split(".")

    if not is_ip_number(ips):
        return False

    if not is_ip_range(ips):
        return False

    return True

print(is_correct_ip_format("192.168.0.1"))
print(is_correct_ip_format("192.168.0.1."))
print(is_correct_ip_format("192.168.0.1000"))
print(is_correct_ip_format("192.168.1"))
print(is_correct_ip_format("192.168.0.0.1"))
