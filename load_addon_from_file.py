import bpy
import os

filename = os.path.join(os.path.dirname(bpy.data.filepath), "NameOfAddOn.py")
exec (compile(open(filename).read(), filename, 'exec'))
