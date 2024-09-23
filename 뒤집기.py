s = input()
z_c = 0
o_c = 0
for i in range(1,len(s),2):
    if s[i] == 1 and s[i-1] == 1:
        z_c += 1
for i in range(1,len(s),2):
    if s[i] == 0 and s[i-1] == 0:
        o_c += 1
print(o_c, z_c)