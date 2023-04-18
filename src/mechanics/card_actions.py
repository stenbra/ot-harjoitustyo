from mechanics.data_loader import DataLoader
class ActionLoader:
    def __init__(self):
        self.action_stats_file="src/gamedata/action_base_stats.txt"
        self.action_interactions_file="src/gamedata/action_interactions.txt"
        self.action_visuals_file="src/gamedata/action_visual_data.txt"

    def LoadActionInteractions(self):
        data = DataLoader.LoadDataFromFile(self.action_interactions_file)
        for i in data:
            for j in data[i]:
                data[i][j]=self.ParseInteraction(data[i][j])
        return data
    
    def LoadActionBaseStats(self):
        data = DataLoader.LoadDataFromFile(self.action_stats_file)
        return data

    def LoadActionVisuals(self):
        data = DataLoader.LoadDataFromFile(self.action_visuals_file)
        return data
    
    def ParseInteraction(self,interactionString):
        if interactionString == None:
            return None
        interactionInfo = [0]*4 # [p1 advantage,p1 damage,p2 advantage ,p2 damage]
        s = interactionString.split("-")
        for i in s:
            d =i.split("<")
            if "P1" in d[0]:
                c=0
            elif "P2" in d[0]:
                c=2
            else:
                return None
            if len(d)==1:
                 return None
            j = d[1].split(">")
            if "AD" in j[0]:
                    interactionInfo[c]=int(j[1])
            if "DMG" in j[0]:
                    interactionInfo[c+1]=int(j[1])
        return interactionInfo



    
        