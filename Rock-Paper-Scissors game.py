import random
user_choice= int(input("enter your choice:type 0 for rock , 1 for paper ,2 for scissor: "))
if user_choice>=3 or user_choice<0:
	print ("you enter invail number,you loose")
else:
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(computer_choice)

    if computer_choice == user_choice:
     print("it is draw")
    elif computer_choice==0  or user_choice==2:
    	print("you loose")
    elif user_choice==0 or computer_choice==2:
     print("you win")
    elif computer_choice>user_choice:
     print("you loose")
    elif computer_choice <user_choice:
      print("you win")
