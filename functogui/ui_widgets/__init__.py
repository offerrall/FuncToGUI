from .ui_base import *
from .ui_bool import *
from .ui_color import *
from .ui_list import *
from .ui_numeric import *
from .ui_str import *
from .ui_os import *
from .ui_time import *
from .ui_date import *



PROPERTY_TYPES = {
    "strUi": CustomStrProperty,
    "intUi": CustomIntProperty,
    "boolUi": CustomBoolProperty,
    "listUi": CustomListProperty,
    "fileUi": CustomFileProperty,
    "floatUi": CustomFloatProperty,
    "colorUi": CustomColorProperty,
    "folderUi": CustomFolderProperty,
    "passwordUi": CustomPasswordProperty,
    "timeUi": CustomTimeProperty,
    "dateUi": CustomDateProperty,
}