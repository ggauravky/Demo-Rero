from collections import deque

def solve_board_game():
    # Read input
    m, n = map(int, input().split())
    
    # Read the grid
    grid = []
    for i in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # Read source and destination
    src_r, src_c = map(int, input().split())
    dest_r, dest_c = map(int, input().split())
    
    # Read move rule
    move_x, move_y = map(int, input().split())
    
    # BFS to find shortest path
    def bfs():
        # Queue stores (row, col, distance)
        queue = deque([(src_r, src_c, 0)])
        
        # Visited set to avoid revisiting cells
        visited = set()
        visited.add((src_r, src_c))
        
        while queue:
            curr_r, curr_c, dist = queue.popleft()
            
            # Check if we reached destination
            if curr_r == dest_r and curr_c == dest_c:
                return dist
            
            # Try all 4 directions
            # Forward: (r + move_x, c + move_y)
            # Right: (r + move_y, c - move_x) - 90° clockwise rotation
            # Left: (r - move_y, c + move_x) - 90° counter-clockwise rotation  
            # Backward: (r - move_x, c - move_y) - 180° rotation
            
            directions = [
                (curr_r + move_x, curr_c + move_y),      # Forward
                (curr_r + move_y, curr_c - move_x),      # Right
                (curr_r - move_y, curr_c + move_x),      # Left
                (curr_r - move_x, curr_c - move_y)       # Backward
            ]
            
            for new_r, new_c in directions:
                # Check bounds
                if 0 <= new_r < m and 0 <= new_c < n:
                    # Check if cell is passable (value = 0) and not visited
                    if grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c, dist + 1))
        
        # If destination not reachable
        return -1
    
    result = bfs()
    print(result)

# Test with provided examples
def test_examples():
    print("Testing Example 1:")
    # Example 1 data
    grid1 = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 0]
    ]
    
    def bfs_test(grid, src_r, src_c, dest_r, dest_c, move_x, move_y):
        m, n = len(grid), len(grid[0])
        queue = deque([(src_r, src_c, 0)])
        visited = set()
        visited.add((src_r, src_c))
        
        while queue:
            curr_r, curr_c, dist = queue.popleft()
            
            if curr_r == dest_r and curr_c == dest_c:
                return dist
            
            directions = [
                (curr_r + move_x, curr_c + move_y),      # Forward
                (curr_r + move_y, curr_c - move_x),      # Right
                (curr_r - move_y, curr_c + move_x),      # Left
                (curr_r - move_x, curr_c - move_y)       # Backward
            ]
            
            for new_r, new_c in directions:
                if 0 <= new_r < m and 0 <= new_c < n:
                    if grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c, dist + 1))
        
        return -1
    
    # Test Example 1
    result1 = bfs_test(grid1, 1, 0, 5, 3, 1, 2)
    print(f"Example 1 result: {result1} (Expected: 3)")
    
    # Test Example 2
    grid2 = [
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0]
    ]
    
    result2 = bfs_test(grid2, 0, 0, 4, 4, 0, 2)
    print(f"Example 2 result: {result2} (Expected: 4)")

# Run tests
test_examples()

# Uncomment the line below to run the actual solution
# solve_board_game()