from django.utils import timezone

def calculate_actual_cycle(actual_month, actual_year):
    quarter = (actual_month+2) // 3
    match quarter:
        case 1:
            date_start = timezone.datetime(actual_year, 1, 1)
            date_end = timezone.datetime(actual_year, 3, 31)
        case 2:
            date_start = timezone.datetime(actual_year, 4, 1)
            date_end = timezone.datetime(actual_year, 6, 30)
        case 3: 
            date_start = timezone.datetime(actual_year, 7, 1)
            date_end = timezone.datetime(actual_year, 9, 30)
        case 4:
            date_start = timezone.datetime(actual_year, 10, 1)
            date_end = timezone.datetime(actual_year, 12, 31)
    return date_start, date_end, quarter
    