```mermaid
---
title: Monopoli
---
 classDiagram
      Pelaaja "2-8" --  Pelilauta
      Noppa "2" --  Pelilauta
      Pelinappula  -- "2-8" Pelaaja
      Ruutu "40" -- "1" Pelilauta
      Ruutu  --  Pelinappula


      Pelilauta <-- Vankila
      Pelilauta <-- AloitusRuutu
      Ruutu <-- Vankila
      Ruutu <-- AloitusRuutu
      Ruutu <-- Sattumajayhteismaa
      Ruutu <-- Asematjalaitokset
      Ruutu <-- Katuruutu

      Sattumajayhteismaa <-- Kortti

      class Noppa{
          arvo
          heitä()
      }
      class Pelaaja{
      }
      class Pelinappula{
          pelaaja
          sijainti
      }
      class Pelilauta{
          vankila_id
          aloitusruutu_id
      }
      class Ruutu{
          ruutu_id
          getPos()
          seuraava_ruutu
          Toiminto()
      }
      class Vankila{
      }
      class AloitusRuutu{
      }
      class Sattumajayhteismaa{

      }
      class Asematjalaitokset {
      }
      class Katuruutu{
        nimi
      }
      class Kortti{
        Toiminto()
      }
```
