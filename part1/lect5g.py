import sys
def calc_total(s):
    return s[0]+s[1]

#student = (20,31)
try:
    student=(int(sys.argv[1]),int(sys.argv[2]))
    print(calc_total(student))
except:
    print("You have to enter two numbers:")
    print("example: lect5g.py 10 20")

