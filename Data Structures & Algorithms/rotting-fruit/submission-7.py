class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        orangeQueue = deque()

        freshCount = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1: freshCount += 1
                if grid[r][c] == 2:
                    orangeQueue.append((r, c))

        if len(orangeQueue) == 0 and not freshCount: return 0
        elif len(orangeQueue) == 0 and freshCount: return -1

        # Initialize the visited set and the queue by adding the top left corner
        # as starting position
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        length = 0
        while freshCount > 0 and orangeQueue:
            for _ in range(len(orangeQueue)):
                (r, c) = orangeQueue.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshCount -= 1
                        orangeQueue.append((nr, nc))
            length += 1

        # Returns -1 immediately if ANY cell contains 1
        return length if not freshCount else -1