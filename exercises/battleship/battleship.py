
import curses
import time

##
## An implementation of the game Battleship
##

def task_initScreen():
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	screen.keypad( 1 )
	curses.curs_set( 0 )
	screen.move( 0, 0 )
	screen.addstr( ">" )
	screen.move( 1, 0 )
	screen.addstr( "#" )
	task_drawBoard( screen )
	return screen

def task_terminateScreen( screen ):
	curses.curs_set( 1 )
	curses.nocbreak()
	screen.keypad( 0 )
	curses.echo()
	curses.endwin()
	return

class Ship:
	def __init__( self ):
		self.points = []
		return

class Player:
	def __init__( self ):
		self.ships = []
		self.shots = []
		return

class Environment:
	def __init__( self ):
		self.resetCursor()
		self.players = [ Player(), Player() ]
		self.current = None
		self.opponent = None
		self.rotate = False
		self.ship_placement = None
		self.current_offset_x = 0
		self.opponent_offset_x = 11
		self.ship_stack = None
		
		#mode -1 - initial mode
		#mode 0  - setup player on the right side
		#mode 1  - setup player on the left side
		#mode 2  - right side player attack
		#mode 3  - left side player attack
		
		self.mode = -1
		return
	
	def resetCursor( self ):
		self.cursor = ( 4, 4 )
		self.rotate = False
		return
	
	def currentCursorOffset( self ):
		if self.mode == 0:
			return 0
		elif self.mode == 1:
			return 11
		else:
			return self.opponent_offset_x
	
	def getOrientationString( self ):
		if self.rotate:
			return "Vertical"
		else:
			return "Horizontal"
	
	def turn( self ):
		self.rotate = not self.rotate
		return
	
	def cursorCoversCurrentShips( self ):
		return self.coversCurrentShips( self.cursor )
	
	def cursorCoversOpponentShips( self ):
		return self.coversOpponentShips( self.cursor )
	
	def coversCurrentShips( self, coords ):
		return self.coversShips( coords, self.current )
	
	def coversOpponentShips( self, coords ):
		return self.coversShips( coords, self.opponent )
	
	def coversShips( self, coords, player ):
		for ship in player.ships:
			for point in ship.points:
				if point[ 0 ] == coords[ 0 ] and point[ 1 ] == coords[ 1 ]:
					return True
				else:
					pass
		return not task_validCoord( coords )
	
	def advance( self ):
		self.mode = self.mode + 1
		if self.mode > 3:
			self.mode = 2
		else:
			pass
		self.resetCursor()
		if self.mode % 2 == 0:
			self.current = self.players[ 0 ]
			self.opponent = self.players[ 1 ]
			self.current_offset_x = 0
			self.opponent_offset_x = 11
		else:
			self.current = self.players[ 1 ]
			self.opponent = self.players[ 0 ]
			self.current_offset_x = 11
			self.opponent_offset_x = 0
		if self.mode == 0:
			self.ship_stack = task_getShipStack()
			return "Player 1 - place your ships!"
		elif self.mode == 1:
			self.ship_stack = task_getShipStack()
			return "Player 2 - place your ships!"
		elif self.mode == 2:
			return "Player 1 - attack your opponents ships!"
		else:
			return "Player 2 - attack your opponents ships!"
	
	def allowAdvance( self ):
		return len( self.ship_stack ) == 0
	
	def turnShipPoint( self, point ):
		if self.rotate:
			return ( point[ 1 ], point[ 0 ], point[ 2 ] )
		else:
			return point
	
	def allowPlacement( self ):
		index = len( self.ship_stack )
		if index == 0:
			return False
		else:
			ship = self.ship_stack[ index - 1 ]
			for point in ship.points:
				s_point = self.turnShipPoint( point )
				n_point = ( self.cursor[ 0 ] + s_point[ 0 ], self.cursor[ 1 ] + s_point[ 1 ], s_point[ 2 ] )
				if self.coversCurrentShips( n_point ):
					return False
				else:
					pass
			return True
	
	def place( self ):
		source_ship = self.ship_stack.pop()
		new_ship = Ship()
		for point in source_ship.points:
			s_point = self.turnShipPoint( point )
			n_point = ( self.cursor[ 0 ] + s_point[ 0 ], self.cursor[ 1 ] + s_point[ 1 ], s_point[ 2 ] )
			new_ship.points.append( n_point )
		self.current.ships.append( new_ship )
	
	def shoot( self ):
		self.current.shots.append( self.cursor )
		for ship in self.opponent.ships:
			i = 0
			for point in ship.points:
				if point[ 0 ] == self.cursor[ 0 ] and point[ 1 ] == self.cursor[ 1 ]:
					ship.points[ i ] = ( point[ 0 ], point[ 1 ], True )
					return True
				else:
					pass
				i = i + 1
		return False
	
	def opponentDefeated( self ):
		for ship in self.opponent.ships:
			for point in ship.points:
				if point[ 2 ]:
					pass
				else:
					return False
		return True
	
