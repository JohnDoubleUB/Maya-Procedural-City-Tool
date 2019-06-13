#Procedural City Tool - Class

###This is the complete script in file, simply run all of this to start the tool and all the supporting modules!

import maya.cmds as ma
import random
   
class topologyGather:
    
    ### Variables that are independent of any one instance of the class ###
    
    ##Class variables (This is where any information that carries across objects is stored
    
    __minValue__ = 0 #This allows the minimum value to be set for the, changed from within minUpdate()
    __selectAmount__ = 0 #This is the amount of faces to be selected randomly
    __randomOutput__ = [] #This contains the randomly generated verts
    __Orientation__ = "Unchanged"
    __UVdp__ = 6 #This is the amount of decimal points gathered for UV positioning, can be altered within class here or later in code
    
    ##Interaction with BuildConstructor variables
    
    __BuildingComplexity__ = 0 #0 is simple
    __BuildRange__ = 5
    __BuildHeight__ = 10
    __Thickness__ = 1
    __ThicknessRange__ = 0
    
    ##Custom building selection a self is now initallised so this is a little redundant 
    
    __CustomMeshes__ = []
    
    ##Complex Building Settings
    
    __Levels__ = 2
    __LevelRange__ = 0
    __RoofMultiplyerMax__ = 2
    __RoofMultiplyerMin__ = 2
    
    ##Booleans
    __DuplicateSelect__ = False
    __GroupAfterCreation__ = True
    
    #########
    __instanceCount__ = 0 ## amount of instances of the class
    #########
    
    """Though __ doesn't actually do anything it is usefull for using as syntax to signify variables that shouldnt 
    really be accessed or altered outside of the class itself as python doesnt make use of private variables within classes
    making all technically accessible from outside itself (However functions are still able to keep variables created within them
    to themselves. These variables either have getters for external access or do not need accessing from outside the class at all"""
    
    ### On initalisation of the class this is all done ###
    
    def __init__(self, fC, oN): #parameters; (int(facecount), str(object name) )
        if isinstance(fC, str) == True:
            print 'No object selected!'  #If an object isnt currently selected
            pass
        else:
            ### Provided object is selected instance variables are created ###
            self.faceNoList = []
            self.faceCount = fC
            self.Name = oN[0]
            
            self.__CustomMeshes__ = []
            
            self.__selectAmount__ = self.faceCount/2
            
            for faceCountList in xrange (topologyGather.__minValue__, self.faceCount):
                self.faceNoList.append(faceCountList)
            ### To track amount of instances 
            topologyGather.__instanceCount__ = topologyGather.__instanceCount__ + 1
            self.__instanceCount__ = topologyGather.__instanceCount__
            
            
    ### Returns random face numbers (by default half unless int is specified) as a list of numbers ###
    def __randomFaces__(self):
        tempFaceList = []
        tempRandList = []
        randSelect = 0
        
    ### transfers the items into a list that will be used to ensure no replications of numbers are randomly chosen
        for listItem in self.faceNoList:
            tempFaceList.append(listItem)
            
        for _ in range(self.__selectAmount__):
            randSelect = random.choice(tempFaceList)
            tempRandList.append(randSelect)
            tempFaceList.remove(randSelect)
        
        self.__randomOutput__ = tempRandList
        return self.__randomOutput__
    
    ### self.Getattrs ###           
    
    def currentTotal(self):
        return len(self.faceNoList)
    
    def lastRandom(self):
        return self.__randomOutput__
    
    def currentInstance(self):
        return self.__instanceCount__
    
    ### class.Getattrs ###
    
    def UVDecimal(self):
        return topologyGather.__UVdp__
    
    def totalInstances(self):
        return topologyGather.__instanceCount__
    
    ##These are not initialised as self instances in the class and so only return as unique if instructed by the user
    ### Get Attributes for external use! ###     
        
    def getBuildingComplexity(self):
        cComplexity = []
        cComplexity.append(self.__BuildingComplexity__)
        if self.__BuildingComplexity__ == 0:
            cComplexity.append("Simple")
        elif self.__BuildingComplexity__ == 1:
            cComplexity.append("Complex")
        elif self.__BuildingComplexity__ == 2:
            cComplexity.append("Custom")
        return cComplexity
    
    def getBuildRange(self):
        return self.__BuildRange__
    
    def getBuildHeight(self):
        return self.__BuildHeight__
        
    def getAmountEdit(self):
        return self.__selectAmount__
        
    def getOrientation(self):
        return self.__Orientation__
        
    def getGroupAfterCreation(self):
        return self.__GroupAfterCreation__
    
    def getLevels(self):
        return self.__Levels__
    
    def getLevelRange(self):
        return self.__LevelRange__
        
    def getRoofMultMax(self):
        return self.__RoofMultiplyerMax__
    
    def getRoofMultMin(self):
        return self.__RoofMultiplyerMin__
        
    def getThickness(self):
        return self.__Thickness__
    
    def getThicknessRange(self):
        return self.__ThicknessRange__
    
    def getCustomMeshes(self):
        return self.__CustomMeshes__

    ### Set Attributes for external use! ### 
    
    def addCustomMesh(self, toAdd):
        self.__CustomMeshes__.append(toAdd)
   
    def removeCustomMesh(self, toRemove):
        if len(self.__CustomMeshes__) > 0:
            self.__CustomMeshes__.remove(toRemove)
        else:
            print "This list has no items!"
    
    def setThicknessRange(self, setting):
        if setting < self.__Thickness__ and setting >= 0:
            self.__ThicknessRange__ = setting
            print "This is happening"
        else:
            print "Range cannot be below 0, or greater than/equal to thickness setting!"
    
    def setThickness(self, setting):
        if setting > self.__ThicknessRange__: 
            self.__Thickness__ = setting
            print "This is also happening"
        else:
            print "Thickness cannot be less than or equal to the range or below 0!"
    
    def setRoofMultMin(self, setting):
        if setting <= self.__RoofMultiplyerMax__ and setting >= 0:  
            self.__RoofMultiplyerMin__ = setting
        else:
            print "Roof Min cannot be more than max or less than 0!"
    
    def setRoofMultMax(self, setting):
        if setting >= self.__RoofMultiplyerMin__:
            self.__RoofMultiplyerMax__ = setting
        else:
            print "Max cannot be less than the min"
    
    def setLevelRange(self, setting):
        if setting >= 0 and setting < self.__Levels__:
            self.__LevelRange__ = setting
        else:
            print "Level range cannot be less than 0 or more/equal to levels!"
    
    def setLevels(self, setting):
        if setting >= 2 and setting > self.__LevelRange__:
            self.__Levels__ = setting
        else:
            print "Levels cannot be less than 2 or less than/equal to the range!"
    
    def setGroupAfterCreation(self, boolean):
        self.__GroupAfterCreation__ = boolean
    
    def setOrientation(self, setting):
        self.__Orientation__ = setting
    
    def setBuildingComplexity(self, setting):
        if type(setting) == int:
            if setting >= 0 and setting <= 2:
                self.__BuildingComplexity__ = setting
                print setting
            else:
                print "Value may only be between 0 and 2!"
        else:
            print "Value is cannot be a string!"
            
    def setBuildHeight(self, setting):
        if type(setting) == int or type(setting) == float:
            if setting > 0:
                self.__BuildHeight__ = setting    
            else:
                print "Height cannot be negative!"     
        else:
            print "Value is cannot be a string!"
            
    def setBuildRange(self, setting):
        if type(setting) == int or type(setting) == float:
            if setting < self.__BuildHeight__ and setting > 0:
                self.__BuildRange__ = setting
            else:
                print "Value cannot be below 0 or the same as or larger than height! "
        else:
             print "Value cannot be a string!"
        
    ### Clear old count list and then input a new value provided by the user ###
    
    def minUpdate(self, minChange):
        topologyGather.__minValue__ = minChange
        self.faceNoList = []
        for faceCountList in xrange (topologyGather.__minValue__, self.faceCount):
                self.faceNoList.append(faceCountList)
    
    
    ### Manually change the amount of points selected (Initallised as half of the points by default) ###
    def selectAmountEdit(self, number):
        if type(number) == int:
            self.__selectAmount__ = number
            print "number was changed to %s" % number
        else:
            print "invalid value!"
        
    ### Determine what object is selected on creation of generated objects ###
    
    ### Create objects based upon the random facelist points, no orientation/rotation ###
    
    def createObject(self):
        ##RandomSelection
        topologyGather.__randomFaces__(self)
        #################
        
        #Create all buildings before placement
        tempBuild = buildConstructor(self.Name, self.__BuildHeight__, self.__BuildRange__, self.__Thickness__, self.__ThicknessRange__, self.__BuildingComplexity__, self.__selectAmount__, self.__Levels__, self.__LevelRange__, self.__RoofMultiplyerMax__, self.__RoofMultiplyerMin__, self.__CustomMeshes__)
        
        tempNamestore = []
        tempXYZstore = []
        iterA = -1
        tempList = tempBuild.getBuildList()
        for vert in self.__randomOutput__:
            vertO = ma.xform(self.Name +".vtx[%s]" % vert, q=True, ws=True, t=True)
            iterA = iterA + 1
            tempObj = tempList[iterA]
            ##tempNamestore.append(str(tempObj[0]))
            ##tempXYZstore.append(vertO)
            ma.move(vertO[0], vertO[1], vertO[2], tempObj, xyz = True)
        ##print tempNamestore
        ##print tempXYZstore
        if self.__GroupAfterCreation__:
            ma.group(tempList, n = str(self.Name) + "_Group_#")
            ma.select(self.Name)
        else:
            ma.select(self.Name)
    
    #Point on polly constraint version of the above function (Allowing orientation/rotation) to be determined  
      
    def createObjectOrientated(self):
        ##Temporary Storage for UV values
        tempUStore = []
        tempVStore = []
        iterA = -1
        
        ##RandomSelection
        topologyGather.__randomFaces__(self)
        #################
        
        #To gather UV information
        
        for vert in self.__randomOutput__:
            ##Construct from the number the rest of the name 
            currentVert = str(self.Name)+".vtx[%s]" % str(vert)
            print currentVert
            
            ##Get current vert UV values
            ma.select(currentVert)
            vertUV = ma.polyEvaluate(bc2 = True)
            tempUStore.append(vertUV[0][0])
            tempVStore.append(vertUV[1][0])
            ma.select(deselect = True)
        
        #To create objects, constrain and place
        
        #Create all buildings before placement
        
        tempOBuild = buildConstructor(self.Name, self.__BuildHeight__, self.__BuildRange__, self.__Thickness__, self.__ThicknessRange__, self.__BuildingComplexity__, self.__selectAmount__, self.__Levels__, self.__LevelRange__, self.__RoofMultiplyerMax__, self.__RoofMultiplyerMin__, self.__CustomMeshes__)
        tempOList = tempOBuild.getBuildList()
        for item in tempUStore:
            ##Count the iteration
            iterA = iterA + 1
            ##Store the UV details
            vertU = item
            vertV = tempVStore[iterA]
            
            ##Create Object
            tempObj = tempOList[iterA]
            
            ##Create Constraint
            ##use pSphere1.vtx[80] as the constraint of tempObj (PolyCube)
            tempConstraintName = ma.pointOnPolyConstraint(str(self.Name)+".vtx[%s]" % str(self.__randomOutput__[iterA]), tempObj)
            
            ##Give values to the constraint UVs
            ma.setAttr(str(tempConstraintName[0]) + ".%s" % self.Name + "U0", vertU)
            ma.setAttr(str(tempConstraintName[0]) + ".%s" % self.Name + "V0", vertV)
            ##Remove constraint
            ma.delete(str(tempConstraintName[0]), cn= True)   
        if self.__GroupAfterCreation__:
            ma.group(tempOList, n = str(self.Name) + "_Group_#")
            ma.select(self.Name)
        else:
            ma.select(self.Name)
            
