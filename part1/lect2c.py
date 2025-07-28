students = [25,20,18]
std_iter = iter(students)
while True:
    try:
        print(next(std_iter))
    except:
        break