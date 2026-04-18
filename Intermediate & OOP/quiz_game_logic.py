# This program simulates a quiz game similar to KBC.
# It presents multiple-choice questions to the user, checks answers, and calculates the prize money based on correct responses.


print('''"Welcome to Kaun Banega Crorepati"
If you feel the question is too difficult, you can simply type 'Quit the game' as your answer.
Let's start the game!''')
quiz = ["Which planet is known as the Red Planet? a) Mars b) Venus c)Jupiter d) Saturn","What is the capital of Japan? a) Seoul b) Beijing c) Tokyo d) Bangkok","Who wrote the novel Pride and Prejudice? a) Jane Austen b) Charles Dickens c) William Shakespeare d) Emily Bronte ","What is the largest ocean on Earth? a) Atlantic Ocean b) Indian Ocean c) Arctic Ocean d) Pacific Ocean","What is the chemical symbol for gold? a) Fe b) Ag c) Au d) Cu","Which gas do plants need to perform photosynthesis? a) Oxygen b) Nitrogen c) Carbon Dioxide d) Hydrogen","Who invented the telephone? a) Thomas Edison b) Alexander Graham Bell c) Guglielmo Marconi d) Nikola Tesla","What is the largest continent by land area? a) Africa b) South America c) Asiad)Australia","Which animal is the largest mammal in the world? a) Elephant b) Giraffe c) Blue Whale d) Rhinoceros","What is the chemical formula for water?a) CO2 b) O2 c) H2O d) NH3"]
quiz_answer = ["a","c","a","d","c","c","b","c","c","c"]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
answers = []
money = 0
for i in range(10):
  ques = quiz[i]
  user_input = input(f"Your question for ₹{levels[i]}:\n{ques}? ")
  answers.append(user_input)
  if (quiz_answer[i] == answers[i]):
    print(f"You win the ₹{levels[i]}")
    if (i<4):
      money = levels[i]
    elif(i==4 or i<=8):
      money = 10000
    else:
      money = 320000
  elif(answers[i] == "Quit the game"):
    money = levels[i]
    break
  else:
    print("You lose the game")
    break
print(f"You take home ₹{money}")
print('''Thank you for your Participation.
Congratulations for your price money!!''')
