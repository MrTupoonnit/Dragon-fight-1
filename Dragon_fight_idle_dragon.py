#Dragon Fight game

#User info and stats
user_name = input("What should we call you ? :  ")
user_hp = 100
user_skills = ["Sword Attack","Molotov Cocktail","Bow and Arrow Attack","Poison Spikes"]
damage_points = [10,15,12,15]
amount_available = [99,3,5,2]

#Enemy info and stats 

enemy = "Dragon"
enemy_hp = 75
enemy_skills = ["Fire Breath","Claw Attack","Tail Whip"]
enemy_damage_points = [20,15,15]

while True  :
    print(f"While Traveling through the woods,{user_name} encountered a {enemy}..Now a battle begins ")
    print(f"{ user_name}: {user_hp} Vs {enemy}: {enemy_hp}")
    for number, skill in enumerate(user_skills, start =1) :
        print(f"{number}.{skill}")
    print()
    action = input("Please select An attack:")
    if action == "1" :
        print(f"{ user_name}: used {user_skills[0]}")
        print(f"This delt {damage_points[0]} damage to the {enemy}")
        enemy_hp -= int(damage_points[0])
        if enemy_hp <= 0 :
            print(f"Alas the brave { user_name} has slain the {enemy}")
            print("Thank you for playing")
            break 
        print(f"{ user_name}: {user_hp} Vs {enemy}: {enemy_hp}")
        amount_available[0] -= 1
        print(f"You have {amount_available[0] } {user_skills[0]}(s) left ")
       

    elif action == "2" :
        print(f"{ user_name}: used {user_skills[1]}")
        print(f"This delt {damage_points[1]} damage to the {enemy}")
        enemy_hp -= int(damage_points[1])
        if enemy_hp <= 0 :
            print(f"Alas the brave { user_name} has slain the {enemy}")
            print("Thank you for playing")
            break
        print(f"{ user_name}: {user_hp} Vs {enemy}: {enemy_hp}")
        amount_available[1] -= 1
        print(f"You have {amount_available[1] } {user_skills[1]}(s) left ")
        

    elif action == "3" :
        print(f"{ user_name}: used {user_skills[2]}")
        print(f"This delt {damage_points[2]} damage to the {enemy}")
        enemy_hp -= int(damage_points[2])
        if enemy_hp <= 0 :
            print(f"Alas the brave { user_name} has slain the {enemy}")
            print("Thank you for playing")
            break
        print(f"{ user_name}: {user_hp} Vs {enemy}: {enemy_hp}")
        amount_available[2] -= 1
        print(f"You have {amount_available[2] } {user_skills[2]}(s) left ")
        

    elif action == "4" :
        print(f"{ user_name}: used {user_skills[3]}")
        print(f"This delt {damage_points[3]} damage to the {enemy}")
        enemy_hp -= int(damage_points[3])
        if enemy_hp <= 0 :
            print(f"Alas the brave { user_name} has slain the {enemy}")
            print("Thank you for playing")
            break
        print(f"{ user_name}: {user_hp} Vs{enemy}: {enemy_hp}")
        amount_available[3] -= 1
        print(f"You have {amount_available[3]} {user_skills[3]}(s) left ")
        

    
