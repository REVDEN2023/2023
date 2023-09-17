print("Игра крестики нолики")

elements = list(range(1,10))

def gamer_inp(gamer_sel):  # ввод игрока
   valid = False

   while not valid:
      gamer_input = input("Введите число от 1 до 9 --->  " + gamer_sel+"  ")
      gamer_input = int(gamer_input) # перевод в число

      if gamer_input >= 1 and gamer_input <= 9:
         if(str(elements[gamer_input-1]) not in "XO"):
            elements[gamer_input-1] = gamer_sel
            valid = True

def draw(elements): # печать элементов
   for i in range(3):
      print(elements[0+i*3], " ", elements[1+i*3], " ", elements[2+i*3])

def test(elements):
   field_win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))  #поле выигрыша
   for i in field_win:
       if elements[i[0]] == elements[i[1]] == elements[i[2]]:
          return elements[i[0]]
   return False

def main(elements):
    index = 0
    win = False
    while not win:
        draw(elements)
        if index % 2 == 0: gamer_inp("X")
        else: gamer_inp("O")

        index = index + 1

        if index > 4:

           jndex = test(elements)
           if jndex:
              print()
              print()
              draw(elements)
              print()
              print(jndex, " выиграл ")
              print()
              win = True
              break

        if index == 9:
            print()
            print()
            draw(elements)
            print()
            print(" ничья ")
            break
main(elements)
