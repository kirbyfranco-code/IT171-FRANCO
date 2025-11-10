player_x = 0
player_y = 0

treasure_x = 15
treasure_y = 3

game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    print(f"Player position: ({player_x}, {player_y})")
    move = input("Enter move (up/down/left/right or quit): ").lower()

    if move == "up":
        player_y += 1
    elif move == "down":
        player_y -= 1
    elif move == "left":
        player_x -= 1
    elif move == "right":
        player_x += 1
    elif move == "q":
        print("Game ended. Goodbye!")
        break
    else:
        print("Invalid move! Please enter up, down, left, right, or quit.")
        continue
    if player_x == treasure_x and player_y == treasure_y:
        print(
            f" Congratulations! You found the treasure at ({treasure_x}, {treasure_y})!")
        game_running = False

