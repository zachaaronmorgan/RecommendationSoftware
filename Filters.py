from collections import deque

def score_year_sort(video_games,filter_type,num_filter_type, upper_bound=None, lower_bound=None, value=None):
    if len(video_games) <= 1:
        return video_games
    middle = len(video_games) // 2
    left = video_games[:middle]
    right = video_games[middle:]
    sleft = score_year_sort(left,filter_type, num_filter_type,upper_bound,lower_bound,value)
    sright = score_year_sort(right, filter_type,num_filter_type,upper_bound,lower_bound,value)
    return score_year_merge(sleft,sright,filter_type,num_filter_type,upper_bound,lower_bound,value)

def score_year_merge(left, right, filter_type, num_filter_type, upper_bound, lower_bound, value):
    left = deque(left)
    right = deque(right)
    
    result = []

    if num_filter_type == 'Range':
        while left and right:
            # print(f"Left: {len(left)}, Right: {len(right)}")  # Debug statement
            left_value = int(left[0][filter_type])
            right_value = int(right[0][filter_type])
            
            if lower_bound <= left_value <= upper_bound:
                # print("Adding values from the left side...")
                result.append(left.popleft())
            elif lower_bound <= right_value <= upper_bound:
                # print("Adding values from the right side...")
                result.append(right.popleft())
            else:
                # Remove elements that do not meet the criteria
                if left and (left_value < lower_bound or left_value > upper_bound):
                    # print("Removing value from left side...")
                    left.popleft()
                if right and (right_value < lower_bound or right_value > upper_bound):
                    # print("Removing value from right side...")
                    right.popleft()

        # After the main loop, add remaining valid elements
        while left:
            left_value = int(left[0][filter_type])
            if lower_bound <= left_value <= upper_bound:
                result.append(left.popleft())
            else:
                left.popleft()
        
        while right:
            right_value = int(right[0][filter_type])
            if lower_bound <= right_value <= upper_bound:
                result.append(right.popleft())
            else:
                right.popleft()

    elif num_filter_type == 'Value':
        while left and right:
            # print(f"Left: {len(left)}, Right: {len(right)}")  # Debug statement
            left_value = int(left[0][filter_type])
            right_value = int(right[0][filter_type])
            
            if left_value == value:
                # print("Adding values from the left side...")
                result.append(left.popleft())
            elif right_value == value:
                # print("Adding values from the right side...")
                result.append(right.popleft())
            else:
                # Remove elements that do not meet the criteria
                if left:
                    # print("Removing value from left side...")
                    left.popleft()
                if right:
                    # print("Removing value from right side...")
                    right.popleft()

        # After the main loop, add remaining valid elements
        while left:
            left_value = int(left[0][filter_type])
            if left_value == value:
                result.append(left.popleft())
            else:
                left.popleft()
        
        while right:
            right_value = int(right[0][filter_type])
            if right_value == value:
                result.append(right.popleft())
            else:
                right.popleft()

    return result

def platform_genre_sort(video_games,filter_type,value):
    if len(video_games) <= 1:
        return video_games
    middle = len(video_games) // 2
    left = video_games[:middle]
    right = video_games[middle:]
    sleft = platform_genre_sort(left,filter_type,value)
    sright = platform_genre_sort(right,filter_type,value)
    return platform_genre_merge(sleft,sright,filter_type,value)

def platform_genre_merge(left, right, filter_type, values):
    left = deque(left)
    right = deque(right)
    result = []
    values_set = set(map(str.strip, values))  # Convert values to a set and strip whitespaces

    # print(f"Values Set: {values_set}")  # Debugging statement

    while left and right:
        left_value_str = left[0][filter_type]
        right_value_str = right[0][filter_type]

        # print(f"Raw Left Values: {left_value_str}")  # Debugging statement
        # print(f"Raw Right Values: {right_value_str}")  # Debugging statement

        # Ensure left_value_str and right_value_str are strings and not empty
        if isinstance(left_value_str, str) and left_value_str:
            left_values = set(map(str.strip, left_value_str.split(',')))
        else:
            left_values = set()

        if isinstance(right_value_str, str) and right_value_str:
            right_values = set(map(str.strip, right_value_str.split(',')))
        else:
            right_values = set()

        # print(f"Processed Left Values: {left_values}")  # Debugging statement
        # print(f"Processed Right Values: {right_values}")  # Debugging statement

        if values_set & left_values:
            # print(f"Adding from left: {left[0]}")  # Debugging statement
            result.append(left.popleft())
        elif values_set & right_values:
            # print(f"Adding from right: {right[0]}")  # Debugging statement
            result.append(right.popleft())
        else:
            if left:
                # print(f"Removing from left: {left[0]}")  # Debugging statement
                left.popleft()
            if right:
                # print(f"Removing from right: {right[0]}")  # Debugging statement
                right.popleft()
    
    while left:
        left_value_str = left[0][filter_type]
        # print(f"Remaining Raw Left Values: {left_value_str}")  # Debugging statement
        if isinstance(left_value_str, str) and left_value_str:
            left_values = set(map(str.strip, left_value_str.split(',')))
            # print(f"Remaining Processed Left Values: {left_values}")  # Debugging statement
            if values_set & left_values:
                # print(f"Adding remaining from left: {left[0]}")  # Debugging statement
                result.append(left.popleft())
            else:
                left.popleft()
        else:
            left.popleft()
    
    while right:
        right_value_str = right[0][filter_type]
        # print(f"Remaining Raw Right Values: {right_value_str}")  # Debugging statement
        if isinstance(right_value_str, str) and right_value_str:
            right_values = set(map(str.strip, right_value_str.split(',')))
            # print(f"Remaining Processed Right Values: {right_values}")  # Debugging statement
            if values_set & right_values:
                # print(f"Adding remaining from right: {right[0]}")  # Debugging statement
                result.append(right.popleft())
            else:
                right.popleft()
        else:
            right.popleft()

    return result




