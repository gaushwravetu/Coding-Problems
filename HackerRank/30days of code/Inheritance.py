

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        result=0
        for score in scores:
            result += score
        avg = result/len(scores)
        if avg < 40:
            return 'T'
        elif avg < 55:
            return 'D'
        elif avg < 70:
            return 'P'
        elif avg < 80:
            return 'A'
        elif avg < 90:
            return 'E'
        else:
            return 'O'


   
