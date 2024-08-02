# Python solution file
# Reading input
n, m = map(int, input().split())
scores = [list(map(float, input().split())) for _ in range(m)]

# Calculating average scores for each student
averages = [sum(student_scores) / m for student_scores in zip(*scores)]

# Printing averages, each rounded to one decimal place
for avg in averages:
    print(f"{avg:.1f}")
