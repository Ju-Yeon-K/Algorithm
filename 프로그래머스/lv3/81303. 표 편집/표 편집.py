def solution(n, k, cmds):
    now = k
    a = {i: [i-1, i+1] for i in range(n)}
    v = ['O'] * n
    del_list = []
    
    for cmd in cmds:
        cmd = cmd.split(' ')
        if len(cmd) > 1:
            num = int(cmd[1])
            if cmd[0] == 'D':

                for _ in range(num):
                    now = a[now][1]
            elif cmd[0] == 'U':

                for _ in range(num):
                    now = a[now][0]
        else:
            if cmd[0] == 'C':
                pre = a[now][0]
                nex = a[now][1]

                v[now] = 'X'
                del_list.append([pre, now, nex])

                if nex == n:
                    now = a[now][0]
                else:
                    now = a[now][1]

                if pre == -1:
                    a[nex][0] = pre
                elif nex == n:
                    a[pre][1] = nex
                else:
                    a[pre][1] = nex
                    a[nex][0] = pre
            
            elif cmd[0] == 'Z':
                pre, k, nex = del_list.pop()
                v[k] = 'O'

                if pre == -1:
                    a[nex][0] = k

                elif nex == n:
                    a[pre][1] = k
                else:
                    a[pre][1] = k
                    a[nex][0] = k

    return ''.join(v)
