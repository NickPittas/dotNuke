import os
import sys
import nuke

############################################################################################################################################
##### INIT.PY ######
import __future__
import sys
nuke.pluginAddPath('./Plugins/3D')
nuke.pluginAddPath('./Plugins/Other')
nuke.pluginAddPath('./Python')
nuke.pluginAddPath('./Python/kiss')
nuke.pluginAddPath('./Python/Km-Rendering-Finished-main')
nuke.pluginAddPath('./Python/Startup')
nuke.pluginAddPath('./Python/Startup/dot_studio')
nuke.pluginAddPath('./Python/Startup/BaitTools')
nuke.pluginAddPath('./Python/StartupUI')
nuke.pluginAddPath('./Python/Time_Keeper')
# nuke.pluginAddPath('./Python/VP_MyLittleHelpers')
# nuke.pluginAddPath('./Python/VP_Lord_of_Nodes')
nuke.pluginAddPath('./Python/WrapItUp')
nuke.pluginAddPath('./Python/Backdrop_Helper_Toolkit')
nuke.pluginAddPath('./Python/nuke-vector-matrix-master')
nuke.pluginAddPath('./Python/MassivePanel')
nuke.pluginAddPath('./Python/KnobScripter')
nuke.pluginAddPath('./Python/JNS_Tools')
nuke.pluginAddPath('./Python/ProjectBrowser')
nuke.pluginAddPath('./Python/LabelConnector')
nuke.pluginAddPath('./Python/stamps')
nuke.pluginAddPath('./Python/ColorSpaceTransform') 

############################################################################################################################################

import W_backdropper # Alt+shift+b
import W_hotbox, W_hotboxManager # `
import frameServerStatus
import TrackedRoto
import mps2
# import knob_scripter # alt+z
import proxy_panel
import AnimationMaker
import reformat_presets
reformat_presets.nodePresetReformat()
import cam_presets
cam_presets.nodePresetCamera()
import combine_retimes
import bgNukes
import render_progress_panel
import custom_write_node
import Sequence_Browser  # Import the module where SequenceBrowserPanel is defined
import ffmpeg_convert
ffmpeg_convert.create_ffmpeg_converter_panel()

############################################################################################################################################
# import F_Backdrop 
# nukescripts.autoBackdrop = F_Backdrop.autoBackdrop # Original backdrop function replacement
# nuke.menu('Nodes').addCommand( 'Other/Backdrop', 'F_Backdrop.autoBackdrop()', 'ctrl+alt+b', 'Backdrop.png') # ctrl+alt+b
############################################################################################################################################

import version_increment

############################################################################################################################################
nuke.knobDefault("Root.format", "HD_1080")
nuke.knobDefault("Root.fps", "25")
nuke.knobDefault("Merge2.label", "[value bbox]\nmix [value mix]")
nuke.knobDefault("Grade.label", "[value mix]")
nuke.addFormat("12000 12000 1.0 12K LL180 Sphere")
nuke.addFormat("10000 10000 1.0 10K LL180 Sphere")
nuke.addFormat("8000 8000 1.0 8K LL180 Sphere")
nuke.addFormat("4000 4000 1.0 4K Proxy LL180 Sphere")
############################################################################################################################################
# Import the search and replace script
import search_replace_panel
############################################################################################################################################
# Node Graph Utils ##
import node_graph_utils
ICONS_ROOT = os.path.join(os.path.dirname(__file__), 'icons')
node_graph_utils.install_menus(icons_root=ICONS_ROOT, install_experimental_menus=True)
############################################################################################################################################

############################################################################################################################################
import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex(('127.0.0.1', 8188)) == 0:
        import nuke_comfyui as comfyui
        comfyui.setup()
    sock.close()
except:
    pass
############################################################################################################################################

