import os, csv

path = "D:\Coding\Python\DIscord_Bot/memories"

class Memory():

    def __init__(self):
        super().__init__()
    
    def makeFolder(name):
        folderpath = path + "/" + str(name)
        
        os.mkdir(folderpath)
    
    def makeFile(name):
        folderpath = path + "/" + str(name)
        filepath = folderpath + f"/{name}.csv"
        f = open(filepath, 'w')
        f.close()
    
    def searchFolder(name):
        upperpath = path
        names = os.listdir(upperpath)
        folderpath = path + "/" + str(name)

        if name in names:
            return folderpath
        return None
    
    def searchFile(name):
        folderpath = path + "/" + str(name)
        filename = name + ".csv"
        filepath = folderpath + "/" + filename
        names = os.listdir(folderpath)

        if filename in names:
            return filepath
        return None
    
    def writeFile(path, key, value):
        f = open(path, 'a', newline="")
        adder = csv.writer(f)
        insert = []
        insert.append(key)
        insert.append(value)
        adder.writerow(insert)
        f.close()
    
    def readFile(path):
        f = open(path, 'r')
        read = csv.reader(f)
        reader = []
        for line in read:
            reader.append(line)
        
        print(reader)

        listToDict = {}
        for line in reader:
            listToDict[str(line[0])] = str(line[1])
        f.close()
        return listToDict
    
    def deleteFile(path, key):
        f = open(path, 'r')
        reader = csv.reader(f)
        listToDict = {}
        for line in reader:
            listToDict[str(line[0])] = str(line[1])
        f.close()
        elements = listToDict
        remove = elements.pop(str(key))
        dictToList = []
        for key in list(elements.keys()):
            row = []
            row.append(str(key))
            row.append(str(elements[key]))
            dictToList.append(row)
        f = open(path, 'w', newline="")
        updater = csv.writer(f)
        for line in dictToList:
            updater.writerow(line)
        f.close()
        return remove


if __name__ == "__main__":
    Memory()