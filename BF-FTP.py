#!/usr/bin/env python
# Autor: Xavi Bel
# Website: xavibel.com
# Date: 23/06/2019
# BooFuzz FTP fuzzing template
from boofuzz import *
import time

def main():
        session = Session(
                sleep_time=10,
                target=Target(
                        connection=SocketConnection("192.168.1.99",69,proto='udp')
                ),
        )


        s_initialize("write")
        s_static("\x00\x02")
        s_string("filename")
        s_static("\x00")
        s_static("netascii")
        s_static("\x00")

        session.connect(s_get('write'))
        session.fuzz()

if __name__ == "__main__":
        main()
