print ("devoppement de base.. python")

CONST_INCREASE=1
CONST_DESINCREASE= -1
CONST_DEFAULT_AGE = 35
CONST_DEFAULT_STATISTIC = 5
CONST_DEFAULT_INIT_STAGE = 0
CONST_START_CYCLE_AT = 1
CONST_SYST_MODULE_ENABLE = True




class Scene:


   def __init__(self, name, start=CONST_START_CYCLE_AT, status=True, stage=CONST_DEFAULT_INIT_STAGE, index = CONST_INCREASE):
       self.__SetName(name)
       self.SetStart(start)
       self.SetStatus(status)
       self.SetStage(stage)
       self.__index = index
       self.__finished = False

   def __SetName (self, name):
      self.__name = name

   def SetStart (self, start=CONST_START_CYCLE_AT):
      self.__start= start

   def SetStatus (self, status):
      self.__status = status 

   def SetStage(self, stage=CONST_DEFAULT_INIT_STAGE):
      self.__stage = stage

   def SwitchStatus (self):
      self.__status = not self.__status

   def SwitchToFinished (self):
      self.__finished = not self.__finished

   def GoNextStage(self):
      self.__stage += self.__index

   def GoPreviousStage (self):
      self.__stage -= self.__index

   def GetName (self):
      return self.__name

   def GetStart(self):
      return self.__start

   def GetStatus (self):
      return self.__status

   def GetStage(self):
      return self.__stage

   def IsFinished(self):
      return self.__finished


class Stats:


   def __init__(self):
      self.__stats = {}

   def GetStatistic(self, key):
      return self.__stats[key]

   def SetStatistic(self, key,newValue):
      self.__stats[key]= newValue

   def IncreaseStatistic (self, key, increase = CONST_INCREASE):
      self.__stats[key]+=increase

   def DecreaseStatistic (self, key, decrease = CONST_DESINCREASE):
      self.__stats[key]-=decrease

   def GetLenStats (self):
      return len(self.__stats)

   def StatisticAppend (self, key, value):
      self.__stats[key] = value

   def GetAllStatistics(self):
      return self.__stats


class Person:


   def __init__(self, name, occupation, Stats={}, age=CONST_DEFAULT_AGE,  surname = ""): 
      self.__name = name
      self.SetStats(Stats)
      self.SetOlder (age)
      self.SetOccupation (occupation)
      self.SetSurname (surname)

   def SetSurname (self, surname):
      self.__surname = surname

   def SetStats(self, Stats):
      self.__Stats = Stats

   def SetOlder(self, older):
      self.__older = older

   def SetOccupation(self, occupation):
      self.__occupation = occupation

   def GetName(self):
      return self.__name

   def GetSurname(self):
      return self.__surname

   def GetStats(self):
      return self.__Stats

   def GetOlder(self):
      return self.__older

   def GetOccupation(self):
      return self.__occupation


class PersonStd(Person):


   def __init__(self,name, occupation, gender, Stats={}, age=CONST_DEFAULT_AGE,  surname = ""):
      super().__init__(name, occupation, Stats, age, surname)
      self.SetGender(gender)

   def SetGender (self, gender):
      self.__gender = gender

   def GetGender (self):
      return self.__gender


class PersonFactoryOld:

   def __init__(self, character, name, occupation, personstats, age=CONST_DEFAULT_AGE, surname=""):
      self.personObject = self.createPerson (character, name, occupation, personstats, age, surname)

   def createPerson(self, character, name, occupation, personstats, age, surname=""):
      StatsData = self.__CreateStats (personstats)
      personObject = Person(character, name, occupation, StatsData, age, surname)

      return personObject

   def __CreateStats(self, Statistics):
      Liste = Stats()

      for statistic in Statistics:
         Liste.statisticApend(statistic, CONST_DEFAULT_STATISTIC)

      return Liste

   def getPerson(self):
      return self.personObject


class PersonFactory:  

   @staticmethod
   def create (name, occupation, personstats, age=CONST_DEFAULT_AGE, surname=""):
      StatsData = PersonFactory.CreateStats (personstats)
      return Person(name, occupation, StatsData, age, surname)

   @staticmethod
   def CreateStats(Statistics, value =CONST_DEFAULT_STATISTIC):
      Liste = Stats()

      for statistic in Statistics:
         Liste.StatisticAppend(statistic, value)

      return Liste


class PersonFactoryStd (PersonFactory):

    @staticmethod
    def create (name, occupation, gender, personstats, age=CONST_DEFAULT_AGE, surname=""):
      StatsData = PersonFactoryStd.CreateStats (personstats)
      return PersonStd(name, occupation, gender, StatsData, age, surname)


