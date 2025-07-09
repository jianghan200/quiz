def reverse_list(l:list):

    """
    Reverse a list without using any built in functions
    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """

    if not l:  
        return []
    
    # Create a shallow copy to avoid modifying the original
    result = l[:]  
    
    # Two-pointer: swap elements from both ends
    left = 0
    right = len(result) - 1
    
    while left < right:
        # Swap elements at left and right 
        temp = result[left]
        result[left] = result[right]
        result[right] = temp
        
        # Move pointers to the middle
        left += 1
        right -= 1
    
    return result


def solve_sudoku(matrix):
    """
    Write a programme to solve 9x9 Sudoku board.
 
    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.
 
    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    """
    def is_valid(board, row, col, num):
        """Check if placing num at (row, col) is valid"""
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        """Solve the Sudoku using backtracking"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:  # Empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            
                            if solve(board):  # Recursively solve
                                return True
                            
                            board[i][j] = 0  # Backtrack
                    
                    return False  # No valid number found
        
        return True  # All cells filled
    
    # Create a copy to avoid modifying the original
    board = [row[:] for row in matrix]
    
    if solve(board):
        return board
    else:
        return None  # No solution exists


# Example usage and test 
if __name__ == "__main__":
    # Simple test for reverse_list
    print("\nTesting reverse_list:")
    test_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(test_list)
    print(f"Original: {test_list}")
    print(f"Reversed: {reversed_list}")

    # None or empty list
    print(f"None reversed: {reverse_list([])}")
    print(f"Empty list reversed: {reverse_list(None)}")
    
    # Single element
    print(f"Single element reversed: {reverse_list([42])}")
    print("\n")

    # Test case - empty cells represented by 0
    test_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original puzzle:")
    for row in test_puzzle:
        print(row)
    
    solution = solve_sudoku(test_puzzle)
    
    if solution:
        print("\nSolution:")
        for row in solution:
            print(row)
    else:
        print("\nNo solution exists!")
    
    # Verify the solution
    def verify_solution(board):
        """Verify if the solution is correct"""
        # Check rows
        for row in board:
            if sorted(row) != list(range(1, 10)):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if sorted(column) != list(range(1, 10)):
                return False
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        box.append(board[i][j])
                if sorted(box) != list(range(1, 10)):
                    return False
        
        return True
    
    if solution and verify_solution(solution):
        print("\n✓ Solution is valid!")
    elif solution:
        print("\n✗ Solution is invalid!")
    else:
        print("\n✗ No solution found!")

   