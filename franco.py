player_kirby = 0
player_chip = 0

treasure_x = 15
treasure_y = 3

game_running = True

print("Welcome to Franco's Maze")
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    print(f"Player position: ({player_kirby}, {player_chip})")
    move = input("Enter move (w to go up/s to go down/a to go left/d to go right or q to quit): ").lower()
 
    if move == "w":
        player_chip += 1
    elif move == "s":
        player_chip -= 1
    elif move == "a":
        player_kirby -= 1
    elif move == "d":
        player_kirby += 1
    elif move == "q" or move == "quit":
        print("Game ended. Goodbye!")
        break
    else:
        print("Invalid move! Please enter up, down, left, right, or q.")
        continue

    # Check if player reached the treasure
    if player_kirby == treasure_x and player_chip == treasure_y:
        print(f" Congratulations! You found the treasure at ({treasure_x}, {treasure_y})!")
        game_running = False





