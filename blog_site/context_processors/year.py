import datetime


def now_year(request):
    """Adds a variable with the current year"""
    return {
        'now_year': datetime.datetime.now().year
    }
