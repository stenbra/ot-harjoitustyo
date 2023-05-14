## Structure

![](./images/structure.png)

## Class Structure
```mermaid
---
title: The game, Slightly outdated but mostly the same
---
 classDiagram
      DataLoader --> ActionLoader
      ActionLoader --> CardPool
      CardStats --> CardPool
      CardComparer --> Health
      CardComparer -- Player
      CardComparer -- TurnHandler
      TurnHandler --> Game

      Scene -- MainMenu
      Scene -- Game
      Game <-- Player
      Game <--TurnHandler
      TurnHandler -- DrawPile
      TurnHandler -- Hand
      DrawPile --> Hand
      Game --> Scenemanager
      MainMenu --> Scenemanager
      Card --> Hand
      CardPool --> Card
      CardPool --> Player
      Scenemanager --> main


      class DataLoader{
        load_data_from_file()
        parse_data()
      }

      class ActionLoader{
        uses data_loader to load data then formats it
        load_action_interactions()
        load_action_base_stats()
        load_action_visuals()
        parse_interaction()
      }
      class CardPool{
        create_cards()
        card_stats
        card_visuals
      }

      class CardStats{
        damage
        speed
        action
      }
      class CardComparer{
        compare_cards()
        get_faster_card()
      }
      class Health{
        take_damage()
        die()
      }
      class Player{
        deck
        advantage
        get_advantage()
        set_advantage()
      }
      class TurnHandler{
        ----
      }
      class Scene{
        update()
      }
      class Scenemanager{
        updates and manages scenes
        active_scene
        update()
        add_scene()
        set_active_scene()
      }
      class MainMenu{
        update()
        end()
        start()
      }
      class Game{
        update()
        ---
      }
      class main{
        core Loop
        updates scenemanager and initializes loaders and handlers
      }
      class DrawPile{
        draw()
        shuffle_new_deck()
      }
      class Hand {
        play_selected()
      }
      class Card{
        select_card()
      }
```

## Main funtions

### Turn Handling

#### Start of turn and card selection phase
```mermaid
sequenceDiagram
  participant Turnhandler
  participant Card
  participant Hand
  participant Deck
  Turnhandler->>Hand: hands.new_hand() 
  Hand->>Deck: draw()
  Deck-->>Hand: returns list of cards
  Hand->>Card: initialize Card() for the hand
  Card->>Hand: "click card" hand.set_selected()
  Hand->>Hand: self.update_marker_positions()
  Game->>Hand: clicked "LOCK IN" 
  Hand->>Hand: play_selected()
  Hand->> Turnhandler: turn_handler.lock_in_cards()
  Turnhandler->>Turnhandler: if both players have locked their cards go to battle_phase

```

#### combat phase
```mermaid
sequenceDiagram
  participant Turnhandler
  participant CardComparer
  participant AnimationHandler
  participant Deck
  Turnhandler->>Turnhandler: get_combat_data() 
  Turnhandler->>Turnhandler: self.state=2 
  Turnhandler->>CardComparer: self.card_comparer(cards and players) 
  note right
    this will happen twice since 2 cards are played per player each round
  end note
  Turnhandler->>CardComparer: self.get_faster_card()
  CardComparer->>Turnhandler: card_combat_data
  Turnhandler->>Turnhandler: if state is 2 and no animations are running
  Turnhandler->>Turnhandler: self.check_for_rounds()
  note right
    this will happen twice since 2 cards are played per player each round
  end note
  Turnhandler->>AnimationHandler: self.animation_handler.add_to_animation_queue(animation)
  Turnhandler->>Turnhandler: if len(self.combat_data)
  Turnhandler-->>Turnhandler: True
  Turnhandler-->>Turnhandler: self.state=3
  Turnhandler->>Turnhandler: if state is 3 and no animations are running
  Turnhandler->>Turnhandler: self.end_turn()

```