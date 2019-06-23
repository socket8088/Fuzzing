#!/usr/bin/env python
# Author: Xavi Bel
# Webpage: xavibel.com
# Date: 23/06/2019
# BooFuzz HTTP fuzzing template

from boofuzz import *
import time

def main():
    session = Session(
	sleep_time=10,
        target=Target(
            connection=SocketConnection("192.168.1.99", 7510, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    #with s_block("Request-Line"):
    s_static("GET /topology/index.html HTTP/1.1\r\n")

    # Host
    s_static("Host", name='host-string')
    s_delim(":")
    s_delim(" ")
    s_string("192.168.1.99",  name='host-ip-address')
    s_delim("\r\n")

    # Other headers
    s_static("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0\r\n")
    s_static("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n")
    s_static("Accept-Language: en-US,en;q=0.5\r\n")
    s_static("Accept-Encoding: gzip, deflate\r\n")
    s_static("Connection: keep-alive\r\n")

    s_static("\r\n", "Request-CRLF")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
	main()
