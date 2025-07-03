class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Fairly easy for a medium problem
        # Mainly because the time complexity can't be improved more than O(n^2)
        # Important ideas you forgot:
        #   1. No need to add items to the set first and then check for length at the end, that's stupid
        #       Just check if current element is already in set or not. If it is, invalid, else add element to set and continue
        #   2. No need for a 4-way-nested-loop at the end to check for each 3x3 box.
        #       Just use integer division by 3 i.e. // 3

        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (not 1<=int(num)<=9) or num in seen:
                    return False
                seen.add(num)
            seen.clear()

        for i in range(9):
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                if (not 1 <= int(num) <= 9) or num in seen:
                    return False
                seen.add(num)
            seen.clear()

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num = board[k][l]
                        if num == ".":
                            continue
                        if (not 1 <= int(num) <= 9) or num in seen:
                            return False
                        seen.add(num)
                seen.clear()

        return True

        # A more elegant solution that uses hashsets:
        #
        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)
        #
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if (board[r][c] in rows[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // 3, c // 3)]):
        #             return False
        #
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c // 3)].add(board[r][c])
        #
        # return True

solution = Solution()
print(solution.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))