class CollectionSceneFactory:

      @staticmethod
      def CreateScene(nameScene):
         return Scene(nameScene)

      @staticmethod
      def Create(nameScene):
         Liste = {}

         for scene in nameScene:
            Liste[scene] = CollectionSceneFactory.CreateScene(scene)

         return Liste

      @staticmethod
      def UpdateScenesByStackToken (collectionScene, stackToken):

         if len(stackToken)>0 and len(collectionScene)>0:

            for Token in stackToken:

               if StackTokenFactory.IsTypeOfLaunch(Token):

                  collectionScene[Token.GetScene()].SwitchStatus()

               elif StackTokenFactory.IsTypeOfEnd(Token):

                  collectionScene[Token.GetScene()].SwitchToFinished()

               elif StackTokenFactory.IsTypeOfStage(Token):

                  if Token.GetMode():

                     if Token.GetStep()>0:

                        collectionScene[Token.GetScene()].GoNextStage()

                     else: 
                        collectionScene[Token.GetScene()].GoPreviousStage()

                  else:
                     collectionScene[Token.GetScene()].SetStage(Token.GetStep())

         return collectionScene


class Token:


      def __init__(self, nameScene):
         self.__name = nameScene

      def GetScene (self):
         return self.__name


class End (Token):
   pass


class Launch (Token):
   pass


class Stage (Token):


   def __init__ (self,idScene, step):
      super().__init__(idScene)
      self.__step = step
      self.__mode = True

   def GetStep (self):
      return self.__step

   def GetMode (self):
      return self.__mode

   def SwitchMode(self):
      self.__mode = not self.__mode
      return self.__mode


class StackTokenFactory:

   @staticmethod
   def CreateLaunch (nameScene):
      return Launch(nameScene)

   @staticmethod
   def CreateEnd (nameScene):
      return End(nameScene)

   @staticmethod
   def CreatedStage (nameScene, step):
      return Stage(nameScene, step)

   @staticmethod
   def IsTypeOfLaunch(token:Token):
      return isinstance (token, Launch)

   @staticmethod
   def IsTypeOfEnd (token:Token):
      return isinstance (token, End)

   @staticmethod
   def IsTypeOfStage(token:Token):
      return isinstance (token, Stage)

   @staticmethod
   def AppendLaunchTokenCreated (collection, nameScene):
      Token = StackTokenFactory.CreateLaunch(nameScene)
      return collection.append (Token)

   @staticmethod
   def AppendEndTokenCreated (collection, nameScene):
      Token = StackTokenFactory.CreateEnd (nameScene)
      return collection.append (Token)

   @staticmethod
   def AppendStageTokenCreated (collection, nameScene, step=CONST_INCREASE, mode=True):
      Token = StackTokenFactory.CreatedStage(nameScene, step)

      if not mode:
         Token.SwitchMode()

      return collection.append(Token)


class Request:


   def __init__ (self, stackToken):
      self.__stacktoken = stackToken

   def Check(self):
      pass

   def GetStackToken (self):
      return self.__stacktoken

   def SetStackToken (self, stackToken):
      self.__stacktoken = stackToken


class Request_timing (Request):


   def __init__ (self, stackToken, currentCycle, index):
      super().__init__(stackToken)
      self.__currentCycle = currentCycle
      self.__index = index


class Request_gaming (Request):


   def __init__(self, stackToken, community):
      super().__init__(stackToken)
      self.__community= community


class Request_sort (Request):


   def __init__ ( self, CollectionModule, FonctionSort):
      self.__resultModules = CollectionModule
      self.__FonctionSort = FonctionSort

   def SetCollectionModule (self, CollectionModule):
      self.__CollectionModule = CollectionModule 

   def GetCollectionModuleSort (self):
      return self.__CollectionModule



class RequestFactory:


   def CreateRequestTiming (stackToken, currentCycle, index):
      return Request_timing(stackToken, currentCycle, index)

   def CreateRequestGaming (stackToken, community):
      return Request_gaming (stackToken, community)

   def CreateRequestSort (CollectionModule, FonctionSort):
      return Request_sort (CollectionModule, FonctionSort)


class FonctionSort:


   def TakeFirstElementInCollection (Collection):
      result = {}
      element = next(iter(Collection.items()))
      result[element[0]] = element[1]
      return result

   def TakeNfirstElementinCollection (Collection, n):
      result = {}
      if len (Collection)<n:
         n=len(Collection)

      keysIter = iter(Collection.keys())
      index =0
      while index <n:
         libelle = next(keysIter)
         result[libelle] = Collection[libelle]
         index +=1

      return result





