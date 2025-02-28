import nuke
def nodePresetsStartup():
  nuke.setUserPreset("ColorCorrect", "Antetokoumpo Close Up", {'saturation': '1.15', 'contrast': '1.05', 'selected': 'true'})
  nuke.setUserPreset("ColorCorrect", "Bear", {'saturation': '1.05', 'contrast': '1.2', 'selected': 'true'})
  nuke.setUserPreset("Grade", "Human", {'multiply': '1.090872407 1.15006721 1.25999999 1', 'whitepoint': '1 0.9913569689 0.9851074815 1', 'selected': 'true', 'black': '-0.007000000682 0 0.00699999975 0'})
  nuke.setUserPreset("Grade", "Antetokoumpo Close Up", {'blackpoint': '0.004', 'white': '0.95 1 1.05 1', 'white_panelDropped': 'true', 'multiply': '1.18', 'gamma': '1.13', 'selected': 'true'})
