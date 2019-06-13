#Procedural City Tool - UI

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

nameList = []
windowID = "myWindowID"
listBreak = '|----------------------------------|'


if ma.window ( windowID, exists = True ):
        ma.deleteUI( windowID )

windowID = ma.window( windowID, title = "Surface City Generator", sizeable=False, resizeToFitChildren=True) 
ma.rowColumnLayout("SingleColumn", numberOfColumns = 1, columnWidth = (1,300))
ma.rowColumnLayout(windowID, numberOfColumns = 2, columnWidth = [(1,150),(2,150)])

ma.window( windowID, edit=True, widthHeight=(300, 600) )
ma.text( label='Surface Object List' )
ma.text( label='Surface Options' )
ma.textScrollList("scrollList1", numberOfRows=7, allowMultiSelection=False, append=[listBreak], selectItem=listBreak, showIndexedItem=4 )

ma.rowColumnLayout(numberOfRows=4)
ma.button( label='Add Selected Surface', command="addSelected()", w = 150)
ma.button( label='Delete From List', command="deleteListItem()", w = 150)
ma.button( label='Select Surface in world', command="selectInWorld()", w = 150)
ma.button( label='Build City', command = "buildCity()", w = 150)
ma.setParent("..")
    
ma.setParent("..")

###########Tabb

ma.rowColumnLayout("TabbedSection", numberOfColumns = 1, columnWidth = [(1,300)])
tabs = ma.tabLayout()

##############################################################################################
   
### Distribution ###

child1 = ma.rowColumnLayout(numberOfColumns=2, columnWidth = [(1,150),(2,140)])
ma.text(label = "Building Orientation: ", al = "right")
ma.optionMenu("oriDD", en = False, changeCommand = "updateOrientationMenu(\"oriDD\")")
ma.menuItem( label='Unchanged' )
ma.menuItem( label='UV Rotation' )
ma.text(label = "Random Amount: ", al = "right")
ma.intField("randAmount", minValue = 1,value = 1, ed = False, cc = "editIntField(\"randAmount\", \"itemDict[currentSelected].selectAmountEdit(newValue)\")")
ma.setParent( '..' )
 
### City Settings ###

child2 = ma.rowColumnLayout(numberOfColumns=2, columnWidth = [(1,150),(2,140)])
ma.text("Building Complexity: ", al = "right")
ma.optionMenu("CompDropdown", changeCommand = "updateComplexityMenu(\"CompDropdown\")", en = False)
ma.menuItem( label='Simple' )
ma.menuItem( label='Complex' )
ma.menuItem( label='Custom' )
ma.separator(h = 5)
ma.separator(h = 5)
ma.text(label = 'Height: ', al = "right")
ma.floatField("maxH" ,minValue = 1, value = 1, cc ="heightFields(True)", pre = 2, step = 0.5, ed = False)
ma.text(label = 'Height Range: ', al = "right")
ma.floatField("noiseH" ,minValue = 0, cc ="heightFields(False)", pre = 2,step = 0.5, ed = False) 
ma.text(label = "")
ma.checkBox("groupAC", label='Group After Creation', ofc = "checkBoxGroup(False)", onc = "checkBoxGroup(True)" , ed = False, v = True )
ma.separator(h = 5)
ma.separator(h = 5)
ma.text(label = 'Thickness: ', al = "right")
ma.floatField("thickMax" ,minValue = 1, value = 1, cc ="thickFields(True)", pre = 2, step = 0.5, ed = False)
ma.text(label = 'Thickness Range: ', al = "right")
ma.floatField("thickRange" ,minValue = 0, value = 1, cc ="thickFields(False)", pre = 2, step = 0.5, ed = False)
ma.separator()
ma.separator()
ma.text(label = "Complex Settings", bgc = (0.2, 0.2, 0.2), al = "left")
ma.separator()

ma.text(label = 'Max Levels: ', al = "right")
ma.intField("levelAmount" ,minValue = 2, value = 2, cc="levelFields(True)", step = 1, ed = False)
ma.text(label = 'Level Range: ', al = "right")
ma.intField("levelRange" ,minValue = 0, value = 0, cc="levelFields(False)", step = 1, ed = False)

ma.separator()
ma.separator()

ma.text(label = 'Roof Height: ', al = "right")
ma.intField("roofMax" ,minValue = 2, value = 2, cc = "roofFields(True)", step = 1, ed = False)
ma.text(label = 'Minimum Height: ', al = "right")
ma.intField("roofMin" ,minValue = 2, value = 2, cc = "roofFields(False)", step = 1, ed = False)

ma.separator()
ma.separator()
ma.text(label = "Custom Meshes", bgc = (0.2, 0.2, 0.2), al = "left", h = 10)
ma.separator()
ma.text(label = 'Building Meshes', h = 20)
ma.text(label = 'Mesh Options', h = 20)

ma.separator()
ma.separator()

ma.textScrollList("customMeshList", numberOfRows=3, allowMultiSelection=False, showIndexedItem=4 )

ma.rowColumnLayout(numberOfColumns=1)
ma.button("addBuild", label='Add Selected Mesh', command = "addCustomValidate()",en = False,  w = 150)
ma.button("removeBuild", label='Remove Mesh', command = "removeCustomValidate()", en = False, w = 150)
ma.setParent("..")

ma.setParent( '..' )

### Surface Info ###

child3 = ma.rowColumnLayout(numberOfColumns=2, columnWidth = [(1,150),(2,140)])
ma.text(label='Vertex Count:', align='right' )
ma.text("vertVal", label = "N/A")
ma.text(label = 'Current Building Complexity:', align='right')
ma.text("compVal", label = "N/A")
ma.setParent( '..' )

ma.tabLayout( tabs, edit=True, tabLabel=((child1, 'Distribution'), (child2, 'City Settings'), (child3, 'Surface Info')))
ma.setParent('..')

### Error Log Section ###

ma.rowColumnLayout("B_Error", bgc = (0.35,0.35,0.35))
ma.text("TF_Error",label = "", align='center', w = 300, h = 20)
ma.setParent('..')

###########

print "Show window"
ma.showWindow(windowID)