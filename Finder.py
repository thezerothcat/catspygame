import Map
import CellObject
import pygame

import Paths
from Paths import *
			

def attacks(actor, mapcells, position):
    targets = {}
    for arange in actor.weapon.range: 
        thisrange = arange * mapcells.cellsize
        last = Point(actor.rect.x, actor.rect.y)
        for apath in actor.validpaths:
            last = apath[-1]
            if (last.x - thisrange >= 0):
                t = mapcells.cells[(last.x - thisrange, last.y)].contents
                if t != None and t.alive == True and t.friends != actor.friends:
                    newpath = Path(Point(0,0))
                    newpath.poplast()
                    for apoint in apath:
                        newpath.add(Point(apoint.x, apoint.y))
                    if t in targets.keys():
                        if len(targets[t].points) > len(newpath.points):
                            targets[t] = newpath
                    else:
                            targets[t] = newpath
            if (last.y - thisrange >= 0):
                t = mapcells.cells[(last.x, last.y - thisrange)].contents
                if t != None and t.alive == True and t.friends != actor.friends:
                    newpath = Path(Point(0,0))
                    newpath.poplast()
                    for apoint in apath:
                        newpath.add(Point(apoint.x, apoint.y))
                    if t in targets.keys():
                        if len(targets[t].points) > len(newpath.points):
                            targets[t] = newpath
                    else:
                            targets[t] = newpath
            if(last.x + thisrange <= 288):
                t = mapcells.cells[(last.x + thisrange, last.y)].contents
                if t != None and t.alive == True and t.friends != actor.friends:
                    newpath = Path(Point(0,0))
                    newpath.poplast()
                    for apoint in apath:
                        newpath.add(Point(apoint.x, apoint.y))
                    if t in targets.keys():
                        if len(targets[t].points) > len(newpath.points):
                            targets[t] = newpath
                    else:
                            targets[t] = newpath
            if (last.y + thisrange <= 288):
                t = mapcells.cells[(last.x, last.y + thisrange)].contents
                if t != None and t.alive == True and t.friends != actor.friends:
                    newpath = Path(Point(0,0))
                    newpath.poplast()
                    for apoint in apath:
                        newpath.add(Point(apoint.x, apoint.y))
                    if t in targets.keys():
                        if len(targets[t].points) > len(newpath.points):
                            targets[t] = newpath
                    else:
                            targets[t] = newpath
    
	#use sets to remove duplicates
    return targets
	

def findcell((x, y)):
    dest = Point(-1,-1)
    if x < 320:
        if x >= 0:
            dest.x = 0
            if x >= 32:
                dest.x = 32
                if x >= 64:
                    dest.x = 64
                    if x >= 96:
                        dest.x = 96
                        if x >= 128:
                            dest.x = 128
                            if x >= 160:
                                dest.x = 160
                                if x >= 192:
                                    dest.x = 192
                                    if x >= 224:
                                        dest.x = 224
                                        if x >= 256:
                                            dest.x = 256
                                            if x >= 288:
                                                dest.x = 288
    if y < 320:
        if y >= 0:
            dest.y = 0
            if y >= 32:
                dest.y = 32
                if y >= 64:
                    dest.y = 64
                    if y >= 96:
                        dest.y = 96
                        if y >= 128:
                            dest.y = 128
                            if y >= 160:
                                dest.y = 160
                                if y >= 192:
                                    dest.y = 192
                                    if y >= 224:
                                        dest.y = 224
                                        if y >= 256:
                                            dest.y = 256
                                            if y >= 288:
                                                dest.y = 288

    return dest



