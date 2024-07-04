cnt = 0
total_grade = 0
for i in range(20):
    li = input().split()
    num = float(li[1])
    grade = li[2]
    if grade == "A+":
        total_grade += 4.5 * num
        cnt += num
    elif grade == "A0":
        total_grade += 4.0 * num
        cnt += num
    elif grade == "B+":
        total_grade += 3.5 * num
        cnt += num
    elif grade == "B0":
        total_grade += 3.0 * num
        cnt += num
    elif grade == "C+":
        total_grade += 2.5 * num
        cnt += num
    elif grade == "C0":
        total_grade += 2.0 * num
        cnt += num
    elif grade == "D+":
        total_grade += 1.5 * num
        cnt += num
    elif grade == "D0":
        total_grade += 1.0 * num
        cnt += num
    elif grade == "F":
        cnt += num
print(round(float(total_grade/cnt), 5))
