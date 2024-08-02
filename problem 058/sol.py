# Python solution file
n, m = map(int, input().split())
scores = [list(map(float, input().split())) for _ in range(m)]
averages = [sum(student_scores) / m for student_scores in zip(*scores)]
for avg in averages:
    print(f"{avg:.1f}")
