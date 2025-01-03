# 3 Employee performance

def calc_employee_performance(score):
    if 85<score<=100:
        if 95<score<=100:
            performance="Excellent"
        else:
            performance="Very Good"
    elif 70<score<=85:
        if 80<score<=85:
            performance="Satisfactory"
        else:
            performance="Good"
    elif 50<score<=70:
        if 50<score<=70:
            performance ="Needs Improvement"
    elif score<=50:
        performance="Poor"
    else:
        print("Invalid Input")
    
    return performance

employee_score=int(input("Enter Employee score: "))
employee_performance = calc_employee_performance(employee_score)

print("The Employee Performance is : ",employee_performance)
