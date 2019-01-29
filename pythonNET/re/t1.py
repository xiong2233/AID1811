import re 
import sys

def get_address(port):
    #提取一段内容
    f = open("1.txt")
    while True:
        data = ""
        for line in f:
            if line !="\n":
                data +=line
            else:
                break
        #已经到了文件结尾
        if not data:
            return "Not Found"
        #匹配首单词，查看是否为目标段落
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if PORT == port:
            # pattern = r"address is ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})"   
            pattern = r"address in ((\d{1:3\.}{3}\d{1,3}/\d+|Unkown))"
            address = re.search(pattern,data).group(1)
            return address
if __name__ == "__main__":
    port = sys.argv[1]
    addr = get_address(port)
    print(addr)