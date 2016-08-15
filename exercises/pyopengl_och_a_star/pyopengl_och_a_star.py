
from time import *
from math import *
from random import *
from PIL import Image
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *

## 
## Rendering with OpenGL
## 

TEXTURE = 0
NODES = None
NODE_PATH = None

def task0_initOpenGL():
	glutInit( "" )
	glutInitWindowSize( 480, 480 )
	glutInitWindowPosition( 0, 0 )
	window = glutCreateWindow( b"Python OpenGL" )
	glutReshapeFunc( task0_reshape )
	glutKeyboardUpFunc( task0_keyboard )
	glutDisplayFunc( task0_render )
	glutIdleFunc( task0_render )
	task0_initProgram()
	glutMainLoop()
	task0_terminateProgram()

def task0_reshape( win_wid, win_hei ):
	glViewport( 0, 0, win_wid, win_hei )
	glMatrixMode( GL_PROJECTION )
	glLoadIdentity()
	glOrtho( 0.0, win_wid, 0.0, win_hei, 0.0, 1.0 )
	glMatrixMode( GL_MODELVIEW )

def task0_keyboard( a, b, c ):
	task2_rebuildNodes()

def task0_render():
	global NODES
	global NODE_PATH
	glClear( GL_COLOR_BUFFER_BIT )
	glLoadIdentity()
	
	glEnable( GL_TEXTURE_2D )
	glColor3f( 1.0, 1.0, 1.0 )
	glBegin( GL_QUADS )
	glTexCoord2f( 0.0, 0.0 )
	glVertex2f( 0.0, 480.0 )
	glTexCoord2f( 10.0, 0.0 )
	glVertex2f( 480.0, 480.0 )
	glTexCoord2f( 10.0, 10.0 )
	glVertex2f( 480.0, 0.0 )
	glTexCoord2f( 0.0, 10.0 )
	glVertex2f( 0.0, 0.0 )
	glEnd()
	
	#This is for task2
	glDisable( GL_TEXTURE_2D )
	task2_renderNodes( NODES, 10, 10 )
	task2_renderNodePath( NODE_PATH, 10, 10 )
	
	glutSwapBuffers()
	sleep( 1.0 )

def task0_loadTexture( image_path ):
	texture = glGenTextures( 1 )
	if texture is not 0:
		image = Image.open( image_path )
		image_width = image.size[ 0 ]
		image_height = image.size[ 1 ]
		image_data = image.tostring( "raw", "RGBX", 0, -1 )
		glActiveTexture( GL_TEXTURE0 )
		glBindTexture( GL_TEXTURE_2D, texture )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST )
		glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST )
		glTexImage2D( GL_TEXTURE_2D, 0, 3, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data )
	return texture

def task0_initProgram():
	global TEXTURE
	global NODES
	global NODE_PATH
	glLineWidth( 8.0 )
	glPointSize( 16.0 )
	TEXTURE = task0_loadTexture( "tile.png" )
	task2_rebuildNodes()

def task0_terminateProgram():
	global TEXTURE
	glDeleteTexture( TEXTURE )

## 
## Path finding with A*
## 

class Node:
	
	def __init__( self, posx, posy ):
		self.position = ( posx, posy )
		self.cost_g = 0
		self.cost_h = 0
		self.cost_f = 0
		self.opened = False
		self.closed = False
		self.enabled = True
		self.parent = None
		self.edges = []
	
	def addEdgeNode( self, node ):
		self.edges.append( node )
	
	def getEdges( self ):
		return self.edges
	
	def getGCostTo( self, node ):
		cost = 0
		if node is not None:
			cost = cost + node.cost_g
			if ( self.position[ 0 ] is node.position[ 0 ]
				or self.position[ 1 ] is node.position[ 1 ] ):
				cost += 10
			else:
				cost += 14
		return cost
	def getHCostTo( self, node ):
		cost = ( abs( self.position[ 0 ] - node.position[ 0 ] )
			+ abs( self.position[ 1 ] - node.position[ 1 ] ) ) * 10
		return cost
	def applyCostsToSelf( self, end_node ):
		self.cost_g = self.getGCostTo( self.parent )
		self.cost_h = self.getHCostTo( end_node )
	def getFCost( self ):
		return self.cost_g + self.cost_h

