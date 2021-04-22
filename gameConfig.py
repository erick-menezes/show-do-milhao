import json

class Game():
    def __init__(self):
        self.file = open('./questions.json', 'r', encoding='utf-8')
        self.perguntas = json.load(self.file)

    # Ainda trabalhando nisso!
    #       
    #     self.total = 0
    #     self.pular = 3
    #     self.passe = []

    # def ganhar():
    #     if self.total >= 0 and self.total < 5000:
    #         self.ponto = self.total + 1000
    #     elif self.total == 5000:
    #         self.ponto = self.total + 5000
    #     elif self.total > 5000 and self.total < 50000:
    #         self.ponto = self.total + 10000
    #     elif self.total == 50000:
    #         self.ponto = self.total + 50000
    #     elif self.total > 50000 and self.total < 500000:
    #         self.ponto = self.total + 100000
    #     else:
    #         self.ponto = self.total + 500000

    #     return str(self.ponto)

    # def iniciarJogo():
    #    return null 