#!/usr/bin/env python3

#creating a list containing ip address, port, and it's up or down
my_list = [ "192.168.0.5", 5060, "UP" ]

# creating a new iplist 
ip_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# returns the 1st index of my_list
print("The first item in the list (IP): " + my_list[0] )

# returns the int value of my_list
print("The second item in the list (port): " + str(my_list[1]) )

# returns the last index value of my_list
print("The last item in the list (state): " + my_list[2] )


##displaying the ip address from iplist
# different way - using f-string print(f"The ip address: {ip_list[3]} and {ip_list[4]})
print("The ip addresses from ip_list:" + ip_list[3] + " and " + ip_list[4])


