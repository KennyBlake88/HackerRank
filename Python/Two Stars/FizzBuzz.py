def fizzBuzz(n):
    for i in range(1,n):
        string = ""
        # Write your code here
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            string = str(i)
        print(string)
fizzBuzz(15)