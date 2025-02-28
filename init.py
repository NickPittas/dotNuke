import nuke
import os
import sys
import __future__
import sys

nuke.pluginAddPath('./icons')

nuke.pluginAddPath('./higx/PointRender')
nuke.pluginAddPath('./NukeSurvivalToolkit')
nuke.pluginAddPath('./pixelfudger3')
nuke.pluginAddPath("./connect_v3.11")
nuke.pluginAddPath('./smartRender_v3.25')
nuke.pluginAddPath('./spin_nuke_gizmos/gizmos')
nuke.pluginAddPath('./Cattery/vitmatte')
nuke.pluginAddPath('./magicdefocus2')


# #sys.path.append("c:/users/nick/appdata/roaming/python/python310/site-packages")
# #sys.path.append("c:/users/npitt/appdata/local/programs/python/python310/lib/site-packages")
# #sys.path.append("c:/users/nick/appdata/roaming/python/python310/lib/site-packages")
# #sys.path.append("c:/program files/python310/lib/site-packages")
# #nuke.pluginAddPath('C:/Users/Nick/AppData/Roaming/Python/Python310/site-packages')
# #nuke.pluginAddPath('c:/users/nick/appdata\local/programs/python/python310/lib/site-packages')
# nuke.pluginAddPath('./Blink/VoxelRenderer-master/plugin')



def initFolder(targetFolder):
    if targetFolder in sys.path:
        return
    if not os.path.isdir(targetFolder):
        print ('Path is not valid (%s)' % targetFolder)
    sys.path.append(targetFolder)

