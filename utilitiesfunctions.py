from Information import *
import inquirer

def welcome_message():
    print("Hello and welcome to Video Game Recommender 1.0!")

def select_filter(filter_choices):
    game_filters_q = [inquirer.List('filter', message="Choose the filters you would like to apply to the games list in the order of importance. First being most important and last the least important.", choices=filter_choices)]
    chosen_filter = inquirer.prompt(game_filters_q)
    return chosen_filter['filter']

def select_genre(genres):
    genre_filters_q = [inquirer.List('genre', message="Choose which genres you want to filter by", choices=genres)]
    chosen_genre = inquirer.prompt(genre_filters_q)
    return chosen_genre['genre']

def select_filter_list(filter_choices):
    filter_choices_untouched = filter_choices.copy()
    filters_priority = []
    while len(filter_choices) > 0 and (len(filters_priority) == 0 or len(filters_priority) < len(filter_choices_untouched) -1):
        chosen_filter = select_filter(filter_choices)
        if chosen_filter == 'No Other Filters' and len(filter_choices) == len(filter_choices_untouched):
            print("I am sorry, but you have not selected any filters. To continue you must select at least one filter from the list.")
            
        elif chosen_filter == 'No Other Filters' and len(filter_choices) != len(filter_choices_untouched):
            print(f"You have selected to filter by {filters_priority}")
            return filters_priority
            
        else:
            filters_priority.append(chosen_filter)
            filter_choices.remove(chosen_filter)
    
    print(f"You have selected to filter by {filters_priority}")
    return filters_priority

def get_filter_by(filters_priority):
    genre_filters = []
    platform_filters = []
    for filter in filters_priority:
        if filter == 'Genre':
            print(f"You have selected to filter by {filter}. Please choose which {filter} or {filter}s you want to filter by in the order of importance. First being most important and last the least important.\n")
            print(f"Available {filter}s:\n{genres}")
            genres.append("No Other Filters")
            genre_filters = select_filter_list(genres)
        
        elif filter == 'Platform':
            print(f"You have selected to filter by {filter}. Please choose which {filter} or {filter}s you want to filter by in the order of importance. First being most important and last the least important.\n")
            print(f"Available {filter}s:\n{platforms}")
            platforms.append("No Other Filters")
            platform_filters = select_filter_list(platforms)

    return genre_filters, platform_filters

def get_filter_traits():
    traits = input("Enter the max, min values in the form and order max, min: ").strip()
    try:
        max, min = traits.split(',')
        max, min = int(max), int(min)
    
    except ValueError as e:
        print("Invalid input please enter a maximum value followed by a comma and then minimum value like 5,2 1980,2000.")
        return get_filter_traits()
    
    return max, min
