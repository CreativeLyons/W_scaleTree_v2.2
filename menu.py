import W_scaleTree
nuke.menu('Nuke').addCommand('Edit/Node/W_scaleTree', 'W_scaleTree.scaleTreeFloatingPanel()', 'F4')
n = nuke.menu("Nuke")
st = n.findItem("Edit")
st.addCommand('W_scaleTree', 'W_scaleTree.scaleTreeFloatingPanel()', 'F4',icon = "W_ScaleTree_icon.png")