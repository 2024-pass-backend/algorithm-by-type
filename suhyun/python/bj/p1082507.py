import sys

class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

n = int(sys.stdin.readline())
a = []

for i in range(n):
    student = sys.stdin.readline().split()
    student[1:] = map(int, student[1:])
    a.append(Student(*student))
    
a.sort(key = lambda x : (-x.korean, x.english, -x.math, x.name))

names = [elem.name for elem in a]

for name in names:
    print(name)
    