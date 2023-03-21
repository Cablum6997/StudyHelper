import glob
import os
import random


def createClass():
    while True:
        plainName = open("plainClassName.txt", "a")
        userinput = input("Enter name of Class: ")
        if userinput == "done":
            startScreen()
        plainName.write(userinput + "\n")
        userinput = userinput + ".txt"
        print(userinput, "Created!")
        classNameFile = open(userinput, 'w')


def addContent():
    while True:
        plainName = open("plainClassName.txt", "r")
        file_contents = plainName.read()
        print(file_contents)
        userinput = input("which class would you like to add content to? ")
        if userinput == "done":
            startScreen()
        userinput = userinput + ".txt"
        while True:
            
            classNameFile = open(userinput, 'a')
            theInput = input("Enter the question: ")
            if theInput == "done":
                addContent()
            classNameFile.write(theInput + " - ")
            theInput = input("Enter the answer to the question: ")
            classNameFile.write(theInput + "\n")

def study():
    ##init variables & lists
    index = 0
    x = 0
    wholeList = []
    questions = []
    answers = []
    ordRand = ["random", "order"]
    randord = 0
    randIndex = 0

    
    
    ## get class to study
    userinput = input("What class do you want to study? ")
    if userinput == 'done':
        startScreen()
    file = userinput + ".txt"
    theFile = open(file, "r")

    nextLine = theFile

    while userinput not in ordRand:
        userinput = input("Would you like your questions to be in a random or in order? (enter random or order) ")
        if userinput == "random":
            randord = 1
        if userinput == "order":
            randord == 0

    ##splitting the file and putting the contents into the correct lists
    
    while nextLine != "":
        nextLine = theFile.readline()
        anotherLine = nextLine.split("-")
        questions.append(anotherLine[0])
        
        answers.append(anotherLine[-1])
        wholeList.append(anotherLine)

    ch = '\n'
  
    answers = [elem.replace(ch, '') for elem in answers]

    questions.pop(-1)
    answers.pop(-1)

    
##    print(wholeList)
##    print(questions)
##    print(answers)
##    print(random.choice(questions))
    questionLength = 0
##    print(randord)
    if randord == 1:
##        randIndex = random.randint(0, len(questions))
        questionLength = len(questions)
        questionLength = questionLength -1
        randIndex = random.randint(0, questionLength)
##        print(randIndex)
##        print(questionLength)
        finished = ['done']
        print("type 'done' when you are done " + "\n")
        while userinput not in finished:
            
            try:
                x = x + 1
                question = questions[randIndex]
    ##            print(questions[randIndex])
                print(x,")", question)
                userinput = input("What is the answer to the question above ")
                if userinput == 'done':
                    study()
                if userinput in answers[randIndex] and userinput != "":
                    print("Correct!")
                else:
                    print("Incorrect!")
                randIndex = random.randint(0, questionLength)
            except IndexError:
                randIndex = random.randint(0, questionLength)
                pass

    if randord == 0:
        orderIndex = 0
        questionLength = len(questions)
        questionLength = questionLength -1
        finished = ['done']
        print("type 'done' when you are done " + "\n")
        while userinput not in finished:
            try:
                x = x + 1
                question = questions[orderIndex]
        ##            print(questions[randIndex])
                print(x,")", question)
                userinput = input("What is the answer to the question above ")
                if userinput == 'done':
                    study()
                if userinput in answers[orderIndex] and userinput != "":
                    print("Correct!")
                else:
                    print("Incorrect!")
               
                orderIndex = orderIndex + 1
            except IndexError:
                randIndex = random.randint(0, questionLength)
                orderIndex = 0
                pass
        



def quiz():
    randIndex = 0
    score = 0
    correct = 0
    options = ['ps', 'quiz']
    userinput = ''
    questions = []
    answers = []
    wholeList = []
    x = 1
    quizLength = 0
    Class = ""
    eachLine = ''
    scoreFile = open("QuizScores.txt", 'a')
    
    while userinput not in options:
        userinput = input("Would you ike to look at previous quiz scores or start a quiz (enter ps or quiz) ")


    if userinput == 'quiz':
        userinput = input("What class do you want to study? ")
        if userinput == 'done':
            startScreen()
        Class = userinput
        file = userinput + ".txt"
        theFile = open(file, "r")

        nextLine = theFile

        while nextLine != "":
            nextLine = theFile.readline()
            anotherLine = nextLine.split("-")
            questions.append(anotherLine[0])
            
            answers.append(anotherLine[-1])
            wholeList.append(anotherLine)

        ch = '\n'
      
        answers = [elem.replace(ch, '') for elem in answers]

        questions.pop(-1)
        answers.pop(-1)

        questionLength = 0

        questionLength = len(questions)
        questionLength = questionLength -1
        randIndex = random.randint(0, questionLength)
        quizLength = len(questions)
        
##        print(randIndex)
##        print(questionLength)
        finished = ['done']
        print("type 'done' when you are done " + "\n")
        while userinput not in finished:
            
            try:
                
                question = questions[randIndex]
    ##            print(questions[randIndex])
                print(x,")", question)
                userinput = input("What is the answer to the question above ")
                if userinput in answers[randIndex] and userinput != "":
                    print("Correct!")
                    questions.pop(randIndex)
                    answers.pop(randIndex)
                    correct = correct + 1
                    x = x + 1
                    
                else:
                    print("Incorrect!")
                    questions.pop(randIndex)
                    answers.pop(randIndex)
                    x = x + 1
                questionLength = len(questions)
                if questionLength == 0:
                    score = correct / quizLength * 100
                    score = str(score)
                    scoreFile.write(Class + " " + "-" + " " + score + "%" + "\n")
                    scoreFile.close()
                    print("Score:", score,"%")
                    userinput = input("Enter 'done' to continue: ")
                    if userinput == 'done':
                        
                        
                        startScreen()
                    
                randIndex = random.randint(0, questionLength)
                
                
            except IndexError:
                randIndex = random.randint(0, questionLength)
                pass
            

        
            
        
def startScreen():
    options = ['1', '2', '3', '4']
    userinput = ""

    while userinput not in options:
        
        userinput = input('''What would you like to do?
              1. Study
              2. Quiz
              3. Add Content
              4. Create new class

              Please Enter a number: ''')

    if userinput == "1":
        study()

    if userinput == "2":
        quiz()

    if userinput == "3":
        addContent()

    if userinput == "4":
        createClass()


startScreen()