## Menus    ##
############################################################################################################################################
import SetRotoShapesLifetimeAll
import lifetimeRoto
menuBar = nuke.menu('Nuke')
m = menuBar.addMenu("Tools")
m.addCommand("Set Roto Lifetime to All","SetRotoShapesLifetimeAll.SetRotoShapesLifetimeAll()")
m.addCommand('Set Roto Lifetime to In/Out keyframes', 'lifetimeRoto.setRotoLifeTime()', 'shift+l') # shift+i
import pasteToSelected
import PasteForEachNode
m.addCommand('Paste To Selected', 'pasteToSelected.pasteToSelected()', index=10)
m.addCommand('Paste For Each Node', "PasteForEachNode.PasteForEachNode()", "ctrl+shift+v", shortcutContext=2) # ctrl+shift+v
import pasteTransformation
m.addCommand("Paste Transformation(copy)", "pasteTransformation.pasteTransformation(link = False)", "alt+v") # alt+v
m.addCommand("Paste Transformation(link)", "pasteTransformation.pasteTransformation(link = True)", "shift+v") # shift+v
############################################################################################################################################

############################################################################################################################################
## Deadline ##
import DeadlineNukeClient
menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("&Thinkbox")
tbmenu.addCommand("Submit Nuke To Deadline", DeadlineNukeClient.main, "")
############################################################################################################################################

# HotBox   ##
import channel_hotbox
nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+q') # alt+q
############################################################################################################################################

############################################################################################################################################
## Plugins and Python Scripts from Nukepedia
##  3D      ##
threeDeeMenu = toolbar.addMenu('Nukepedia/3D')
import animatedSnap3D
threeDeeMenu.addCommand('Animated Snap 3D', 'animatedSnap3D.run()')
threeDeeMenu.addCommand("3DE4/LD_3DE4_Anamorphic_Standard_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_4')")
threeDeeMenu.addCommand("3DE4/LD_3DE4_Anamorphic_Rescaled_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Rescaled_Degree_4')")                    
threeDeeMenu.addCommand("3DE4/LD_3DE4_Anamorphic_Standard_Degree_6", "nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_6')")                    
threeDeeMenu.addCommand("3DE4/LD_3DE4_Anamorphic_Rescaled_Degree_6", "nuke.createNode('LD_3DE4_Anamorphic_Rescaled_Degree_6')")                    
threeDeeMenu.addCommand("3DE4/LD_3DE4_Radial_Standard_Degree_4", "nuke.createNode('LD_3DE4_Radial_Standard_Degree_4')")
threeDeeMenu.addCommand("3DE4/LD_3DE4_Radial_Fisheye_Degree_8", "nuke.createNode('LD_3DE4_Radial_Fisheye_Degree_8')")
threeDeeMenu.addCommand("3DE4/LD_3DE_Classic_LD_Model", "nuke.createNode('LD_3DE_Classic_LD_Model')")

##  Other   ##
otherMenu = toolbar.addMenu('Nukepedia/Other')
otherMenu.addCommand("Files/Localize Off", "Pause_localize()")
otherMenu.addCommand("Files/Localize On", "Start_localize()")
from bvfx_relativize import *
from bvfx_findPath import *
otherMenu.addCommand('Files/findPath', 'bvfx_findPath()')
otherMenu.addCommand('Files/relativize', 'bvfx_relativize()')
import WrapItUp
import RevealInExplorer
otherMenu.addCommand('Files/RevealInExplorer','RevealInExplorer.Revealexplr()')
import version_increment
otherMenu.addCommand('Files/Increment Write Version', 'version_increment.create_write_node()')
import dupReadDestroy
otherMenu.addCommand("Files/Remove Dupe Read", "dupReadDestroy.dupReadDestroy().destroy")
global glToggleRS; glToggleRS=0
otherMenu.addCommand( "Align/.Align Read Nodes  "            , "nuke.load('sbnAlignReadNodes_2020.py'), sbnAlignNodes('default')", "L", shortcutContext=2) # L
otherMenu.addCommand( "Align/.Align Read Nodes (vertical)"   , "nuke.load('sbnAlignReadNodes_2020.py'), sbnAlignNodes('vertical')", "shift+L", shortcutContext=2) # shift+L
otherMenu.addCommand( "Align/.Align Read Nodes (horizontal)" , "nuke.load('sbnAlignReadNodes_2020.py'), sbnAlignNodes('horizontal')", "", shortcutContext=2)
otherMenu.addCommand( "Align/.Align Read Nodes (wave)"       , "nuke.load('sbnAlignReadNodes_2020.py'), sbnAlignNodes('wave')", "", shortcutContext=2)
otherMenu.addCommand( "Align/.Align Read Nodes (zigzag)"     , "nuke.load('sbnAlignReadNodes_2020.py'), sbnAlignNodes('zigzag')", "", shortcutContext=2)

