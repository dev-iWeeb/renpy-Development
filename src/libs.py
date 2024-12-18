CONST_INCREASE_DESINCREASE = 1
CONST_DEFAULT_AGE = 35
CONST_DEFAULT_LEGAL_AGE = 18
CONST_DEFAULT_STATISTIC = 5
CONST_DEFAULT_INIT_STAGE = 0
CONST_START_CYCLE_AT = 1
CONST_DEFAULT_BODYCOUNT = 0
CONST_SYST_MODULE_ENABLE = True
CONST_SPEAK_ANSWER_DIAG_IS_SAME = False
CONST_SYNC_RELATION_ALLBODY = True  #TODO réaranger ce mode peut être trop général..

CONFIG_STATISTIC = ["Affinity", "Colère", "Santé", "Assurance"]


class Stats:

    def __init__(self):
        self.__stats = {}

    def GetStatistic(self, key):
        return self.__stats[key]

    def SetStatistic(self, key, newValue):
        self.__stats[key] = newValue

    def IncreaseStatistic(self, key, increase=CONST_INCREASE_DESINCREASE):
        self.__stats[key] += increase

    def DecreaseStatistic(self, key, decrease=CONST_INCREASE_DESINCREASE):
        self.__stats[key] -= decrease

    def GetLenStats(self):
        return len(self.__stats)

    def StatisticAppend(self, key, value):
        self.__stats[key] = value

    def GetAllStatistics(self):
        return self.__stats

    def __str__(self):
        return f'{self.__stats}'


class Person:

    def __init__(self, name, occupation, age=CONST_DEFAULT_AGE, pnj= True, Stats={}, Profile={}, surname="",
                 ageDefault=CONST_DEFAULT_AGE, legalAge=CONST_DEFAULT_LEGAL_AGE):
        self.__name = name
        self.__ageDefault = ageDefault
        self.__legalAge = legalAge
        self.SetStats(Stats)
        self.SetOlder(age)
        self.SetPnj(pnj)
        self.SetOccupation(occupation)
        self.SetSurname(surname)
        self.SetProfile(Profile)

    def SetSurname(self, surname):
        self.__surname = surname

    def SetStats(self, Stats):
        self.__Stats = Stats

    def SetOlder(self, older):
        if older >= self.__legalAge:
            self.__older = older
        else:
            self.__older = self.__legalAge

    def SetPnj(self, pnj):
        self.__Pnj = pnj

    def IsPnj(self):
        return self.__Pnj

    def SetProfile(self, Profile):
        self.__Profile = Profile

    def SetOccupation(self, occupation):
        self.__occupation = occupation

    def GetName(self):
        return self.__name

    def GetSurname(self):
        return self.__surname

    def GetStats(self) -> Stats:
        return self.__Stats

    def GetProfile(self):
        return self.__Profile

    def GetOlder(self):
        return self.__older

    def GetOccupation(self):
        return self.__occupation

    def __str__(self):
        return f'Name : {self.GetName()} -Occupation : {self.GetOccupation()} -Age :{self.GetOlder()}'


class PersonStd(Person):

    def __init__(self, name, occupation, age=CONST_DEFAULT_AGE, pnj = True, Stats={}, Profile={}, surname="",
                 bodycount=CONST_DEFAULT_BODYCOUNT, ageDefault=CONST_DEFAULT_AGE, legalAge=CONST_DEFAULT_LEGAL_AGE):
        super().__init__(name, occupation, age, pnj, Stats, Profile, surname, ageDefault, legalAge)
        self.SetBodyCount(bodycount)

    def SetBodyCount(self, bodycount):
        self.__bodyCount = bodycount

    def GetBodyCount(self):
        return self.__bodyCount

    def __str__(self):
        return f'Name : {self.GetName()} -Occupation : {self.GetOccupation()} -Age :{self.GetOlder()} -Bodycount : {self.GetBodyCount()}'


