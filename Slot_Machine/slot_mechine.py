import random

class player:
    def __init__(self) -> None:
        self.current_balance = 1000
        self.total_deposit = 0

    def deposit(self):
        
        while True:
            amount = input(f'Deposit money, your current balance : {self.current_balance}\n $')
            if amount.isdigit() and int(amount) >=0:
                self.current_balance += int(amount)
                self.total_deposit += int(amount)
                print(f'your current balance : {self.current_balance} $')
                break
            else:
                print('enter a valid number')

        return amount
    
    def pay(self,amount):
        self.current_balance -= amount

    def collect(self,amount):
        self.current_balance += amount
        
    


class slot:
    def __init__(self) -> None:
        self.fruit_symbols = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍑","💝","💛","💎"]
        self.pay_table = {
        ("🍒", "🍒", "🍒"): 2,
        ("🍋", "🍋", "🍋"): 4,
        ("🍊", "🍊", "🍊"): 6,
        ("🍇", "🍇", "🍇"): 8,
        ("🍉", "🍉", "🍉"): 10,
        ("🍑", "🍑", "🍑"): 12,
        ("💝", "💝", "💝"): 20,
        ("💛", "💛", "💛"): 40,
        ("💎", "💎", "💎"): 100
        }

        self.current_roll = []
        self.til_last_win = 0

        
    def print_paylines(self):
        #print(type(roll))
        print(f"$ {self.current_roll[0]} , {self.current_roll[1]} , {self.current_roll[2]} $")
        
    def pity_roll(self):
        self.current_roll = ["🍒", "🍒", "🍒"]

    def roll(self):
        if self.til_last_win <10:
            self.current_roll = random.choices(self.fruit_symbols,weights=(9,8,7,6,5,4,3,2,1), k=3)
        else:
            self.til_last_win = 0
            return self.pity_roll()
        

    def bet(self,player):
        while True:
            bets = input(f"place your bets: ")
            if bets == 'exit':
                print(f"$You spend total of {player.total_deposit} on this game$")
                print("gg")
                exit()

            if bets.isdigit():
                if player.current_balance < int(bets) or player.current_balance == 0:
                    print("insufficient funds, deposit funds? (y/n)")
                    yn = input()
                    if yn == 'y':
                        player.deposit()
                    else:
                        print(f"$You spend total of {player.total_deposit} dollar on this game$")
                        print("gg")
                        exit()
                else:
                    player.pay(int(bets))
                    break
            else:
                print('enter a valid number')

        return int(bets)

    def print_pay_table(self):
        for key, value in self.pay_table.items():
            print(f"{key}: {value}")

    def check_results(self,bets,gamer):
        t_result =tuple(self.current_roll)
        if t_result in self.pay_table:
            print("🎉🎉🎉 You win")
            winning = self.pay_table.get(t_result) * bets
            gamer.collect(winning)
            self.til_last_win = 0
        else:
            self.til_last_win +=1
            

        
        
def main():
    game = slot()
    gamer = player()
    game.print_pay_table()
    print('''
          Enter 'exit' to end game

          You start with $1000 
          ''')
    while True:
        print("========================================")
        bets = game.bet(gamer)
        game.roll()
        game.print_paylines()
        game.check_results(bets,gamer)
        print(f"Your current balance is ${gamer.current_balance}")

        

if __name__ == '__main__':
    main()