## Class Structure
```mermaid
---
title: The game
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
