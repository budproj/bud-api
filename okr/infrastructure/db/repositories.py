from typing import List, Optional

from django.db import connection

from okr.infrastructure.db.mappers import map_key_result_orm_to_entity, map_cycle_date_orm_to_entity, \
    map_cycle_orm_to_entity
from okr.application.interfaces import IKeyResultRepository, ICycleRepository, ITeamRepository
from okr.domain.entities import Cycle, KeyResult, CycleDate
from okr.models import CycleORM, KeyResultORM


class DjangoKeyResultRepository(IKeyResultRepository):
    def find_by_team_id(self, team_id: str) -> Optional[List[KeyResult]]:
        try:
            kr_orm = KeyResultORM.objects.filter(team__id=team_id, objective__cycle__active=True)
            return [map_key_result_orm_to_entity(i) for i in kr_orm]
        except KeyResultORM.DoesNotExist:
            return None
    
    
class DjangoCycleRepository(ICycleRepository):
    def find_cycle_by_team_id(self, team_id: str) -> Optional[List[Cycle]]:
        cycle_orm = CycleORM.objects.filter(team__id=team_id, active=True)
        return [map_cycle_orm_to_entity(i) for i in cycle_orm]
        
    def find_cycle_dates_by_team_id(self, team_id: str) -> Optional[List[CycleDate]]:
        query = """
            SELECT
                CAST(EXTRACT(YEAR FROM cy.date_start) AS TEXT) AS year,
                CAST(CEIL(EXTRACT(MONTH FROM cy.date_start) / 3.0) AS TEXT) AS quarter
            FROM 
                cycle cy
            LEFT JOIN team_company tico ON
                tico.company_id = cy.team_id
            WHERE 
                tico.team_id = %s  
            GROUP BY
                year, quarter
            ORDER BY
                year DESC, quarter DESC
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [team_id])
            rows = cursor.fetchall()
            return [map_cycle_date_orm_to_entity(i) for i in rows]


class DjangoCompanyRepository(ITeamRepository):
    def find_team_company_by_id(self, team_id: str) -> Optional[str]:
        query = """
            SELECT
                company_id
            FROM 
                team_company
            WHERE
                team_id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [team_id])
            row = cursor.fetchone()
            return str(row[0]) or None
    