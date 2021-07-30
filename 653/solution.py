import json
import numpy


#start with a function that finds the furthest top-left point

def areOverlapping(rect1, rect2):
     corner_x = rect1["top_left"]
     corner_y = rect2["top_left"]
     if corner_x[0] < corner_y[0] and corner_x[1] > corner_y[1]:
          return checkDims(rect1,rect2)    
     elif corner_x[0] > corner_y[0] and corner_x[1] < corner_y[1]:
          return checkDims(rect2,rect1)
     else:  
          return False
def checkDims(ul,br):
     ul["bottom_right"] = (ul["top_left"][0]-ul["dimensions"][0],ul["top_left"][1]-ul["dimensions"][1])
     br["bottom_right"] = (br["top_left"][0]-br["dimensions"][0],br["top_left"][1]-br["dimensions"][1])
     if ul['bottom_right'][0] > br["bottom_right"][0] and ul["bottom_right"][1] < br["bottom_right"][1]:
          return True
     else:
          return False
            
rects = [{
  "top_left": (1, 4),
  "dimensions": (3, 3) # width, height
},
{
  "top_left": (-1, 3),
  "dimensions": (2, 1)
},
{
  "top_left": (0, 5),
  "dimensions": (4, 3)
}]
print(areOverlapping(rects[0],rects[2]))
print(areOverlapping(rects[1],rects[2]))