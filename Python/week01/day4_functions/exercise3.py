# Grade Calculator
score = int(input("Enter your score from 0 to 100 to find out the Grade: "))

def calculate_grade():
    if score>=90 and score<=100:
        return 'F'
    elif score >=80 and score <90:
        return 'B'
    elif score >=70 and score <80:
        return 'C'
    elif score >=60 and score <70:
        return 'D'
    elif score >=0 and score <60:
        return 'F'
    else:
        return 'Invalid score Entered'

print(f"You scored {score} Marks, Which is Grade {calculate_grade()}")
