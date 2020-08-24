import sys
import math

SECT_SZ = 5

# Find all intersections of line and grid, as well as starting point and ending point
# Allocate sectors for present systems
# Look in area around the intersection
# Add all sectors (if not present) in that range

class System:
	name = ''
	coords = [0.0, 0.0, 0.0]

	def __init__(self, name, x, y, z):
		self.name = name
		self.coords[0] = x
		self.coords[1] = y
		self.coords[2] = z
	
	def getCoords(self):
		return self.coords
	
	def getName(self):
		return self.name

class Line:
	equations = [None, None, None]

	def __init__(self, coords1, coords2):
		self.equations[0] = Equation(coords1[0] - coords2[0], coords1[0])
		self.equations[1] = Equation(coords1[1] - coords2[1], coords1[1])
		self.equations[2] = Equation(coords1[2] - coords2[2], coords1[2])
	
	def getX(self):
		return self.equations[0]
	
	def getY(self):
		return self.equations[1]
	
	def getZ(self):
		return self.equations[2]

class Equation:
	slope = 0.0
	offset = 0.0
	
	def __init__(self, slope, offset):
		self.slope = slope
		self.offset = offset
	
	def getSlope(self):
		return self.slope
	
	def getOffset(self):
		return self.offset
		
def findPlaneIntersections(path, coord1, coord2):
	points = []
	equations = [path.getX(), path.getY(), path.getZ()]

	for i in range(3):
		#Initialize the coordinates so we're always increasing
		left = coord1[i]
		right = coord2[i]
		if left > right:
			left = coord2[i]
			right = coord1[i]

		intersection = left
		if(left % SECT_SZ != 0.0):
			intersection = ((left // int(SECT_SZ)) + 1) * SECT_SZ
			
		while intersection <= right:
			#Calculate the t value
			t = (intersection - equations[i].getOffset()) / equations[i].getSlope()

			new_point = []
			for j in range(3):
				if j == i:
					new_point.append(intersection)
				else:
					new_point.append(equations[j].getSlope() * t + equations[j].getOffset())
					
			points.append(new_point)
			intersection += 5.0
	
	return points

def checkSectorValidity(sector_dict, hash_point, sys_lst):
	return hash_point[0] in sector_dict.keys() and hash_point[1] in sector_dict[hash_point[0]].keys() and hash_point[2] in sector_dict[hash_point[0]][hash_point[1]] and sector_dict[hash_point[0]][hash_point[1]][hash_point[2]][0] not in sys_lst

def getHash(point, offset):
	return (point + offset) // SECT_SZ

def getSystemsInRange(sector_dict, points):
	sys_lst = []
	half_sect = SECT_SZ / 2.0

	for point in points:
		#Getting the polar offset quadrants and base (above, below, left, right, fore, back, and center)
		search_offsets = [half_sect * -1, 0, half_sect]
		for x_off in search_offsets:
			x_hash = getHash(point[0], x_off)
			for y_off in search_offsets:
				y_hash = getHash(point[1], y_off)
				for z_off in search_offsets:
					z_hash = getHash(point[2], z_off)

					#If the hashed sector exists and the systems haven't been added and it's polar
					if checkSectorValidity(sector_dict, (x_hash, y_hash, z_hash), sys_lst) and ((x_off == 0 and y_off == 0) or (y_off == 0 and z_off == 0) or (z_off == 0 and x_off == 0)):
						for system in sector_dict[x_hash][y_hash][z_hash]:
							sys_lst.append(system)
		
		#Getting the remaining points (the eight remaining spots at the diagonal extremes of the sphere)
		diag_pos = half_sect / math.sqrt(2)
		search_offsets = [diag_pos * -1, diag_pos]
		for x_off in search_offsets:
			x_hash = getHash(point[0], x_off)
			for y_off in search_offsets:
				y_hash = getHash(point[1], y_off)
				for z_off in search_offsets:
					z_hash = getHash(point[2], z_off)

					#If the hashed sector exists and the systems haven't been added
					if checkSectorValidity(sector_dict, (x_hash, y_hash, z_hash), sys_lst):
						for system in sector_dict[x_hash][y_hash][z_hash]:
							sys_lst.append(system)
	
	return sys_lst

def cullSystems():
	source = ""
	dest = ""
	source_coords = [0.0, 0.0, 0.0]
	dest_coords = [0.0, 0.0, 0.0]
	sector_dict = {}
	max_fuel = 0.0

	first_line = 1
	for line in sys.stdin:
		input_val = line.strip('\n').split(' ')
		if first_line:
			#Setting the source and destination, as well as the fuel amount (to output in the results)
			source = input_val[0]
			dest = input_val[1]
			first_line = 0
		else:
			#Parsing the line of input
			name = input_val[0]
			x_coord = float(input_val[1])
			y_coord = float(input_val[2])
			z_coord = float(input_val[3])
			
			new_sys = System(name, x_coord, y_coord, z_coord)
			
			#Check if the system is the destination or source
			if name == source:
				source_coords = [x_coord, y_coord, z_coord]
			if name == dest:
				dest_coords = [x_coord, y_coord, z_coord]

			#The case a switch statement is MADE for, and I'm using Python ;-;
			x_hash = x_coord // SECT_SZ
			y_hash = y_coord // SECT_SZ
			z_hash = z_coord // SECT_SZ
			if x_hash not in sector_dict.keys():
				sector_dict[x_hash] = {}
				sector_dict[x_hash][y_hash] = {}
				sector_dict[x_hash][y_hash][z_hash] = [new_sys]
			elif y_hash not in sector_dict[x_hash].keys():
				sector_dict[x_hash][y_hash] = {}
				sector_dict[x_hash][y_hash][z_hash] = [new_sys]
			elif z_hash not in sector_dict[x_hash][y_hash].keys():
				sector_dict[x_hash][y_hash][z_hash] = [new_sys]
			else:
				sector_dict[x_hash][y_hash][z_hash].append(new_sys)

	direct_path = None
	if source != dest:
		direct_path = Line((source_coords[0], source_coords[1], source_coords[2]), (dest_coords[0], dest_coords[1], dest_coords[2]))
	else:
		#Base case
		return getSystemsInRange(sector_dict, [source_coords])
	
	points = findPlaneIntersections(direct_path, source_coords, dest_coords)
	points.append(source_coords)
	points.append(dest_coords)

	new_system_lst = getSystemsInRange(sector_dict, points)
	new_system_lst.sort(key=lambda system: system.getName())

	return new_system_lst

new_system_lst = cullSystems()
for system in new_system_lst:
	print(system.getName())
