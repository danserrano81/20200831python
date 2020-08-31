#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
This is a doc-string, best practice says this is the place to show off, explain what your code
 does, list who must keep it up to date, etc."""

def main():
    """Learning about the input function"""

useripv4 = input("Please enter an IPv4 IP address:")

# concatenation
print("You told me the IPv4 address is: " + useripv4, sep=" ", end="\n")

# giving the print function mulitple elements
print("You told me the IPv4 address is:", useripv4, sep=" ", end="\n")

# f-string (new in python 3.6)
print(f"You told me the IPv4 address is: {useripv4}", sep=" ", end="\n")

if __name__ == "__main__":
    main()
