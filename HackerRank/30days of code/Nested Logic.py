rd, rm, ry = [int(e) for e in input().strip().split(' ')]
dd, dm, dy = [int(e) for e in input().strip().split(' ')]

# Check the biggest category: year
if ry < dy:
    print(0)
elif ry == dy:
    # Check the next biggest category: month
    if rm < dm:
        print(0)
    elif rm == dm:
        # Check the last category: day
        if rd <= dd:
            print(0)
        else:
            print(str((rd - dd) * 15))
    else:
        print(str((rm - dm) * 500))
else:
    print('10000')
