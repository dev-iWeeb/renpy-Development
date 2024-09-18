#coding:utf-8
import sys
sys.path.append ('..')
from src.libs import Person
import unittest


class TestPerson(unittest.TestCase):

  def Test_if_person_is_created(self):

    pDebard = Person("Debard", "Judgment", "Femme", 35)
    self.assertIsInstance(pDebard, Person)

  def Test_if_person_Older_is_positif_When_Older_negatif (self):
    pDebard = Person("Debard", "Judgment", "Femme", -8)
    self.assertGreater(pDebard.GetOlder(), 0)

  def Test_if_person_Older_is_positif_When_Older_zero (self):
    pDebard = Person("Debard", "Jument", "Femme", 0)
    self.assertGreater(pDebard.GetOlder(), 0)
    


if __name__ == '__main__':
    unittest.main()


    
  