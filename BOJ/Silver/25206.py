# 25206

total_gpa_mul_grade = 0.0 # 학점*과목평점 합
total_gpa = 0 # 학점 총합

for _ in range(20):
    _, a, b = map(str, input().split(" "))
    a = float(a)
    
    if b != "P":
      total_gpa += a
    
    if b == "A+":
        b = 4.5
    elif b == "A0":
        b = 4.0
    elif b == "B+":
        b = 3.5
    elif b == "B0":
        b = 3.0
    elif b == "C+":
        b = 2.5
    elif b == "C0":
        b = 2.0
    elif b == "D+":
        b = 1.5
    elif b == "D0":
        b = 1.0
    else:
        b = 0
    
    total_gpa_mul_grade += a * b
    
print("%.6f" %(total_gpa_mul_grade / total_gpa) if total_gpa != 0 else 0.0)