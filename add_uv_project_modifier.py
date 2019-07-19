import bpy
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Add UV Project Modifier",
    "author" : "Danni Coy",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

def register():
    bpy.utils.register_class(AddUVProjectModifierOperator)

def unregister():
    bpy.utils.unregister_class(AddUVProjectModifierOperator)

def add_uv_project_modifier():
    project_onto = bpy.context.active_object
    projector_obs = list(filter(lambda x : x != project_onto, bpy.context.selected_objects))
    modifier = project_onto.modifiers.new(name="UVProject", type='UV_PROJECT')
    modifier.projector_count = min(10,len(projector_obs))
    for i in range (0, modifier.projector_count):
        modifier.projectors[i].object = projector_obs[i]

class AddUVProjectModifierOperator(bpy.types.Operator):
    bl_idname = "object.adduvprojectmodifier"
    bl_label = "AddUVProjectModifier"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        add_uv_project_modifier()
        return {'FINISHED'} 
    def execute(self, context):
        add_uv_project_modifier()
        return {'FINISHED'}
    @classmethod
    def poll(self, context):
        return context.object is not None
