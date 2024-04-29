"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import random
import arcade
# import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

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
    PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
    PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
    COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    ATTACK_FRAME_WIDTH = 154 / 2
    ATTACK_FRAME_HEIGHT = 154 / 2

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.rock_still = arcade.Sprite("assets/srock.png", .5, 0, 0, 0, 0,
                                        (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4) + 7, 170)
        self.paper_still = arcade.Sprite("assets/spaper.png", .5, 0, 0, 0, 0,
                                         256 + self.ATTACK_FRAME_WIDTH + 5, 165)
        self.scissors_still = arcade.Sprite("assets/scissors.png", .5, 0, 0, 0, 0,
                                            247 - self.ATTACK_FRAME_WIDTH + 5, 165)
        self.player = arcade.Sprite("assets/faceBeard.png")
        self.player.center_y = self.PLAYER_IMAGE_Y
        self.player.center_x = self.PLAYER_IMAGE_X
        self.player.scale = .2
        # Cree la sprite du computer et lui donne ses values
        self.computer = arcade.Sprite("assets/compy.png")
        self.computer.center_y = self.COMPUTER_IMAGE_Y
        self.computer.center_x = self.COMPUTER_IMAGE_X
        # Cree la liste de sprites du computer et du player et les y ajoute
        self.players = None
        self.win = None
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = None
        self.draw_round = None
        self.game_state = GameState.NOT_STARTED
        # CHANGER SA DANS SETU
        self.evil_rock = None
        self.evil_paper = None
        self.evil_scissors = None

    def setup(self):
        self.player_attack_chosen = False
        self.players = arcade.SpriteList()
        self.players.extend([self.computer, self.player])
        self.evil_rock = arcade.Sprite("assets/srock.png", .5, 0, 0, 0, 0, self.computer.center_x, 165, 1, 1, True)
        self.evil_paper = arcade.Sprite("assets/spaper.png", .5, 0, 0, 0, 0, self.computer.center_x, 165, 1, 1, True)
        self.evil_scissors = arcade.Sprite("assets/scissors.png", .5, 0, 0, 0, 0, self.computer.center_x, 165, 1, 1,
                                           True)

# Validates victory selon ce que le joueur a choisis comme attaque et le randint du computer attack
    def validate_victory(self):
        if self.player_attack_type == AttackType.ROCK:
            if self.computer_attack_type == 0:
                print('draw')
                self.win = "draw"
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 2:
                print('win')
                self.win = "True"
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 1:
                print('lost')
                self.win = "False"
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
        elif self.player_attack_type == AttackType.SCISSORS:
            if self.computer_attack_type == 0:
                print('lost')
                self.win = "False"
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 2:
                print('draw')
                self.win = "draw"
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 1:
                print('win')
                self.win = "True"
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
        else:
            if self.computer_attack_type == 0:
                print('win')
                self.win = "True"
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 2:
                print('lost')
                self.win = "False"
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
            elif self.computer_attack_type == 1:
                print('draw')
                self.win = "draw"
                self.game_state = GameState.ROUND_DONE

    def draw_possible_attack(self):

        # ROCK
        self.rock_still.draw()
        arcade.draw_rectangle_outline((SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4), 165, self.ATTACK_FRAME_WIDTH,
                                      self.ATTACK_FRAME_HEIGHT, arcade.color.RED)
        # PAPER
        self.paper_still.draw()
        arcade.draw_rectangle_outline(256 + self.ATTACK_FRAME_WIDTH + 5, 165, self.ATTACK_FRAME_WIDTH,
                                      self.ATTACK_FRAME_HEIGHT, arcade.color.RED)
        # SCISSORS
        self.scissors_still.draw()
        arcade.draw_rectangle_outline(256 - (self.ATTACK_FRAME_WIDTH + 5), 165, self.ATTACK_FRAME_WIDTH,
                                      self.ATTACK_FRAME_HEIGHT, arcade.color.RED)

        # COMPUTER ATTACK (Le carré seulement)
        arcade.draw_rectangle_outline(self.computer.center_x, 165, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT,
                                      arcade.color.RED)

