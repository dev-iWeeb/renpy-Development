from src.libs import Completed, Launch, Logger, CollectionSceneFactory, PersonFactory, PersonFactoryStd, StackTokenFactory, RequestFactory, ExtensionSceneModule, FonctionSort, GamePlay, GameSessionStd, InjectionFonction, InjectionFxSort, Action, Stage, Staging, SingleTone, Person, Stats, Token; Launch, Stage, Stats, PersonFactory, PersonFactoryStd

print("Repliy anc Try programiz.pro")






## Test des Fonctions et Classes
print("********** SingleTone *****************")

login = Logger("Demo")
login2 = Logger ("demo")

print (login.GetValue())
print("login et login 2 sont identique ?", login is login2)

GameDemo = GamePlay()

GameDemo.AppendTokenToStackToken(Launch("intro"))
GameDemo.AppendTokenToStackToken(Stage("welcome",1))


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

jeton1 = Completed("Torride")

jeton2 = Launch("Lancement")


print(jeton1.GetScene())

print(jeton2.GetScene())

print(isinstance(jeton2, Completed))

print(isinstance(jeton2, Launch))

#print(type(jeton1))

#print(type(jeton2))

scoreScene = []

scoreScene.append(StackTokenFactory.CreateLaunch("Declaration"))
scoreScene.append(StackTokenFactory.CreateCompleted("Preambule"))
scoreScene.append(StackTokenFactory.CreateCompleted("Presentation"))
scoreScene.append(StackTokenFactory.CreateLaunch("Embauche"))

for Scene in scoreScene:
   print (str(type(Scene))+ " intitullé ; " + Scene.GetScene())


StageDemo = Stage("Dialogue",-1)

print ("on va evoluer la scene "+StageDemo.GetScene()+" de "+str(StageDemo.GetStep()))

