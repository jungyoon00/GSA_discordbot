import random as rd

class Dice():

    def __init__(self):
        super().__init__()
    
    def roll_dice_client():
        result = rd.randrange(1, 7)
        return result
    
    def roll_dice_game():
        client_result = rd.randrange(1, 7)
        bot_result = rd.randrange(1, 7)
        if client_result > bot_result:
            win = "You win"
        elif client_result == bot_result:
            win = "Tie"
        elif client_result < bot_result:
            win = "Bot wins"
        
        return client_result, bot_result, win

if __name__ == "__main__":
    Dice()