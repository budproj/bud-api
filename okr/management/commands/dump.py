from datetime import timedelta

from django.utils import timezone
from django.core.management.base import BaseCommand

from api.utils.calculate_actual_cycle import calculate_actual_cycle
from user.models import User
from team.models import Team
from task_manager.models import Task
from okr.models import Objective, Cycle, KeyResult

class Command(BaseCommand):
    help = 'Create database for local usages'

    def handle(self, *args, **options):
        users = self.create_users()
        
        TEAM_1 = self.create_team(
            name = 'NERV',
            description = 'Organização para-militar especial criada para combater os Anjos depois do Segundo Impacto.',
            parent = None,
            user = users[1],
            users_list = users,
        )
        
        TEAM_2 = self.create_team(
            name = 'SEELE',
            description = 'Organização religiosa que tem como objetivo secreto a Instrumentalidade Humana.',
            parent = TEAM_1,
            user = users[1],
            users_list = [ users[1] ],
        )
        
        TEAM_3 = self.create_team(
            name = 'Fugitivos da instrumentalização',
            description = 'Os que escolheram a realidade.',
            parent = None,
            user = users[0],
            users_list = [ users[3] ]
        )
        
        year = timezone.now().year
        date_start, date_end, quarter = calculate_actual_cycle(timezone.now().month, year)

        CYCLE_1 = self.create_cycle(
            date_start = timezone.datetime(year, 1, 1),
            date_end = timezone.datetime(year, 12, 31),
            team = TEAM_1,
            period = f'{year}',
            cadence = 'YEARLY',
            parent = None
        )
        
        CYCLE_2 = self.create_cycle(
            date_start = date_start,
            date_end = date_end,
            team = TEAM_1,
            period = f'Q{quarter}',
            cadence = 'QUARTER',
            parent = CYCLE_1
        )
        
        CYCLE_3 = self.create_cycle(
            date_start = timezone.datetime(year, 1, 1),
            date_end = timezone.datetime(year, 12, 31),
            team = TEAM_2,
            period = f'{year}',
            cadence = 'YEARLY',
            parent = None
        )
        
        CYCLE_4 = self.create_cycle(
            date_start = date_start,
            date_end = date_end,
            team = TEAM_2,
            period = f'Q{quarter}',
            cadence = 'QUARTER',
            parent = CYCLE_3
        )
        
        CYCLE_5 = self.create_cycle(
            date_start = timezone.datetime(year, 1, 1),
            date_end = timezone.datetime(year, 12, 31),
            team = TEAM_3,
            period = f'{year}',
            cadence = 'YEARLY',
            parent = None
        )
        
        CYCLE_6 = self.create_cycle(
            date_start = date_start,
            date_end = date_end,
            team = TEAM_3,
            period = f'Q{quarter}',
            cadence = 'QUARTER',
            parent = CYCLE_5
        )
        
        OBJECTIVE_1 = self.create_objective(
            title = 'Combater os anjos.',
            cycle = CYCLE_2,
            owner = users[1],
            team = TEAM_1,
            description = '',
            mode = 'PUBLISHED'
        )
        
        OBJECTIVE_2 = self.create_objective(
            title = 'Iniciar o terceiro impacto',
            cycle = CYCLE_3,
            owner = users[1],
            team = TEAM_2,
            description = '',
            mode = 'PUBLISHED'
        )
        
        OBJECTIVE_3 = self.create_objective(
            title = 'Montar a resistência',
            cycle = CYCLE_6,
            owner = users[0],
            team = TEAM_3,
            description = '',
            mode = 'PUBLISHED'
        )
        
        KEY_RESULT_1 = self.create_key_result(
            title = 'Derrotar os anjos',
            goal = 13.0,
            initial_value = 0.0,
            description = 'Derrotar todos os anjos antes que eles entrem na NERV.',
            format = 'NUMBER',
            objective = OBJECTIVE_1,
            team = TEAM_1,
            owner = users[0],
            support_team = [users[2], users[3]], 
        )
        
        KEY_RESULT_2 = self.create_key_result(
            title = 'Ter controle total do EVA-01',
            goal = 100.0,
            initial_value = 0.0,
            description = '',
            format = 'PERCENTAGE',
            objective = OBJECTIVE_1,
            team = TEAM_1,
            owner = users[0],
            support_team = (), 
        )
        
        KEY_RESULT_3 = self.create_key_result(
            title = 'Fundir Adão e Eva',
            goal = 100.0,
            initial_value = 0.0,
            description = '',
            format = 'PERCENTAGE',
            objective = OBJECTIVE_2,
            team = TEAM_2,
            owner = users[1],
            support_team = (), 
        )
        
        KEY_RESULT_4 = self.create_key_result(
            title = 'Clones da Rey',
            goal = 4000.0,
            initial_value = 0.0,
            description = '',
            format = 'NUMBER',
            objective = OBJECTIVE_2,
            team = TEAM_2,
            owner = users[1],
            support_team = [ users[2] ], 
        )
        
        KEY_RESULT_5 = self.create_key_result(
            title = 'Redomas pelo mundo',
            goal = 20.0,
            initial_value = 0.0,
            description = '',
            format = 'NUMBER',
            objective = OBJECTIVE_3,
            team = TEAM_3,
            owner = users[3],
            support_team = (), 
        )
        
        TASK_1 = self.create_task(
            team_id = TEAM_1,
            key_result_id = KEY_RESULT_1, 
            title = 'Manter os danos de tokyo 3 menores que 40%',
            description = 'Diminuir os danos á cidade.',
            priority = 3,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[1],
            support_team = [users[0].first_name + '' + users[0].last_name],
        )
        
        TASK_2 = self.create_task(
            team_id = TEAM_1,
            key_result_id = None,
            title = 'Preparar tanques para novos ataques',
            description = '',
            priority = 2,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[1],
            support_team = [],
        )
        
        TASK_3 = self.create_task(
            team_id = TEAM_1,
            key_result_id = None, 
            title = 'Ouvir musica',
            description = '',
            priority = 1,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[0],
            support_team = [],
        )
        
        TASK_4 = self.create_task(
            team_id = TEAM_1,
            key_result_id = KEY_RESULT_1, 
            title = 'Derrotar o anjo Sachiel',
            description = 'Impedir outro impacto derrotando o anjo Sachiel',
            priority = 1,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[1],
            support_team = [],
        )
        
        TASK_5 = self.create_task(
            team_id = TEAM_1,
            key_result_id = KEY_RESULT_2, 
            title = 'Impedir o modo berserk',
            description = '',
            priority = 5,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[0],
            support_team = [],
        )
        
        TASK_5 = self.create_task(
            team_id = TEAM_2,
            key_result_id = KEY_RESULT_4, 
            title = 'Clones',
            description = '',
            priority = 5,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[1],
            support_team = [],
        )
        
        TASK_6 = self.create_task(
            team_id = TEAM_2,
            key_result_id = KEY_RESULT_5, 
            title = 'Resistir',
            description = '',
            priority = 5,
            due_date = timezone.now() + timedelta(days=5),
            owner = users[3],
            support_team = [],
        )
    
    def create_users(self):
        USER_1, created = User.objects.get_or_create(
            email='shinji.ikari@getbud.co',
            role='GOD',
            first_name='Shinji',
            last_name='Ikari',
            status='ACTIVE',
        )

        if created:
            USER_1.set_password('robosgigantes123')
            USER_1.save()
            
        USER_2, created = User.objects.get_or_create(
            email='gendo.ikari@getbud.co',
            role='GOD',
            first_name='Gendo',
            last_name='Ikari',
            status='ACTIVE',
        )

        if created:
            USER_2.set_password('robosgigantes123')
            USER_2.save()
            
        USER_3, created = User.objects.get_or_create(
            email='rei.ayanami@getbud.co',
            role='GOD',
            first_name='Rei',
            last_name='Ayanami',
            status='ACTIVE',
        )

        if created:
            USER_3.set_password('robosgigantes123')
            USER_3.save()
        
        USER_4, created = User.objects.get_or_create(
            email='asuka.langley@getbud.co',
            role='GOD',
            first_name='Asuka',
            last_name='Langley',
            status='ACTIVE',
        )

        if created:
            USER_4.set_password('robosgigantes123')
            USER_4.save()
            
        return (USER_1, USER_2, USER_3, USER_4)
    
    def create_team(self, name, description, parent, user, users_list):
        TEAM, created = Team.objects.get_or_create(
            name=name,
            description=description,
            parent=parent,
            owner=user,
        )
        #if created:
         #   for i in users_list:
          #      TEAM.users.add(i)
           # TEAM.save()
        return TEAM
                
    def create_cycle(self, date_start, date_end, team, period, cadence, parent, active = True):
        CYCLE, created = Cycle.objects.get_or_create(
            date_start = date_start,
            date_end = date_end,
            team = team,
            period = period,
            cadence = cadence,
            parent = parent,
            active = active
        )
        return CYCLE
            
    def create_objective(self, title, cycle, owner, team, description, mode):
        OBJECTIVE, created = Objective.objects.get_or_create(
            title = title,
            cycle = cycle,
            owner = owner,
            team = team, 
            description = description,
            mode = mode
        ) 
        
        return OBJECTIVE
    
    def create_key_result(
        self, 
        title, 
        goal,
        initial_value,
        description,
        format,
        objective,
        team,
        owner,
        support_team,
        type = 'ASCENDING',
        mode = 'PUBLISHED',
        comment_count = {},
        ):
        KEY_RESULT, created = KeyResult.objects.get_or_create(
            title = title,
            goal = goal,
            initial_value = initial_value,
            description = description,
            format = format,
            objective = objective,
            team = team,
            owner = owner,
            type = type,
            mode = mode,
            comment_count = comment_count
        )
        #if created:
         #   for i in support_team:
          #      KEY_RESULT.support_team.add(i)
           # KEY_RESULT.save()
        return KEY_RESULT
    
    def create_task(
        self, 
        team_id, 
        key_result_id, 
        title,
        description,
        priority,
        due_date,
        owner,
        support_team,
        ):
        TASK, created = Task.objects.get_or_create(
            team_id=team_id,
            key_result_id=key_result_id,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            owner=owner,
            support_team=support_team,   
        )
        return TASK