from mechanics.data_loader import DataLoader


class ActionLoader:
    """class, which loads and parses the data for card stats/visuals/interactions
      since they are wierdly structured txt files

    Attributes:
        action_stats_file: path to the action_base_stat file
        action_interactions_file: path to the action_interactions file
        action_visuals_file: path to the action_visuals_data file
    """
    def __init__(self):
        self.action_stats_file = "src/gamedata/action_base_stats.txt"
        self.action_interactions_file = "src/gamedata/action_interactions.txt"
        self.action_visuals_file = "src/gamedata/action_visual_data.txt"

    def load_action_interactions(self):
        """loads the data and parses it into a dictionary from the interactions file 
        Returns: the data dictionary
        """
        data = DataLoader.load_data_from_file(self.action_interactions_file)
        for i in data:
            for j in data[i]:
                data[i][j] = self.parse_interaction(data[i][j])
        return data

    def load_action_base_stats(self):
        """loads the data and  from the base_stats file 
        Returns: the data from the file
        """
        data = DataLoader.load_data_from_file(self.action_stats_file)
        return data

    def load_action_visuals(self):
        """loads the data and  from the action_visuals file
        Returns: the data from the file
        """
        data = DataLoader.load_data_from_file(self.action_visuals_file)
        return data

    def parse_interaction(self, interaction_string):
        """Parses the data from a string into a dictionary with a special structure
        Args:
            interaction_string: the raw text data from the interaction file that will be parsed

        Returns: None if there is no string or if the string is wrongly formatted,
          else it returns the dictionary of the data in the string
        """
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
