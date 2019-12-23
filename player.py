class WOFPlayer:
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self,amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):
    def __init__(self,name):
        WOFPlayer.__init__(self,name)

    def getMove(self,category, obscuredPhrase, guessed):
        Category = input("Category: {}").format(self.category)
        Phrase = input("obscured_phrase: {}").format(self.obscuredPhrase)
        Guessed =  input("guessed: {}").format(self.guessed)

        return input("Guess a letter, phrase, or type 'exit' or 'pass':")

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        list = []
        if self.prizemoney >= 250:
            for l in LETTERS:
                list.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    list.append(l)
        return list

    def getMove(self, category, obscuredPhrase, guessed):
        list = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(list) == 0:
            return 'pass'
        else:
            if FlipResult==True:
                for l in self.SORTED_FREQUENCIES:
                    if l in list:
                        return l
            elif FlipResult==False:
                return random.choice(list)
