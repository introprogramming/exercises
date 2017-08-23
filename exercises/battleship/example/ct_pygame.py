#CT_Pygame version 1.01

#Import needed modules.
import pygame, sys, time, math
from pygame.locals import *

#Define several global variables used for setting up the window
#and keep track of the program state.
__WINDOW = None
__CANVAS = None
__FONT = None
__FONT_NAME = None
__FONT_SIZE = 32
__WINDOW_TITLE = ""
__WINDOW_SIZE = ( 720, 480 )
__BACKGROUND_COLOR = ( 0, 0, 0, 255 )
__OBJECTS = {}
__RENDER_LIST = []
__LOADED_IMAGES = {}
__KEYS_DOWN = {}
__FPS = 30.0
__START_FUNCTION = None
__UPDATE_FUNCTION = None
__KEY_PRESSED_FUNCTION = None
__KEY_RELEASED_FUNCTION = None
__KEY_HELD_FUNCTION = None
__MOUSE_MOVED_FUNCTION = None
__MOUSE_PRESSED_FUNCTION = None
__MOUSE_RELEASED_FUNCTION = None
__RAY_CAST_FUNCTION = None
__RAY_CAST_ENTERED_FUNCTION = None
__RAY_CAST_EXITED_FUNCTION = None
__COLLISION_FUNCTION = None
__MOUSE_POSITION = ( 0, 0 )
__DESTROYED_OBJECTS = []
__CREATED_OBJECTS = []

# A class for storing a single object's properties.
class ctObject:
	def __init__( self, surface, position, size, rotation, name, solid, visible ):
		self.surface = surface
		self.position = position
		self.size = size
		self.rotation = rotation
		self.hovered = False
		self.solid = solid
		self.visible = visible
		self.name = name

## Pygame functions needed for setting up the library environment.

def ctStartApp():
	global __WINDOW, __CANVAS
	global __WINDOW_TITLE, __WINDOW_SIZE
	pygame.init()
	__WINDOW = pygame.display
	__WINDOW.set_caption( __WINDOW_TITLE )
	__CANVAS = __WINDOW.set_mode( ( __WINDOW_SIZE ) )
	ctLoadFont()

def ctEndApp():
	pygame.quit()

def ctLoadFont( font_path = None, font_size = 32 ):
	#Load a new font for use when creating text objects.
	global __FONT
	if font_path:
		font_path = open( font_path )
	__FONT = pygame.font.Font( font_path, font_size )

def ctMainLoop():
	global __OBJECTS, __DESTROYED_OBJECTS, __CREATED_OBJECTS, __WINDOW, __FPS, __MOUSE_POSITION, __KEYS_DOWN
	global __UPDATE_FUNCTION, __KEY_PRESSED_FUNCTION, __KEY_RELEASED_FUNCTION, __KEY_HELD_FUNCTION
	global __COLLISION_FUNCTION, __RAY_CAST_FUNCTION, __RAY_CAST_ENTERED_FUNCTION, __RAY_CAST_EXITED_FUNCTION
	while True:
		#Create marked objects.
		if len( __CREATED_OBJECTS ) > 0:
			for ( tag, obj ) in __CREATED_OBJECTS:
				__OBJECTS[ tag ] = obj
			__CREATED_OBJECTS = []
		#Since someone might attempt to bind new callback functions in mid game
		#we will have to recalculate these booleans every iteration.
		take_mouse_events = __RAY_CAST_FUNCTION or __RAY_CAST_ENTERED_FUNCTION or __RAY_CAST_EXITED_FUNCTION
		#Iterate over all held keys.
		if __KEY_HELD_FUNCTION:
			ctCallUserHeldKeys()
		#Process all new program events.
		for event in pygame.event.get():
			#Quit if received a "quit" event.
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				__KEYS_DOWN[ event.key ] = True
				ctCallUserKeyPressed( event.key )
			elif event.type == pygame.KEYUP:
				__KEYS_DOWN.pop( event.key, None )
				ctCallUserKeyReleased( event.key )
			elif take_mouse_events:
				#Only handle mouse events if at least one callback function is bound.
				if event.type == pygame.MOUSEMOTION:
					__MOUSE_POSITION = event.pos
					ctCallUserMouseMoved( event.buttons )
					if __RAY_CAST_ENTERED_FUNCTION or __RAY_CAST_EXITED_FUNCTION:
						ctRayCast( "auto:mouse", event.pos, hover_action = True )
				elif event.type == pygame.MOUSEBUTTONDOWN:
					__MOUSE_POSITION = event.pos
					ctCallUserMousePressed( event.button )
					if __RAY_CAST_FUNCTION:
						ctRayCast( "auto:mouse", event.pos )
				elif event.type == pygame.MOUSEBUTTONUP:
					__MOUSE_POSITION = event.pos
					ctCallUserMousePressed( event.button )
		#Allow for the user to update the game.
		if __UPDATE_FUNCTION:
			ctCallUserUpdate()
		#Test for collisions only when a callback is bound.
		if __COLLISION_FUNCTION:
			ctCollisionPass( "auto:collision" )
		#Draw the scene.
		ctDrawScene()
		#Destroy marked objects.
		if len( __DESTROYED_OBJECTS ) > 0:
			for tag in __DESTROYED_OBJECTS:
				__OBJECTS.pop( tag, None )
			__DESTROYED_OBJECTS = []
		#Cap frame rate
		time.sleep( 1.0 / __FPS )

