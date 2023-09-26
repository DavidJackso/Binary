onep = input()
twop = input()
oneb = str(bin(int(onep))[2:])
twob = str(bin(int(twop))[2:])
sum  = ""
i = -7


def x8(a):
    while len(a) < 8:
        a = '0' + a
    return a


oneb = x8(oneb)
twob = x8(twob)
while i < 0:
   a = int(oneb[-i]) + int(twob[-i])
   if a == 1:
       sum = "1" + sum
   else:
       sum = "0" + sum
   i = i + 1
print(sum)

