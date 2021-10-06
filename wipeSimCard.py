import sys
import time
import serial
import serial.tools.list_ports

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 {} <port>".format(sys.argv[0]))
        return

    port = sys.argv[1]
    ser = serial.Serial(port, 115200, timeout=1)
    time.sleep(2)
    ser.write(b'AT+CPBS="SM"\r\n')
    ser.write(b'AT+CPBW=1,"",7\r\n')
    time.sleep(2)
    ser.close()
    print("Done!")


if __name__ == "__main__":
    main()