lines = open('input.txt').read().splitlines()

l = len(lines)

def run(flip = None):
    ips = []
    ip = 0
    acc = 0

    while 0 <= ip < l:
        if ip in ips:
            return ('looped', acc)
        ips.append(ip)
        op, val = lines[ip].split()
        if flip and ip == flip:
            if op == 'nop':
                op = 'jmp'
            elif op == 'jmp':
                op = 'nop'
        # print(op, val)
        val = int(val)
        if op == 'acc':
            acc += val
            ip += 1
        elif op == 'jmp':
            ip += val
        elif op == 'nop':
            ip += 1
    return ('finished', acc)

print(run()[1])

for i in range(l):
    # could check if lines[i] == 'nop' here to skip
    # a useless run interation
    ans = run(i)
    if (ans[0] == 'finished'):
        print(ans[1])
