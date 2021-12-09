fwd1 = 0
depth1 = 0

fwd2 = 0
depth2 = 0
aim2 = 0

for line in open('in', 'r'):
    cmd, msr = line.split()
    msr = int(msr)

    if cmd == 'forward':
        fwd1 += msr
        fwd2 += msr
        depth2 += msr*aim2
    elif cmd == 'up':
        depth1 -= msr
        aim2 -= msr
    else:
        depth1 += msr
        aim2 += msr

print(fwd1*depth1)
print(fwd2*depth2)