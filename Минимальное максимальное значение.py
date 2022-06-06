buff = 0
res_max = 0
res_min = 0
num = [6, 1,  2, 3, 4, 5]
len_mass = len(num)
for i in range(len(num)):
    buff = num[i]
    if(i == 0):
        res_max = buff
    if(buff > res_max):
        res_max = buff

for i in range(len(num)):
    buff = num[i]
    if(i == 0):
        res_min = buff
    if(buff < res_min):
        res_min = buff
print(res_max)
print(res_min)