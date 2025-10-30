# 3 times
# summary - notes
# math
# algo with dry - dict(TC)
# code
# optimize

target_dict = int(input("Enter the target"))
cur_dict = 1
j1, j2 = 0, 1
steps = 1

while cur_dict != target_dict:
    power = j1 + j2
    if cur_dict + power <= target_dict:
        cur_dict += power
        j1 = j2
        j2 = power
        steps += 1
    else:
        j1, j2 = 0, 1
        steps += 2
else:
    print(steps)

