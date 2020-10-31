import requests, serial

URL = 'http://127.0.0.1:8000/' 


ser = serial.Serial("/dev/cu.usbmodem141301", 9600)

print('아두이노 연결 성공')

while True:
    res = None

    try:
        if ser.readable():
           res = ser.readline()
           print(res)
           data = {'data':res}
           response = requests.post(URL, data=data)


    except serial.serialutil.SerialException:
        print("아두이노 연결 실패")
        break
