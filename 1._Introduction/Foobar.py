# Program written on the first day of Advanced Python, Computer Science, KEA

# Given {0- 100}
# If divisible by 3 = print foo
# If divisible by 5 = print bar
# Otherwise print x

for i in range(101):
    if i % 3 == 0:
        print("foo", end="")
    if i % 5 == 0:
        print("bar", end="")
    if i % 3 != 0 and i % 5 != 0:
        print(i, end="")
    print("")  # Add a newline when a number has been evaluated