##Internal functions for callbacks.

def ctCallUserStart():
	global __START_FUNCTION
	if __START_FUNCTION:
		__START_FUNCTION()

def ctCallUserUpdate():
	global __UPDATE_FUNCTION
	if __UPDATE_FUNCTION:
		__UPDATE_FUNCTION()

def ctCallUserKeyPressed( key ):
	global __KEY_PRESSED_FUNCTION
	if __KEY_PRESSED_FUNCTION:
		__KEY_PRESSED_FUNCTION( key )

def ctCallUserKeyReleased( key ):
	global __KEY_RELEASED_FUNCTION
	if __KEY_RELEASED_FUNCTION:
		__KEY_RELEASED_FUNCTION( key )

def ctCallUserHeldKeys():
	global __KEY_HELD_FUNCTION, __KEYS_DOWN
	if __KEY_HELD_FUNCTION:
		for key in __KEYS_DOWN:
			__KEY_HELD_FUNCTION( key )

def ctCallUserMouseMoved( buttons ):
	global __MOUSE_MOVED_FUNCTION
	if __MOUSE_MOVED_FUNCTION:
		__MOUSE_MOVED_FUNCTION( buttons )

def ctCallUserMousePressed( button ):
	global __MOUSE_PRESSED_FUNCTION
	if __MOUSE_PRESSED_FUNCTION:
		__MOUSE_PRESSED_FUNCTION( button )

def ctCallUserMouseReleased( button ):
	global __MOUSE_RELEASED_FUNCTION
	if __MOUSE_RELEASED_FUNCTION:
		__MOUSE_RELEASED_FUNCTION( button )

def ctCallUserRayCast( name, tag, abs_pos, rel_pos ):
	global __RAY_CAST_FUNCTION
	if __RAY_CAST_FUNCTION:
		__RAY_CAST_FUNCTION( name, tag, abs_pos, rel_pos )

def ctCallUserRayCastEntered( name, tag, abs_pos, rel_pos ):
	global __RAY_CAST_ENTERED_FUNCTION
	if __RAY_CAST_ENTERED_FUNCTION:
		__RAY_CAST_ENTERED_FUNCTION( name, tag, abs_pos, rel_pos )

def ctCallUserRayCastExited( name, tag, abs_pos, rel_pos ):
	global __RAY_CAST_EXITED_FUNCTION
	if __RAY_CAST_EXITED_FUNCTION:
		__RAY_CAST_EXITED_FUNCTION( name, tag, abs_pos, rel_pos )

def ctCallUserCollision( name, tag0, tag1, correction ):
	global __COLLISION_FUNCTION
	if __COLLISION_FUNCTION:
		__COLLISION_FUNCTION( name, tag0, tag1, correction )

