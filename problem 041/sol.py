# Python solution file
# Step 1: Read the number of students
n = int(input())

# Step 2: Read the column names and find the index of the 'MARKS' column
columns = input().split()
marks_index = columns.index('MARKS')
 
# Step 3: Initialize a variable to store the total marks
total_marks = 0

# Step 4: Read each student's data and add their marks to total_marks
for _ in range(n):
    student_data = input().split()
    total_marks += int(student_data[marks_index])

# Step 5: Calculate the average marks
average_marks = total_marks / n

# Step 6: Print the average marks rounded to 2 decimal places
print(f"{average_marks:.2f}")
