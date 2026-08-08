class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initialColor = image[sr][sc]
        if initialColor == color: return image
        ROW, COL = len(image), len(image[0])
        def dfs(image: List[List[int]], r: int, c: int, color: int):
            if min(r, c) < 0 or c == COL or r == ROW or \
                image[r][c] != initialColor: return
            
            image[r][c] = color

            dfs(image, r-1, c, color)
            dfs(image, r+1, c, color)
            dfs(image, r, c - 1, color)
            dfs(image, r, c + 1, color)

        dfs(image, sr, sc, color)
        return image