# Draws the computer attack selon ce qu'il a recu avec le randint
    def draw_computer_attack(self):
        if self.computer_attack_type == 0:
            self.evil_rock.draw()
        if self.computer_attack_type == 1:
            self.evil_paper.draw()
        if self.computer_attack_type == 2:
            self.evil_scissors.draw()
        else:
            pass

    def draw_scores(self):
        # Player score
        arcade.draw_text('Le pointage du joueur est ' + str(self.player_score),
                         self.player.center_x - self.ATTACK_FRAME_WIDTH - 50,
                         165 - self.ATTACK_FRAME_HEIGHT, arcade.color.CYAN, 12, int(self.ATTACK_FRAME_WIDTH * 3),
                         align="center")
        # Computer score
        arcade.draw_text("Le pointage de l'ordinateur est " + str(self.computer_score),
                         self.computer.center_x - self.ATTACK_FRAME_WIDTH - 50,
                         165 - self.ATTACK_FRAME_HEIGHT, arcade.color.CYAN, 12, int(self.ATTACK_FRAME_WIDTH * 3 + 50),
                         align="center")

    def draw_instructions(self):
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text('Appuyez sur "Space" pour commencer la partie!', 360, 440)
        if self.game_state == GameState.GAME_OVER:
            arcade.draw_text('Appuyez sur "Space" pour recommencer une partie!', 360, 440)
            if self.player_score == 3:
                arcade.draw_text('Vous avez gagné la partie!', 375, 360, arcade.color.GO_GREEN, 20)
            if self.computer_score == 3:
                arcade.draw_text("L'ordinateur a gagné la partie...", 375, 360, arcade.color.RED_DEVIL, 20)
        if self.game_state == GameState.ROUND_DONE:
            arcade.draw_text('La round est terminée cliquer sur "space" pour la continuer', 360, 440)
        if self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text('Appuyez sur une des icones pour faire votre choix!', 360, 440)

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
        if self.player_score == 3 or self.computer_score == 3:
            pass
        else:
            if self.win == "True":
                arcade.draw_text('Vous avez gagné la ronde!', 420, 390)
            elif self.win == "False":
                arcade.draw_text("L'ordinateur a gagné la ronde", 420, 390)
            elif self.win == "draw":
                arcade.draw_text("C'est une égalité!", 420, 390)
            else:
                pass

        self.draw_instructions()
        self.players.draw()
        self.draw_possible_attack()
        self.draw_computer_attack()

        # Va mettre les scores dès que la game commence
        if self.game_state == GameState.NOT_STARTED:
            pass
        else:
            self.draw_scores()

        # Rend la sprite originale invisible et commence l'animation de l'attaque choisie
        if self.player_attack_chosen:
            if self.player_attack_type == AttackType.ROCK:
                self.rock.center_x = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4) + 7
                self.rock.center_y = 165
                self.rock_still.alpha = 0
                self.rock.draw()
            if self.player_attack_type == AttackType.PAPER:
                self.paper.center_x = 256 + self.ATTACK_FRAME_WIDTH + 5
                self.paper.center_y = 165
                self.paper_still.alpha = 0
                self.paper.draw()
            if self.player_attack_type == AttackType.SCISSORS:
                self.scissors.center_x = 256 - (self.ATTACK_FRAME_WIDTH + 5)
                self.scissors.center_y = 165
                self.scissors_still.alpha = 0
                self.scissors.draw()
        else:
            self.scissors_still.alpha = 255
            self.rock_still.alpha = 255
            self.paper_still.alpha = 255
        pass

    def on_update(self, delta_time: 1 / 60):

        # Tout le temps vérifier si le joueur gagne ou non quand un round est actif
        if self.game_state == GameState.ROUND_ACTIVE:
            self.validate_victory()

        # Randomizes l'attaque du computer quand le player aura choisi son attaque
        if self.player_attack_chosen:
            if self.computer_attack_type == -1:
                pc_attack = random.randint(0, 2)
                if pc_attack == 0:
                    self.computer_attack_type = 0
                elif pc_attack == 1:
                    self.computer_attack_type = 1
                else:
                    self.computer_attack_type = 2
            if self.computer_attack_type != -1:
                pass

        if not self.player_attack_chosen:
            self.computer_attack_type = -1
        # UPDATES THE ANIMATIONS
        if self.player_attack_chosen:
            if self.player_attack_type == AttackType.ROCK:
                self.rock.on_update()
            if self.player_attack_type == AttackType.PAPER:
                self.paper.on_update()
            if self.player_attack_type == AttackType.SCISSORS:
                self.scissors.on_update()
        if self.player_score == 3:
            self.game_state = GameState.GAME_OVER
        if self.computer_score == 3:
            self.game_state = GameState.GAME_OVER

        # Change le GameState lorsque space est appuyé
    def on_key_press(self, key, key_modifiers):
        if arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                print("game started")
                self.game_state = GameState.ROUND_ACTIVE

            if self.game_state == GameState.ROUND_DONE:
                self.reset_round()
                self.game_state = GameState.ROUND_ACTIVE
            if self.game_state == GameState.GAME_OVER:
                self.player_score = 0
                self.computer_score = 0
                self.reset_round()
                self.game_state = GameState.ROUND_ACTIVE

    # Fonction qui sert à reset les variables à la fin d'une game ou à la fin d'un round
    def reset_round(self):
        self.win = None
        self.computer_attack_type = -1
        self.player_attack_chosen = False
        self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
        self.player_won_round = False
        self.draw_round = False

    # Le player choisis ici son AttackType durant GameState.ROUND_ACTIVE seulement sinon il est triste D:
    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.game_state == GameState.NOT_STARTED:
            print("game not started :C")
        elif self.game_state == GameState.ROUND_DONE:
            print("round done :C")
        elif self.game_state == GameState.GAME_OVER:
            print("boohoo game is over :(")
        else:
            if self.rock_still.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.player_attack_chosen = True
                print("rock")
            if self.paper_still.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.player_attack_chosen = True
                print("papers")
            if self.scissors_still.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.player_attack_chosen = True
                print("scis")


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
