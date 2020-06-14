if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    averages = {}

    for i in student_marks.keys():
        avg = sum(student_marks.get(i))/len(student_marks.get(i))
        averages[i] = format(avg, '.2f')
    
    print(averages.get(query_name))
