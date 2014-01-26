"""
Radiance Materials Info

-
Provided by Honybee 0.0.36
    
    Args:
        RADMaterial: Radiance material name
    Returns:
        RADMaterialStr: Radiance material definition

"""

ghenv.Component.Name = "Honeybee_Radiance Materials Info"
ghenv.Component.NickName = 'RADMaterialsInfo'
ghenv.Component.Message = 'VER 0.0.42\nJAN_24_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "1 | Daylight | Material"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

import scriptcontext as sc
import Grasshopper.Kernel as gh


if sc.sticky.has_key('honeybee_release'):
    
    hb_RADMaterialAUX = sc.sticky["honeybee_RADMaterialAUX"]()
    
    if RADMaterial!= None:
        # check if the name is in the library
        addedToLib, materialName = hb_RADMaterialAUX.analyseRadMaterials(RADMaterial, False)
        
        if materialName in sc.sticky["honeybee_RADMaterialLib"].keys():
            RADMaterialStr = hb_RADMaterialAUX.getRADMaterialString(materialName)
        
else:
    print "You should first let Honeybee to fly..."
    w = gh.GH_RuntimeMessageLevel.Warning
    ghenv.Component.AddRuntimeMessage(w, "You should first let Honeybee to fly...")