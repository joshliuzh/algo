
def knapsack(weights, values, capacity):
    """
    bounded knapsack algorithm, where at most 1 of item for each can be chosen.
    """
    if len(weights) != len(values):
        return 0
    zipped = sorted(zip(weights, values))
    weights = [t[0] for t in zipped]
    values =  [t[1] for t in zipped]
    n = len(weights)
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(capacity + 1):
            if 0 in [i, j]:
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j]= max(dp[i][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
                
    return dp[-1][-1]
weights = [1, 2, 3, 4, 5, 9]
values = [2, 3, 6, 7, 8, 999]
capacity = 10
knapsack(weights, values, capacity)
