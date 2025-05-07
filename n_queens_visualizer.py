import pygame
import numpy as np
import math
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 6
CELL_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load Queen Image
QUEEN_IMAGE = pygame.image.load("queen.png")
QUEEN_IMAGE = pygame.transform.scale(QUEEN_IMAGE, (CELL_SIZE, CELL_SIZE))

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Queens Problem")

def calculate_conflicts(board):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def generate_initial_board():
    return np.random.randint(0, BOARD_SIZE, BOARD_SIZE)

def generate_all_neighbors(board):
    neighbors = []
    for row in range(BOARD_SIZE):
        current_col = board[row]
        for col in range(BOARD_SIZE):
            if col != current_col:
                new_board = board.copy()
                new_board[row] = col
                neighbors.append(new_board)
    return neighbors

def hill_climbing(initial_board):
    current = initial_board.copy()
    iterations = 0
    restarts = 0
    start_time = time.time()
    while True:
        yield current
        iterations += 1
        current_conflict = calculate_conflicts(current)
        if current_conflict == 0:
            print(f"Hill Climbing Solved in {iterations} iterations and {restarts} restarts, Time: {time.time() - start_time:.2f}s")
            return
        neighbors = generate_all_neighbors(current)
        best_neighbor = None
        best_conflict = current_conflict
        for neighbor in neighbors:
            conflict = calculate_conflicts(neighbor)
            if conflict < best_conflict:
                best_conflict = conflict
                best_neighbor = neighbor.copy()
        if best_neighbor is None:
            current = generate_initial_board()
            restarts += 1
        else:
            current = best_neighbor

def simulated_annealing(initial_board, initial_temp=100.0, cooling_rate=0.95):
    current = initial_board.copy()
    current_conflict = calculate_conflicts(current)
    temp = initial_temp
    iterations = 0
    start_time = time.time()
    while True:
        yield current
        iterations += 1
        if current_conflict == 0:
            print(f"Simulated Annealing Solved in {iterations} iterations, Time: {time.time() - start_time:.2f}s")
            return
        row = np.random.randint(BOARD_SIZE)
        new_col = np.random.randint(BOARD_SIZE)
        while new_col == current[row]:
            new_col = np.random.randint(BOARD_SIZE)
        neighbor = current.copy()
        neighbor[row] = new_col
        neighbor_conflict = calculate_conflicts(neighbor)
        delta_e = current_conflict - neighbor_conflict
        if delta_e > 0 or (delta_e <= 0 and math.exp(delta_e / temp) > np.random.random()):
            current = neighbor
            current_conflict = neighbor_conflict
        temp *= cooling_rate
        if temp < 0.1:
            temp = 0.1

def local_beam_search(k, initial_states):
    beam = [state.copy() for state in initial_states]
    iterations = 0
    start_time = time.time()
    while True:
        best_state = min(beam, key=lambda x: calculate_conflicts(x))
        yield best_state.copy()
        iterations += 1
        if calculate_conflicts(best_state) == 0:
            print(f"Local Beam Search Solved in {iterations} iterations, Time: {time.time() - start_time:.2f}s")
            return
        all_neighbors = []
        for state in beam:
            for row in range(BOARD_SIZE):
                current_col = state[row]
                for col in range(BOARD_SIZE):
                    if col != current_col:
                        neighbor = state.copy()
                        neighbor[row] = col
                        all_neighbors.append(neighbor)
        all_neighbors.sort(key=lambda x: calculate_conflicts(x))
        seen = set()
        unique_neighbors = []
        for neighbor in all_neighbors:
            key = tuple(neighbor)
            if key not in seen:
                seen.add(key)
                unique_neighbors.append(neighbor)
        beam = unique_neighbors[:k]
        while len(beam) < k:
            beam.append(generate_initial_board())

def draw_board(board):
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if board[row] == col:
                screen.blit(QUEEN_IMAGE, (col * CELL_SIZE, row * CELL_SIZE))
    font = pygame.font.Font(None, 36)
    conflicts = calculate_conflicts(board)
    text = font.render(f'Conflicts: {conflicts}', True, RED)
    screen.blit(text, (10, 10))
    pygame.display.update()

def main():
    initial_board = generate_initial_board()
    
    # Uncomment the desired algorithm
    algorithm = hill_climbing(initial_board)
    # algorithm = simulated_annealing(initial_board, initial_temp=100.0, cooling_rate=0.95)
    # k = 5
    # initial_states = [generate_initial_board() for _ in range(k)]
    # algorithm = local_beam_search(k, initial_states)
    
    pygame.time.set_timer(pygame.USEREVENT, 500)
    running = True
    solution_found = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT and not solution_found:
                try:
                    board = next(algorithm)
                    draw_board(board)
                except StopIteration:
                    solution_found = True
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    print("Solution found!")
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