## Functions for drawing onto the window.

def ctClearCanvas():
	global __CANVAS
	__CANVAS.fill( __BACKGROUND_COLOR )

def ctDrawScene():
	#Clear the window and draw all objects.
	global __WINDOW, __RENDER_LIST, __CANVAS
	ctClearCanvas()
	for tag in __RENDER_LIST:
		try:
			obj = ctGetObject( tag )
		except KeyError:
			continue
		if obj.visible:
			scaled_surface = pygame.transform.scale( obj.surface, obj.size )
			rotated_surface = pygame.transform.rotate( scaled_surface, obj.rotation )
			final_surface = rotated_surface
			new_size = final_surface.get_size()
			new_position = (
				obj.position[ 0 ] - ( new_size[ 0 ] - obj.size[ 0 ] ) / 2.0,
				obj.position[ 1 ] - ( new_size[ 1 ] - obj.size[ 1 ] ) / 2.0 )
			__CANVAS.blit( final_surface, new_position )
	#Update the displayed window content.
	__WINDOW.flip()
	__WINDOW.update()

## Helpful functions for "ray casting".

def ctGetCenter( position, size ):
	return ( position[ 0 ] + size[ 0 ] / 2, position[ 1 ] + size[ 1 ] / 2 )

def ctRotatePointAround( position, center, r ):
	#Rotate the point "position" around the point "center" with "r" deg.
	radi = r * math.pi / 180.0
	c = math.cos( radi )
	s = math.sin( radi )
	dx = position[ 0 ] - center[ 0 ]
	dy = position[ 1 ] - center[ 1 ]
	nx = c * dx - s * dy + center[ 0 ]
	ny = s * dx + c * dy + center[ 1 ]
	return ( nx, ny )

def ctRayCast( name, position, hover_action = False ):
	#Cast a ray (namned "name") into the window at "position" and call the configured callback function
	#for each hit. Note that the name "auto:mouse" is used by the update loop.
	global __RENDER_LIST
	for tag in __RENDER_LIST:
		try:
			obj = ctGetObject( tag )
		except KeyError:
			continue
		center = ctGetCenter( obj.position, obj.size )
		off = ctRotatePointAround( position, center, obj.rotation )
		if ( off[ 0 ] >= obj.position[ 0 ] and off[ 0 ] <= obj.position[ 0 ] + obj.size[ 0 ]
			and off[ 1 ] >= obj.position[ 1 ] and off[ 1 ] <= obj.position[ 1 ] + obj.size[ 1 ] ):
			if hover_action and obj.hovered is False:
				obj.hovered = True
				ctCallUserRayCastEntered( name, tag, position, ( off[ 0 ] - obj.position[ 0 ], off[ 1 ] - obj.position[ 1 ] ) )
			if not hover_action:
				ctCallUserRayCast( name, tag, position, ( off[ 0 ] - obj.position[ 0 ], off[ 1 ] - obj.position[ 1 ] ) )
		elif hover_action and obj.hovered:
			obj.hovered = False
			ctCallUserRayCastExited( name, tag, position, ( off[ 0 ] - obj.position[ 0 ], off[ 1 ] - obj.position[ 1 ] ) )

## Functions for collision.

