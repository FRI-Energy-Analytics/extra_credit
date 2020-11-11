## https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    ## [#, #, #, #]
    marks = student_marks[query_name]

    ## sum of marks
    score_sum = sum(marks)

    ## number of marks
    score_length = len(marks)

    average = score_sum / score_length

    print("%.2f" % average)
