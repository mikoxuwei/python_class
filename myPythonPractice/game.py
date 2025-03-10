import random

class Character:
    def __init__(self, name, job, attack, health):
        self.name = name
        self.job = job
        self.attack = attack
        self.health = health

    def level_up(self):
        self.attack += 10
        self.health += 20

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def is_alive(self):
        return self.health > 0

def create_enemy(level, is_boss=False):
    if is_boss:
        return Enemy(f"Boss 第{level}關", level * 15, level * 100)
    else:
        return Enemy(f"小兵 第{level}關", level * 10, level * 50)

def battle(player, enemy):
    choices = ["剪刀", "石頭", "布"]
    
    def get_winner(player_choice, enemy_choice):
        if player_choice == enemy_choice:
            return "平手"
        elif (player_choice == "剪刀" and enemy_choice == "布") or \
             (player_choice == "石頭" and enemy_choice == "剪刀") or \
             (player_choice == "布" and enemy_choice == "石頭"):
            return "玩家"
        else:
            return "敵人"

    while player.is_alive() and enemy.is_alive():
        player_choice = input("請選擇: 剪刀, 石頭, 布: ")
        while player_choice not in choices:
            player_choice = input("無效的選擇，請重新選擇: 剪刀, 石頭, 布: ")
        
        enemy_choice = random.choice(choices)
        print(f"敵人選擇了: {enemy_choice}")
        
        winner = get_winner(player_choice, enemy_choice)
        if winner == "平手":
            print("平手，重新猜拳！")
            continue
        elif winner == "玩家":
            enemy.health -= player.attack
            print(f"{player.name} 攻擊了 {enemy.name}，{enemy.name} 剩餘血量: {enemy.health}")
        else:
            player.health -= enemy.attack
            print(f"{enemy.name} 攻擊了 {player.name}，{player.name} 剩餘血量: {player.health}")
    
    return player.is_alive()

def main():
    print("歡迎來到RPG遊戲！")
    name = input("請輸入你的名字: ")
    print("選擇你的職業: 1. 戰士 2. 法師")
    job_choice = input("請輸入職業編號: ")
    if job_choice == '1':
        player = Character(name, "戰士", 20, 100)
    else:
        player = Character(name, "法師", 25, 80)

    level = 1
    while True:
        print(f"第{level}關開始！")
        enemy = create_enemy(level)
        print(f"你遇到了 {enemy.name}！")
        if not battle(player, enemy):
            print("你被擊敗了！遊戲結束。")
            break

        print(f"你擊敗了 {enemy.name}！")
        boss = create_enemy(level, is_boss=True)
        print(f"你遇到了 {boss.name}！")
        if not battle(player, boss):
            print("你被擊敗了！遊戲結束。")
            break

        print(f"你擊敗了 {boss.name}！")
        player.level_up()
        print(f"恭喜你升級了！攻擊力: {player.attack}, 血量: {player.health}")

        next_level = input("是否進入下一關？(y/n): ")
        if next_level.lower() != 'y':
            print("遊戲結束。")
            break

        level += 1

if __name__ == "__main__":
    main()