def task1_AStarSearch( start_node, end_node ):
	if start_node is None:
		print( "Missing a starting node." )
		return None
	elif end_node is None:
		print( "Missing an end node." )
		return None
	elif start_node.position is end_node.position:
		print( "Already there." )
		return []
	elif not start_node.enabled:
		print( "Start node blocked." )
		return None
	elif not end_node.enabled:
		print( "End node blocked." )
		return None
	else:
		current = start_node
		opened = [ start_node ]
		closed = []
		start_node.applyCostsToSelf( end_node )
		start_node.opened = True
		number_of_iterations = 0
		while ( number_of_iterations < 200
			and current is not None ):
			number_of_iterations += 1
			open_cost = 99999999999
			current = None
			for node in opened:
				if node.getFCost() < open_cost:
					current = node
					open_cost = node.getFCost()
			if current is end_node:
				break
			elif current not in opened:
				print( "Failed, no path available." )
				return None
			else:
				opened.remove( current )
			closed.append( current )
			current.closed = True
			current.opened = False
			for node in current.edges:
				if not node.enabled or node.closed:
					continue
				elif node.opened:
					if node.cost_g <= node.getGCostTo( current ):
						continue
				else:
					opened.append( node )
					node.opened = True
				node.parent = current
				node.applyCostsToSelf( end_node )
		for node in opened:
			node.opened = False
		for node in closed:
			node.closed = False
		path = []
		while current is not None:
			path.append( current )
			current = current.parent
		result = list( reversed( path ) )
		print( "The path consists of " + str( len( result ) ) + " nodes." )
		return result

def task1_buildRandomNodeField( width, height ):
	nodes = []
	for x in range( 0, width ):
		l = []
		nodes.append( l )
		for y in range( 0, height ):
			l.append( Node( x, y ) )
	for x in range( 0, width ):
		for y in range( 0, height ):
			node = nodes[ x ][ y ]
			#These are edges to direct neighbours
			if x > 0:
				node.addEdgeNode( nodes[ x - 1 ][ y ] )
			if y > 0:
				node.addEdgeNode( nodes[ x ][ y - 1 ] )
			if x < width - 1:
				node.addEdgeNode( nodes[ x + 1 ][ y ] )
			if y < height - 1:
				node.addEdgeNode( nodes[ x ][ y + 1 ] )
			#And these are for diagonal neighbours
			if x > 0 and y > 0:
				node.addEdgeNode( nodes[ x - 1 ][ y - 1 ] )
			if x < width - 1 and y > 0:
				node.addEdgeNode( nodes[ x + 1 ][ y - 1 ] )
			if x < width - 1 and y < height - 1:
				node.addEdgeNode( nodes[ x + 1 ][ y + 1 ] )
			if x > 0 and y < height - 1:
				node.addEdgeNode( nodes[ x - 1 ][ y + 1 ] )
			#This is for setting a node to disabled
			if random() >= 0.75:
				node.enabled = False
	return nodes

## 
## Putting it all together
## 

def task2_renderNodes( nodes, dimx, dimy ):
	if nodes is None:
		return
	else:
		step_x = 480.0 / dimx
		step_y = 480.0 / dimy
		init_x = step_x / 2.0
		init_y = step_y / 2.0
		for xs in nodes:
			for node in xs:
				if node.enabled:
					glColor3f( 0.0, 1.0, 0.0 )
				else:
					glColor3f( 0.0, 0.0, 1.0 )
				glBegin( GL_POINTS )
				glVertex2f( init_x + step_x * node.position[ 0 ],
					init_y + step_y * node.position[ 1 ] )
				glEnd()

def task2_renderNodePath( path_nodes, dimx, dimy ):
	if ( path_nodes is None
		or len( path_nodes ) <= 1 ):
		return
	else:
		step_x = 480.0 / dimx
		step_y = 480.0 / dimy
		init_x = step_x / 2.0
		init_y = step_y / 2.0
		from_pos = path_nodes[ 0 ].position
		for node in path_nodes:
			to_pos = node.position
			glBegin( GL_LINE_STRIP )
			glVertex2f( init_x + step_x * from_pos[ 0 ],
				init_y + step_y * from_pos[ 1 ] )
			glVertex2f( init_x + step_x * to_pos[ 0 ],
				init_y + step_y * to_pos[ 1 ] )
			glEnd()
			from_pos = to_pos

def task2_rebuildNodes():
	global NODES
	global NODE_PATH
	NODES = task1_buildRandomNodeField( 10, 10 )
	NODE_PATH = task1_AStarSearch( NODES[ 0 ][ 0 ], NODES[ 9 ][ 9 ] )
	task0_render()

## 
## Start the program
## 

task0_initOpenGL()