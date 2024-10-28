import random

def initialize_board():
    return [[0] * 9 for _ in range(9)]

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)), end="\n")

def is_valid(board, row, col, num): # 3가지 규칙 체크 함수
    # 1. 행에 중복된 숫자가 있는지
    if num in board[row]:
        return False

    # 2. 열에 중복된 숫자가 있는지
    if num in [board[i][col] for i in range(9)]:
        return False

    # 3. 3x3 박스에 중복된 숫자가 있는지
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row+3):
        for c in range(start_col, start_col+3):
            if board[r][c] == num:
                return False
    return True

def find_empty_location(board): # 빈 칸을 찾는 함수
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_sudoku(board):
    # 빈 위치 찾기
    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True # 다 푼 경우
    
    row, col = empty_loc

    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            ##### 재귀(recursive) 함수 #####
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0 # 무르기 <- 풀 수 없는 스도쿠가 입력으로 들어올 수 있기 때문
        
        return False
    
def generate_sudoku():
    puzzle = []

    numbers = [0] * 9 + list(range(1,10))

    for _ in range(9): # 행 9개
        row = []
        for _ in range(9): # 열 9개

            rand_int = random.choice(numbers)
            row.append(rand_int)
        puzzle.append(row)
    return puzzle

def play_sudoku():
    board = generate_sudoku()  # 스도쿠 퍼즐을 생성
    print("스도쿠 게임을 시작합니다!")
    print_board(board)

    while True:
        # 사용자가 입력한 값으로 행, 열, 숫자를 받음
        try:
            row = int(input("행을 입력하세요 (1-9): ")) - 1
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            # 유효한 입력인지 확인
            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9):
                print("잘못된 입력입니다. 1에서 9 사이의 숫자를 입력하세요.")
                continue

            if board[row][col] != 0:
                print("이미 값이 입력된 칸입니다.")
                continue

            # 숫자가 해당 위치에 올바르게 입력될 수 있는지 확인 (검증)
            if is_valid(board, row, col, num):
                board[row][col] = num  # 입력한 숫자를 보드에 반영
                print_board(board)

                # 스도쿠가 완성되었는지 확인
                if not find_empty_location(board): # 빈 곳을 못 찾으면!
                    print("축하합니다! 스도쿠를 완성했습니다.")
                    break
            else:
                print("잘못된 이동입니다. 게임을 종료합니다.")
                break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

# 프로그램 실행
play_sudoku()