def ctAABB( pos0, size0, r0, pos1, size1, r1 ):
	#Perform a simple implementation of the "Separate normal axis theorem" (AABB-collision)
	#on two rectangles defined by a position, size and rotation in deg. Will return "None"
	#on no collision or a correction vector that should be applied to the "0" object in order
	#to correct the placement so no collision occours.
	def sub( a, b ):
		return ( a[ 0 ] - b[ 0 ], a[ 1 ] - b[ 1 ] )
	def dot( a, b ):
		return a[ 0 ] * b[ 0 ] + a[ 1 ] * b[ 1 ]
	def norm( a ):
		#Return normalized normal vector
		l = math.sqrt( a[ 0 ] * a[ 0 ] + a[ 1 ] * a[ 1 ] )
		return ( a[ 1 ] / l, - a[ 0 ] / l )
	def neg( a ):
		return ( - a[ 0 ], - a[ 1 ] )
	def mul( f, a ):
		return ( f * a[ 0 ], f * a[ 1 ] )
	center_a = ctGetCenter( pos0, size0 )
	center_b = ctGetCenter( pos1, size1 )
	a0 = ctRotatePointAround( pos0, center_a, r0 )
	a1 = ctRotatePointAround( ( pos0[ 0 ] + size0[ 0 ], pos0[ 1 ] ), center_a, r0 )
	a2 = ctRotatePointAround( ( pos0[ 0 ] + size0[ 0 ], pos0[ 1 ] + size0[ 1 ] ), center_a, r0 )
	a3 = ctRotatePointAround( ( pos0[ 0 ], pos0[ 1 ] + size0[ 1 ] ), center_a, r0 )
	ax = ( a0, a1, a2, a3 )
	b0 = ctRotatePointAround( pos1, center_b, r1 )
	b1 = ctRotatePointAround( ( pos1[ 0 ] + size1[ 0 ], pos1[ 1 ] ), center_b, r1 )
	b2 = ctRotatePointAround( ( pos1[ 0 ] + size1[ 0 ], pos1[ 1 ] + size1[ 1 ] ), center_b, r1 )
	b3 = ctRotatePointAround( ( pos1[ 0 ], pos1[ 1 ] + size1[ 1 ] ), center_b, r1 )
	bx = ( b0, b1, b2, b3 )
	#Yes, I know we actually only have to check two normals per object,
	#but this was supposed to be a general implementation at some point.
	#I can easily be rewritten to take convex polygon shapes if needed.
	axs = (
		norm( sub( a1, a0 ) ),
		norm( sub( a2, a1 ) ),
		norm( sub( a3, a2 ) ),
		norm( sub( a0, a3 ) ),
		norm( sub( b1, b0 ) ),
		norm( sub( b2, b1 ) ),
		norm( sub( b3, b2 ) ),
		norm( sub( b0, b3 ) ) )
	pss = ( a0, a1, a2, a3, b0, b1, b2, b3 )
	min_len = sys.float_info.max
	min_norm = ( 1, 0 )
	for i in xrange( 0, 8 ):
		d = axs[ i ]
		p = pss[ i ]
		min_a = sys.float_info.max
		max_a = - sys.float_info.max
		min_b = sys.float_info.max
		max_b = - sys.float_info.max
		for a in ax:
			l = dot( d, sub( a, p ) )
			min_a = min( min_a, l )
			max_a = max( max_a, l )
		for b in bx:
			l = dot( d, sub( b, p ) )
			min_b = min( min_b, l )
			max_b = max( max_b, l )
		if( max_a < min_b or min_a > max_b ):
			return False
		else:
			len0 = ( max_a - min_b )
			len1 = ( max_b - min_a )
			if min( len0, len1 ) < min_len:
				if len0 < len1:
					min_len = len0
					min_norm = neg( d )
				else:
					min_len = len1
					min_norm = d
	return mul( min_len, min_norm )

def ctCollisionPass( name ):
	#Will iterate through all objects and check for collisions.
	#If any are found then the collision callback function will be
	#called with "name" as the identifier.
	global __OBJECTS
	ls = list( __OBJECTS )
	ln = len( ls )
	for i in xrange( 0, ln ):
		tag0 = ls[ i ]
		obj0 = ctGetObject( tag0 )
		for n in xrange( i + 1, ln ):
			tag1 = ls[ n ]
			obj1 = ctGetObject( tag1 )
			#Make sure only solid object collide
			if obj0.solid and obj1.solid:
				res = ctAABB( obj0.position, obj0.size, - obj0.rotation, obj1.position, obj1.size, - obj1.rotation )
				if res:
					ctCallUserCollision( name, tag0, tag1, res )

## Functions for loading graphics.

def ctGetImage( image_path ):
	global __LOADED_IMAGES
	try:
		return __LOADED_IMAGES[ image_path ]
	except KeyError:
		img = pygame.image.load( image_path ).convert_alpha()
		__LOADED_IMAGES[ image_path ] = img
		return img 

