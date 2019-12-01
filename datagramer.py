import serial

def datagramize(number: int, offset=0, address=0):
    number_str: str = str(number)
    byte_arr: bytearray = bytearray(len(number_str) + 6)
    byte_arr[0] = 0xaa                  # starting byte
    byte_arr[1] = 0x56                  # mode
    byte_arr[2] = len(number_str) - 1   # data length
    byte_arr[3] = offset                # offset
    byte_arr[4] = address               # address
    sum: int = 0
    for i in range(len(number_str)):    # data
        byte_arr[5+i] = int(number_str[i]) + 0x30
        sum = sum + byte_arr[5+i]
    sum = sum % 0x100
    byte_arr[5+len(number_str)] = sum   # check sum
    return byte_arr

def datagramize2(number: int, offset=0, address=0):
    number_str: str = str(number)
    byte_arr: bytearray = bytearray(13)
    byte_arr[0] = 0xfe                  # starting byte
    byte_arr[1] = address               # address
    j = -(10 - len(number_str) - offset)
    for i in range(10):                 # data
        if j < 0:
            byte_arr[2+i] = 0x0a
        elif j < len(number_str):
            byte_arr[2+i] = int(number_str[j])
        else:
            byte_arr[2+i] = 0x0a
        j = j + 1
    byte_arr[12] = 0x8f
    return byte_arr

def show_error(err_no):
    send(err_no)

def send(number):
    a = datagramize2(number)
    print(a)
    ser = serial.Serial('/dev/serial0', 57600)
    sent = ser.write(a)
    ser.close()
