class TrieNode:
    def __init__(self, word: str):
        self.children, self.word, self.isWord = {}, word, False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(cur.word + c)
            cur = cur.children[c]
        cur.isWord = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode("")
        for w in words: root.addWord(w)

        m, n, result, seen = len(board), len(board[0]), set(), set()

        def dfs(r, c, node):
            if r < 0 or \
                c < 0 or \
                r >= m or \
                c >= n or \
                (r, c) in seen or \
                board[r][c] not in node.children : return

            seen.add((r, c))
            node = node.children[board[r][c]]
            if node.isWord: result.add(node.word)

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            seen.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return list(result)


    # Not really any better, same runtime as below
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     letter_map = defaultdict(list)
    #     m, n, result, seen= len(board), len(board[0]), [], set()

    #     for row in range(m):
    #             for col in range(n):
    #                 letter_map[ board[row][col] ].append((row, col))

    #     for word in words:
    #         if word[0] not in letter_map: continue

    #         for (row, col) in letter_map[word[0]]:

    #             def dfs(word, r, c) -> bool:
    #                 if len(word) == 0: return True
    #                 elif word[0] != board[r][c]: return False

    #                 seen.add((r, c))

    #                 if (r-1, c) not in seen and r > 0 and dfs(word[1:], r-1, c):
    #                     seen.remove((r, c))
    #                     return True
    #                 if (r+1, c) not in seen and r < m - 1 and dfs(word[1:], r+1, c):
    #                     seen.remove((r, c))
    #                     return True
    #                 if  (r, c-1) not in seen and c > 0 and dfs(word[1:], r, c-1):
    #                     seen.remove((r, c))
    #                     return True
    #                 if (r, c+1) not in seen and c < n - 1 and dfs(word[1:], r, c+1):
    #                     seen.remove((r, c))
    #                     return True
                    
    #                 seen.remove((r, c))
    #                 return False
                    
    #             if dfs(word, row, col): 
    #                 result.append(word)
    #     return result

    # O(W * m * n * 4^w) - Backtracking - very inefficient, time limit exceeded
    # where w is length of longest word
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    #     seen = set()
    #     result = []
    #     m, n = len(board), len(board[0])
    #     # print(m, n)

    #     for word in words:

    #         for row in range(m):
    #             for col in range(n):
    #                 if word[0] != board[row][col]: continue

    #                 def dfs(word, r, c) -> bool:
    #                     # print(word, r, c)
    #                     if len(word) == 0: return True
    #                     elif word[0] != board[r][c]: return False

    #                     seen.add((r, c))
    #                     paths = []
    #                     if (r-1, c) not in seen and r > 0 and dfs(word[1:], r-1, c):
    #                         seen.remove((r, c))
    #                         return True
    #                     if (r+1, c) not in seen and r < m - 1 and dfs(word[1:], r+1, c):
    #                         seen.remove((r, c))
    #                         return True
    #                     if  (r, c-1) not in seen and c > 0 and dfs(word[1:], r, c-1):
    #                         seen.remove((r, c))
    #                         return True
    #                     if (r, c+1) not in seen and c < n - 1 and dfs(word[1:], r, c+1):
    #                         seen.remove((r, c))
    #                         return True
                        
    #                     seen.remove((r, c))
    #                     return False
                    
    #                 if dfs(word, row, col): 
    #                     result.append(word)
                     
    #     return result






# class PrefixTree:
#     def __init__(self, board: List[List[str]]):
#         self.root = TrieNode()
#         self.board = board
#         self.index = defaultdict(list)

#         def dfs(self, board: List[List[str]]):

        
#         for r in len(board):
#             for c in len(r):
#                 letter = board[r][c]

#                 root.children[(r,c)] = TrieNode(letter)
#                 self.index[letter].append((r, c))



#     def search(self, word: str) -> bool:
#         curr = self.root
#         for c in word:
#             if c not in curr.children: return False
#             curr = curr.children[c]
#         return curr.word
        
#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root
#         for c in prefix:
#             if c not in curr.children: return False
#             curr = curr.children[c]
#         return True

