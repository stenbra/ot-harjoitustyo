class DataLoader:
    @staticmethod
    def LoadDataFromFile(file):
        f = open(file,"r")
        fData = f.read()
        f.close()
        data= DataLoader.ParseData(fData)
        return data
    
    @staticmethod
    def ParseData(data):
        dataDict ={}
        body = data.split("##")[1].replace("\n","")
        actions= body.split("_")
        for i in actions:
            actionDataDict={}
            dataParts = i.split("|")
            for j in range(1,len(dataParts)):
                parts=dataParts[j].split(":")
                if len(parts)== 2:
                    actionDataDict[parts[0]] = parts[1]
                else:
                    actionDataDict[parts[0]]= None
            dataDict[dataParts[0]]=actionDataDict
        return dataDict