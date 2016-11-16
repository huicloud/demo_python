#!/usr/bin/env python3

from dzhua_pb2 import UAResponse
from MSG_pb2 import MSG
from urllib.request import urlopen
import snappy
import io


host = "http://gw.yundzh.com"

# replace to your's token
token = "00000003:1474968294:796afc42045d9886729f8acd872fa2b0507590e9"

def build_url(service, params, compress=False, binary=True):
    buff = []
    if params != None:
        params["token"] = token
    else:
        params = {"token":token}

    if compress:
        params["compresser"] = "snappy"

    if binary:
        params["output"] = "pb"
    else:
        params["output"] = "json"

    for k, v in params.items():
        buff.append(k + "=" + v)

    return host + service + "?" + "&".join(buff)



def demo_get(service, params, compress=False):
    url = build_url(service, params, compress)

    print("REQ:")
    print(url)

    ua = UAResponse()
    msg = MSG()


    print()

    print("RESP:")

    if compress:
        data = snappy.decompress(urlopen(url).read())
    else:
        data = urlopen(url).read()


    ua.ParseFromString(data)
    if ua.Err == 0:
        msg.ParseFromString(ua.Data)

        # TODO: handle msg here
        print(msg) 
    else:
        print(ua)


demo_get("/quote/dyna", {"obj":"SH600000"}, True)
demo_get("/quote/dyna", {"obj":"SH600000"}, False)

