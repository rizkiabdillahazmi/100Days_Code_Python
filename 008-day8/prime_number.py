# Write your code below this line ๐
def prime_checker(number):
    hasil = 0
    for n in range(1, number+1):
        cek = number % n
        if (cek == 0):
            hasil += 1
    if hasil == 2:
        print("It's Prime Number")
    else:
        print("It's not prime number")
# Write your code above this line ๐


# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