############# BUILDING CLASS


## All the main functionality of this class is on initial creation of an instance

class buildConstructor:
    ##These are all the different building settings for the classes
    __BuildingHeight__ = 0 #This may only need to be an instanced variable
    __HeightNoise__ = 0 #This determines the maximum variation in height from the actual set height, this creates variation <-- Provide a way of calculating a percentage range height
    __Thickness__ = 1
    __ThicknessNoise__ = 0
    ##For Complex Buildings
    __Levels__ = 6
    __LevelRange__ = 5
    __RoofMultiplyerMax__ = 40
    __RoofMultiplyerMin__ = 5
    ##
    __CustomList__ = []
    ##
    __BuildingComplexity__ = 0 #0 is single cubes instead of complex extruded structures
    __BuildingName__ = "GenericBuilding" 
    __BuildingCount__ = 0 #This probably only needs to be an instanced variable
    
    __InstanceCount__ = 0

    #When instance is created include: Name, height, heightrange, thickness, thicknessrange, complexity, amount of buildings, building levels(if complex), max amount of roof(if complex), min amount of roof(if complex), custom building meshes list(if custom)
    def __init__(self, buildName, buildHeight, buildRange, buildThickness , thicknessRange , buildComplexity , buildingAmount, levels, levelRange, roofMMax, roofMMin, customBuildingList):
        #Set for the unique instance
        self.__BuildingName__ = buildName
        self.__BuildingHeight__ = buildHeight
        self.__BuildingComplexity__ = buildComplexity
        self.__InstanceCount__ = buildConstructor.__countInstance__(self)
        self.__BuildingCount__ = buildingAmount
        self.__Thickness__ = buildThickness
        self.__ThicknessNoise__ = thicknessRange
        
        self.__Levels__ = levels
        self.__LevelRange__ = levelRange
        self.__RoofMultiplyerMax__ = roofMMax
        self.__RoofMultiplyerMin__ = roofMMin
        
        self.__HeightNoise__ = buildRange 
        self.__CustomList__ = customBuildingList
        
        self.__BuildingNameReturn__ = [] #This will store the 
        
        #All the appropriate gathering of data has been achieved by this point, Moving on to the creation of the buildings!
        
        buildConstructor.__createBuilding__(self)
        
    def __countInstance__(self):
        buildConstructor.__InstanceCount__ = buildConstructor.__InstanceCount__ + 1
        return buildConstructor.__InstanceCount__
        
    def __createBuilding__(self):
        if self.__BuildingComplexity__ == 0:
            buildConstructor.__simpleBuilding__(self)
        elif self.__BuildingComplexity__ == 1:
           buildConstructor.__complexBuilding__(self)
        elif self.__BuildingComplexity__ == 2:
            buildConstructor.__customBuildings__(self)
    
    
    
    
    #This is called if the user requests a complexity of 0
    
    def __simpleBuilding__(self):
        print "Simple building"
        
        #Locally storing for function use
        
        buildingCount = self.__BuildingCount__
        heightMax = self.__BuildingHeight__ + self.__HeightNoise__
        heightMin = self.__BuildingHeight__ - self.__HeightNoise__
        buildName = self.__BuildingName__
        thickMin = self.__Thickness__ - self.__ThicknessNoise__
        thickMax = self.__Thickness__ + self.__ThicknessNoise__
        
        #Check that heightMin is not less than 1 (Because this may vause an issue)
        
        if heightMin < 1:
            heightMin = 1
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        else:
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        
        if thickMin < 1:
            thickMin = 1
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
        else:
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
        
        #Now all the neccesary checks have been made, creating the buildings!
        
        for _ in xrange(buildingCount):
            randHeight = random.uniform(heightMin, heightMax + 1)
            randThickness = random.uniform(thickMin, thickMax + 1)
            simpleBuilding = ma.polyCube(name = str(buildName) + "_#", sx = 1, sy = 1, sz = 1, h = 1)
            pivotTransform = 0
            pivotTransform = float(randHeight / 2)
            ma.move(0, -0.5, 0, str(simpleBuilding[0])+".scalePivot", str(simpleBuilding[0])+".rotatePivot", absolute = True)  
            
            # Height Scaling            
            ma.setAttr(str(simpleBuilding[0]) + ".scaleY", randHeight)
            
            # Thickness
            ma.setAttr(str(simpleBuilding[0]) + ".scaleX", randThickness)
            ma.setAttr(str(simpleBuilding[0]) + ".scaleZ", randThickness)
            
            self.__BuildingNameReturn__.append(str(simpleBuilding[0]))
        print "Buildings created, use getBuildList() to return this information"
    
    # Building Generating function
    
    def __skyScraper__(self, name, height, thickness, levels, tip, roofMult, tipType):
        roofHeight = float(height)/roofMult #Designating amount of total height for roof
        levelsHeight = float(height)-roofHeight #Determining the total room in height for levels
        levelHeight = float(levelsHeight)/levels #Distributing between the total levels
        roofTip = float(tip) / levels
        
        
        testBuilding = ma.polyCube(name = str(name)+"_#", sx = 1, sy = 1, sz = 1, h = 1)
        testBuildingName = testBuilding[0]

        ma.move(0, -0.5, 0, str(testBuildingName)+".scalePivot", str(testBuildingName)+".rotatePivot", absolute = True)
        
        
        ma.scale(thickness,levelHeight,thickness, str(testBuildingName))
        levels = levels -1 #One level removed as this is the base height
        for _ in range(levels):
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=0, ls=(0.9, 0.9, 0.9) )
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=levelHeight, ls=(1, 1, 1) )
        
        #Different Roofs
        if tipType == 0:
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=roofHeight, ls=(roofTip, roofTip, roofTip) )
            tipMerge = ma.polyListComponentConversion(str(testBuildingName)+".f[1]", fromFace = True, toVertex = True)
            ma.polyMergeVertex(tipMerge, d=0.01)
        elif tipType == 1:
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=roofHeight, ls=(1, 1, 1))
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=0, ls=(roofTip, roofTip, roofTip))
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=-roofHeight/10, ls=(1, 1, 1))
            tipMerge = ma.polyListComponentConversion(str(testBuildingName)+".f[1]", fromFace = True, toVertex = True)
            ma.polyMergeVertex(tipMerge, d=0.01)
        elif tipType == 2:
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=roofHeight, ls=(roofTip, 0, roofTip) )
            tipMerge = ma.polyListComponentConversion(str(testBuildingName)+".f[1]", fromFace = True, toVertex = True)
            ma.polyMergeVertex(tipMerge, d=0.01)
        elif tipType == 3:
            ma.polyExtrudeFacet(str(testBuildingName)+".f[1]", kft=False, ltz=roofHeight, ls=(0, roofTip, 0) )
            tipMerge = ma.polyListComponentConversion(str(testBuildingName)+".f[1]", fromFace = True, toVertex = True)
            ma.polyMergeVertex(tipMerge, d=0.01)
            
        ma.delete(str(testBuildingName), ch = True)
        ma.select(str(testBuildingName))
        return str(testBuildingName)
    # Complex Building Function
    
    def __complexBuilding__(self):
        print "Complex building"
        
        #Locally storing for function use
        buildingCount = self.__BuildingCount__
        heightMax = self.__BuildingHeight__ + self.__HeightNoise__
        heightMin = self.__BuildingHeight__ - self.__HeightNoise__
        buildName = self.__BuildingName__
        thickMin = self.__Thickness__ - self.__ThicknessNoise__
        thickMax = self.__Thickness__ + self.__ThicknessNoise__
        levelMax = self.__Levels__ + self.__LevelRange__
        levelMin = self.__Levels__ - self.__LevelRange__
        roofMultMin = self.__RoofMultiplyerMin__
        roofMultMax = self.__RoofMultiplyerMax__
        
        #Check that heightMin is not less than 1 (Because this may vause an issue)
        
        if heightMin < 1:
            heightMin = 1
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        else:
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        
        if thickMin < 1:
            thickMin = 1
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
        else:
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
        
        #Now all the neccesary checks have been made, creating the buildings!
        
        for _ in xrange(buildingCount):
            randHeight = random.uniform(heightMin, heightMax + 1)
            randThickness = random.uniform(thickMin, thickMax + 1)
            
            #Creation handled by skyscraper function; name, height, thickness, ((levels, tip, roofMult, tipType))
            complexBuilding = self.__skyScraper__(str(buildName), randHeight, randThickness, random.randint(levelMin,levelMax), 1, random.randint(roofMultMin, roofMultMax), random.randint(0,3))
            
            self.__BuildingNameReturn__.append(str(complexBuilding))
        print "Buildings created, use getBuildList() to return this information"
    
    
    def __customBuildings__(self):
        #Store the object names locally for use
        customObjects = self.__CustomList__
        buildingCount = self.__BuildingCount__
        heightMax = self.__BuildingHeight__ + self.__HeightNoise__
        heightMin = self.__BuildingHeight__ - self.__HeightNoise__
        buildName = self.__BuildingName__
        thickMin = self.__Thickness__ - self.__ThicknessNoise__
        thickMax = self.__Thickness__ + self.__ThicknessNoise__
        
        #Check that heightMin is not less than 1 (Because this may vause an issue)
        
        if heightMin < 1:
            heightMin = 1
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        else:
            print "Max height: %s" % heightMax
            print "Min height: %s" % heightMin
        
        if thickMin < 1:
            thickMin = 1
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
        else:
            print "Max thick: %s" % thickMax
            print "Min thick: %s" % thickMin
            
       #Onto the duplicating of the buildings
      
        for _ in xrange(buildingCount):
            randHeight = random.uniform(heightMin, heightMax + 1)
            randThickness = random.uniform(thickMin, thickMax + 1)
            
            randomBuilding = ma.duplicate(str(random.choice(self.__CustomList__)))
            
            ma.move(0,0,0,str(randomBuilding[0]), a = True)
            
            # Height Scaling            
            ma.setAttr(str(randomBuilding[0]) + ".scaleY", randHeight)
            
            # Thickness
            ma.setAttr(str(randomBuilding[0]) + ".scaleX", randThickness)
            ma.setAttr(str(randomBuilding[0]) + ".scaleZ", randThickness)
            
            self.__BuildingNameReturn__.append(str(randomBuilding[0]))
        print "Buildings created, use getBuildList() to return this information"
        
        
    # Get attr for the list of created objects for given instance
        
    def getBuildList(self):
        print "Instance Returning BuildList"
        return self.__BuildingNameReturn__


