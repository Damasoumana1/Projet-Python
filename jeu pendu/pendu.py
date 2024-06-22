def pendu():
    wordDictionnary = []
    import random
    fichier = open("../Projet Python/bibliothèque.txt", "r")
    for x in fichier:
        wordDictionnary.append(x.rstrip("\n"))
    choosenWord = random.choice(wordDictionnary)
    findLetter = []
    tentatives =  5
    while tentatives > 0:
        wordDab = ""
        for letter in choosenWord:
            if letter in findLetter:
                wordDab = letter + " "
            else:
                wordDab = wordDab + "* "    
        print(wordDab)
        wordLetter = input("enter a letter: ")
        if wordLetter in choosenWord:
            print("Good. you have found a letter",)
            findLetter.append(wordLetter)
            print (wordDab)
        else:
            print("This letter does not exist in the word")
            tentatives = tentatives - 1
        if(all(letter in findLetter for letter in choosenWord)):
            print("=======congratulation: you have found the good word=======",choosenWord)
            break
        if (tentatives == 0):
            print("you have lost. The word is: ",choosenWord)


continuer = "yes"       
while continuer == "yes":
    if continuer == "yes": 
        pendu() 
    continuer = input("enter 'yes' to continue or no to quit: ")        
print("-------Good Bye-------") 