class PersonFactory:

    @staticmethod
    def create(name, occupation, age=CONST_DEFAULT_AGE, pnj = True, personstats=CONFIG_STATISTIC, Profile={}, surname="",
               ageDefault=CONST_DEFAULT_AGE, legalAge=CONST_DEFAULT_LEGAL_AGE):
        StatsData = PersonFactory.CreateStats(personstats)
        return Person(name, occupation, age, pnj, StatsData, Profile, surname, ageDefault, legalAge)

    @staticmethod
    def CreateStats(Statistics, value=CONST_DEFAULT_STATISTIC):
        Liste = Stats()

        for statistic in Statistics:
            Liste.StatisticAppend(statistic, value)

        return Liste

    @staticmethod
    def updatePersonByStats(ObjetPerson: Person, personstats):
        StatsData = PersonFactory.CreateStats(personstats)
        ObjetPerson.SetStats(StatsData)

        return ObjetPerson

    @staticmethod
    def InsertProfileRelation(ObjetPersonDest: Person, ObjetPersonExp: Person, configProfil={}):
        profil = dict()
        key_relation = "relation"
        profil[key_relation] = dict()
        profil[key_relation][ObjetPersonExp.GetName()] = configProfil

        if not key_relation in ObjetPersonDest.GetProfile():
            ObjetPersonDest.SetProfile(profil)
        else:
            if not ObjetPersonExp.GetName() in ObjetPersonDest.GetProfile()[key_relation]:
                newAddPersonProfil = ObjetPersonDest.GetProfile()
                newAddPersonProfil[key_relation][ObjetPersonExp.GetName()] = configProfil
                ObjetPersonDest.SetProfile(newAddPersonProfil)
            else:
                # TODO Repasser pour une évolution  (maj des statistiques)
                pass

        return ObjetPersonDest

    @staticmethod
    def InsertSecret(ObjetPersonDest: Person, secret):
        profil = {}
        profil["secrets"] = []
        profil["secrets"].append(secret)


class PersonFactoryStd:

    @staticmethod
    def create(name, occupation, age=CONST_DEFAULT_AGE, pnj = True, personstats=CONFIG_STATISTIC, profile={}, surname="",
               bodycount=CONST_DEFAULT_BODYCOUNT, ageDefault=CONST_DEFAULT_AGE, legalAge=CONST_DEFAULT_LEGAL_AGE):
        Pfactory = PersonFactory.create(name, occupation, age, pnj, personstats, profile, surname, ageDefault, legalAge)
        return PersonStd(Pfactory.GetName(), Pfactory.GetOccupation(), Pfactory.GetOlder(), Pfactory.IsPnj(), Pfactory.GetStats(),
                         Pfactory.GetProfile(), Pfactory.GetSurname(), bodycount)

    @staticmethod
    def InsertProfileRelationStd(ObjetPersonDest: Person, ObjetPersonExp: Person, configProfil={}):
        return PersonFactory.InsertProfileRelation(ObjetPersonDest, ObjetPersonExp, configProfil)


class Scene:

    def __init__(self, name, start=CONST_START_CYCLE_AT, status=True, stage=CONST_DEFAULT_INIT_STAGE,
                 index=CONST_INCREASE_DESINCREASE):
        self.__SetName(name)
        self.SetStart(start)
        self.SetStatus(status)
        self.SetStage(stage)
        self.__index = index
        self.__finished = False

    def __SetName(self, name):
        self.__name = name

    def SetStart(self, start=CONST_START_CYCLE_AT):
        self.__start = start

    def SetStatus(self, status):
        self.__status = status

    def SetStage(self, stage=CONST_DEFAULT_INIT_STAGE):
        if stage >= 0:
            self.__stage = stage

    def SwitchStatus(self):
        self.__status = not self.__status

    def SwitchToFinished(self):
        self.__finished = not self.__finished

    def GoNextStage(self):
        self.__stage += self.__index

    def GoPreviousStage(self):
        if self.__stage >= 0:
            self.__stage -= self.__index

    def GetName(self):
        return self.__name

    def GetStart(self):
        return self.__start

    def GetStatus(self):
        return self.__status

    def GetStage(self):
        return self.__stage

    def IsExecuted(self):
        return self.__finished


