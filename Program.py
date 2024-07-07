from Information import *
from utilitiesfunctions import *
from LinkedList import *


welcome_message()
desired_filters = LinkedList()

filter_choices = ['genre', 'platform', 'score', 'year', 'No Other Filters']

filters_priority = select_filter_list(filter_choices)

genre_filters_priority, platform_filters_priority, year_filter, score_filter = get_filter_by(filters_priority)


if year_filter == 'Range':
    newest_year, oldest_year = get_number_filter_traits(year_filter,'y')
    print(f"You have selected to filter year by {year_filter}: {oldest_year} to {newest_year}")
    
elif year_filter == 'Value':
    year_desired = get_number_filter_traits(year_filter,'y')
    print(f"You have selected to filter year by {year_filter}: {year_desired}")
    
if score_filter == 'Range':
    highest_score, lowest_score = get_number_filter_traits(score_filter, 's')
    print(f"You have selected to filter scores by {score_filter}: {lowest_score} to {highest_score}")
    
elif score_filter == 'Value':
    desired_score = get_number_filter_traits(score_filter,'s')
    print(f"You have selected to filter scores by {score_filter}: {desired_score}")

if genre_filters_priority:
    print(f"You have selected to filter genre by {genre_filters_priority}")

if platform_filters_priority:
    print(f"You have selected to filter platform by {platform_filters_priority}")

