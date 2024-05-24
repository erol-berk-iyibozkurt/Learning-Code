import random
predicted_number = random.randint(0,50)
my_favourite_number = 15
if predicted_number < 15:
  print("My favourite number is bigger than ", predicted_number)
elif predicted_number == my_favourite_number:
  print("My favourite number is 15. You guessed my favourite number. Congratulations :)")
else:
  print("My favourite number is smaller than", predicted_number)
  