def ctGetTextImage( message, color ):
	global __FONT
	return __FONT.render( message, 1, color )

## Function for creating and manipulating objects.

def ctGetObject( tag ):
	global __OBJECTS, __CREATED_OBJECTS
	try:
		return __OBJECTS[ tag ]
	except KeyError:
		for ( t, o ) in __CREATED_OBJECTS:
			if tag == t:
				return o
		return None

def ctCreateObject( tag, image_path, position = ( 0, 0 ), size = None, rotation = 0.0, name = "", solid = True, visible = True ):
	#Creates a new image object with the identifier in "tag" by loading the image found at "image_path".
	ctCreateEntity( tag, ctGetImage( image_path ), position, size, rotation, name, solid, visible )

def ctCreateText( tag, message = "", color = ( 255, 255, 255, 255 ), position = ( 0, 0 ), size = None, rotation = 0.0, name = None, solid = True, visible = True ):
	if name == None:
		name = message
	#Creates a new text object with the identifier in "tag" with the text passed as "message".
	ctCreateEntity( tag, ctGetTextImage( message, color ), position, size, rotation, name, solid, visible )

def ctCreateEntity( tag, surface, position, size, rotation, name, solid, visible ):
	#Not to be used outside the wrapper module.
	global __CREATED_OBJECTS, __RENDER_LIST
	if size == None:
		size = surface.get_size()
	obj = ctObject( surface, position, size, rotation, name, solid, visible )
	__CREATED_OBJECTS.append( ( tag, obj ) )
	__RENDER_LIST.append( tag )

def ctDestroyObject( tag ):
	#Destroys a object given the tag in "tag".
	global __DESTROYED_OBJECTS, __RENDER_LIST
	__DESTROYED_OBJECTS.append( tag )
	__RENDER_LIST.remove( tag )

def ctSetObjectImage( tag, image_path, size = None ):
	#Swaps the object image with a new image.
	obj = ctGetObject( tag )
	obj.surface = ctGetImage( image_path )
	if size == None:
		obj.size = obj.surface.get_size()

def ctSetObjectText( tag, message = "", color = ( 255, 255, 255, 255 ), size = None ):
	#Swaps the object image with a new image.
	obj = ctGetObject( tag )
	obj.surface = ctGetTextImage( message, color )
	if size == None:
		obj.size = obj.surface.get_size()

def ctPlaceObject( tag, new_position ):
	#Places the object with the identifier in "tag" at position (x, y).
	ctGetObject( tag ).position = new_position

def ctPlaceCenterObject( tag, new_position ):
	#Places the center of object with the identifier in "tag" at position (x, y).
	obj = ctGetObject( tag )
	obj.position = (
		new_position[ 0 ] - obj.size[ 0 ] / 2,
		new_position[ 1 ] - obj.size[ 1 ] / 2 )

def ctMoveObject( tag, direction ):
	#Moves the object with the identifier in "tag" with the offset (dx, dy).
	obj = ctGetObject( tag )
	obj.position = (
		obj.position[ 0 ] + direction[ 0 ],
		obj.position[ 1 ] + direction[ 1 ] )

def ctMoveObjectInDirection( tag, direction ):
	#Moves the object with the identifier in "tag" with the object local offset (dx, dy).
	obj = ctGetObject( tag )
	radi = obj.rotation * math.pi / 180.0
	radi2 = radi + math.pi / 2.0
	obj.position = (
		obj.position[ 0 ] + ( direction[ 0 ] * math.cos( radi ) + direction[ 1 ] * math.cos( radi2 ) ),
		obj.position[ 1 ] - ( direction[ 0 ] * math.sin( radi ) + direction[ 1 ] * math.sin( radi2 ) ) )

def ctAngleObject( tag, new_angle ):
	#Sets the object rotation with the identifier in "tag" to "new_angle" in deg.
	ctGetObject( tag ).rotation = new_angle

def ctRotateObject( tag, angle ):
	#Rotates the object rotation with the identifier in "tag" with "angle" in deg.
	ctGetObject( tag ).rotation += angle

