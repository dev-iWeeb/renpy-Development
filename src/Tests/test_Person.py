import unittest
from libs import Person 

class TestPerson(unittest.TestCase):

  def Test_if_person_is_created(self):

    pDebard = Person("Debard", "Jument", "Femme", 35)
    self.assertIsInstance(pDebard, Person)

  def Test_if_person_Older_is_positif_When_Older_negatif (self):
    pDebard = Person("Debard", "Jument", "Femme", -8)
    self.assertGreater(pDebard.GetOlder(), 0)

  def Test_if_person_Older_is_positif_When_Older_zero (self):
    pDebard = Person("Debard", "Jument", "Femme", 0)
    self.assertGreater(pDebard.GetOlder(), 0)
    
    
    

    '''''
    dictionaryStd = {"name": "Anpunimous", "occupation": "Professeur d histoire", "gender": "Femme", "age": 35}
    PStd = PersonFactory.create(dictionaryStd["name"], dictionaryStd["occupation"], dictionaryStd["gender"], data)
    self.assertEqual(PStd.GetGender(), dictionaryStd["gender"])
    self.assertEqual(PStd.GetSurname(), dictionaryStd["name"])
    self.assertEqual(PStd.GetOccupation(), dictionaryStd["occupation"])
    self.assertEqual(PStd.GetAge(), dictionaryStd["age"])
    
  