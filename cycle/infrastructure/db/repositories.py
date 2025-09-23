from typing import List, Optional

from django.db import connection

from cycle.infrastructure.db.mappers import map_cycle_date_orm_to_entity, map_cycle_orm_to_entity
from cycle.application.interfaces import ICycleRepository
from cycle.domain.entities import CycleDate
from cycle.models import CycleORM
    
    
class DjangoCycleRepository(ICycleRepository):
    def find_cycle_by_team_id(self, team_id):
        cycle_orm = CycleORM.objects.filter(team__id=team_id, active=True)
        return [map_cycle_orm_to_entity(i) for i in cycle_orm], 200, None
        
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
    