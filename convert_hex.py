# Convert the string from Mitel DHCP Option generator to
# Meraki MX DHCP server format with : between characters
# Python3 

s = input("Enter Hex String: ")
print(':'.join(s[i:i+2] for i in range(0, len(s), 2)))
