

# PROBLEM 2

total_marks = int(input("Input Total marks : "))
obtained_marks = int(input("Input Obtained marks : "))
per = (obtained_marks/total_marks)*100
print(per)
if per < 40:
    print("fail")
else:
    print("pass")