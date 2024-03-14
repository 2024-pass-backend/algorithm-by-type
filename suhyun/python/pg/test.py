ar = "ABCA"
print(ar.count("d"))
# print(ar.index("D"))

print(chr(ord('a') + 25))

a = []
print(len(a))

print(chr(122))
print(ord('v'))

str = "string"
print(str[3])

str = "123"
strr = "1234"
print(int(str))

score = [3, 3, 2, 4, 5]
s = []
m = 2
for i in range(0, len(score), m):
    s.append(score[i:i+m])

print(score[0:3])

print(s)

st = "수원시"
if "수원" in st:
    print("있음")
else:
    print("ㅌ")

a = [i for i in range(1, 6)]
print("a")
print(a)

numbers = [1,1,1]
print(*numbers)

pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }

pad = {'1':(0,0), '2':(0,1), '3':(0,2),
       '4':(1,0), '5':(1,1), '6':(1,2),
       '7':(2,0), '8':(2,1), '9':(2,2),
       '*':(3,0), '0':(3,1), '#':(3,2)
}

for key, value in pad.items():
    print(f"Key: {key}, Value: {value}, Type: {type(value)}")

answer = 'L'
print(answer + "R")


