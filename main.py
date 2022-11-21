print("Enter a Number: ", end="")
try:
    num = int(input())
    temp = num
    sum = 0
    while temp!=0:
        rem = temp%10
        sqr = rem*rem
        sum = sum+sqr
        temp = int(temp/10)
    print("\nSum of squares of digits of", num, "=", sum)

except ValueError:
    print("\nInvalid Input!")