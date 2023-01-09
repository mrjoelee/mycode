#!/usr/bin/env python3
"""Joe || joe.lee@tlgcohort.com"""


# python3 - m pip install crayons
import crayons

# function to iterate the ips
def devicereboot(devicecmd):
    for ip in devicecmd.keys():
        print(f'{crayons.yellow("Connection to..")} {ip} "REBOOTING NOW!')
    return None

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    
    ##run the devicereboot
    devicereboot(devicecmd) # call function to connect and reboot

# call our main function
if __name__ == "__main__":
    main()

