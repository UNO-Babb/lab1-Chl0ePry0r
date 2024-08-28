#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  adjectiveOne = input("Adjective 1")
  verbOne = input("Verb 1")
  adjectiveTwo = input("Adjective 2")
  nounOne = input("Plural Noun 1")
  verbTwo = input("Verb 2")
  adjectiveThree = input("Adjective 3")
  nounTwo = input("Plural Noun 2")
  adjectiveFour = input("Adjective 4")
  adjectiveFive = input("Adjective 5")
  nounThree = input("Plural Noun 3")
  #Print the story with the user supplied words.
  print("Our school has really", adjectiveOne, "food.")
  print("Just thinking about it makes my stomach", verbOne,".") 
  print("The spaghetti is", adjectiveTwo, "and tastes like", nounOne,".")
  print("One day, I swear one of my meatballs started to", verbTwo,"!" )
  print("The turkey tacos are totally", adjectiveThree, "and look kind of like old", nounTwo,".")
  print("My friend Dana actually likes the meatloaf, even though it is", adjectiveFour, "and", adjectiveFive,".")
  print("I call it mystery meatloaf and think it is really made out of", nounThree,".")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
