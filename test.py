x = int(input("Enter a number: "))

if x % 2 == 0:
    print("this is even")
elif x % 5 == 0:
    print("this is not even")
    print("this is divisibleby five")
elif x % 3 == 0:
    print("this is not even")
    print("this is not divisible by five")
    print("this is divisible by three")

