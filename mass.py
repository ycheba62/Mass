from random import random
let
{};
M = 5
N = 5
count = 0
a = []
for i in range(N):
    b = []
    for j in range(N):
        n = int(random()*100)
        if 9 < n < 100:
            count += 1
        b.append(n)
    a.append(b)
for i in a:
    print(i)()
print  ("Количество двузначных чисел: %d" % count)
end