def task_makeLargeShip():
	ship = Ship()
	ship.points.append( ( 0, 0, False ) )
	ship.points.append( ( 1, 0, False ) )
	ship.points.append( ( 2, 0, False ) )
	return ship
	
def task_makeSquareShip():
	ship = Ship()
	ship.points.append( ( 0, 0, False ) )
	ship.points.append( ( 1, 0, False ) )
	ship.points.append( ( 1, 1, False ) )
	ship.points.append( ( 0, 1, False ) )
	return ship
	
def task_makeSmallShip():
	ship = Ship()
	ship.points.append( ( 0, 0, False ) )
	return ship

def task_getShipStack():
	return [ task_makeSmallShip(), task_makeSmallShip(), task_makeSquareShip(), task_makeLargeShip() ]

def task_mainLoop( screen ):
	environment = Environment()
	task_outputSplash( screen, environment.advance() )
	while( True ):
		task_clearPlayer( screen, environment.current_offset_x )
		task_drawPlayer( screen, environment.current, environment.current_offset_x )
		task_hidePlayer( screen, environment.opponent_offset_x )
		task_drawPlayerShots( screen, environment )
		task_drawCursor( screen, environment, environment.opponent, environment.currentCursorOffset() )
		screen.refresh()
		command = task_getCommand( screen )
		cmd = command[ 0 ]
		coords = command[ 1 ]
		if cmd == "exit":
			if coords is None:
				task_outputSplash( screen, "Exiting program" )
			else:
				task_outputSplash( screen, "'exit' does not take any arguments" )
			break
		elif cmd == "turn":
			if coords is None:
				if environment.mode > 1:
					task_outputSplash( screen, "Turning of ships is not allowed in 'battle' mode!" )
				else:
					environment.turn()
					task_outputSplash( screen, "Orientation: " + environment.getOrientationString() )
			else:
				task_outputSplash( screen, "'turn' does not take any arguments" )
		elif cmd == "done":
			if coords is None:
				if environment.mode > 1:
					task_outputSplash( screen, "Turn skipping is not allowed in 'battle' mode!" )
				elif environment.allowAdvance():
					task_outputSplash( screen, environment.advance() )
				else:
					task_outputSplash( screen, "You have " + str( len( environment.ship_stack ) ) + " more ships to place." )
			else:
				task_outputSplash( screen, "'done' does not take any arguments" )
		elif cmd == "place":
			if coords is None:
				if environment.mode > 1:
					task_outputSplash( screen, "Placement of ships is not allowed in 'battle' mode!" )
				elif environment.allowPlacement():
					environment.place()
					task_outputSplash( screen, "Placed ship at " + task_coordinateToString( environment.cursor ) )
				else:
					task_outputSplash( screen, "Unable to place ship at coordinates!" )
			else:
				task_outputSplash( screen, "'place' does not take any arguments" )
		elif cmd == "move":
			str_coords = task_coordinateToString( coords )
			if task_validCoord( coords ):
				task_outputSplash( screen, "Moving to " + str_coords )
				environment.cursor = coords
			else:
				task_outputSplash( screen, "Invalid coordinates" + str_coords )
		elif cmd == "shoot":
			if coords is None:
				if environment.mode < 2:
					task_outputSplash( screen, "Shooting of ships is not allowed in 'prepare' mode!" )
				else:
					task_outputSplash( screen, "Shooting at " + task_coordinateToString( environment.cursor ) )
					hit = environment.shoot()
					task_drawPlayerShots( screen, environment )
					if hit:
						task_outputSplash( screen, "And it is a hit!" )
						if environment.opponentDefeated():
							if environment.current is environment.players[ 0 ]:
								task_outputSplash( screen, "Player 1 wins!" )
							else:
								task_outputSplash( screen, "Player 2 wins!" )
							break
						else:
							pass
					else:
						task_outputSplash( screen, "...but missed!" )
					environment.advance()
			else:
				task_outputSplash( screen, "'shoot' does not take any arguments" )
		else:
			task_outputSplash( screen, "Unknown command: " + cmd )
		task_removeCursor( screen, environment, environment.currentCursorOffset() )
	return

