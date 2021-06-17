num = int(input("Enter the number to check for prime"))
mod_counter = 0

for i in range(2, num):
    if num % i == 0:
        mod_counter += 1

if mod_counter != 0:
    print("The given number is not a prime number")
else:
    print("The given number is a prime number")
