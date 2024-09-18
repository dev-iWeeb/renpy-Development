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