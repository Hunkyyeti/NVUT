#3d test
import hw

def render(vertexTable, lineTable,color):
    focalLength = 100
    
    pointTable = {}
    vertexTableKeys = vertexTable.keys()
    
    for vertex in vertexTable:
        xProjected = (focalLength * vertexTable[vertex][0])/(focalLength + vertexTable[vertex][2])
        yProjected = (focalLength * vertexTable[vertex][1])/(focalLength + vertexTable[vertex][2])
        pointTable.update({vertex: [int(xProjected), int(yProjected)]})
    
    for line in lineTable:
        x1 = pointTable[line[0]][0]
        x2 = pointTable[line[1]][0]
        y1 = pointTable[line[0]][1]
        y2 = pointTable[line[1]][1]
        hw.line(x1,y1,x2,y2,color)
