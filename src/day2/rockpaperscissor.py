import os


# Read the input data file, split the file by new line and store the values in a list
with open(os.path.join(os.getcwd(), "src/day2", "inputdata.txt"), "r") as f:
    data = f.read()


def part1():
    total_score = 0

    # Move Rock gets a score of 1, Paper gets 2 and Scissor gets a score of 3
    move_X = 1
    move_Y = 2
    move_Z = 3

    # Assign scores to steps when player loses, makes a draw or wins.
    move_lose = 0
    move_draw = 3
    move_won = 6

    for item in data.split("\n"):
        # Split each item by space. First item is player 1 move and second item is player 2 move.
        player_1_move = item.split(" ")[0]
        player_2_move = item.split(" ")[1]

        # Apply the strategies
        if player_1_move == "A" and player_2_move == "X":
            total_score += move_X + move_draw
        elif player_1_move == "A" and player_2_move == "Y":
            total_score += move_Y + move_won
        elif player_1_move == "A" and player_2_move == "Z":
            total_score += move_Z + move_lose
        elif player_1_move == "B" and player_2_move == "X":
            total_score += move_X + move_lose
        elif player_1_move == "B" and player_2_move == "Y":
            total_score += move_Y + move_draw
        elif player_1_move == "B" and player_2_move == "Z":
            total_score += move_Z + move_won
        elif player_1_move == "C" and player_2_move == "X":
            total_score += move_X + move_won
        elif player_1_move == "C" and player_2_move == "Y":
            total_score += move_Y + move_lose
        elif player_1_move == "C" and player_2_move == "Z":
            total_score += move_Z + move_draw
        else:
            raise ValueError(
                f"Unknown move, player_1 {player_1_move}: player_2 {player_2_move}"
            )

    return total_score


def part2():
    # rock > scissor > paper > rock
    # Rock: [A, X] = 1
    # Paper: [B, Y] = 2
    # Scissor: [C, Z] = 3
    # X -> Lose = 0
    # Y -> Draw = 3
    # Z -> Win = 6
    total_score = 0
    lose = 0
    draw = 3
    win = 6

    move_x = 1
    move_y = 2
    move_z = 3

    for item in data.split("\n"):
        player_1_move = item.split(" ")[0]
        final_outcome = item.split(" ")[1]

        if player_1_move == "A" and final_outcome == "X":
            total_score += lose + move_z
        elif player_1_move == "A" and final_outcome == "Y":
            total_score += draw + move_x
        elif player_1_move == "A" and final_outcome == "Z":
            total_score += win + move_y
        if player_1_move == "B" and final_outcome == "X":
            total_score += lose + move_x
        elif player_1_move == "B" and final_outcome == "Y":
            total_score += draw + move_y
        elif player_1_move == "B" and final_outcome == "Z":
            total_score += win + move_z
        if player_1_move == "C" and final_outcome == "X":
            total_score += lose + move_y
        elif player_1_move == "C" and final_outcome == "Y":
            total_score += draw + move_z
        elif player_1_move == "C" and final_outcome == "Z":
            total_score += win + move_x

    return total_score


if __name__ == "__main__":
    print(f"Total Score: {part1()}")
    print(f"Total Score: {part2()}")
