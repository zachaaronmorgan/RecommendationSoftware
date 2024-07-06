from Information import *
from utilitiesfunctions import *
from LinkedList import *
import inquirer


welcome_message()
desired_filters = LinkedList()

filter_choices = ['Genre', 'Platform', 'Review', 'Year', 'Rank', 'No Other Filters']

filters_priority = select_filter_list(filter_choices)

genre_filters_priority, platform_filters_priority = get_filter_by(filters_priority)

max, min = get_filter_traits()

# print(videogames_filtered)