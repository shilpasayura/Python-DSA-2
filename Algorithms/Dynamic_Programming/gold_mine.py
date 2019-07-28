N = int(raw_input())
gold = list()
for _ in range(N):
    gold.append(map(int, raw_input().split()))


def get_max_gold(gold, n, m):
    max_gold = [[0 for i in range(N)] for j in range(N)]
    for col in range(n-1, -1, -1):
        for row in range(m):
            if col == n-1:
                right = 0
            else:
                right = max_gold[row][col+1]

            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = max_gold[row-1][col+1]

            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = max_gold[row+1][col+1]

            max_gold[row][col] = gold[row][col] + max(right, right_up, right_down)

    max_ele = max_gold[0][0]
    for i in range(n):
        max_ele = max(max_ele, max_gold[i][0])

    return max_ele


print get_max_gold(gold, N, N)