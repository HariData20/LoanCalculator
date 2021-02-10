n1 = int(input())
ref_time = 10.5

if n1 + ref_time > 24:
    print('Wednesday')
elif n1 + ref_time < 0:
    print('Monday')
elif 0 < n1 + ref_time < 24:
    print('Tuesday')