import retimeRoto
otherMenu.addCommand('Retime Roto', 'retimeRoto.start()')
otherMenu.addCommand('setReferenceFrame', 'nuke.load("jre_setReferenceFrame"), setReferenceFrame()','shift+f') # shift+F
import animated_cornerpin_to_matrix
otherMenu.addCommand("Animated CornerPin To Matrix", "animated_cornerpin_to_matrix.animatedCP2MTX()", icon="CornerPin.png")
import CornerPinToMatrix
otherMenu.addCommand('CornerPin To Matrix', 'cornerpin_to_matrix()', icon='CornerPin.png')
import autoCrop_MB
otherMenu.addCommand("Run AutoCropMB on Selected", "autoCrop_MB.autoCrop_MB")
import AutoCropTool
otherMenu.addCommand("Run AutoCropTool on Selected", "autocroptool()")

import CmdLineRender
otherMenu.addCommand('CL Render', 'CmdLineRender.CLrender(nuke.selectedNodes())')

import Dots
otherMenu.addCommand ('Dots', 'Dots.Dots()', ',') # , 
import ProjectsPanel
otherMenu.addCommand ('Projects Panel', 'ProjectsPanel.ProjectPanel()')
import presetBackdrop
otherMenu.addCommand('Preset Backdrop', 'presetBackdrop.presetBackdrop()', 'alt+b') # alt+b


############################################################################################################################################

############################################################################################################################################
def Pause_localize():
	nodes = nuke.allNodes()
	for read in nodes:
		if read.Class() == "Read":
			policy_off = read.knob('localizationPolicy').setValue(3)

def Start_localize():
	nodes = nuke.allNodes()
	for read in nodes:
		if read.Class() == "Read":
			policy_off = read.knob('localizationPolicy').setValue(0)


############################################################################################################################################

############################################################################################################################################
# def SG_write():
# 	import sgtk
# 	eng = sgtk.platform.current_engine()
# 	app = eng.apps["tk-nuke-writenode"]
# 	if app:
# 		app.convert_to_write_nodes() 

# SGwriteMenu = nuke.menu("Nodes").addMenu("SG Write Convert")
# SGwriteMenu.addCommand("SG Write Convert", "SG_write()")
############################################################################################################################################

############################################################################################################################################

nuke.pluginAddPath('./Python/nuke_node_operator/nodes_operator')
import node_operator_main_v01
import importlib

toolbar = nuke.menu("Nodes")
i = toolbar.addMenu("Studio")
# reload node operator
def start_NOP():
    importlib.reload(node_operator_main_v01)
    node_operator_main_v01.start()
i.addCommand("Node Operator v0.1", "start_NOP()")

############################################################################################################################################
import nuke
toolbar = nuke.menu("Nodes")
toolbar.addCommand('Cattery/Segmentation/ViTMatte', 'nuke.createNode("vitmatte")', icon="vitmatte.png")

import SphereResolutionLL180
nuke.menu("Nuke").addCommand('File/Apply Sphere Project Settings', 'SphereResolutionLL180.setup_resolutions()')
