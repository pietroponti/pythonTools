###################################################
###################################################
#### TOOL FOR BAKING TRANSFORMS BETWEEN NODES #####
###################################################
###################################################
nodes = hou.selectedNodes()

#Variables
geoAnim=nodes[0]
geoBake=nodes[1]

axis=('tx','ty','tz','rx','ry','rz')

firstFrame = raw_input('Please Enter first frame')
lastFrame = raw_input('Please Enter last frame')

for i in range (firstFrame,lastFrame):

    hou.setFrame(i)
    setKey = hou.Keyframe()
    setKey.setFrame(i)

    xform = geoAnim.worldTransform()
    geoBake.setWorldTransform(xform)
    
    for ax in axis:
        anim = geoBake.parm(ax).eval()
        setKey.setValue(anim)
        geoBake.parm(ax).setKeyframe(setKey)

    
