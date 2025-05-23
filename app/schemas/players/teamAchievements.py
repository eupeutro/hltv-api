from typing import List, Optional

from pydantic import HttpUrl

from app.schemas.base import AuditMixin, HLTVBaseModel


class teamAchievementDetail(HLTVBaseModel):
    id: str
    name: str
    
class teamAchievementDetails(HLTVBaseModel):
    placement: str
    team: teamAchievementDetail
    tournament: teamAchievementDetail
    player_stats_url: HttpUrl

class PlayerTeamAchievements(HLTVBaseModel, AuditMixin):
    id: str
    achievement_count: Optional[int] = None
    achievements: Optional[List[teamAchievementDetails]] = None