#label Run_sceneModule:
class ExtensionSceneModule:

   @staticmethod
   def CreateCollectionModule (CollectionScenes, listeModule):
       CollectionModules = {}

       for indexModule in listeModule:
             CollectionModules[indexModule] = CollectionScenes[indexModule]

       return CollectionModules



   def Proceed (CollectionsScenes, listeModule, Commnunity, scenePlay, currentCycle, fonctionTriage, params= [], FactoryRequest= RequestFactory):

      if len(listeModule)>0:
         stackToken = []
         RequestTiming = FactoryRequest.CreateRequestTiming (stackToken, currentCycle, scenePlay)
         stackToken = ExtensionSceneModule.GetStackTokenoduleByTrigger(RequestTiming)

         RequestGaming = FactoryRequest.CreateRequestGaming (stackToken, Commnunity)
         stackToken = ExtensionSceneModule.GetStackTokenModuleByGaming (RequestGaming, stackToken)

         if len(stackToken)>0:
            CollectionsScenes = CollectionSceneFactory.UpdateScenesByStackToken(CollectionsScenes, stackToken)

      return ExtensionSceneModule.GetCollectionModuleSort (CollectionsScenes, listeModule, fonctionTriage, params)


   def GetStackTokenoduleByTrigger (RequestTiming:Request):

      RequestTiming.Check()
      return RequestTiming.GetStackToken()


   def GetStackTokenModuleByGaming (RequestGaming:Request, stackToken):

      RequestGaming.SetStackToken(stackToken)
      RequestGaming.Check()
      return RequestGaming.GetStackToken()


   def GetCollectionModuleActive (CollectionsScene,listeModule):

      result = {}
      for module in listeModule:
         if CollectionsScene[module].GetStatus():
            result[module] = CollectionsScene[module]

      return result


   def GetCollectionModuleSort (CollectionScenes, listeModule, fonctionTriage, params):

      CollectionModule = ExtensionSceneModule.GetCollectionModuleActive(CollectionScenes, listeModule)
      fonctionTriage.Setter (CollectionModule, params)
      result = fonctionTriage.GetFonctionSelected()
      return result



class GamePlay:

   __instance = None
   __stacktoken = []


   def __new__(cls):

      if cls.__instance is None:
         print('Creating the object')
         cls.__instance = super(GamePlay, cls).__new__(cls)

         # Put any initialization here.

      return cls.__instance


   def AppendTokenToStackToken (cls, Token:Token):  

      cls.__stacktoken.append (Token)


   def CheckScore (cls, community):

      cls.__stacktoken = []
      cls.__community = community


   def Proceed():
      pass



class SingleTone:

   __instance = None
   __params = []


   def __new__(cls):

         if cls.__instance is None:
            print('Creating the object')
            cls.__instance = super(SingleTone, cls).__new__(cls)

            # Put any initialization here.

         return cls.__instance


   def SetParamsValue (cls,params):
      cls.__params.append (params)


   def SetParamsTable (cls, params):
      cls.__params = params

   def GetParams (cls):
      return cls.__params



class GameSessionStd (SingleTone):

   def Check (cls):
      print("Notification de GameSession.. active")


class Logger(object):

   _instance = None


   def __new__(cls, value):

      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(Logger, cls).__new__(cls)
         # Put any initialization here.
         cls._value = value

      return cls._instance

   def GetValue(cls):
      return cls._value


"""

   def GetValue (self):
      return self.__value
"""


class InjectionFonction:

   def __init__(self, fonctionInjected):
      self.fx = fonctionInjected

   def Setter (self, Collection, params):
      self.Collection = Collection
      self.params = params

   def GetFonctionSelected ():
    pass


class InjectionFxSort (InjectionFonction):

   def GetFonctionSelected (self):
      return self.fx.TakeNfirstElementinCollection (self.Collection,self.params[0])


def move_zeroes_to_end(n):

   nToStr = str(n)
   numberSort = ""

   for number in nToStr:

      if number =="0":
            numberSort = numberSort + number
      else: 
            numberSort = number + numberSort

   return int(numberSort)


class Action:


   def __init__(self):
      self.__Members = {}


   def AppendMember (self, keyMember, Member):

      if keyMember not in self.__Members: #32
         self.__Members[keyMember] = Member 

   def RemoveMemberFrom (self, keyMember):

      if keyMember in self.__Members: #32
         del self.__Members[keyMember]

   def GetMembers (self):
      return self.__Members

   def SetMembers (self, Members):
      self.__Members = Members


class Staging: # Version python


   def __init__(self, Community, Action:Action):
      self.__Community = Community
      self.__Action =  Action
      self.__moreAction = ""

   def ToSTagePerson (self, namePerson):

      if namePerson in self.__Community: #32
         self.__Action.AppendMember (namePerson, self.__Community [namePerson])

   def ExcludePerson (self, namePerson):
         self.__Action.RemoveMemberFrom (namePerson)

   def GetPersons (self):
      return self.__Action.GetMembers

   def SetAction (self, Action):
      self.__Action = Action

   def AppendMoreAction (self, Action):
      self.__moreAction = Action



## Test des Fonctions et Classes
print("**********Ch1*************")

nbre = 1020304050


print(move_zeroes_to_end (nbre))

modulo = 1%2

print(modulo)

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
