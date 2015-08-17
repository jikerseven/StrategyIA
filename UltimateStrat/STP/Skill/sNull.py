from UltimateStrat.STP.Skill.SkillBase import SkillBase
from PythonFramework.Util.Pose import Pose

__author__ = 'jbecirovski'


class sNull(SkillBase):
    """
    sNull generate next pose which is its pose
    """
    def __init__(self):
        SkillBase.__init__(self, self.__class__.__name__)

    def act(self, pose_player, pose_target, pose_goal):
        return pose_player.copy()