# Longest Common Subsequence

arr1 = raw_input()
arr2 = raw_input()
m = len(arr1)
n = len(arr2)


def lcs(arr1, arr2, m, n):
    if m == 0 or n == 0:
        return 0
    elif arr1[m-1] == arr2[n-1]:
        return 1 + lcs(arr1, arr2, m-1, n-1)
    else:
        return max(lcs(arr1, arr2, m, n-1), lcs(arr1, arr2, m-1, n))


def dp_lcs(arr1, arr2, m, n):
    L = [[None]* (n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif arr1[i-1] == arr2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


print dp_lcs(arr1, arr2, m, n)
print lcs(arr1, arr2, m, n)
