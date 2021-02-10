money = int(input())
if 23 <= money < 678:
    buy = money // 23
    if buy > 1:
        print(buy,'chickens')
    else:
        print(buy,'chicken')
elif 678 <= money < 1296:
    buy = money // 678
    print(buy, 'goat')
elif 1296 <= money < 3848:
    buy = money // 1296
    if buy > 1:
        print(buy,'pigs')
    else:
        print(buy,'pig')
elif 3848 <= money < 6769:
    buy = money // 3848
    print(buy,'cow')
elif 6769 <= money:
    buy = money // 6769
    print(buy,'sheep')
else:
    print('None')