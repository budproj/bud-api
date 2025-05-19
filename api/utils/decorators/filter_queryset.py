from django.db.models import Q

from typing import List

def query_filter_allowed(fields: List):
    def function_query_filter(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            request = args[1]
            filter = Q()
            for key in fields:
                value = request.query_params.get(key)
                
                match(key):
                    case 'deleted_at__isnull':
                        value = bool(value)
                        filter &= Q(**{key: value})
                    case _:
                        if value is not None and value != '':
                            filter &= Q(**{key: value})
            self.queryset = self.queryset.filter(filter)
            return func(*args, **kwargs)
        return wrapper
    return function_query_filter 