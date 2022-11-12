import threeD

vertexTable = {
    "a": [10,60,60],
    "b": [60,60,60],
    "c": [10,10,60],
    "d": [60,10,60],
    "e": [10,60,10],
    "f": [60,60,10],
    "g": [10,10,10],
    "h": [60,10,10]
    }

lineTable = [
    ["a","b"],
    ["a","c"],
    ["a","e"],
    ["b","f"],
    ["b","d"],
    ["c","g"],
    ["c","d"],
    ["d","h"],
    ["e","f"],
    ["e","g"],
    ["f","h"],
    ["g","h"]
    ]
hw.oled.fill(0)
threeD.render(vertexTable,lineTable,1)
hw.oled.show()
hw.pressAToCont()
