#!/usr/bin/env python3
"""
Conditionals - strings test true
"""

def main():
    """runtime"""
    ipchk = "192.168.0.1"

    #a string tests as True
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)

if __name__ == "__main__":
    main()
