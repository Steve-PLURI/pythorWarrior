# My first Python game
# Monster Battle

from random import randint 

print('')
print('<> A WARRIOR FOR PYTHOR <>')
print('')
print('---' * 20)
print('')
print('A cacophony of birds suddenly erupts from the vast forest')
print('You find yourself in a strange place with no memory of how')
print('')
print('')
print('You are surrounded by fog and stagger about disoriented')
print('Suddenly the Lands of Pythor open forth before your eyes')
print('')
print('')
print('An elderly woman approaches you from beyond the grey mist')
print('"Welcome stranger, let me tell you about our troubles."')
print('')
print('---' * 20)
print('')
print('   This was once a lush and beautiful land,')
print('   full of riches. Then a demonic monster')
print('   appeared and the land became dark---')
print('')
print('')
print('   We call it Yurhwan and it terrorizes us of')
print('   our very existence. The prophecy tells')
print('   of a Warrior that will be our salvation;')
print('')
print('')
print('   You--- you must be the Warrior heaven-sent')
print('   to protect us! To arms, Warrior, for')
print('   the monster approaches... and it is hungry')
print('')

game_running = True
game_results = []
round_count = 0

def calc_monster_attack(attack_min, attack_max):
  return randint(attack_min, attack_max)

def calc_player_attack(attack_min, attack_max):
  return randint(attack_min, attack_max)

def calc_player_heal(heal_min, heal_max):
  return randint(heal_min, heal_max)

def game_ends(winner_name):
  print('')
  print(winner_name + ' is the VICTOR!')
  print('')

while game_running == True:
  counter = 0
  new_round = True
  player = {'name': 'Hero', 'attack_min': 7, 'attack_max': 13, 'heal_min': 15, 'heal_max': 17, 'health': 100}
  monster = {'name': 'Yurhwan', 'attack_min': 10, 'attack_max': 20, 'health': 100}

  print('---' * 20)
  print('')
  
  other_count = 0
  name_phase = True

  while name_phase == True:
    player['name'] = input("Please tell us your name, Warrior: ")

    if not player['name'].isalpha():
        print('')
        print('     Sorry, fine Warrior, but I cannot understand')
        print('     I only know Standard tongue')
        print('')

    else:
        player['name'] = player['name'].lower()
        player['name'] = player['name'].title()
        name_phase = False

  print('')
  print('---' * 20)
  print('   Combatant starting STATS')
  print('---' * 20)
  print('')
  print('Warrior:   ' + str(player['name']))
  print('Attack:    Lt damage')
  print('Heal:      Mod HP restore')
  print('Health:    ' + str(player['health']) + ' HP')
  print('')
  print('Monster:   ' + str(monster['name']))
  print('Attack:    Hvy damage')
  print('Health:    ' + str(monster['health']) + ' HP')
  print('')

  while new_round == True:
    counter = counter + 1
    player_won = False
    monster_won = False

    print('---' * 20)
    print('   Please select an ACTION')
    print('---' * 20)
    print('')
    print('1) Attack Enemy')
    print('2) Heal Yourself')
    print('3) Show Results')
    print('4) Instructions')
    print('5) Exit Game')
    print('')

    player_choice = input('SELECTION > ')
    print('')
    print('---' * 20)


    if player_choice == '1':
        rand_player_attack = calc_player_attack(player['attack_min'], player['attack_max'])
        monster['health'] = monster['health'] - rand_player_attack
        print('     ATTACK ' + str(counter))
        print('---' * 20)
        print('')
        print(player['name'])
        print('Damage:      ' + str(rand_player_attack))
        print('')

        if monster['health'] <= 0:
            player_won = True

        else:
            rand_monster_attack = calc_monster_attack(monster['attack_min'], monster['attack_max'])
            player['health'] = player['health'] - rand_monster_attack
            print(monster['name'])
            print('Damage:      ' + str(rand_monster_attack))
            print('')

            if player['health'] <= 0:
                monster_won = True

    elif player_choice == '2':
        rand_monster_attack = calc_monster_attack(monster['attack_min'], monster['attack_max'])
        rand_player_heal = calc_player_heal(player['heal_min'], player['heal_max'])
        player['health'] = player['health'] + rand_player_heal
        player['health'] = player['health'] - rand_monster_attack
        print('     HEAL ' + str(counter))
        print('---' * 20)
        print('')
        print(player['name'])
        print('Heal:         ' + str(rand_player_heal))
        print('')
        print(monster['name'])
        print('Damage:       ' + str(rand_monster_attack))
        print('')

        if player['health'] <= 0:
            monster_won = True

    elif player_choice == '3':
        for player_stat in game_results:
            print('')
            print(player_stat)
            print('')
    
    elif player_choice == '4':
        print('     INSTRUCTIONS')
        print('---' * 20)
        print('')
        print('   If you choose to 1) attack, you will strike')
        print('   with a rapid slash that is weak in damage')
        print('')
        print('')
        print('   If you choose to 2) heal, you will restore')
        print('   a moderate amount of HPoints to your health')
        print('')
        print('')
        print('   Regardless of what action you choose, the')
        print('   demonic Yur only knows to savagely attack')
        print('')
        print('')
        print('   If you choose to 3) view results, the names &')
        print('   scores of previous Warriors will be displayed')
        print('')

    elif player_choice == '5':
        new_round = False
        game_running = False
        break

    else:
        print('')
        print('That is not an option')
        print('')
        
    if player_won == False and monster_won == False:
        print('---' * 20)
        print('     HEALTH')
        print('---' * 20)
        print('')
        print(player['name'])
        print('HPoints:      ' + str(player['health']))
        print('')
        print(monster['name'])
        print('HPoints:      ' + str(monster['health']))
        print('')

    elif player_won == True:
        game_ends(player['name'])
        round_result = {'Name': player['name'], 'Remaining HP': player['health'], 'Rounds': counter}
        game_results.append(round_result)
        new_round = False

    elif monster_won == True:
        game_ends(monster['name'])
        round_result = {'Name': player['name'], 'Remaining HP': player['health'], 'Rounds': counter}
        game_results.append(round_result)
        new_round = False
            