############# UI IMPLEMENTATION


##Class instances will be stored here and accessed via here
itemDict = {}

## displays at the bottom of the window
def buildCity():
    global itemDict
    global listBreak
    orientation = ma.optionMenu("oriDD", q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if not str(itemDict[currentSelected].getBuildingComplexity()[1]) == "Custom":
        if currentSelected == listBreak:
            errorLog("Cannot generate without a surface!", 1)
        else:
            errorLog("", 0)
            if orientation == "Unchanged":
                itemDict[currentSelected].createObject()
            else:
                itemDict[currentSelected].createObjectOrientated()
    else:
        if not len(itemDict[currentSelected].getCustomMeshes()) == 0:
            if currentSelected == listBreak:
                errorLog("Cannot generate without a surface!", 1)
            else:
                errorLog("", 0)
                if orientation == "Unchanged":
                    itemDict[currentSelected].createObject()
                else:
                    itemDict[currentSelected].createObjectOrientated()
        else:
            errorLog("Please add custom meshes!", 1)
                
## Used for to update the group after creation option when the tick box is changed, checked and turns out to have changed
def checkBoxGroup(boolean):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    itemDict[currentSelected].setGroupAfterCreation(boolean)
    
## Used to make changes to the height fields but also to prevent the user from makeing the range heigher than the maximum
def heightFields(maxOrRange):
    global itemDict
    heightValue = ma.floatField("maxH" , q = True, v = True)
    rangeValue = ma.floatField("noiseH" , q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if heightValue <= rangeValue:
        selectionUpdate()
        errorLog("Height cannot be equal to or less than range!", 1)
    else:
        errorLog("", 0)
        if maxOrRange == True:
            itemDict[currentSelected].setBuildHeight(heightValue)
        else:
            itemDict[currentSelected].setBuildRange(rangeValue)

## Similar to the height fields for changing values but also input validation            
def thickFields(maxOrRange):
    global itemDict
    thickValue = ma.floatField("thickMax" , q = True, v = True)
    rangeValue = ma.floatField("thickRange", q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if thickValue <= rangeValue:
        selectionUpdate()
        errorLog("Thickness cannot be equal to or less than Range!", 1)
    else:
        errorLog("", 0)
        if maxOrRange == True:
            itemDict[currentSelected].setThickness(thickValue)
        else:
            itemDict[currentSelected].setThicknessRange(rangeValue)

## for levels, again to change values but also for input validation            
def levelFields(maxOrRange):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    maxValue = ma.intField("levelAmount", q = True, value = True)
    rangeValue = ma.intField("levelRange", q = True, value = True)
    if maxValue <= rangeValue:
        errorLog("Levels cannot be equal to or less than Range!", 1)
        selectionUpdate()
    else:
        errorLog("", 0)
        if maxOrRange == True:
            itemDict[currentSelected].setLevels(maxValue)
        else:
            itemDict[currentSelected].setLevelRange(rangeValue)
            
def roofFields(maxOrMin):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    maxValue = ma.intField("roofMax", q = True, value = True)
    minValue = ma.intField("roofMin", q = True, value = True)
    if maxValue < minValue:
        errorLog("Minimum height cannot be more than the height!", 1)
        selectionUpdate()
    else:
        errorLog("", 0)
        if maxOrMin == True:
            itemDict[currentSelected].setRoofMultMax(maxValue)
        else:
            itemDict[currentSelected].setRoofMultMin(minValue)

def addToCustom(itemToAdd):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    #To be used as part of the addCustomValidation after checks have been done
    ma.textScrollList("customMeshList", e = True, a = itemToAdd, si = itemToAdd )
    itemDict[currentSelected].addCustomMesh(itemToAdd)
    
def removeCustomValidate():
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    #Checking to see if there are infact any items to remove
    if len(itemDict[currentSelected].getCustomMeshes()) > 0:
        customSelected = ma.textScrollList("customMeshList", q = True, si = True)
        customSelected = customSelected[0]
        itemDict[currentSelected].removeCustomMesh(customSelected)
        ma.textScrollList("customMeshList", e = True, ri = customSelected)
        errorLog("", 0)
    else:
        errorLog("No items exist to be removed!", 1)
    

def addCustomValidate():
    global itemDict
    itemExists = False
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    itemToAdd = ma.ls(selection = True)
    #check if item is selected and if it is only one
    if len(itemToAdd) == 1:
        itemToAdd = itemToAdd[0]
        # Check if items exist on the list already
        if len(itemDict[currentSelected].getCustomMeshes()) > 0:
            
            #list has items, check if selected item is already on the list
            for item in itemDict[currentSelected].getCustomMeshes():
                if str(item) == str(itemToAdd):
                    #If item is identical to currently checked list item
                    itemExists = True
                else:
                    #If it gets here, the item currently being checked is not the same as the selected
                    errorLog("", 0)    
                    
            #List has items, items have been checked against the item to add, if itemExists is false item can be added
            if not itemExists:
                #Item does not exist on the list and can be safely added!
                ##
                addToCustom(itemToAdd)
                ##
                
            else:
                #Item exists and cannot be added again
                errorLog("Item already on list!", 1)       
        else:
            #List is empty, item can be safely added!
            ##
            addToCustom(itemToAdd)
            ##
            
            errorLog("", 0) 
    else:
        errorLog("No items or multiple items selected!", 1)

## used to enquire to if the build complexity is set to custom, if it is then the function unlocks the custom mesh section and loads any existing settings if there are any
def isBuildCustom():
    global itemDict
    currentComplexity = ma.optionMenu("CompDropdown", q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if str(currentComplexity) == "Custom":
        ma.textScrollList("customMeshList", e = True, ra = True, en = True)
        ma.button("addBuild", e = True, en = True)
        ma.button("removeBuild", e = True , en = True)
        if len(itemDict[currentSelected].getCustomMeshes()) > 0:
            for item in itemDict[currentSelected].getCustomMeshes():
                ma.textScrollList("customMeshList", e = True, append = item, si = item)
        else:
            errorLog( "" , 0 )
        
    else:
        ma.textScrollList("customMeshList", e = True, ra = True, en = False)
        ma.button("addBuild", e = True, en = False)
        ma.button("removeBuild", e = True , en = False)

## Same as custom except applies to the complex settings        
def isBuildComplex():
    global itemDict
    currentComplexity = ma.optionMenu("CompDropdown", q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if str(currentComplexity) == "Simple":
        ma.intField("levelAmount", e= True, ed = False, value = 2)
        ma.intField("levelRange", e= True, ed = False, value = 0)
        ma.intField("roofMax", e= True, ed = False, value = 2)
        ma.intField("roofMin", e= True, ed = False, value = 2)
    else:
        ma.intField("levelAmount", e= True, ed = True, value = itemDict[currentSelected].getLevels())
        ma.intField("levelRange", e= True, ed = True, value = itemDict[currentSelected].getLevelRange())
        ma.intField("roofMax", e= True, ed = True, value = itemDict[currentSelected].getRoofMultMax())
        ma.intField("roofMin", e= True, ed = True, value = itemDict[currentSelected].getRoofMultMin())
    

def editIntField(fieldName, stringCommand):
    global itemDict
    newValue = ma.intField(fieldName , q = True, v = True)
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    exec(stringCommand)
    
def updateOrientationMenu(Dropdown):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    result = ma.optionMenu(Dropdown, q = True, v = True)
    itemDict[currentSelected].setOrientation(result)
    

def updateComplexityMenu(Dropdown):
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    result = ma.optionMenu(Dropdown, q = True, v = True)
    options = { 'Simple': 0, 'Complex' : 1, 'Custom' : 2 }
    itemDict[currentSelected].setBuildingComplexity(options[result])
    selectionUpdate()

def errorLog(textInput, bGColour):
    boxColour = [(0.35,0.35,0.35), (0.75,0.35,0.35)]
    ma.rowColumnLayout("B_Error",e = True, bgc = boxColour[bGColour])
    ma.text("TF_Error", e = True, label = textInput)

def updateText(textInstanceSTR, updatedValue):
    ma.text(textInstanceSTR, e = True, label = updatedValue)

def selectionUpdate():
    global itemDict
    global listBreak
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if currentSelected == str(listBreak):
        print "listBreak selected!"
        updateText("vertVal","N/A")
        updateText("compVal","N/A")
        ma.optionMenu("CompDropdown", e = True, en = False)
        ma.optionMenu("CompDropdown", e = True, v = "Simple")
        ma.floatField("maxH" , e= True, ed = False, value = 1)
        ma.floatField("noiseH" , e= True, ed = False, value = 0)
        ma.optionMenu("oriDD", e = True, en = False)
        ma.optionMenu("oriDD", e = True, v = "Unchanged")
        ma.intField("randAmount", e= True, ed = False, value = 10)
        ma.checkBox("groupAC", e= True, ed = False, value = True)
        ma.floatField("thickMax" , e = True, ed = False, value = 1)
        ma.floatField("thickRange", e = True, ed = False, value = 0)
        ma.intField("levelAmount", e= True, ed = False, value = 2)
        ma.intField("levelRange", e= True, ed = False, value = 0)
        ma.intField("roofMax", e= True, ed = False, value = 2)
        ma.intField("roofMin", e= True, ed = False, value = 2)
        ma.textScrollList("customMeshList", e = True, ra = True, en = False)
        ma.button("addBuild", e = True, en = False)
        ma.button("removeBuild", e = True , en = False)
    else:
        updateText("vertVal",itemDict[currentSelected].faceCount)
        updateText("compVal",str(itemDict[currentSelected].getBuildingComplexity()[1]))
        print itemDict[currentSelected].getBuildingComplexity()[1]
        ma.optionMenu("CompDropdown", e = True, v = str(itemDict[currentSelected].getBuildingComplexity()[1])) #Currently cannot have unique complexiries
        ma.optionMenu("CompDropdown", e = True, en = True)
        ma.floatField("maxH" , e= True, ed = True, value = itemDict[currentSelected].getBuildHeight())
        ma.floatField("noiseH" , e= True, ed = True, value = itemDict[currentSelected].getBuildRange())
        ma.optionMenu("oriDD" , e= True, en = True, value = itemDict[currentSelected].getOrientation())
        ma.intField("randAmount", e= True, ed = True, value = itemDict[currentSelected].getAmountEdit())
        ma.checkBox("groupAC", e= True, ed = True, value = itemDict[currentSelected].getGroupAfterCreation())
        ma.floatField("thickMax" , e = True, ed = True, value = itemDict[currentSelected].getThickness())
        ma.floatField("thickRange", e = True, ed = True, value = itemDict[currentSelected].getThicknessRange())
        isBuildComplex()
        isBuildCustom()

def deleteListItem():
    global listBreak
    global itemDict
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if currentSelected == str(listBreak):
        print "This is not an item and cannot be deleted!"
        errorLog("This is not deleteable!", 1)
    else:
        errorLog("", 0)
        ma.textScrollList("scrollList1", e = True, ri = currentSelected)
        del itemDict[str(currentSelected)]
    ##Checking if an item is selected or not
    selectionUpdate()
    
        
    
def selectInWorld():
    currentSelected = ma.textScrollList("scrollList1", q = True, si = True)
    currentSelected = currentSelected[0]
    if currentSelected == str(listBreak):
        print "This is not an item."
        errorLog("This is not an item", 1)
    else:
        errorLog("", 0)
        ma.select(str(currentSelected))
    

def printListSelected():
    what = ma.textScrollList("scrollList1", q = True, si = True)
    print what


def addSelected():
    global itemDict
    selected = ma.ls(selection = True)
    currentlyListed = ma.textScrollList("scrollList1", q = True, ai = True)
    alreadyExists = False
    if len(selected) >= 2:
        errorLog("Multiple Items Selected!", 1)
    else:
        if len(selected) >= 1:
            for listItem in currentlyListed:
                if str(selected[0]) == listItem:
                    alreadyExists = True
                else:
                    pointlessNote = "Object is unique"
            if alreadyExists == False:
                ma.textScrollList("scrollList1", e = True, append=[str(selected[0])], selectItem=str(selected[0]), selectCommand = "selectionUpdate()")
                itemDict[str(str(selected[0]))] = topologyGather(ma.polyEvaluate(v=True), ma.ls(selection = True))
                print "Adding To List"
                updateText("vertVal",itemDict[selected[0]].faceCount)
                updateText("compVal",str(itemDict[selected[0]].getBuildingComplexity()[1]))
                errorLog("", 0)
                selectionUpdate()
            else:
                print "Item with this name already exists on the list!"
                errorLog("Item Already on List!", 1)
        else:
            print "no item is selected in the world!"
            errorLog("No Item selected in world!", 1)
