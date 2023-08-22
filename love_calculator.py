print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name1_count_T = name1.count('t')
name1_count_R = name1.count('r')
name1_count_U = name1.count('u')
name1_count_E = name1.count('e')
name1_count_L = name1.count('l')
name1_count_O = name1.count('o')
name1_count_V = name1.count('v')
name1_count_LE = name1.count('e')

name2_count_T = name2.count('t')
name2_count_R = name2.count('r')
name2_count_U = name2.count('u')
name2_count_E = name2.count('e')
name2_count_L = name2.count('l')
name2_count_O = name2.count('o')
name2_count_V = name2.count('v')
name2_count_LE = name2.count('e')

total_true = name1_count_T + name1_count_R + name1_count_U + name1_count_E + name2_count_T + name2_count_R + name2_count_U + name2_count_E
total_love = name1_count_L + name1_count_O + name1_count_V + name1_count_E + name2_count_L + name2_count_O + name2_count_V + name2_count_E

score = str(total_true) + str(total_love)
score_int = int(score)

if score_int < 10 or score_int > 90:
    print("Your score is " + score +", you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
    print("Your score is " + score + ", you are alright together.")
else: 
    print("Your score is " + score + ".")