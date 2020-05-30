for i in range(n - 1, -1, -1):
    print(i)
    if numbers[i] < numbers[-1]:
        runnerUp = numbers[i]
        print(runnerUp)
        break