class Solution:
    """
    有一个机器人的位于一个 m × n 个网格左上角。
    机器人每一时刻只能向下或者向右移动一步。
    机器人试图达到网格的右下角。
    问有多少条不同的路径？
    答:此题即为在m+n-2步中，挑选出m-1步向下或者n-1步向右的组合。即为求组合数的问题
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        return self.factorial(m + n - 2) / (
            self.factorial(m - 1) * self.factorial(n - 1))

    def factorial(self, x):
        factorial = 1
        for n in range(1, x + 1):
            factorial = n * factorial
        return factorial

    """
    现在考虑路径中存在障碍物。
    问有多少条不同的路径？
    答:此题只需要减去通过障碍物的路径即可。
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        sum = self.uniquePaths(m, n)
        # write your code here
        for m in range(len(obstacleGrid)):
            for n in range(len(obstacleGrid[0])):
                sum = sum - self.uniquePaths(m,n)
        return sum


s = Solution()
print(s.uniquePaths(5, 4))
