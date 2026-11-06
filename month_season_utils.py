def month_number_to_name(month_number):
    import calendar
    month_name = calendar.month_abbr[month_number]
    return month_name 

def month_name_to_number(month_name):
    if type(month_name) == int:
        month_number = month_name
    else:
        month_number = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9, 
            'oct': 10,
            'nov': 11,
            'dec': 12
        }[month_name]
    return month_number 

def month_in_season(month):
    month = month_name_to_number(month)

    if month == 12:
        month = 0

    seasons = {
        0: 'winter',
        1: 'spring',
        2: 'summer',
        3: 'fall'
    }

    season_number = month // 3
    season = seasons[season_number]
    return season
