onep = input()
twop = input()
oneb = str(bin(int(onep))[2:])
twob = str(bin(int(twop))[2:])
sum  = ""
i = -7
b = 0

def x8(a):
    while len(a) < 8:
        a = '0' + a
    return a


oneb = x8(oneb)
twob = x8(twob)
while i < 0:
   a = int(oneb[-i]) + int(twob[-i]) + b
   if a == 1:
       sum = "1" + sum
       b = 0
   elif a == 2:
       sum = "0" + sum
       b = 1
   elif a == 0:
       sum = "0" + sum
       b = 0
   i = i + 1
print(sum)

