#email newsletter
import re
email = input("Whats your email? ")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com|gov|co\.uk$", email):
    print ("Valid")
else:
    print ("Invalid ")

emails = []

file = open("emails.txt", "a")
file.write(f"{email}\n")
file.close