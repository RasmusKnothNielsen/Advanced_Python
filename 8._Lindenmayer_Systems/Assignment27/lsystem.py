from turtle import *

class LSystem:

    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def generation(self, n, word):
        if n == 0:
            return word
        else:
            result = ''
            for char in list(word):
                if char in self.rules:
                    result += self.rules[char]
                else:
                    result += char
            return self.generation(n-1, result)
    
    def draw(self, n, distance, angle):
        stack = []
        ls = self.generation(n, self.axiom)
        switcher = {
            'F': lambda: forward(distance),
            'G': lambda: forward(distance),
            '1': lambda: forward(distance),
            '0': lambda: forward(distance),
            '+': lambda: left(angle),
            '-': lambda: right(angle),
            '[': lambda: stack.append((xcor(), ycor(), heading())),
            ']': lambda: self.setXYZ(stack.pop())
        }
        for char in list(ls):
            func = switcher.get(char, lambda: None)
            func()
        
    def setXYZ(self, xyz):
        x, y, z = xyz
        up()
        setx(x)
        sety(y)
        seth(z)
        down()
