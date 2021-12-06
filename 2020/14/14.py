import re
from itertools import product

lines = open('in', 'r').read().splitlines()
pattern = re.compile(r'mem\[(\d+)\]\s=\s(\d+)')

def p1():
    mem = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split()[-1]
        else:
            addr, num = map(int, pattern.match(line).groups())
            newval = 0
            for i, bit in enumerate(reversed(mask)):
                vbit = num & (2**i)
                if bit == 'X':
                    newval += vbit
                elif bit == '1':
                    newval += 2**i
                elif bit == '0':
                    pass
            mem[addr] = newval
    return mem

mem = p1()
print(sum(mem.values()))

def apply_bit_mask_str(value, mask):
    newval = ''
    for i, bit in enumerate(mask):
        if bit == '0':
            newval += value[i]
        elif bit == '1':
            newval += '1'
        elif bit == 'X':
            newval += 'X'
    return newval

def generate_addr_list(value_str):
    c = value_str.count('X')
    addrs = []
    for i in product('10', repeat=c):
        val = list(value_str)
        j = 0
        for e in range(len(val)):
            if val[e] == 'X':
                val[e] = i[j]
                j += 1
        addrs.append(''.join(val))
    return addrs

def p2():
    mem = {}
    mask = None
    addrs = []
    for line in lines:
        if line.startswith('mask'):
            mask = line.split()[-1]
        else:
            addr, num = map(int, pattern.match(line).groups())
            addr = bin(addr).replace('b', '').rjust(36, '0')
            newaddr = apply_bit_mask_str(addr, mask)
            addrs = generate_addr_list(newaddr)
            for _addr in addrs:
                mem[int(_addr, 2)] = num
    return mem

mem = p2()
print(sum(mem.values()))
