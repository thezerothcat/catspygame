class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Path:
    def __init__(self, thispoint):
        self.index = 0
        self.points = [thispoint] #Point(thispoint)
		
    def add(self, thispoint):
        self.points.append(thispoint)

    def poplast(self):
        self.points.pop()

    def next(self):
        if self.index == len(self.points):
            self.index = 0
            raise StopIteration
        self.index = self.index + 1
        return self.points[self.index - 1]

    def __iter__(self): 
        return self

    def __getitem__(self, index):
        return self.points[index]

class PathSet:
    def __init__(self, apath):
        self.paths = [apath] #Path(path)
        self.longest = len(self.paths[0].points)
        self.shortest = len(self.paths[0].points)
        self.index = 0

    def next(self):
        if self.index == len(self.paths):
            self.index = 0
            raise StopIteration
        self.index = self.index + 1
        return self.paths[self.index - 1]

    def __iter__(self): 
        return self

    def addpoints(self, movesleft, mapcells):
        lastpath = self.paths[0]
        lastpoint = lastpath.points[-1]

#for i in range(0, movesleft):
#self.checkLeft(lastpoint, lastpath, movesleft, mapcells)

#for i in 
        self.checkLeft(lastpoint, lastpath, movesleft, mapcells)
        self.checkRight(lastpoint, lastpath, movesleft, mapcells)
        self.checkUp(lastpoint, lastpath, movesleft, mapcells)
        self.checkDown(lastpoint, lastpath, movesleft, mapcells)
				
    def checkLeft(self, thispoint, lastpath, movesleft, mapcells):
        leftpoint = Point(thispoint.x - mapcells.cellsize, thispoint.y)

        if leftpoint.x >= 0:
            nextcell = mapcells.cells[(leftpoint.x, leftpoint.y)]
            if nextcell.walkable == True:
                leftpath = Path(Point(0, 0))
                leftpath.poplast()
                for apoint in lastpath:
                    leftpath.add(Point(apoint.x, apoint.y))
                leftpath.add(leftpoint)
                self.paths.append(leftpath)		

                if (movesleft - 1) > 0:
                    self.checkLeft(leftpoint, leftpath, movesleft - 1, mapcells)
                    self.checkUp(leftpoint, leftpath, movesleft - 1, mapcells)
                    self.checkDown(leftpoint, leftpath, movesleft - 1, mapcells)



    def checkRight(self, thispoint, lastpath, movesleft, mapcells):
        rightpoint = Point(thispoint.x + mapcells.cellsize, thispoint.y)

        if rightpoint.x <= 288:
            nextcell = mapcells.cells[(rightpoint.x, rightpoint.y)]
            if nextcell.walkable == True:
                rightpath = Path(Point(0, 0))
                rightpath.poplast()
                for apoint in lastpath:
                    rightpath.add(Point(apoint.x, apoint.y))
                rightpath.add(rightpoint)
                self.paths.append(rightpath)

                if (movesleft - 1) > 0:
                    self.checkRight(rightpoint, rightpath, movesleft - 1, mapcells)
                    self.checkUp(rightpoint, rightpath, movesleft - 1, mapcells)
                    self.checkDown(rightpoint, rightpath, movesleft - 1, mapcells)
			

	
    def checkUp(self, thispoint, lastpath, movesleft, mapcells):
        uppoint = Point(thispoint.x, thispoint.y - mapcells.cellsize)

        if uppoint.y >= 0:
            nextcell = mapcells.cells[(uppoint.x, uppoint.y)]
            if nextcell.walkable == True:
                uppath = Path(Point(0, 0))
                uppath.poplast()
                for apoint in lastpath:
                    uppath.add(Point(apoint.x, apoint.y))
                uppath.add(uppoint)
                self.paths.append(uppath)

                if (movesleft - 1) > 0:
                    self.checkLeft(uppoint, uppath, movesleft - 1, mapcells)
                    self.checkRight(uppoint, uppath, movesleft - 1, mapcells)
                    self.checkUp(uppoint, uppath, movesleft - 1, mapcells)

    def checkDown(self, thispoint, lastpath, movesleft, mapcells):
        downpoint = Point(thispoint.x, thispoint.y + mapcells.cellsize)

        if downpoint.y <= 288:
            nextcell = mapcells.cells[(downpoint.x, downpoint.y)]
            if nextcell.walkable == True:
                downpath = Path(Point(0, 0))
                downpath.poplast()
                for apoint in lastpath:
                    downpath.add(Point(apoint.x, apoint.y))
                downpath.add(downpoint)
                self.paths.append(downpath)

                if (movesleft - 1) > 0:
                    self.checkLeft(downpoint, downpath, movesleft - 1, mapcells)
                    self.checkRight(downpoint, downpath, movesleft - 1, mapcells)
                    self.checkDown(downpoint, downpath, movesleft - 1, mapcells)


    def __getitem__(self, index):
        return self.paths[index]
