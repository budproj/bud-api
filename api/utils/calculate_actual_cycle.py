from django.utils import timezone

def calculate_actual_cycle(actual_month, actual_year):
    quarter = (actual_month+2) // 3

    date_start = timezone.datetime(actual_year, (quarter-1)*3+1, 1)
    date_end = timezone.datetime(actual_year, quarter*3+1, 1)

    return date_start, date_end, quarter
    