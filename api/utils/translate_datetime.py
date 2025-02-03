from datetime import datetime, timedelta, date
import calendar
from dateutil.relativedelta import relativedelta


class WrongKeywordException(Exception):
    """
    Keyword not an option.
    """

    pass


class TranslateRelativeDate:
    def __init__(self, timezone, last, since, upto):
        if last:
            time_relative, keyword = last.split(' ')
            now = timezone.now()
            if time_relative == '0':
                self.date_range = self._current(now, keyword)
            else:
                self.date_range = self._last(now, keyword, time_relative)
        elif since and upto:
            now = timezone.now()
            self.date_range = self._between(since, upto)
        elif since:
            now = timezone.now()
            self.date_range = self._since(now, since)

    def _current(self, now, keyword):
        match keyword:
            case 'days':
                return now - timedelta(days=1), now + timedelta(days=1)
            case 'weeks':
                current_day = now
                current_week = current_day.isocalendar()
                weekstart = current_day - timedelta(days=current_week.weekday)
                return weekstart, current_day + timedelta(days=1)
            case 'months':
                current_day = now
                return current_day - timedelta(days=current_day.day), current_day
            case 'years':
                current_day = now
                return datetime(current_day.year, 1, 1), current_day
            case _:
                raise WrongKeywordException

    def _last(self, now, keyword, time_relative):
        match keyword:
            case 'weeks':
                current_day = now
                week_selected = current_day - relativedelta(weeks=int(time_relative))
                week_start = week_selected - relativedelta(
                    days=week_selected.isocalendar().weekday
                )
                week_end = week_selected + relativedelta(
                    days=7 - week_selected.isocalendar().weekday
                )
                return week_start, week_end
            case 'months':
                current_day = now
                month_selected = current_day - relativedelta(months=time_relative)
                month_start = date(month_selected.year, month_selected.month, 1)
                month_end = date(
                    month_selected.year,
                    month_selected.month,
                    calendar.monthrange(month_selected.year, month_selected.month)[1],
                )
                return month_start, month_end
            case 'years':
                current_day = now
                year_selected = current_day - relativedelta(years=time_relative)
                year_start = date(year_selected.year, 1, 1)
                year_end = date(year_selected.year, 12, 31)
                return year_start, year_end
            case _:
                raise WrongKeywordException

    def _since(self, now, date):
        return datetime.strptime(date).date(), now

    def _between(self, date_start, date_end):
        return datetime.strptime(date_start).date(), datetime.strptime(date_end).date()


# Keyword
# Last [keyword] OR Current [keyword]
# Since [date_start]
# Between [date_start] [date_end] Since [date_start]
