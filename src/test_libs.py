#coding:utf-8
import sys
import unittest
sys.path.append('')

from src.libs import Person, PersonFactory


from unittest import TestCase


class TestPerson(TestCase):

    def test_if_person_is_created_with_defaultValue(self):
        pDebard = Person("Debard", "Teacher")
        self.assertIsInstance(pDebard, Person)
        print ("with Default value..")
        print (pDebard)

    def test_if_person_is_created(self):
        pDebard = Person("Debard", "Teacher", 22)
        self.assertIsInstance(pDebard, Person)
        print("age 22..")
        print (pDebard)

    def test_if_person_Older_is_positif_When_Older_negatif(self):
        pDebard = Person("Debard", "Teacher", -8)
        print("age -8..")
        self.assertGreater(pDebard.GetOlder(), 0)
        print (pDebard)

    def test_if_person_Older_is_positif_When_Older_zero(self):
        pDebard = Person("Debard", "Teacher", 0)
        print("age 0..")
        self.assertGreater(pDebard.GetOlder(), 0)
        print(pDebard)


class TestFactoryPerson (TestCase):


    def test_if_person_is_created_in_Factory_with_defaultValue(self):
        pPerson = PersonFactory.create("Debard","Teacher")
        self.assertIsInstance(pPerson, Person)
        print("with Default value..")
        print(pPerson)



if __name__ == '__main__':
    unittest.main()