class Module(Scene):
    pass


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
    def UpdateScenesByStackToken(collectionScene, stackToken):

        if len(stackToken) > 0 and len(collectionScene) > 0:

            for Token in stackToken:

                if StackTokenFactory.IsTypeOfLaunch(Token):

                    collectionScene[Token.GetScene()].SwitchStatus()

                elif StackTokenFactory.IsTypeOfCompleted(Token):

                    collectionScene[Token.GetScene()].SwitchToFinished()

                elif StackTokenFactory.IsTypeOfStage(Token):

                    if Token.GetMode():

                        if Token.GetStep() > 0:

                            collectionScene[Token.GetScene()].GoNextStage()

                        else:
                            collectionScene[Token.GetScene()].GoPreviousStage()

                    else:
                        collectionScene[Token.GetScene()].SetStage(Token.GetStep())

        return collectionScene


class Token:

    def __init__(self, nameScene):
        self.__name = nameScene

    def GetScene(self):
        return self.__name


class Stage(Token):

    def __init__(self, idScene, step):
        super().__init__(idScene)
        self.__step = step
        self.__mode = True

    def GetStep(self):
        return self.__step

    def GetMode(self):
        return self.__mode

    def SwitchMode(self):
        self.__mode = not self.__mode
        return self.__mode


class Completed(Token):
    pass


class Launch(Token):
    pass


class StackTokenFactory:

    @staticmethod
    def CreateLaunch(nameScene):
        return Launch(nameScene)

    @staticmethod
    def CreateCompleted(nameScene):
        return Completed(nameScene)

    @staticmethod
    def CreatedStage(nameScene, step):
        return Stage(nameScene, step)

    @staticmethod
    def IsTypeOfLaunch(token: Token):
        return isinstance(token, Launch)

    @staticmethod
    def IsTypeOfCompleted(token: Token):
        return isinstance(token, Completed)

    @staticmethod
    def IsTypeOfStage(token: Token):
        return isinstance(token, Stage)

    @staticmethod
    def AppendLaunchTokenCreated(collection, nameScene):
        Token = StackTokenFactory.CreateLaunch(nameScene)
        return collection.append(Token)

    @staticmethod
    def AppendEndTokenCreated(collection, nameScene):
        Token = StackTokenFactory.CreateCompleted(nameScene)
        return collection.append(Token)

    @staticmethod
    def AppendStageTokenCreated(collection, nameScene, step=CONST_INCREASE_DESINCREASE, mode=True):
        Token = StackTokenFactory.CreatedStage(nameScene, step)

        if not mode:
            Token.SwitchMode()

        return collection.append(Token)


class Request:

    def __init__(self, stackToken):
        self.__stacktoken = stackToken

    def Check(self):
        pass

    def GetStackToken(self):
        return self.__stacktoken

    def SetStackToken(self, stackToken):
        self.__stacktoken = stackToken


class Request_timing(Request):

    def __init__(self, stackToken, currentCycle, index):
        super().__init__(stackToken)
        self.__currentCycle = currentCycle
        self.__index = index


class Request_gaming(Request):

    def __init__(self, stackToken, community):
        super().__init__(stackToken)
        self.__community = community


class Request_sort(Request):

    def __init__(self, CollectionModule, FonctionSort):
        self.__resultModules = CollectionModule
        self.__FonctionSort = FonctionSort

    def SetCollectionModule(self, CollectionModule):
        self.__CollectionModule = CollectionModule

    def GetCollectionModuleSort(self):
        return self.__CollectionModule


class RequestFactory:

    def CreateRequestTiming(stackToken, currentCycle, index):
        return Request_timing(stackToken, currentCycle, index)

    def CreateRequestGaming(stackToken, community):
        return Request_gaming(stackToken, community)

    def CreateRequestSort(CollectionModule, FonctionSort):
        return Request_sort(CollectionModule, FonctionSort)


