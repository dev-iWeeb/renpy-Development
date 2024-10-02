#coding:utf-8
import sys
import unittest

sys.path.append('..')
from src.libs import Person
from unittest import TestCase


class TestPerson(TestCase):

    def test_if_person_is_created_with_dafaultValue(self):
        pDebard = Person("Debard", "Judgment")
        print ("with Default value..")

    def test_if_person_is_created(self):
        pDebard = Person("Debard", "Judgment", 22)
        print ("age 22..")
        self.assertIsInstance(pDebard, Person)

    def test_if_person_Older_is_positif_When_Older_negatif(self):
        pDebard = Person("Debard", "Judgment", -8)
        print("age -8..")
        self.assertGreater(pDebard.GetOlder(), 0)

    def test_if_person_Older_is_positif_When_Older_zero(self):
        pDebard = Person("Debard", "Jument", 0)
        print("age 0..")
        self.assertGreater(pDebard.GetOlder(), 0)




if __name__ == '__main__':
    unittest.main()


