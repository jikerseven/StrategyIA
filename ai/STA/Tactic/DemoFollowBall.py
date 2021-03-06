
# Under MIT licence, see LICENCE.txt

from ai.STA.Tactic.Tactic import Tactic
from ai.STA.Tactic import tactic_constants
from ai.STA.Action.MoveTo import MoveTo
from ai.STA.Action.Idle import Idle
from ai.STA.Tactic import tactic_constants
from RULEngine.Util.geometry import get_distance, get_angle
from RULEngine.Util.Pose import Pose
from RULEngine.Util.constant import POSITION_DEADZONE, BALL_RADIUS

__author__ = 'RoboCupULaval'


class DemoFollowBall(Tactic):
    # TODO : Renommer la classe pour illustrer le fait qu'elle set une Pose et non juste une Position
    """
    méthodes:
        exec(self) : Exécute une Action selon l'état courant
    attributs:
        info_manager: référence à la façade InfoManager
        player_id : Identifiant du joueur auquel est assigné la tactique
    """
    def __init__(self, info_manager, player_id, time_to_live=tactic_constants.DEFAULT_TIME_TO_LIVE):
        target = info_manager.get_ball_position()
        Tactic.__init__(self, info_manager, target, time_to_live=time_to_live)
        assert isinstance(player_id, int)

        self.current_state = self.halt
        self.next_state = self.halt
        self.player_id = player_id
        self.target = target


    def move_to_ball(self):
        self.target = self.info_manager.get_ball_position()
        move = MoveTo(self.info_manager, self.player_id, Pose(self.target))

        if get_distance(self.info_manager.get_player_pose(self.player_id).position, self.target) < POSITION_DEADZONE + BALL_RADIUS:
            self.next_state = self.halt
        else:
            self.move_to_ball

        return move


    def halt(self, reset=False):
        stop = Idle(self.info_manager, self.player_id)

        if get_distance(self.info_manager.get_player_pose(self.player_id).position, self.info_manager.get_ball_position()) < POSITION_DEADZONE:
            self.next_state = self.halt
        else:
            self.next_state = self.move_to_ball
        return stop
