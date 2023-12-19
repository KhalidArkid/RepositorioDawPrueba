
array2={
    "indigo": 350,
    "blau": 450,
    "cian": 490,
    "verd": 550,
    "groc": 620,
    "taronja": 680,
    "vermell": 800,
}

array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

indigo = 10 
blau = 20
cian = 30
verd = 40
groc = 50
taronja = 60
vermell = 70

for i in range(len(array)):
    for j in range(len(array) - i -1):

        if array2 [array[j]] > array2[array[j+1]]:

                array[j], array[j+1] = array[j+1], array[j]

print(array)
