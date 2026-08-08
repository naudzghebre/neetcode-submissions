class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initialColor = image[sr][sc]
        if initialColor == color: return image

        ROW, COL = len(image), len(image[0])
        def dfs(image: List[List[int]], r: int, c: int):
            if min(r, c) < 0 or c == COL or r == ROW or \
                image[r][c] != initialColor: return
            
            image[r][c] = color

            # dfs(image, r-1, c)
            # dfs(image, r+1, c)
            # dfs(image, r, c - 1)
            # dfs(image, r, c + 1)

            if r > 0 and image[r - 1][c] == initialColor:
                dfs(image, r - 1, c)
            if r + 1 < ROW and image[r + 1][c] == initialColor:
                dfs(image, r + 1, c)
            if c > 0 and image[r][c - 1] == initialColor:
                dfs(image, r, c - 1)
            if c + 1 < COL and image[r][c + 1] == initialColor:
                dfs(image, r, c + 1)
        dfs(image, sr, sc,)
        return image
