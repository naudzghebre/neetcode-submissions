from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        # Initialize the visited set and the queue by adding the top left corner
        # as starting position
        visited, queue = set(), deque([(0, 0)])
        print(visited)

        length = 0
        while queue:
            print(queue)
            for _ in range(len(queue)):
                (r, c) = queue.popleft()

                if r == ROW - 1 and c == COL - 1 and grid[r][c] == 0 : return length

                if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited \
                    or grid[r][c] == 1:
                    print("continued: " + f'({r},{c})')
                    continue

                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

                visited.add((r, c))


            length += 1
        return -1


