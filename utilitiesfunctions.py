from Information import *
import inquirer
import re
from datetime import datetime as dt

def welcome_message():
    print("Hello and welcome to Video Game Recommender 1.0!")

def select_filter(filter_choices):
    game_filters_q = [inquirer.List('filter', message="Choose the filters you would like to apply to the games list in the order of importance. First being most important and last the least important", choices=filter_choices)]
    chosen_filter = inquirer.prompt(game_filters_q)
    return chosen_filter['filter']

def select_genre(genres):
    genres_choices = [inquirer.List('genre', message="Choose which genre your game best fits", choices=genres)]
    chosen_genre = inquirer.prompt(genres_choices)
    return chosen_genre['genre']

def select_platform(platforms):
    platforms_choices = [inquirer.List('platform', message="Choose which platform or platforms your game is available on", choices=platforms)]
    chosen_platform = inquirer.prompt(platforms_choices)
    return chosen_platform['platform']

def select_available_platforms(platforms):
    platforms.append('The platform is not listed')
    platform_choices_untouched = platforms.copy()
    platforms_chosen = []
    while len(platforms) > 0 and (len(platforms_chosen) < len(platform_choices_untouched) -1):
        chosen_platform = select_platform(platforms)
        if chosen_platform == 'The platform is not listed' and len(platforms) == len(platform_choices_untouched):
            return platforms_chosen
            
        elif chosen_platform == 'The platform is not listed' and len(platforms) != len(platform_choices_untouched):
            print(f"You have selected the following platforms that your game is available on {platforms_chosen}")
            return platforms_chosen
            
        else:
            platforms_chosen.append(chosen_platform)
            platforms.remove(chosen_platform)
    
    print(f"You have selected the following platforms that your game is available on {platforms_chosen}")
    return platforms_chosen

def select_filter_list(filter_choices, one_response=False):
    if one_response:
        filters = select_filter(filter_choices)
        return filters
    else:
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
    year_filter = None
    score_filter = None
    year_filters = ['Newest', 'Oldest', 'Specific Range', 'Specific Value']
    score_filters = ['Highest', 'Lowest', 'Specific Range', 'Specific Value']
    for filter in filters_priority:
        if filter == 'genre':
            print(f"You have selected to filter by {filter}. Please choose which {filter} or {filter}s you want to filter by in the order of importance. First being most important and last the least important\n")
            genres.append("No Other Filters")
            genre_filters = select_filter_list(genres)
            genres.remove("No Other Filters")
            
        elif filter == 'platform':
            print(f"You have selected to filter by {filter}. Please choose which {filter} or {filter}s you want to filter by in the order of importance. First being most important and last the least important\n")
            platforms.append("No Other Filters")
            platform_filters = select_filter_list(platforms)
            platforms.remove("No Other Filters")
        
        elif filter == 'year':
            print(f"You have selected to filter by {filter}. Please choose whether to filter by newest, oldest, specific range, or year\n")
            year_filter = select_filter_list(year_filters, one_response=True)
        
        elif filter == 'score':
            print(f"You have selected to filter by {filter}. Please choose whether to filter by highest, lowest, specific range, or review\n")
            score_filter = select_filter_list(score_filters, one_response=True)
    return genre_filters, platform_filters, year_filter, score_filter

def get_release_year(message):
    year = input(message)
    current_year = dt.now().year
    if valid_year(year):
        if int(year) > current_year:
            print("Year has not happened yet. Please enter a year that has happened already")
            return get_release_year(message)
        else:
            return int(year)
    else:
        print("Invalid year. Please enter a year in the form YYYY")
        return get_release_year(message)

def valid_year(year):
    pattern = re.compile(r"^\d{4}$")
    if pattern.match(year):
        return True
    else:
        return False

def get_new_game(genres,platforms):
    genres.append('The genre is not listed')
    chosen_genre = select_genre(genres)
    chosen_platforms = select_available_platforms(platforms)
    release_year = get_release_year()
    return chosen_genre, chosen_platforms, release_year


def get_score(message):
    score = input(message)
    try:
        score = int(score)
        if 0 <= score <= 100:
            return score
        else:
            print("You must enter a value between 0 and 100 (inclusive) to continue")
            return get_score(message)
    except ValueError:
        print("You have not entered a number. Please enter a number between 0 and 100 (inclusive) to continue.")
        return get_score(message)

def get_number_filter_traits(number_filter, filter_type):
    if filter_type == 'y':
        if number_filter == 'Specific Range':
            upper_bound = get_release_year("Enter the newest release year you would like to see: ")
            lower_bound = get_release_year("Enter the oldest release year you would like to see: ")
            if upper_bound > lower_bound:
                return upper_bound, lower_bound
            else:
                print("The newest release year must be more recent than the oldest release year!")
                return get_number_filter_traits(number_filter, filter_type)
    elif filter_type == 's':
        if number_filter == 'Specific Range':
            upper_bound = get_score("Enter the highest score you would like to see: ")
            lower_bound = get_score("Enter the lowest score you would like to see: ")
            if upper_bound > lower_bound:
                return upper_bound, lower_bound
            else:
                print("The highest score must be greater than the lowest score")
                return get_number_filter_traits(number_filter, filter_type)