def task_drawPlayer( screen, player, offset_x ):
	for ship in player.ships:
		for point in ship.points:
			if point[ 2 ]:
				symbol = "☠"
			else:
				symbol = "☸"
			screen.move( 3 + point[ 1 ], 1 + offset_x + point[ 0 ] )
			screen.addstr( symbol )
	return

def task_hidePlayer( screen, offset_x ):
	for y in range( 0, 10 ):
		screen.move( 3 + y, 1 + offset_x )
		screen.addstr( "----------" )
	return

def task_clearPlayer( screen, offset_x ):
	for y in range( 0, 10 ):
		screen.move( 3 + y, 1 + offset_x )
		screen.addstr( "          " )
	return

def task_drawPlayerShots( screen, environment ):
	for shot in environment.current.shots:
		screen.move( 3 + shot[ 1 ], 1 + shot[ 0 ] + environment.opponent_offset_x )
		if environment.coversOpponentShips( shot ):
			screen.addstr( "☠" )
		else:
			screen.addstr( "♨" )

def task_removeCursor( screen, environment, offset_x ):
	screen.move( environment.cursor[ 1 ] + 3, environment.cursor[ 0 ] + 1 + offset_x )
	screen.addstr( " " )
	return

def task_drawCursor( screen, environment, player, offset_x ):
	screen.move( environment.cursor[ 1 ] + 3, environment.cursor[ 0 ] + 1 + offset_x )
	if environment.mode >= 2:
		screen.addstr( "☢" )
	elif environment.cursorCoversCurrentShips():
		screen.addstr( "★" )
	else:
		screen.addstr( "☆" )
	return

def task_outputSplash( screen, msg ):
	yx = screen.getyx()
	screen.move( 1, 1 )
	screen.addstr( msg )
	screen.refresh()
	time.sleep( 1 )
	screen.move( 1, 1 )
	screen.clrtoeol()
	screen.refresh()
	screen.move( yx[ 0 ], yx[ 1 ] )
	return

def task_getCommand( screen ):
	curses.curs_set(1)
	screen.move( 0, 1 )
	instr = ""
	final = None
	screen.addstr( "Enter command: " )
	while( True ):
		inchr = screen.getkey()
		if inchr == '\n':
			command = instr
			coord_x = 0
			coord_y = 0
			index = instr.find( ',' )
			if index >= 0:
				command = instr[ 0 : index ]
				index_x = instr.find( ',', index + 1 )
				if index_x >= 0:
					try:
						coord_x = int( instr[ index + 1 : index_x ] )
						coord_y = int( instr[ index_x + 1 : len( instr ) ] )
						final = ( command, ( coord_x, coord_y ) )
						break
					except ValueError:
						pass
				else:
					pass
			else:
				final = ( command, None )
				break
			screen.move( 0, 16 )
			screen.clrtoeol()
			screen.addstr( "Invalid command." )
			screen.refresh()
			time.sleep( 1 )
			screen.move( 0, 16 )
			screen.clrtoeol()
			screen.refresh()
			instr = ""
		else:
			instr += inchr
			screen.addstr( inchr )
			screen.refresh()
	screen.move( 0, 1 )
	screen.clrtoeol()
	screen.refresh()
	curses.curs_set(0)
	return final

def task_drawBoard( screen ):
	for y in range( 0, 10 ):
		symbol = str( y )
		screen.move( 3 + y, 0 )
		screen.clrtoeol()
		screen.addstr( symbol )
		screen.move( 3 + y, 22 )
		screen.addstr( symbol )
		screen.move( 3 + y, 11 )
		screen.addstr( "|" )
	top_text = "0123456789"
	screen.move( 2, 1 )
	screen.addstr( top_text )
	screen.move( 2, 12 )
	screen.addstr( top_text )
	screen.move( 13, 1 )
	screen.addstr( top_text )
	screen.move( 13, 12 )
	screen.addstr( top_text )
	return

def task_validCoord( coords ):
	if coords is None:
		return False
	else:
		return coords[ 0 ] >= 0 and coords[ 0 ] < 10 and coords[ 1 ] >= 0 and coords[ 1 ] < 10

def task_coordinateToString( coords ):
	if coords is None:
		return "Missing coordinates in format x,y"
	else:
		return "(" + str( coords[ 0 ] ) + ", " + str( coords[ 1 ] ) + ")"

def task_program():
	screen = task_initScreen()
	task_mainLoop( screen )
	task_terminateScreen( screen )
	return

task_program()
