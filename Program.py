from Information import *
from utilitiesfunctions import get_number_filter_traits, select_filter_list, get_filter_by, welcome_message
from LinkedList import *
from Filters import platform_genre_sort, score_year_sort

welcome_message()
desired_filters = LinkedList()

filter_choices = ['genre', 'platform', 'score', 'year', 'No Other Filters']

filters_priority = select_filter_list(filter_choices)

genre_filters_priority, platform_filters_priority, year_filter, score_filter = get_filter_by(filters_priority)


result = video_games
for filter in filters_priority:
    if year_filter == 'Range' and filter == 'year':
        newest_year, oldest_year = get_number_filter_traits(year_filter,'y')
        year_ky = 'r-date'
        print(f"You have selected to filter year by {year_filter}: {oldest_year} to {newest_year}")
        result = score_year_sort(result,year_ky,year_filter, upper_bound=newest_year, lower_bound=oldest_year, value=None)
    
    elif year_filter == 'Value' and filter == 'year':
        year_desired = get_number_filter_traits(year_filter,'y')
        year_ky = 'r-date'
        print(f"You have selected to filter year by {year_filter}: {year_desired}")
        result = score_year_sort(result,year_ky,year_filter, upper_bound=None, lower_bound=None, value=year_desired)

    if score_filter == 'Range' and filter == 'score':
        highest_score, lowest_score = get_number_filter_traits(score_filter, 's')
        score_ky = 'score'
        print(f"You have selected to filter scores by {score_filter}: {lowest_score} to {highest_score}")
        result = score_year_sort(result,score_ky,score_filter, upper_bound=highest_score, lower_bound=lowest_score, value=None)

    elif score_filter == 'Value' and filter == 'score':
        desired_score = get_number_filter_traits(score_filter,'s')
        score_ky = 'score'
        print(f"You have selected to filter scores by {score_filter}: {desired_score}")
        result = score_year_sort(result,score_ky,score_filter, upper_bound=None, lower_bound=None, value=desired_score)

    if genre_filters_priority and filter == 'genre':
        print(f"You have selected to filter genre by {genre_filters_priority}")
        result = platform_genre_sort(result,filter,genre_filters_priority)

    if platform_filters_priority and filter == 'platform':
        print(f"You have selected to filter platform by {platform_filters_priority}")
        result = platform_genre_sort(result,filter,platform_filters_priority)
        
if not result:
    print("I am sorry, but I could not find a game that fits your filters. Please try and expand the search to find a match.")
else:
    for game in result:
        print(f"Game Name: {game['name']} \n Score: {game['score']} \n Genres: {game['genre']} \n Platforms: {game['platform']} \n Release Year: {game['r-date']} \n")