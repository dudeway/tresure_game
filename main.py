print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Привет и добро пожаловать на Остров Сокровищ.")
print("Ваша миссия заключается в выборе верного решения.")
choice1 = input("Вы на пересечении дороги. Выберите куда пойти 'налево' или 'направо'?\n").lower()
if choice1 == "налево":
  choice2 = input("Вам предстоит 'плыть' или 'ждать'. Что вы выберете?\n").lower()
  if choice2 == "ждать":
    choice3 = input("Перед вами несколько дверей, какой ключ вы выберете чтобы их открыть? 'жёлтый', 'синий', 'красный'? Также вы можете выбрать свой вариант. Что вы выберете?\n").lower()
    if choice3 == "красный":
      print("Ты сгорел. Игра окончена.")
    elif choice3 == "желтый" or "жёлтый":
      print("Ты нашёл сокровища и победил.")
    elif choice3 == "синий":
      print("Тебя съели. Игра окончена.")
    else:
      print("Ты выбрал не ту дверь. Игра окончена.")
  else:
    print("Ты попал в ловушку. Игра окончена.")
else:
  print("Вы упали глубоко в яму и разбились. \nИгра окончена.")
