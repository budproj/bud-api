from team.domain.entities import Team
from team.models import TeamORM

from user.infrastructure.db.mappers import map_user_orm_to_entity

def map_team_orm_to_entity(team_orm: TeamORM) -> Team:
    return Team(
        id=str(team_orm.id),
        name=team_orm.name,
        gender=team_orm.gender,
        description=team_orm.description,
        parent= str(team_orm.parent.id) if team_orm.parent else None,
        owner=map_user_orm_to_entity(team_orm.owner),
        users=[str(i.id) for i in team_orm.users.all()],
        created_at=team_orm.created_at,
        updated_at=team_orm.updated_at,
        deleted_at=team_orm.deleted_at
    )