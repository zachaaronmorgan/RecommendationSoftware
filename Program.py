from Information import *
from utilitiesfunctions import *
from LinkedList import *
import inquirer


welcome_message()
# desired_filters = LinkedList()

# filter_choices = ['genre', 'platform', 'score', 'year', 'No Other Filters']

# filters_priority = select_filter_list(filter_choices)

# genre_filters_priority, platform_filters_priority, year_filter, score_filter = get_filter_by(filters_priority)

# print(genre_filters_priority, platform_filters_priority, year_filter, score_filter)

upper_bound, lower_bound = get_number_filter_traits("Specific Range",'y')
