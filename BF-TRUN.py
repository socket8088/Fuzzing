#!/usr/bin/env python
# Author: Xavi Bel
# Date: 22/06/2019
# Purpose: 
#	Fuzzing Vulnserver
#	TRUN

from boofuzz import *
import time

def get_banner(target, my_logger, session, *args, **kwargs):
    banner_template = b"Welcome to Vulnerable Server! Enter HELP for help."
    try:
        banner = target.recv(10000)
    except:
        print("Unable to connect. Target is down. Exiting.")
        exit(1)

    my_logger.log_check('Receiving banner..')
    if banner_template in banner:
        my_logger.log_pass('banner received')
    else:
        my_logger.log_fail('No banner received')
        print("No banner received, exiting..")
        exit(1)


def main():

    session = Session(
	sleep_time=1,
        target=Target(
            connection=SocketConnection("192.168.1.99", 9999, proto='tcp')
        ),
    )

    # Setup
    s_initialize(name="Request")
    with s_block("Host-Line"):
        s_static("TRUN", name='command name')
        s_delim(" ")
        s_string("FUZZ",  name='trun variable content')
        s_delim("\r\n")

    # Fuzzing
    session.connect(s_get("Request"), callback=get_banner)
    session.fuzz()


if __name__ == "__main__":
	main()
