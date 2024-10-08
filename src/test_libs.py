import unittest
import libs

from unittest import TestCase
from libs import Person, PersonFactory, PersonStd, Stats, PersonFactoryStd, Scene, Module, Do, DialogueStd, Staging, DialogueDefault


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
        self.assertIsInstance(self.tScene, Scene)

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


class Test_DialogueStd(TestCase):


    def setUp(self):
        self.speak = "Speak"
        self.laugh = "Laugh"
        self.shout = "Shout"
        self.DialogueStd = DialogueStd(self.speak,self.laugh,self.shout)

    def test_if_class_DialogueStd_is_created(self):
        self.assertIsInstance(self.DialogueStd,DialogueStd)
        self.assertIsInstance(self.DialogueStd, Do)

    def test_if_attr_DialogueStd_accessible(self):
        self.assertEqual(self.DialogueStd.speak, self.speak)
        self.assertEqual(self.DialogueStd.laugh, self.laugh)
        self.assertEqual(self.DialogueStd.shout, self.shout)
        self.assertNotEqual(self.DialogueStd.speak,self.shout)


class Test_Staging(TestCase):

    def setUp(self):
        self.speak = "Speak"
        self.laugh = "Laugh"
        self.shout = "Shout"
        self.DialogueStd = DialogueStd(self.speak, self.laugh, self.shout)

        self.caresser = "Caresser"
        self.kiss = "Kiss"
        self.enlacer = "Enlacer"

        class GesteStd(Do):

            def __init__(self, caresser, kiss, enlacer):
                self.caresser = caresser
                self.kiss = kiss
                self.enlacer = enlacer

        self.GesteStd = GesteStd(self.caresser, self.kiss, self.enlacer)

        self.nameP1 = "Constante"
        self.nameP2 = "PtitJean"
        self.nameP3 = "Gus"
        self.members = [self.nameP2, self.nameP3]

        pP1 = PersonStd("Constante","Fleuriste")
        pP2 = PersonStd("PtitJean","Etudiant",16)
        self.community = {}
        self.community[self.nameP1] = pP1
        self.community[self.nameP2] = pP2

        self.Staging = Staging( self.community,DialogueDefault)


    def test_if_Staging_is_created(self):
        self.assertIsInstance(self.Staging, Staging)

    def test_of_GestionMembers_in_ActionClass(self):
        print(f"nbre members dans action : {len(self.Staging.GetPersons())}")
        self.Staging.ToSTagePerson(self.nameP1)
        self.assertGreater(len(self.Staging.GetPersons()), 0)
        print(f"nbre members dans action après inclusion: {len(self.Staging.GetPersons())}")
        self.Staging.ToSTagePerson(self.nameP1)
        print(f"nbre members dans action après inclusion: {len(self.Staging.GetPersons())}")
        self.Staging.ToSTagePerson(self.nameP3)
        print(f"nbre members dans action après inclusion: {len(self.Staging.GetPersons())}")
        self.Staging.ToSTagePerson(self.nameP2)
        print(f"nbre members dans action après inclusion: {len(self.Staging.GetPersons())}")
        self.Staging.ExcludePerson(self.nameP1)
        print(f"nbre members dans action après inclusion: {len(self.Staging.GetPersons())}")
        self.Staging.ExcludePerson(self.nameP3)

    """
    def test_if_attr_of_Action_is_accessible(self):
        self.assertEqual(self.Staging.GetAction().speak, self.speak)
        self.assertEqual(self.Staging.GetAction().laugh, self.laugh)
        self.assertEqual(self.Staging.GetAction().shout, self.shout)
        self.Staging.SetAction(self.GesteStd)
        self.assertNotEqual(self.Staging.GetAction().kiss, self.speak)
        self.assertEqual(self.Staging.GetAction().kiss, self.kiss)
        self.assertEqual(self.Staging.GetAction().enlacer, self.enlacer)
        self.assertEqual(self.Staging.GetAction().caresser, self.caresser)

    def test_simulation_of_code_to_action(self):
        self.Staging.GetAction().SetTo(self.nameP1)
        self.assertTrue(isinstance(self.Staging.GetAction().GetTo(), (list, dict, tuple)))
        print(self.Staging.GetAction().GetTo())
        
       
        self.assertEqual(self.Staging.GetAction().speak, self.speak)
        self.Staging.GetAction().SetTo(self.members)
        self.assertTrue(isinstance(self.Staging.GetAction().GetTo(), (list, dict, tuple)))
        print(self.Staging.GetAction().GetTo())
    """

    def test_simulation_of_code_to_DialogueDefault(self):
        print (self.Staging.GetAction().speak(self.nameP1, self.nameP2))

    def tearDown(self):
        print(f"nbre members dans action Actuellement : {len(self.Staging.GetPersons())}")



if __name__ == '__main__':
    unittest.main()


