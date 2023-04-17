x0 = 1
x1 = 1
x2 = 1
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0

w0 = 1
w1 = 0
w2 = 4
w3 = -7
w4 = 0
w5 = 0
w6 = 0
w7 = 0

thr = 0.5

vec = [x0, x1, x2, x3]
wig = [w0, w1, w2, w3]
s = 0

for x in vec:
    for w in wig:
        s = s + x * w

print(s)
if thr <= s:
    print("YES!")
else:
    print("NO!")
