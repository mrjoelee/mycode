#!/usr/bin/env python3
"""
List Objects and Methods
"""
def main():
    proto = ["ssh", "http", "https"]
    print(proto)
    print(proto[1])
    proto.extend("dns") # this line will add d, n, and s
    print(proto)
if __name__ == "__main__":
    main()
