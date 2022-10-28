import socket
from getmac import  get_mac_address
host=socket.gethostname()
ip=socket.gethostbyname(host)
print("MY IP ADDRESS IS:",ip)
mac_add=get_mac_address()
print(f"MAC ADDRESS IS:{mac_add}")
