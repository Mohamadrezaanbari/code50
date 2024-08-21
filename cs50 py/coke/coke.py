global total
total = 50
user = 0
while total != 0:
    print(f'Amount Due: {total}')
    user = int(input("Insert coin: "))
    expected = [5, 10, 25, 50]
    for a in expected:
        if user == a:
            total = total - user
            if total <= 0:
                total1 = str(total)
                print(f'Change Omkdir wed: {total1.replace('-', '')}')
                total = 0
        else:
            continue
