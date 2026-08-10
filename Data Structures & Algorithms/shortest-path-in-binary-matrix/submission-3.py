class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if ROW != COL: return -1
        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1: return -1

        # Initialize the visited set and the queue by adding the top left corner
        # as starting position
        visited, queue = set(), deque([(0, 0, 1)])
        neighborDirections = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            (r, c, l) = queue.popleft()
            if r == ROW - 1 and c == COL - 1: return l

            # Rotate clockqise and add all children/neighbors
            for dr, dc in neighborDirections:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 0 \
                    and (nr, nc) not in visited):
                    queue.append((nr, nc, l + 1))
                    visited.add((nr, nc))
        return -1

    # BFS without Overwriting Grid
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     if ROW != COL: return -1
    #     if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1: return -1

    #     # Initialize the visited set and the queue by adding the top left corner
    #     # as starting position
    #     visited, queue = set(), deque([(0, 0)])

    #     length = 1
    #     while queue:
    #         for _ in range(len(queue)):
    #             (r, c) = queue.popleft()

    #             if r == ROW - 1 and c == COL - 1: return length

    #             if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited \
    #                 or grid[r][c] == 1:
    #                 continue

    #             # Rotate clockqise and add all children
    #             queue.append((r, c + 1))
    #             queue.append((r + 1, c + 1))
    #             queue.append((r + 1, c))
    #             queue.append((r + 1, c - 1))
    #             queue.append((r, c - 1))
    #             queue.append((r - 1, c - 1))
    #             queue.append((r - 1, c))
    #             queue.append((r - 1, c + 1))

    #             visited.add((r, c))

    #         length += 1
    #     return -1