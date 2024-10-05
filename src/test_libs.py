import unittest
import libs

from unittest import TestCase
from libs import Person, PersonFactory, PersonStd, Stats, PersonFactoryStd, Scene, Module

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

    def setUp(self):
        self.pPerson = PersonFactory.create("Debard","Teacher")
        self.configStastic = ["Morale", "Santé", "Affinté", "Confiance"]

    def test_if_person_is_created_in_Factory_with_defaultValue(self):
        self.assertIsInstance(self.pPerson, Person)
        print("with Default value..")
        print(self.pPerson)

    def test_if_person_is_updated_by_statistic (self):
         self.pPerson = PersonFactory.updatePersonByStats(self.pPerson, self.configStastic)
         self.assertIsInstance(self.pPerson.GetStats(), Stats)
         self.assertGreater(self.pPerson.GetStats().GetLenStats(), 0)



class TestFactoryPersonStd (TestCase):

    def setUp(self):
        self.configStastic = ["Morale", "Santé", "Affinté", "Confiance"]

    def test_if_person_is_created_in_Factory_with_defaultValue(self):
        self.pPerson = PersonFactoryStd.create("Debard","Teacher")
        self.assertIsInstance(self.pPerson, Person)
        print("with Default value..")
        print(self.pPerson)

    def test_if_person_is_created_in_Factory_with_new_params(self):
        expression = 5
        self.pPerson = PersonFactoryStd.create("Debard", "Teacher", 35, {},[], "",5)
        self.assertIsInstance(self.pPerson, PersonStd)


class TestScene (TestCase):

    def setUp(self):
        self.tScene = Scene ( "intro")

    def test_if_scene_is_created_with_defaultValue(self):
        self. assertIsInstance(self.tScene, Scene)

    def test_if_Module_is_created_with_defaultValue(self):
        tModule = Module ("phone")
        self.assertIsInstance(tModule, Module)

    def test_if_scene_switch_to_finished(self):
        self.tScene.SwitchToFinished()
        self.assertTrue(self.tScene.IsExecuted())

    def test_if_scene_switch_to_Desactive(self):
        self.tScene.SwitchStatus()
        self.assertFalse(self.tScene.GetStatus())

    def test_if_scene_go_to_nextStage(self):
        print(f"stage of this scene : {self.tScene.GetStage()}")
        expression = 1
        self.tScene.GoNextStage()
        print(f"next Stage of this scene : {self.tScene.GetStage()}")
        self.assertEqual(self.tScene.GetStage(), expression)

    def test_if_scene_jump_to_Stage(self):
        print(f"stage of this scene : {self.tScene.GetStage()}")
        expression = 5
        self.tScene.SetStage(expression)
        print(f"next Stage of this scene : {self.tScene.GetStage()}")
        self.assertEqual(self.tScene.GetStage(), expression)

    def test_if_scene_jump_to_negativeStage(self):
        expression = -3
        self.tScene.SetStage(expression)
        self.assertGreaterEqual(self.tScene.GetStage(), 0)



if __name__ == '__main__':
    unittest.main()


