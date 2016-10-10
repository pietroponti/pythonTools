###################################################
###################################################
#### TOOL FOR BAKING TRANSFORMS BETWEEN NODES #####
###################################################
###################################################

nodes = hou.selectedNodes()

geoAnim=nodes[0]
geoBake=nodes[1]

axis=('tx','ty','tz','rx','ry','rz')
currentFrame = hou.frame()
setKey = hou.Keyframe()

setKey.setFrame(currentFrame)

for ax in axis:
    anim = geoAnim.parm(ax).eval()
    setKey.setValue(anim)
    geoBake.parm(ax).setKeyframe(setKey)

#for frame in range(1,25):





###################################################
###################################################
##TOOL FOR CREATING NODES AND EDITING PARM FIELDS##
###################################################
###################################################
scene = hou.node('/obj/tentacleRIG1').children()
bones = []
nulls = []
fkBones = [] 
a = 1
b = 1
c = 0

for child in scene:
    if 'chain_bone' in child.name():
        bones.append(child)

for bone in bones:
    newNull = hou.node('/obj/tentacleRIG1').createNode('null','nullBone1')
    newNull.parm('tz').setExpression('-ch("../chain_bone'+str(a)+'/length")')
    newNull.setInput(0,bone,0)
    nulls.append(newNull)
    a += 1   
    
for null in nulls:
    fkBone = hou.node('/obj/tentacleRIG1').createNode('bone','fkBone1')
    fkBone.parm('length').setExpression('ch("../chain_bone'+str(b)+'/length")')
    fkBone.setInput(0,null,0)
    fkBones.append(fkBone)
    b += 1


##THESE TOOLS BELOW HAVE BEEN MADE TO DEAL WITH GEO IMPORTED AS FBX FROM MAYA##

####################################################################
####################################################################
##TOOL FOR COPYING PARM VALUES TO ANOTHER PARM AND REMOVE ORIGINAL##
####################################################################
####################################################################  
scene = hou.selectedNodes()

for item in scene:

    try:
        pivot = item.parmTuple('rpivot').eval()
        print pivot
    except AttributeError:
        pivot = None
    
    if pivot:
    
        item.parmTuple('p').set(pivot)
        item.parmTuple('rpivot').set((0,0,0))
        item.parmTuple('spivot').set((0,0,0))
        item.removeSpareParmTuple(item.parmTuple('rpivot'))
        item.removeSpareParmTuple(item.parmTuple('spivot'))
        
    else:
        
        print 'nothing to change'
    
##########################################################
##########################################################
##TOOL FOR CENTERING SOP GEO TO AN OFFSET TRANSFORM NODE##
##########################################################
##########################################################
#get a list of new geo pieces
newGeo = hou.selectedNodes()

#run an iteration over each item of the above list
for geo in newGeo:

    #find the parent node
    parent = geo.parent()
    
    #fetch the pivot values of the parent node
    pivot = parent.parmTuple('p').eval()
    
    #drop down a transform node called 'TransformPivot'
    transformNode = parent.createNode('xform','xformPivot_'+geo.name())
    
    #connect the transform node to the geo node
    transformNode.setInput(0,geo,0)
    
    #copy the values stored in pivot variable to the t parameter of the newly created transform node
    transformNode.parmTuple('t').set(pivot)
    
