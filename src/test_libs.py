import unittest

from unittest import TestCase
from libs import Person, PersonFactory, PersonStd, Stats, PersonFactoryStd, Scene, Module, Do, Staging, InteractDefault


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


class Test_Action_InteractDefault(TestCase):

    def setUp(self):
        self.nameP1 = "Constante"
        self.nameP2 = "PtitJean"
        self.nameP3 = "Gus"
        self.nameP4 = "PtitVier"
        self.members = [self.nameP2, self.nameP3]
        self.pP1 = PersonStd( self.nameP1 , "Fleuriste")
        self.pP2 = PersonStd( self.nameP2, "Etudiant", 16)
        self.pP3 = PersonStd(self.nameP3, "Etudiant", 14)
        self.pP4 = PersonStd(self.nameP4,"Jardinier")
        self.pMembers = [self.pP2, self.pP3]
        self.community = {self.nameP1: self.pP1, self.nameP2: self.pP2 , self.nameP3: self.pP3}
        self.Staging = Staging(self.community, InteractDefault)
        self.Staging.ToSTagePerson(self.nameP1)
        self.Staging.ToSTagePerson(self.nameP2)
        self.Staging.ToSTagePerson(self.nameP3)
        print("réinit")

    def test_a_person_affected_to_Goto_and_GetFrom_for_speaking_and_using_DialogueDefault(self):
        print(f'GetFrom.GetName : {self.Staging.GetAction().Speak(self.nameP1, self.nameP2).GetFrom()}')
        self.assertEqual(self.nameP1, str(self.Staging.GetAction().Speak(self.nameP1, self.nameP2).GetFrom().GetName()))
        self.assertEqual(self.nameP2,str(self.Staging.GetAction().Speak(self.nameP1, self.nameP2).GetTo()[0].GetName()))

    def test_b_if_person_affected_on_Goto_and_GetFrom_are_Not_in_listMembers(self):
        self.assertIsNone(self.Staging.GetAction().Speak(self.nameP4, self.nameP2).GetFrom())
        self.assertEqual(f'[]',f'{self.Staging.GetAction().Speak(self.nameP4, self.nameP2).GetTo()}')

    def test_c_person_affected_on_Goto_and_GetFrom_by_list_for_speaking_and_using_DialogueDefault(self):
        self.assertEqual(self.nameP1, str(self.Staging.GetAction().Speak(self.nameP1, self.members).GetFrom().GetName()))
        self.assertEqual(f'{self.pMembers}', f'{self.Staging.GetAction().Speak(self.nameP1, self.members).GetTo()}')

    def test_d_if_person_answer_without_speaking_before(self):
        self.Staging.GetAction().Answer(self.nameP1)
        self.assertEqual("[]", f'{self.Staging.GetAction().Answer(self.nameP1)}')


class Test_PersonProfileFactory(TestCase):

    def setUp(self):
        self.nameP1 = "PtitJean"
        self.nameP2 = "Constante"
        self.nameP3 = "Gus"
        self.key_impressions = "impressions"
        self.pP1 = PersonStd(self.nameP1, "Fleuriste")
        self.pP2 = PersonStd(self.nameP2, "Etudiant", 16)
        self.pP3 = PersonStd(self.nameP3 ,"Journaliste")
        self.profilpP1Fin = { self.key_impressions: {self.nameP1:{}}}
        self.profilpP3 = { self.key_impressions: {}}
        self.profilpP3Fin ={ self.key_impressions: {self.nameP2:{}}}
        self.pP3.SetProfile(self.profilpP3)

    def test_a_if_impressionProfil_is_created_on_Person(self):
        self.pP2 = PersonFactory.InsertProfileImpression(self.pP2,self.pP1)
        self.assertEqual(f'{self.profilpP1Fin}', f'{self.pP2.GetProfile()}')

    def test_b_if_profilPerson_is_created_on_impression(self):
        self.pP3 =PersonFactory.InsertProfileImpression(self.pP3, self.pP2)
        self.assertEqual( f'{self.profilpP3Fin}', f'{self.pP3.GetProfile()}')

    def test_c_if_profilPerson_must_be_updated(self):
        pP4 = self.pP3
        pP4.SetProfile(self.profilpP1Fin)
        self.assertEqual(f'{self.profilpP1Fin}', f'{pP4.GetProfile()}')


class Test_Staging(TestCase):

    def setUp(self):
        self.nameP1 = "Constante"
        self.nameP2 = "PtitJean"
        self.nameP3 = "Gus"
        self.key_impressions = "impressions"
        self.members = [self.nameP2, self.nameP3]
        self.pP1 = PersonStd("Constante","Fleuriste")
        self.pP2 = PersonStd("PtitJean","Etudiant",16)
        self.pP3 = PersonStd(self.nameP3,"Etudiant", 14)
        self.profilpP2Fin = {self.key_impressions: {self.nameP1: {}}}
        self.community = {self.nameP1: self.pP1, self.nameP2: self.pP2, self.nameP3: self.pP3}
        self.Staging = Staging( self.community,InteractDefault)

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

    def test_of_two_persons_speak(self):
        self.Staging.ToSTagePerson(self.nameP1)
        self.Staging.ToSTagePerson(self.nameP2)
        self.Staging.ToSTagePerson(self.nameP3)
        self.Staging.GetAction().Speak(self.nameP1, self.nameP2)
        print(f'2 person speak test {self.Staging.GetAction().GetMembers()[self.nameP2]}')
        self.assertEqual(self.Staging.GetAction().GetMembers()[self.nameP2].GetName(), self.nameP2) #TODO inseet profile
        responseCheck = self.Staging.GetAction().Answer(self.nameP1)
        self.assertEqual(self.nameP2, responseCheck.GetFrom().GetName())
        self.assertEqual(self.nameP1, responseCheck.GetTo()[0].GetName())

    def test_if_impression_profil_is_created_in_person_when_speaking(self):
        self.Staging.ToSTagePerson(self.nameP1)
        self.Staging.ToSTagePerson(self.nameP2)
        self.Staging.ToSTagePerson(self.nameP3)
        resultDiscuss = self.Staging.GetAction().Speak(self.nameP1, self.nameP2)
        self.assertEqual(f'{self.profilpP2Fin}',f'{resultDiscuss.GetTo()[0].GetProfile()}')

    def tearDown(self):
        print(f"nbre members dans action Actuellement : {len(self.Staging.GetPersons())}")



if __name__ == '__main__':
    unittest.main()


