str1 = input()
str2 = input()
str3 = input()

len_str1, len_str2, len_str3 = len(str1), len(str2), len(str3)

max_str = max(len_str1,len_str2,len_str3)
min_str = min(len_str1,len_str2,len_str3)
middle_str = (len_str1 + len_str2 + len_str3) - (min_str+max_str)

# compare diff of middle, min string and max,middle string
step_d1 = abs(middle_str - min_str)
step_d2 = abs(max_str - middle_str)

# check rule that d1 == d2
if step_d1 == step_d2:
    print('YES')
else:
    print('NO')