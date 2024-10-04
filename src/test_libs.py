import unittest
import libs

from unittest import TestCase
from libs import Person, PersonFactory, PersonStd, Scene



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


class TestPersonStd (TestCase):

    def setUp(self):
        self.pPerson = PersonStd("Caroline", "Teacher")
        self.configStastic = ["Morale","Santé","Affinté","Confiance"]
        print(self.pPerson)

    def test_if_personStd_is_created_with_defaultValue (self):
        self.assertIsInstance(self.pPerson, PersonStd)


    def test_if_personStd_is_updated_with_setter (self):
        expression = 5
        self.pPerson.SetBodyCount(expression)
        self.assertEqual(self.pPerson.GetBodyCount(), expression)
        print(self.pPerson)


class TestFactoryPerson (TestCase):


    def test_if_person_is_created_in_Factory_with_defaultValue(self):
        pPerson = PersonFactory.create("Debard","Teacher")
        self.assertIsInstance(pPerson, Person)
        print("with Default value..")
        print(pPerson)


class TestFactoryPersonStd (TestCase):


    def test_if_person_is_created_in_Factory_with_defaultValue(self):
        pass


class TestScene (TestCase):

    def test_if_scene_is_created_with_defaultValue(self):
        pass

if __name__ == '__main__':
    unittest.main()


