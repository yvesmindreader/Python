def JumpStep(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return n

    return (JumpStep(n-1) + JumpStep(n - 2))
while 1:
    steps = int(raw_input())
    if steps != 0:
        print "%d cases when steps are %d" % (JumpStep(steps), steps)
    else:
        break
