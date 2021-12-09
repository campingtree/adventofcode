numbers = None
boards = []
boards_f = []

b = []
for line in open('in', 'r'):
    line = line.strip()
    if numbers == None:
        numbers = [int(x) for x in line.split(',')]
        continue
    if line:
        b.append([int(x) for x in line.split()])
    else:
        if b:
            boards.append(b)
        b = []
boards.append(b)

for b in boards:
    assert len(b) == len(b[0]) == 5
    boards_f.append([[False for _ in range(5)] for _ in range(5)])

WON = [False for _ in range(len(boards))]
for num in numbers:
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == num:
                    boards_f[i][j][k] = True
        
        won = False
        for j in range(5):
            ok = True
            for k in range(5):
                if not boards_f[i][j][k]:
                    ok = False
            if ok:
                won = True
        for k in range(5):
            ok = True
            for j in range(5):
                if not boards_f[i][j][k]:
                    ok = False
            if ok:
                won = True

        if won and not WON[i]:
            WON[i] = True
            num_wins = len([j for j in range(len(boards)) if WON[j]])
            if num_wins == 1 or num_wins == len(boards):
                unmarked = 0
                for j in range(5):
                    for k in range(5):
                        if not boards_f[i][j][k]:
                            unmarked += boards[i][j][k]
                print(unmarked * num)