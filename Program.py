from Information import *
from utilitiesfunctions import *
from LinkedList import *


welcome_message()
desired_filters = LinkedList()

filter_choices = ['genre', 'platform', 'score', 'year', 'No Other Filters']

filters_priority = select_filter_list(filter_choices)

genre_filters_priority, platform_filters_priority, year_filter, score_filter = get_filter_by(filters_priority)

print(genre_filters_priority, platform_filters_priority, year_filter, score_filter)

if year_filter == 'Specific Range':
    newest_year, oldest_year = get_number_filter_traits(year_filter,'y')
elif year_filter == 'Specific Value':
    year_desired = get_number_filter_traits(year_filter,'y')

if score_filter == 'Specific Range':
    highest_score, lowest_score = get_number_filter_traits(score_filter, 's')
elif score_filter == 'Specific Value':
    desired_score = get_number_filter_traits(score_filter,'s')

