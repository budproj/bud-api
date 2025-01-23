import enum
from datetime import datetime, timedelta, date
import calendar
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone

class TranslateRelativeDate:
    
    @staticmethod
    def current(keyword):
        match keyword:
            case 'days':
                return Q(created_at__gte=timezone.now().date)
            case 'weeks':
                current_day = timezone.now()
                current_week = current_day.isocalendar()
                weekstart = current_day - timedelta(days=current_week.weekday)
                return Q(created_at__range=(weekstart, current_day + timedelta(days=1)))                
            case 'months':
                current_day = timezone.now()
                return Q(created_at__range=(current_day - timedelta(days=current_day.day), current_day))
            case 'years':
                current_day = timezone.now()
                return Q(created_at__range=(datetime(current_day.year,1,1), current_day))
            case _:
                return Q()
            
    @staticmethod
    def last(keyword, time_relative):
        match keyword:
            case 'weeks':
                current_day = timezone.now()
                week_selected = current_day - relativedelta(weeks=int(time_relative))
                week_start = week_selected - relativedelta(days=week_selected.isocalendar().weekday)
                week_end = week_selected + relativedelta(days=7 - week_selected.isocalendar().weekday)
                return Q(created_at__range=(week_start, week_end))
            case 'months':
                current_day = timezone.now()
                month_selected = current_day - relativedelta(months=time_relative)
                month_start = date(month_selected.year, month_selected.month, 1)
                month_end = date(month_selected.year, month_selected.month, calendar.monthrange(month_selected.year, month_selected.month)[1])
                return Q(created_at__range=(month_start, month_end))
            case 'years':
                current_day = timezone.now()
                year_selected = current_day - relativedelta(years=time_relative)
                year_start = date(year_selected.year, 1, 1)
                year_end = date(year_selected.year, 12, 31)
                return Q(created_at__range=(year_start, year_end))
            case _:
                return Q()
    
    @staticmethod
    def since(date):
        return Q(created_at__range=(datetime.strptime(date).date(), timezone.now().date()))
    
    @staticmethod
    def between(date_start, date_end):
        return Q(created_at__range=(datetime.strptime(date_start).date(),datetime.strptime(date_end).date()))
        

# Keyword
# Last [keyword] OR Current [keyword]
# Since [date_start]
# Between [date_start] [date_end] Since [date_start]