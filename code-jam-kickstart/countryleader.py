T = int(input())
for C in range(T):
    N = int(input())
    max_leader, max_uniq = '', 0
    for n in range(N):
        leader = str(input())
        num_uniq = len(set(leader.replace(' ', '')))
        if num_uniq > max_uniq:
            max_leader, max_uniq = leader, num_uniq
        elif num_uniq == max_uniq:
            if leader < max_leader:
                max_leader = leader
    print('Case #{0}: {1}\n'.format(C + 1, max_leader), end='')