class FonctionSort:

    def TakeFirstElementInCollection(Collection):
        result = {}
        element = next(iter(Collection.items()))
        result[element[0]] = element[1]
        return result

    def TakeNfirstElementinCollection(Collection, n):
        result = {}
        if len(Collection) < n:
            n = len(Collection)

        keysIter = iter(Collection.keys())
        index = 0
        while index < n:
            libelle = next(keysIter)
            result[libelle] = Collection[libelle]
            index += 1

        return result


#label Run_sceneModule:
class ExtensionSceneModule:

    @staticmethod
    def CreateCollectionModule(CollectionScenes, listeModule):
        CollectionModules = {}

        for indexModule in listeModule:
            CollectionModules[indexModule] = CollectionScenes[indexModule]

        return CollectionModules

    def Proceed(CollectionsScenes, listeModule, Commnunity, scenePlay, currentCycle, fonctionTriage, params=[],
                FactoryRequest=RequestFactory):

        if len(listeModule) > 0:
            stackToken = []
            RequestTiming = FactoryRequest.CreateRequestTiming(stackToken, currentCycle, scenePlay)
            stackToken = ExtensionSceneModule.GetStackTokenoduleByTrigger(RequestTiming)

            RequestGaming = FactoryRequest.CreateRequestGaming(stackToken, Commnunity)
            stackToken = ExtensionSceneModule.GetStackTokenModuleByGaming(RequestGaming, stackToken)

            if len(stackToken) > 0:
                CollectionsScenes = CollectionSceneFactory.UpdateScenesByStackToken(CollectionsScenes, stackToken)

        return ExtensionSceneModule.GetCollectionModuleSort(CollectionsScenes, listeModule, fonctionTriage, params)

    def GetStackTokenoduleByTrigger(RequestTiming: Request):

        RequestTiming.Check()
        return RequestTiming.GetStackToken()

    def GetStackTokenModuleByGaming(RequestGaming: Request, stackToken):

        RequestGaming.SetStackToken(stackToken)
        RequestGaming.Check()
        return RequestGaming.GetStackToken()

    def GetCollectionModuleActive(CollectionsScene, listeModule):

        result = {}
        for module in listeModule:
            if CollectionsScene[module].GetStatus():
                result[module] = CollectionsScene[module]

        return result

    def GetCollectionModuleSort(CollectionScenes, listeModule, fonctionTriage, params):

        CollectionModule = ExtensionSceneModule.GetCollectionModuleActive(CollectionScenes, listeModule)
        fonctionTriage.Setter(CollectionModule, params)
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

    def AppendTokenToStackToken(cls, Token: Token):
        cls.__stacktoken.append(Token)

    def CheckScore(cls, community):
        cls.__stacktoken = []
        cls.__community = community

    def Proceed(self):
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

    def SetParamsValue(cls, params):
        cls.__params.append(params)

    def SetParamsTable(cls, params):
        cls.__params = params

    def GetParams(cls):
        return cls.__params


class GameSessionStd(SingleTone):

    def Check(cls):
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


class InjectionFonction:

    def __init__(self, fonctionInjected):
        self.fx = fonctionInjected

    def Setter(self, Collection, params):
        self.Collection = Collection
        self.params = params

    def GetFonctionSelected(self):
        pass


class InjectionFxSort(InjectionFonction):

    def GetFonctionSelected(self):
        return self.fx.TakeNfirstElementinCollection(self.Collection, self.params[0])


