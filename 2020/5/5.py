lines = open('in', 'r').read().splitlines()
bin_lines = [int(x.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for x in lines]
bin_lines.sort()

a1 = max(bin_lines)
a2 = 0

for i in range(len(bin_lines)-1):
    if bin_lines[i+1] - bin_lines[i] == 2:
        a2 = bin_lines[i] + 1
        break

print(a1)
print(a2)
