from typing import Tuple

from cycle.domain.entities import CycleDate, Cycle

from cycle.models import CycleORM


def map_cycle_orm_to_entity(cycle_orm: CycleORM) -> Cycle:
    """Converte um UserORM (modelo Django) para uma entidade User de domínio."""
    return Cycle(
        id=str(cycle_orm.id),
        date_start=cycle_orm.date_start,
        date_end=cycle_orm.date_end,
        team=str(cycle_orm.team.id),
        period=cycle_orm.period,
        cadence=cycle_orm.cadence,
        parent=str(cycle_orm.parent.id) if cycle_orm.parent else None,
        active=cycle_orm.active,
        created_at=cycle_orm.created_at,
        updated_at=cycle_orm.updated_at,
        deleted_at=cycle_orm.deleted_at,
    )
    
def map_cycle_date_orm_to_entity(cycle_date: Tuple[str, str]) -> CycleDate:
    """Converte uma tupla de dados em uma entidade CycleDate."""
    return CycleDate(
        year = cycle_date[0],
        quarter = cycle_date[1],
    )