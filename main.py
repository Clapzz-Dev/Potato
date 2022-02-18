from termcolor import colored

class colorZ:
  Blue = '\033[90m'
  Light = '\033[94m'
  Reset = '\033[0m'
  
import time
import os

print(colorZ.Light + "Loading..")
time.sleep(1)
os.system('clear')
time.sleep(0.5)
print((colorZ.Blue + "Hello. Welcome to" + colorZ.Reset), colored('Potato', 'red'), colorZ.Blue + "by, The EXTG Dev Team\nPotato is an advanced online system.\nSponsored By, Potato Tech and JMail\n\nPlease select an option.\n1, Login with JMail\n2, About Potato\n3, Exit")
select = (input(colorZ.Blue + "Type 1, 2, or 3: " + colorZ.Reset + colorZ.Light))

if select in ("1", "2", "3"):
  if select == "3":
    os.system('clear')
    print(colored("k cya", 'red'))
  elif select == "1":
    os.system('clear')
    time.sleep(1)
    print(colorZ.Light + "Please fill out the captcha below to continue.")
    print(colorZ.Blue + "\n--|---------|")
    print(colorZ.Blue + "--|1|2|3|4|5|")
    print(colorZ.Blue + "--|---------|")
    print(colorZ.Blue + "A |x|x|x|x|x|")
    print(colorZ.Blue + "--|---------|")
    print(colorZ.Blue + "B |x|x|x|z|x|")
    print(colorZ.Blue + "--|---------|")
    print(colorZ.Blue + "C |x|x|x|x|x|")
    print(colorZ.Blue + "--|---------|\n")
    print((colorZ.Blue + "INSTRUCTIONS:\nType the the letter and number on the grid that corresponds with the letter"), colored("Z", "red"), colorZ.Blue + "For example,", colored("A2\n", "red"))
    answer = (input(colorZ.Blue + "Please type your answer: " + colorZ.Reset + colorZ.Light))
    if answer in ("B4"):
      os.system('clear')
      print(colorZ.Blue + "Reloading..")
      os.system('clear')
      time.sleep(0.5)
      print(colorZ.Light + "Welcome to Potato.") 
      time.sleep(1)
      print(colorZ.Blue + "Choose an option.\n1, Get premium\n2, View Docs \n3, Exit")
      select2 = (input(colorZ.Blue + "Type 1, 2, or 3: " + colorZ.Reset + colorZ.Light))
      if select2 in("1", "2", "3"):
        if select2 == "1":
          os.system('clear')
          time.sleep(0.5)
          print((colorZ.Blue + "Click this link to buy premium:"), colored("https://bit.ly/PotatoPremium", 'red'))
        elif select2 == "2":
          os.system('clear')
          time.sleep(1)
          print(colorZ.Light + "Potato Docs")
          print(colorZ.Blue + "-----------")
          print(colorZ.Blue + "* Creators\n* Benefits\n* Info\n* Extra")
        elif select2 == "3":
          os.system('clear')
          print(colored("Ok bye", "red"))
      else:
        print(colored("Invalid Option", 'red'))
    else:
      os.system('clear')
      time.sleep(0.5)
      print(colored("Incorrect.", 'red'))
  elif select == "2":
    os.system('clear')
    time.sleep(1)
    print(colorZ.Light + "Loading..")
    time.sleep(1)
    os.system('clear')
    time.sleep(1)
    print(colorZ.Light + "Creators:")
    print(colorZ.Blue + "Potato was made by", colored("Kam", 'red'), colorZ.Blue + "and", colored("Clapzz", 'red'), colorZ.Blue + "of the EXTG Dev Team. They're working on future updates for Potato and Potato Plus.")
    time.sleep(1)
    print(colorZ.Light + "\nInfo:")
    print((colorZ.Blue + "Potato was created on"), colored("Febuary Third 2022 (2/3/2022)", 'red'))
    time.sleep(1)
    print(colorZ.Light + "\nThe Idea:")
    print(colorZ.Blue + 'It was a Wednesday morning. Kam and Clapzz were at school. They were talking about getting a new phone. Kam thought of Apple. Then when they got to class, went to Replit and started coding. Kam was making something called Apple. Clapzz said, "bruh you`re bad. You can`t use that name." So Kam thought of the name "Potato" and Right there, Potato was created. They got to work as fast as possible, and now, 1 single day later, Potato is almost complete.')
else:
  os.system('clear')
  time.sleep(0.5)
  print(colorZ.Blue + "Invalid Input.\nPlease Restart.")