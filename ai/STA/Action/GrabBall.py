# Under MIT licence, see LICENCE.txt
from .Action import Action
from ...Util.types import AICommand
from RULEngine.Util.Pose import Pose
from RULEngine.Util.geometry import get_angle

__author__ = 'Robocup ULaval'


class GrabBall(Action):
    """
    Action GrabBall: Déplace le robot afin qu'il prenne contrôle de la balle
    Méthodes :
        exec(self): Retourne la pose où se rendre
    Attributs (en plus de ceux de Action):
        player_id : L'identifiant du joueur
    """
    def __init__(self, p_info_manager, p_player_id):
        """
            :param p_info_manager: référence vers l'InfoManager
            :param p_player_id: Identifiant du joueur qui prend le contrôle de la balle
        """
        Action.__init__(self, p_info_manager)
        assert(isinstance(p_player_id, int))
        self.player_id = p_player_id

    def exec(self):
        """
        Place le robot afin qu'il prenne le contrôle de la balle
        :return: Un tuple (Pose, kick) où Pose est la destination du joueur et kick est nul (on ne botte pas)
        """
        ball_position = self.info_manager.get_ball_position()
        destination_orientation = get_angle(self.info_manager.get_player_pose(self.player_id).position, ball_position)
        destination_pose = Pose(ball_position, destination_orientation)
        kick_strength = 0
        return AICommand(destination_pose, kick_strength)
