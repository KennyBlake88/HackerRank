def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    outputList = []
    outputString = " "
    sentence = sentence.split()
    currentString = ""
    for i in sentence:
        for j in i:
            if j.islower():
                currentString += j.upper()
            elif not j.islower():
                currentString += j.lower()
            elif j.isspace():
                currentString += j
        outputList.append(currentString)
        currentString = ""
    outputList.reverse()
    outputString = outputString.join(outputList)
    return outputString
print(reverse_words_order_and_swap_cases("aWESOME is cODING"))