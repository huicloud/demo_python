#!/usr/bin/env python3

from dzhua_pb2 import UAResponse
from MSG_pb2 import MSG
from urllib.request import urlopen
import snappy
import io


host = "http://v2.yundzh.com"

token = "00000003:1472274774:9730aa8b8b4d36e3fc4752b2d6f54583c20ec2ba"

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
        dst = io.BytesIO()
        snappy.stream_decompress(urlopen(url), dst)
        data = dst.getvalue()
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

