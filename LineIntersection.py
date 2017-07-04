class Point:

	def __init__(self,x=0.0,y=0.0):
		self.x = float(x)
		self.y = float(y)

class Line:

	def __init__(self,p1,p2):
		self.p1 = Point(x1,y1)
		self.p2 = Point(x2,y2)

	def yChange(self):
		print 'ychange', self.p2.y , self.p1.y
		d_y = self.p2.y - self.p1.y
		return d_y

	def xChange(self):
		print 'xchange', self.p1.x , self.p2.x
		d_x = self.p1.x - self.p2.x
		return d_x

	def zChange(self):
		d_z = (self.p1.x * self.p2.y) - (self.p2.x * self.p1.y)
		return d_z

class LineCross:

	def __init__(self,l1,l2):
		self.l1 = Line(px1,py1)
		self.l2 = Line(px2,py2)

	def lineConstants(self):
		if (self.l1.xChange() == self.l2.xChange()) & (self.l1.yChange() == self.l2.yChange()) & (self.l1.zChange() == self.l2.zChange()):
			return True
		else:
			return False
	
	def intersection(self):
		intersect = False
		#print self.l1.yChange() , self.l2.xChange() , (self.l2.yChange() , self.l1.xChange())
		dm = ((self.l1.yChange() * self.l2.xChange()) - (self.l2.yChange() * self.l1.xChange()))
		f = self.lineConstants()
		if dm != 0:
			print 'dm not eq 0'
			px = ((self.l1.zChange() * self.l2.xChange()) - (self.l2.zChange() * self.l1.xChange())) / dm
			py = ((self.l2.zChange() * self.l1.yChange()) - (self.l1.zChange() * self.l2.yChange())) / dm	
			if self.limitCheck(px,py):
				intersect = True

		elif dm == 0 & f:
			print 'parallel and in range'
			if self.limitCheck():
				intersect = True

		else:
			print 'parallel and not in range'
			intersect = False

		return intersect

	def limitCheck(self,cx = 'dummy' , cy = 'dummy'):
		val = False
		if cx == 'dummy' and cy == 'dummy':
			lx1 = [self.l1.p1.x,self.l1.p2.x]
			lx2 = [self.l2.p1.x,self.l2.p2.x]
			ly1 = [self.l1.p1.y,self.l1.p2.y]
			ly2 = [self.l2.p1.y,self.l2.p2.y]
			x_in = (self.l2.p1.x or self.l2.p2.x in range(min(lx1),max(lx1))) or (self.l1.p1.x or self.l1.p2.x in range(min(lx2),max(lx2)))
			y_in = (self.l2.p1.y or self.l2.p2.y in range(min(ly1),max(ly1))) or (self.l1.p1.y or self.l1.p2.y in range(min(ly2),max(ly2)))

			if x_in or y_in:
				val = True
		else:
			cxmin = max(min(self.l1.p1.x,self.l1.p2.x),min(self.l2.p1.x,self.l2.p2.x))
			cxmax = min(max(self.l1.p1.x,self.l1.p2.x),max(self.l2.p1.x,self.l2.p2.x))
			cymin = max(min(self.l1.p1.y,self.l1.p2.y),min(self.l2.p1.y,self.l2.p2.y))
			cymax = min(max(self.l1.p1.y,self.l1.p2.y),max(self.l2.p1.y,self.l2.p2.y))

			if (cx >= cxmin & cx <= cxmax) & (cy >= cymin & cy <= cymax):
				val = True
				
		return val

try:

	r1 = raw_input('Please enter the coordinates of first rectangle separated by spaces x1 y1 x2 y2..\n')
	rect1 = map(float, r1.split())

	r2 = raw_input('Please enter the coordinates of second rectangle separated by spaces x1 y1 x2 y2..\n')
	rect2 = map(float, r2.split())

	p_list1 = []
	p_list2 = []

	for i in range(0,8,2):
		p_list1.append(Point(rect1[i],rect1[i+1]))
		p_list2.append(Point(rect2[i],rect2[i+1]))
		
		if i == 6:
			p_list1.append(Point(rect1[0],rect1[1]))
			p_list2.append(Point(rect2[0],rect2[1]))
	
	l_list1 = []
	l_list2 = []

	for p in range(0,4):
		x1 = p_list1[p].x
		y1 = p_list1[p].y
		x2 = p_list1[p+1].x
		y2 = p_list1[p+1].y
		p1 = p_list1[p]
		p2 = p_list1[p+1]
		l1 = Line(p1,p2)
		l_list1.append(l1)
		
		x1 = p_list2[p].x
		y1 = p_list2[p].y
		x2 = p_list2[p+1].x
		y2 = p_list2[p+1].y
		p1 = p_list2[p]
		p2 = p_list2[p+1]
		l2 = Line(p1,p2)
		l_list2.append(l2)
		

	for l1 in l_list1:
		for l2 in l_list2:
			print l1.p1.x , l1.p1.y , l1.p2.x , l1.p2.y
			print l2.p1.x , l2.p1.y , l2.p2.x , l2.p2.y
			px1 , py1 = l1.p1 , l1.p2
			px2 , py2 = l2.p1 , l2.p2 
			lc = LineCross(l1,l2)
			if lc.intersection():
				print 'The two rectangles overlap'
			else:
				continue
except ValueError:
	print 'Please enter numeric value only'

