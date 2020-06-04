class A:
    def __init__(self):
        self.a = 42

class B:
    def __init__(self):
        self.a = 47

class C(A, B):
    def __init__(self):
        super().__init__()
        print(self.a)



if __name__ == '__main__':

    c = C()
