get = int(input("Num: "))

end = get*2 + 1
result = []


for i in range(get):
    if i == 0: continue
    if i == 
    star = "*"*(i*2 -1)
    l = len(star)
    star = "*" + " "*(l-2) + "*"
    result.append(star.center(end))

for i in result:
    print(i)