from mechanics.data_loader import DataLoader


class ActionLoader:
    def __init__(self):
        self.action_stats_file = "src/gamedata/action_base_stats.txt"
        self.action_interactions_file = "src/gamedata/action_interactions.txt"
        self.action_visuals_file = "src/gamedata/action_visual_data.txt"

    def load_action_interactions(self):
        data = DataLoader.load_data_from_file(self.action_interactions_file)
        for i in data:
            for j in data[i]:
                data[i][j] = self.parse_interaction(data[i][j])
        return data

    def load_action_base_stats(self):
        data = DataLoader.load_data_from_file(self.action_stats_file)
        return data

    def load_action_visuals(self):
        data = DataLoader.load_data_from_file(self.action_visuals_file)
        return data

    def parse_interaction(self, interaction_string):
        if interaction_string is None:
            return None
        # [p1 advantage,p1 damage,p2 advantage ,p2 damage]
        interaction_info = [0]*4
        statchanges = interaction_string.split("-")
        for i in statchanges:
            player_statchange = i.split("<")
            if "P1" in player_statchange[0]:
                list_index = 0
            elif "P2" in player_statchange[0]:
                list_index = 2
            else:
                return None
            if len(player_statchange) == 1:
                return None
            j = player_statchange[1].split(">")
            if "AD" in j[0]:
                interaction_info[list_index] = int(j[1])
            if "DMG" in j[0]:
                interaction_info[list_index+1] = int(j[1])
        return interaction_info
