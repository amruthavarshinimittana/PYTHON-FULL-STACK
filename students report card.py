n=int(input("enter the no of students:"))
marks=list(map(int,input("enter the marks:").split()))
if len(marks)!=n:
    print("not sufficient length")
else:
    for i in range(n):
        print(f"marks of student-{i+1}:{marks[i]}")
    print(f"total marks of students:{sum(marks)}")
    print(f"maximum marks of students:{max(marks)}")
    print(f"minimum marks of students:{min(marks)}")
    print(f"average marks of students:{sum(marks)//(n)}")      
