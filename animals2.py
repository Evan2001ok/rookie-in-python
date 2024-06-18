class Dog:
    def speak(self):
        print("woof!")

    def learnname(self, name):
        self.name = name

    def hear(self, words):#when dog hear some one call it, dog speak
        if self.name in words:
            self.speak()
