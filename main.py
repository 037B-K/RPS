"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import random
from enum import Enum
import arcade
#import arcade.gui

from assets.attack_animation import AttackType
from assets.game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """



   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
       PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
       COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
       COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
       self.ATTACK_FRAME_WIDTH = 154 / 2
       self.ATTACK_FRAME_HEIGHT = 154 / 2
       arcade.set_background_color(arcade.color.BLACK_OLIVE)
        #Cree la sprite du player et lui donne ses values
       self.player = arcade.Sprite("sprites/faceBeard.png")
       self.player.center_y = PLAYER_IMAGE_Y
       self.player.center_x = PLAYER_IMAGE_X
       self.player.scale = .2
        #Cree la sprite du computer et lui donne ses values
       self.computer = arcade.Sprite("sprites/compy.png")
       self.computer.center_y = COMPUTER_IMAGE_Y
       self.computer.center_x = COMPUTER_IMAGE_X
        #Cree la liste de sprites du computer et du player et les y ajoute
       self.players = arcade.SpriteList()
       self.players.extend([self.computer, self.player])


       self.rock = arcade.Sprite("sprites/srock.png")
       self.paper = arcade.Sprite("sprites/spaper.png")
       self.scissors = arcade.Sprite("sprites/srock.png")
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = 0

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

       pass



   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """


   def draw_possible_attack(self):
       #ROCK
        arcade.draw_rectangle_outline((SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4), 165, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED)
       #PAPER
        arcade.draw_rectangle_outline(256 + self.ATTACK_FRAME_WIDTH + 5, 165, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED)
       #SCISSORS
        arcade.draw_rectangle_outline(256 - (self.ATTACK_FRAME_WIDTH + 5), 165, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.RED)

       #COMPUTER ATTACK
        arcade.draw_rectangle_outline(self.computer.center_x, 165, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT,arcade.color.RED)

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """



   def draw_scores(self):
       #Player score
        arcade.draw_text("Le pointage du joueur est ", self.player.center_x - self.ATTACK_FRAME_WIDTH-50, 165 - self.ATTACK_FRAME_HEIGHT, arcade.color.CYAN, 12, self.ATTACK_FRAME_WIDTH * 3, align="center")
        #Computer score
        arcade.draw_text("Le pointage de l'ordinateur est", self.computer.center_x - self.ATTACK_FRAME_WIDTH-50, 165 - self.ATTACK_FRAME_HEIGHT, arcade.color.CYAN, 12, self.ATTACK_FRAME_WIDTH * 3, align="center")
   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.draw_instructions()
       self.players.draw()
       self.draw_possible_attack()
       self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)
       pass

   def on_key_press(self, key, key_modifiers):
       if arcade.key.SPACE:
            if self.game_state == 0:
                print("game started")
                self.game_state == 1


            if self.game_state == 2:
                self.game_state == 1
            if self.game_state == 3:
                self.player_score == 0
                self.computer_score == 0
                self.game_state == 1


   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       #self.computer_attack_type = -1
       #self.player_attack_chosen = False
       #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       #self.player_won_round = False
       #self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       if self.rock.collides_with_point((x,y)):
           self.player_attack_type == AttackType.ROCK
           self.player_attack_chosen = True
           print("rock")
       if self.paper.collides_with_point((x,y)):
           self.player_attack_type == AttackType.PAPER
           self.player_attack_chosen = True
           print("papers")
       if self.scissors.collides_with_point((x,y)):
           self.player_attack_type == AttackType.SCISSORS
           self.player_attack_chosen = True
           print("scis")
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """
       pass


def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()
