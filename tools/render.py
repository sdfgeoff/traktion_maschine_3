import bpy
import argparse
import sys
import traceback
import os
import logging


def render(image_filename, res_percent, device):			
	bpy.context.scene.render.resolution_percentage = res_percent
	bpy.context.scene.render.filepath = image_filename
	bpy.context.scene.cycles.device = device
	if device == "GPU":
		bpy.context.scene.render.tile_x = 256
		bpy.context.scene.render.tile_y = 256
	
	bpy.ops.render.render('INVOKE_DEFAULT', write_still=True, use_viewport=False)

