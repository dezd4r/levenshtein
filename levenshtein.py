def levenshtein_algorithm(a: str, b: str):
    n = len(a)
    m = len(b)
    f = [[0] * (m + 1) for i in range(0, n + 1)]

    for i in range(0, n + 1):
        f[i][0] = i

    for i in range(0, m + 1):
        f[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + (a[i - 1] != b[j - 1]))

    return f[n][m]


def normalized_levenshtein(a: str, b: str):
    if len(a) == 0 or len(b) == 0:
        return 1.0

    return levenshtein_algorithm(a, b) / max(len(a), len(b))
