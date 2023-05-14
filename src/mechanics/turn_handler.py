from mechanics.hand import Hand
from mechanics.health import Health
from mechanics.player import Player
from mechanics.call_back import call_back
import time
from ui.animations.combat_comparison import backround_box_move,backround_box_move_random_color,combat_time,game_over
from ui.animations.combat_animations import combat_animation_matcher,enemy_die
from mechanics.audio_resources import audio_resource

class TurnHandler:
    """a class that handles almost all logic that happens during the turns
    
    Attributes:
        players: the players that are batteling
        humans: list of non bot/computer players
        cardpool: object that contains all card data
        hands: the players hands
        card_positons: the position of the cards
        played_cards: the cards that players have locked in
        card_comparer: the object that handles the card comparing
        state: the current state of the turn
        game_mode: the game mode currently only PVE exists
        animation_handler: the object that handles all animatons
        combat_data: the combat data of the card interactions for a turn
        turn: info for what turn it is
        score: current score
        on_game_over: function that is called when the human player dies
    """
    def __init__(self, players, cardpool, card_positions, card_comparer, animation_handler,game_over, game_mode="PVE"):
        self.players = []
        self.humans = players
        self.cardpool = cardpool
        self.hands = {}
        self.card_positions = card_positions
        self.played_cards = []
        self.card_comparer = card_comparer
        self.state = 3
        self.setup_players()
        self.game_mode = game_mode
        self.animation_handler = animation_handler
        self.combat_data = None
        self.turn =0
        self.score = 0
        self.on_game_over = game_over

    def reset_turnhandler(self):
        """Resets/clears the turnhandler
        """
        self.hands = {}
        self.played_cards = []
        self.state = 3
        self.setup_players()
        self.combat_data = None
        self.turn =0
        self.score = 0

    def lock_in_cards(self, player, cards):
        """Function that is called from the player hands when they commit their cards, it checks that 
            a sufficient amount of players have commited their cards before generating combat data, note that
            it gets the card for the computer here
        
        Args:
            player: the player who locked in their cards
            cards: the cards that were commited
        """
        player_cards = {}
        player_cards[player] = cards
        self.played_cards.append(player_cards)
        if self.game_mode == "PVE":
            self.set_computer_cards()
        if len(self.played_cards) >= 2:
            self.get_combat_data()

    def set_computer_cards(self):
        """ gets cards random cards for the computer"""
        computer_cards = {}
        computer_cards[self.players[1]
                       ] = self.cardpool.get_actions_for_computer_opponent()
        self.played_cards.append(computer_cards)

    def start_turn(self):
        """ Makes the players draw new hands and switches state, queues animations
            increments turns
        """
        self.state = 0
        for i in self.hands:
            self.hands[i].new_hand()
        self.combat_data = None
        self.turn = self.turn+1
        animation = backround_box_move(0,2,text="ROUND "+str(self.turn))
        audio_resource.play_anouncer_sound("ROUND")
        self.animation_handler.add_to_animation_queue(animation)

    def end_turn(self):
        """empties played_cards swiches state and stars next turn"""
        self.state = 3
        self.played_cards = []
        self.start_turn()

    def get_combat_data(self):
        """ Gets the combat data of the cards that have been played if
            a player has not played the max amount of cards then idle card 
            actions will be assigned in their place

            combat_data is set
        """
        self.state = 2
        players_cards = {}
        players = []
        for player_card_dict in self.played_cards:
            for player in player_card_dict:
                counter = 0
                cards_with_stats = []
                players.append(player)
                for card in player_card_dict[player]:
                    stats = self.cardpool.card_stats[card]
                    cards_with_stats.append(stats)
                    counter += 1
                # the 2 is a magic number which is the cardslot max, ill get back to this at some point hopefully
                for i in range(2-counter):
                    stats = self.cardpool.card_stats["NONE"]
                    cards_with_stats.append(stats)
                players_cards[player] = cards_with_stats
        rounds =[]
        for i in range(2):
            rounds.append(self.card_comparer.compare_cards(
                players_cards[players[0]][i], players_cards[players[1]][i], players[0], players[1]))
            players[0].set_comparison_advantage(rounds[i][players[0]][1])
            players[1].set_comparison_advantage(rounds[i][players[1]][1])
        self.combat_data= rounds

    def get_after_round_callbacks(self,round_data):
        """Gets the callback functions that play will play after the animations
        
        Args:
            round_data: the combat data of the round
        """
        function_list= []
        for player in round_data:
            if player == "FASTER":
                continue
            function_list.append(player.health.health_call_back(round_data[player][2]))
            function_list.append(player.set_advantage_callback(round_data[player][1]))
        return function_list
    
    def setup_players(self):
        """Sets up the player health,hands and the computer opponent
        """
        self.players = self.humans
        if len(self.players) == 1:
            self.players.append(self.get_computer_opponent())
        for i in self.players:
            i.health = Health(i,self.player_death)
            player_hand = Hand(i, self.cardpool, self.card_positions, self)
            self.hands[i.id] = player_hand

    def player_death(self,player):
        """called on player death
            if the dead player was a computer, then a new opponent is made
            else the game will end shortly
        Args:
            player:the player that died
        """
        if player.is_bot:
            self.score += 1
            self.new_challenger()
            return
        animation= game_over(0,2,text="GAME OVER")
        self.animation_handler.force_animation(animation)   
        self.state=4

    def new_challenger(self):
        """A new computer opponent is loaded and the death animation for the old one is played
        """
        for i in self.players:
            if i.is_bot:
                del self.hands[i.id]
                self.players.remove(i)
        challenger = self.get_computer_opponent()
        challenger.health = Health(i,self.player_death)
        self.players.append(challenger)
        self.hands[challenger.id] = Hand(challenger, self.cardpool, self.card_positions, self)
        self.state = 3
        animation= enemy_die(0,2)
        self.animation_handler.force_animation(animation)  
        audio_resource.play_anouncer_sound("DEATH")
        animation_1= backround_box_move_random_color(0,2,text="NEW CHALLENGER")
        self.animation_handler.add_to_animation_queue(animation_1)     

    def get_computer_opponent(self):
        """ returns a player object that has the attribute is_bot set to true
        Returns: Player object
        """
        return Player("CO-Mput_ER",is_bot=True)
    def game_over(self):
        """plays death voiceline and calls the on_game_over function
        """
        audio_resource.play_anouncer_sound("DEATH")
        self.on_game_over()

    def check_for_rounds(self):
        """Queues animations if there still is combat data
        """
        if len(self.combat_data)==0:
            return
        round = self.combat_data.pop(0)
        after_animation_functions = self.get_after_round_callbacks(round)
        animation = combat_time(round,self.cardpool,duration=6)
        self.animation_handler.add_to_animation_queue(animation)
        battle_animation = combat_animation_matcher(round,duration=2,on_animation_end=after_animation_functions)
        self.animation_handler.add_to_animation_queue(battle_animation)
    
    def update(self):
        """Handles states transitions based on animations and other variables
        """
        self.animation_handler.update()
        if self.state== 0 and self.animation_handler.is_not_running_and_empty_queue():
            self.state =1
        if self.state == 1 and self.combat_data is not None:
            self.state =2
        if self.state ==2:
            if self.animation_handler.is_not_running_and_empty_queue():
                self.check_for_rounds()
                if len(self.combat_data)==0:
                    self.state =3
        if self.state==3 and self.animation_handler.is_not_running_and_empty_queue():
            self.end_turn()
        if self.state==4 and self.animation_handler.is_not_running_and_empty_queue():
            self.game_over()
