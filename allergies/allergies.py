#  File:       allergies.py
#  Purpose:    Write a program that, given a person's allergy score.
#  Programmer: Amal Shehu
#  Course:     Exercism
#  Date:       Saturday 3rd September 2016, 06:00 PM


class Allergies:

    allergy_score = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score
        self.lst = list(item for item in self.allergy_score if
                        self.is_allergic_to(item))

    def is_allergic_to(self, allergens):
        return self.allergy_score[allergens] & self.score
