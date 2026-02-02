def grade(score):
    if score < 0 or score > 100:
        return None
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(grade(59))
print(grade(60))
print(grade(69))
print(grade(70))
print(grade(89))
print(grade(90))
print(grade(100))
print(grade(101))
