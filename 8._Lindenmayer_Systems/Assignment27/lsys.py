class LSystem():
    
    def __init__(self, state, rules):
        self.state = state
        self.rules = rules
    
    def __str__(self):
        return self.state
    
    def evolve(self, num_iter = 1):
        for i in range(num_iter):
            result = ""
            for char in self.state:
                if char in self.rules:
                    result += self.rules[char]
                else:
                    result += char
            self.state = result