def ctSizeObject( tag, new_size ):
	#Sets the object size with the identifier in "tag" to "new_size" (width, height).
	ctGetObject( tag ).size = new_size

## Functions for fetching object values.

def ctGetObjectPosition( tag ):
	return ctGetObject( tag ).position

def ctSetObjectPosition( tag, position ):
	ctGetObject( tag ).position = position

def ctGetObjectSize( tag ):
	return ctGetObject( tag ).size

def ctSetObjectSize( tag, size ):
	ctGetObject( tag ).size = size

def ctGetObjectRotation( tag ):
	return ctGetObject( tag ).rotation

def ctSetObjectRotation( tag, rotation ):
	ctGetObject( tag ).rotation = rotation

def ctGetObjectName( tag ):
	return ctGetObject( tag ).name

def ctSetObjectName( tag, name ):
	ctGetObject( tag ).name = name

def ctGetObjectHovered( tag ):
	#Note that this property only makes sense if
	#at least one of the hover callbacks have been set.
	return ctGetObject( tag ).hovered

def ctGetObjectSolid( tag ):
	return ctGetObject( tag ).solid

def ctSetObjectSolid( tag, solid ):
	ctGetObject( tag ).solid = solid

def ctGetObjectVisible( tag ):
	return ctGetObject( tag ).visible

def ctSetObjectVisible( tag, visible ):
	ctGetObject( tag ).visible = visible

def ctHasObject( tag ):
	return ctGetObject( tag ) != None

## Functions for getting some handy values.

def ctGetMousePosition():
	global __MOUSE_POSITION
	return __MOUSE_POSITION

def ctGetWindowSize():
	global __WINDOW
	return __WINDOW.get_size()

## Function for binding callback functions.

def ctSetup( width, height, title = "", background = ( 0, 0, 0, 255 ), fps = 30.0 ):
	#Allows for setting some inital values used by the program window.
	global __WINDOW_TITLE, __WINDOW_SIZE, __BACKGROUND_COLOR, __FPS
	__WINDOW_TITLE = title
	__WINDOW_SIZE = ( int( width ), int( height ) )
	__BACKGROUND_COLOR = background
	__FPS = min( max( 1, fps ), 128 )

def ctBindFunctions( start = None, update = None, key_pressed = None, key_released = None, key_held = None, mouse_moved = None, mouse_pressed = None, mouse_released = None, ray_cast = None, ray_cast_entered = None, ray_cast_exited = None, collision = None ):
	#Binds each argument as a callback function. If a callback function is set to "None" that type of event will not be generated.
	#NOTE: This function should be called before "ctBegin".
	global __START_FUNCTION, __UPDATE_FUNCTION
	global __KEY_PRESSED_FUNCTION, __KEY_RELEASED_FUNCTION, __KEY_HELD_FUNCTION
	global __MOUSE_MOVED_FUNCTION, __MOUSE_PRESSED_FUNCTION, __MOUSE_RELEASED_FUNCTION
	global __RAY_CAST_FUNCTION, __RAY_CAST_ENTERED_FUNCTION, __RAY_CAST_EXITED_FUNCTION, __COLLISION_FUNCTION
	__START_FUNCTION = start
	__UPDATE_FUNCTION = update
	__KEY_PRESSED_FUNCTION = key_pressed
	__KEY_RELEASED_FUNCTION = key_released
	__KEY_HELD_FUNCTION = key_held
	__MOUSE_MOVED_FUNCTION = mouse_moved
	__MOUSE_PRESSED_FUNCTION = mouse_pressed
	__MOUSE_RELEASED_FUNCTION = mouse_released
	__RAY_CAST_FUNCTION = ray_cast
	__RAY_CAST_ENTERED_FUNCTION = ray_cast_entered
	__RAY_CAST_EXITED_FUNCTION = ray_cast_exited
	__COLLISION_FUNCTION = collision

def ctBegin():
	#Starts the program.
	#NOTE: This function should be called (only once) after "ctBindFunctions".
	ctStartApp()
	ctCallUserStart()
	ctMainLoop()
	ctEndApp()
