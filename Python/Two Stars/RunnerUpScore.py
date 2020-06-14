numbers = [] #intentionally left blank, I put whatever tests I need to in here.
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < numbers[-1]:
        runnerUp = numbers[i]
        print(runnerUp)
        break