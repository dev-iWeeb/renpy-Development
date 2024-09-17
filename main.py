from src.libs import Launch, Logger, CollectionSceneFactory, StackTokenFactory, RequestFactory, ExtensionSceneModule, FonctionSort, GamePlay, GameSessionStd, InjectionFonction, InjectionFxSort, Action, Stage, Staging, SingleTone, Person, Token; Launch, Stage

print("Repliy anc Try programiz.pro")






## Test des Fonctions et Classes
print("********** SingleTone *****************")

login = Logger("Demo")
login2 = Logger ("demo")

print (login.GetValue())
print("login et login 2 sont identique ?", login is login2)

GameDemo = GamePlay()

GameDemo.AppendTokenToStackToken(Launch("intro"))
GameDemo.AppendTokenToStackToken(Stage("welcome",1).GetStep())


GameDemo2 = GamePlay()

GameTuto = GameSessionStd()

GameTuto.SetParamsValue("Fifo")
print (GameTuto.GetParams())

GameTuto.Check()

GameTuto.SetParamsValue("Fifi")
print (GameTuto.GetParams())

GameTuto1 = GameSessionStd()
print (GameTuto1.GetParams())

print("**********CEATE PERSONN *****************")


persoDebard = Stats ()

# affiniStat = Statistic("affinity", 5)
# print (affiniStat.key)
persoDebard.StatisticAppend ("affinity",100)
persoDebard.StatisticAppend ("Colère",2)
persoDebard.StatisticAppend ("Santé",20)
persoDebard.StatisticAppend ("Assurance",50)

#comptes = {"Georges Dupont": 10000, "Luc Martin": 150, "Lucas Anderson": 300, #"Alexandre Petit": 1800.clas74}

# print(persoDebard.getStatistic("Colère")) # -> 150


profilDebard = Person("Debard", "Professeur Histoire",persoDebard)

#profilDebard.Stats.increaseStatistic("affinity", 50)
#profilDebard.Stats.increaseStatistic("Santé")
#profilDebard.Stats.decreaseStatistic("Assurance",30)

#print (profilDebard.Stats.getStatistic("affinity"))
#print(profilDebard.Stats.getStatistic("Santé"))
#print (profilDebard.Stats.getStatistic("Assurance"))
print (profilDebard.GetOlder())

dictionaryDebard = {"name":"Debard", "occupation":"Professeur d histoire","age":35}
excluRenpy = "expression Renpy"

data = ("Affinity","Colère","Santé","Assurance")

# pDebard = PersonFactory(excluRenpy, dictionaryDebard["name"], dictionaryDebard["occupation"], data).getPerson()

pDebard = PersonFactory.create (dictionaryDebard["name"], dictionaryDebard["occupation"], data)

print(pDebard.GetStats().GetAllStatistics())

pDebard.SetSurname("Jument")

print (pDebard.GetSurname())

print("********** Surchage *****************")

dictionaryStd = {"name":"Anpunimous", "occupation":"Professeur d histoire","gender":"Femme", "age":35}

PStd = PersonFactoryStd.create (dictionaryStd["name"], dictionaryStd["occupation"], dictionaryStd["gender"], data)

print (PStd.GetGender())

print ("******************Objet Staging et Action ********************")



print("********** Scene *****************")

tScene = Scene("Intro")

print ('attribut de scene valeur :'+str(tScene.GetStatus()))

tScene.SwitchStatus()

print ('attribut de scene valeur :'+str(tScene.GetStatus()))


print("**** Object collectionScene****")
tempos =["intro","school","Welcome","atHome","interviews"]
#tempos =["intro"]

for tempo in tempos:
   print(tempo)

print ("nbre de scene : "+ str(len(tempos)))

fifoListeScene = CollectionSceneFactory.Create(tempos)

print (fifoListeScene["atHome"].GetName())
print (fifoListeScene["atHome"].IsFinished())

#fifoListeScene["intro"].SwitchToFinished()
#print (fifoListeScene["intro"].IsFinished())

fifoListeScene["Welcome"].GoNextStage()

for nameScene, value in fifoListeScene.items():
   sceneObject = value

   try:
      print (nameScene, sceneObject)
      test = 1/0
   except:
      print("mince....")
      break

stackToken = []
StackTokenFactory.AppendEndTokenCreated(stackToken, "intro")
StackTokenFactory.AppendLaunchTokenCreated(stackToken, "atHome")
StackTokenFactory.AppendStageTokenCreated(stackToken, "Welcome")

fifoListeScene=CollectionSceneFactory.UpdateScenesByStackToken(fifoListeScene, stackToken)

print("intro (end_False): "+str(fifoListeScene["intro"].IsFinished()))
print("atHome (Launch_True): "+str(fifoListeScene["atHome"].GetStatus()))
print("welcome (STage_0): "+str(fifoListeScene["Welcome"].GetStage()))

listDeModule = ["school","interviews"]

scenePlay = 2
currentWeek = 1
Community = {}
triggerModules = Request_timing (fifoListeScene, 1,2)
gamingModules = Request_gaming (fifoListeScene,{})
#sortModule = Request_sort(fifoListeScene, FonctionSort)
fonctionDeTirage = InjectionFxSort(FonctionSort)
params =[1]

ListeModulesTest = ExtensionSceneModule.Proceed (fifoListeScene, listDeModule, Community, scenePlay, currentWeek, fonctionDeTirage, params)

#print (triggerModules.Check())

print(triggerModules.GetStackToken())

print (ListeModulesTest)




print("+++++ Heritage +++++++")
#Heritage modele
class Mere:
    def parler(self):
        print("Je suis la mère")

class Pere:
    def jouer(self):
        print("Je suis le père")

class Enfant(Mere, Pere):
    pass

e = Enfant()
e.parler()  # Affiche "Je suis la mère"
e.jouer()  # Affiche "Je suis le père"

#print (type(e))
print(isinstance(e, Enfant))

Jeton = ("Launch","End")

jeton1 = End("Torride")

jeton2 = Launch("Lancement")


print(jeton1.GetScene())

print(jeton2.GetScene())

print(isinstance(jeton2, End))

print(isinstance(jeton2, Launch))

#print(type(jeton1))

#print(type(jeton2))

scoreScene = []

scoreScene.append(StackTokenFactory.CreateLaunch("Declaration"))
scoreScene.append(StackTokenFactory.CreateEnd("Preambule"))
scoreScene.append(StackTokenFactory.CreateEnd("Presentation"))
scoreScene.append(StackTokenFactory.CreateLaunch("Embauche"))

for Scene in scoreScene:
   print (str(type(Scene))+ " intitullé ; " + Scene.GetScene())


StageDemo = Stage("Dialogue",-1)

print ("on va evoluer la scene "+StageDemo.GetScene()+" de "+str(StageDemo.GetStep()))

