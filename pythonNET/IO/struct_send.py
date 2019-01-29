from socket import * 
import struct
s = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',6655)

#与接收方有同样的数据结构
st = struct.Struct('i5sf')
while True:
    id = int(input("id:"))
    name = input("name:")
    height = float(input("height:"))
    data = st.pack(id,name.encode(),height)
    s.sendto(data,ADDR)