class Staging:  # Version python

    class Action:

        def __init__(self, Do):
            self.__Members = {}
            self.__Do = Do

        def AppendMember(self, keyMember, Member):

            if keyMember not in self.__Members:  # 32
                self.__Members[keyMember] = Member

        def RemoveMemberFrom(self, keyMember):

            if keyMember in self.__Members:  # 32
                del self.__Members[keyMember]

        def GetMembers(self):
            return self.__Members

        def SetMembers(self, Members):
            self.__Members = Members

        def Do(self): #Emplacement de dialogue staticSTD
            self.__Do.SetMembers (self.__Members)
            #print (self.__Members)
            return self.__Do

        def ChangeDoing(self, Do):
            self.__Do = Do


    def __init__(self, Community, do):
        self.__Community = Community
        self.__Action = self.Action(do)

    def ToSTagePerson(self, namePerson):

        if namePerson in self.__Community:  #32
            self.__Action.AppendMember(namePerson, self.__Community[namePerson])

    def ExcludePerson(self, namePerson):
        self.__Action.RemoveMemberFrom(namePerson)

    def GetPersons(self):
        return self.__Action.GetMembers()

    def GetAction(self): # emplacement Static Dialogue
        return self.__Action.Do()

    def SetAction(self, Do):
        self.__Action.ChangeDoing(Do)


class Do:

    def __init__(self):
      self.__to = []
      self.__from = None

    def SetTo (self, person):
      self.__to.append(person)
      return self.__to

    def SetFrom (self, namePerson):
       self.__from = namePerson

    def GetTo (self):
       return self.__to

    def GetFrom(self):
       return  self.__from

    def __str__(self):
        return f'GetFrom : {self.GetFrom()} - GetTo : {self.GetTo()}'


class InteractDefault:

    do = None
    members = None
    valid = None

    @staticmethod
    def Speak (exp, dest):
      return InteractDefault.Core(exp, dest, True)

    @staticmethod
    def Answer(exp):
        result = []
        if not InteractDefault.valid == None and not InteractDefault.do == None and len(InteractDefault.members)>0:
            if exp == InteractDefault.do.GetFrom().GetName() and not exp == InteractDefault.do.GetTo()[0].GetName():
                newExp = InteractDefault.do.GetTo()[0].GetName()
                relationType = False
                if CONST_SPEAK_ANSWER_DIAG_IS_SAME:
                    relationType = True
                result = InteractDefault.Core(newExp, exp,relationType)
                InteractDefault.valid = None
                #TODO à défaut, on définira la première personne de la liste comme personne principal
        return result

    def Meditate (exp):
        result = []
        relationType = False
        result = InteractDefault.Core(exp, exp, relationType)

        return result

    @staticmethod
    def Core(exp, dest, relationType,option=CONST_SYNC_RELATION_ALLBODY):
        InteractDefault.do = Do()
        InteractDefault.valid = True

        if not exp in InteractDefault.members:
            InteractDefault.valid = False

        if not isinstance(dest, (list, dict, tuple)):
            if not dest in InteractDefault.members:
                InteractDefault.valid = False
            dest = [dest]
        else:
            for person in dest:
                if not person in InteractDefault.members:
                    InteractDefault.result = False  #TODO pour l'instant, on rejette tout l'ensemble si un élèment n'est pas dans la liste

        if InteractDefault.valid:
            expPerson = InteractDefault.members[exp]
            InteractDefault.do.SetFrom(expPerson)

            if not expPerson.IsPnj and relationType:
                relationType = False

            for person in dest:
                majPerson = InteractDefault.members[person]
                if relationType:
                    majPerson = PersonFactory.InsertProfileRelation(majPerson, expPerson)
                else:
                   print(f' response de dest influence {majPerson.GetStats()}') # TODO évolution sur un mode différent de réaction..

                InteractDefault.do.SetTo(majPerson)

            if option:
                for personKey in InteractDefault.members.keys():
                    if not (personKey == expPerson.GetName()) and not personKey == dest[0]:
                        majProfilPerson = InteractDefault.members[personKey]
                        majProfilPerson = PersonFactory.InsertProfileRelation(majProfilPerson, expPerson)
                        InteractDefault.members[personKey] = majProfilPerson

        return InteractDefault.do

    @staticmethod
    def SetMembers (members):
        InteractDefault.members = members
        print(f"Ds dialogueDefault {InteractDefault.members}")

    @staticmethod
    def GetMembers ():
        return InteractDefault.members







