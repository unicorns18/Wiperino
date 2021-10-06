import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def get_open_ports():
    ports = get_ports()
    open_ports = []
    for port in ports:
        if port.device != "":
            open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    print(print_open_ports())