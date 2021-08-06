#Weighted Exam Score Average

#Enter number of exams
number_exams = int(input("Enter number of exams:"))
print(number_exams)

# How many credits they cover
total_credits = int(input("Enter number of exams covered: "))

# Start with zero average and add percentages from each exam
average = 0
for exam in range(number_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter number of credits covered:  "))
    average = average + score*exam_credits/total_credits
    print("The average is", average)