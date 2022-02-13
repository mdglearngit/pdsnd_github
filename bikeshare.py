import time
import pandas as pd
import numpy as np

""" webpages I read when completing project to help me troubleshoot my code or get ideas on how to approach a requirement. """
""" https://docs.python.org/3.6/library/index.html """
""" https://pandas.pydata.org/pandas-docs/stable/reference/general_functions.html#top-level-dealing-with-datetimelike """
""" https://www.python.org/dev/peps/pep-0257/ """
""" https://blog.finxter.com/how-to-filter-a-dictionary-in-python/ """
""" https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.dayofweek.html """
""" https://www.geeksforgeeks.org/how-to-filter-dataframe-rows-based-on-the-date-in-pandas/ """
""" https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/ """
""" https://datatofish.com/if-condition-in-pandas-dataframe/ """
""" https://www.geeksforgeeks.org/convert-floats-to-integers-in-a-pandas-dataframe/ """
""" https://www.datasciencemadesimple.com/join-or-concatenate-string-python-dataframe/ """
""" https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/ """
""" https://stackoverflow.com/questions/52457656/using-conditional-if-else-logic-with-pandas-dataframe-columns """
""" https://www.geeksforgeeks.org/ways-to-apply-an-if-condition-in-pandas-dataframe-2/ """
""" https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8"""
""" https://www.machinelearningplus.com/pandas/pandas-iloc-how-to-select-rows-using-index-in-dataframes/ """
""" https://stackoverflow.com/questions/5164642/python-print-a-generator-expression """

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""Creates dictionary to map month name entered to a numeric value to facilitate data filtering."""
"""Dictionary values are sets to support user input of 'all' """
MONTH_DATA = { 'january': [1],
              'february': [2],
              'march': [3],
              'april': [4],
              'may': [5],
              'june': [6],
              'all': [1, 2, 3, 4, 5, 6]}

""" Creates dictionary to map day of week entered to a numeric value to facilitate data filtering."""
DAY_DATA = {  'monday': [0],
              'tuesday': [1],
              'wednesday': [2],
              'thursday': [3],
              'friday': [4],
              'saturday': [5],
              'sunday': [6],
              'all': [0,1, 2, 3, 4, 5 ,6]}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_input = input("Input the name of the city you would like to analyze. Valid selections are Chicago, New York City, or Washington: ")
            """Converts input to lower case to enable case insensitive data entry."""
            if str(city_input.lower()) in CITY_DATA.keys():
                """Prints selection to user to provide immediate feedback to user."""
                print("You selected " + city_input.lower())
                break
            else:
                """ Provides instructions to user should input be invalid."""
                print("I'm sorry, we don't have data for that city. Please enter either chicago, new york city, or washington.")

        except ValueError:
            """ Provides instructions to user should input be invalid."""
            print("That is not a valid value. Please enter either chicago, new york city, or washington.")


    # TO DO: get user input for month (all, january, february, ... , june)
    """Defines variable month using month_data dictionary."""
    while True:
        try:
            month = input("Input the full name of the month you would like to analyze. If you would like to see every month, input 'all'. ")
            """Converts input to lower case to enable case insensitive data entry."""
            if str(month.lower()) in MONTH_DATA.keys():
                """Prints selection to user to provide immediate feedback to user."""
                print("You selected " + month)
                break
            else:
                """ Provides instructions to user should input be invalid."""
                print("I'm sorry, we don't have data for that month. Please enter january, february, march, april, may, june or all.")

        except ValueError:
            """ Provides instructions to user should input be invalid."""
            print("That is not a valid value. Please enter january, february, march, april, may, june, or all.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    """Defines variable day using day_data dictionary."""

    while True:
        try:
            day = input("Input the full name of the day of week you would like to analyze. If you would like to see every day, input 'all'. ")
            """Converts input to lower case to enable case insensitive data entry."""
            if str(day.lower()) in DAY_DATA.keys():
                """Prints selection to user to provide immediate feedback to user."""
                print("You selected " + day)
                break
            else:
                  """ Provides instructions to user should input be invalid."""
                  print("I'm sorry, we don't have data for that day. Please enter sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all.")

        except ValueError:
              """ Provides instructions to user should input be invalid."""
              print("That is not a valid value. Please enter sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all.")

    """Include print line to test code"""
    #print(city_input, month, day)
    """Changes input values to lower case."""
    city = city_input.lower()
    month = month.lower()
    day = day.lower()

    """Include print line to test code"""
    #print(city, month, day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    """Include print lines to test code"""
    #print(city, month, day)
    #print(CITY_DATA.keys())
    #print(CITY_DATA.values())
    #print(CITY_DATA.get(city))
    #print(MONTH_DATA.keys())
    #print(MONTH_DATA.get(month))
    #print(DAY_DATA.keys())
    #print(DAY_DATA.get(day))

    """Uses Pandas dataframes to import the csv file based on user input to calculate the desired statistics."""
    read_city = pd.read_csv(CITY_DATA.get(city))

    """Creates dataframe."""
    df = pd.DataFrame(read_city)
    #print(df.head())

    """Creates new dataframe that filters the original dataframe on the values input by the user."""
    filtered_df = df[(pd.DatetimeIndex(df['Start Time']).month.isin(MONTH_DATA.get(month))) & (pd.DatetimeIndex(df['Start Time']).dayofweek.isin(DAY_DATA.get(day)))]

    """Adds a city column to dataframe to filter on city to handle that washington does not have gender or birth year columns."""
    filtered_df = filtered_df.assign(City = city)

    """Include print line to test code"""
    #print(filtered_df.head())

   # Display dataframe
   # df
   # return df
    return filtered_df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """Extracts month from the Start Time column to create a month column."""
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()
    print('Most Frequent Start Month:', popular_month)


    # TO DO: display the most common day of week
    """Determines day of week from the Start Time column to create a day of week column."""
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    popular_dayofweek = df['dayofweek'].mode()
    print('Most Frequent Start Day of Week:', popular_dayofweek)

    # TO DO: display the most common start hour
    """Extracts hour from the Start Time column to create an hour column."""
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()
    print('Most Frequent Start Station:', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()
    print('Most Frequent End Station:', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    """Concatenates start and end stations to create a route column as a string. """
    df['route'] = df["Start Station"]+ " to " + df["End Station"].map(str)
    popular_route = df['route'].mode()
    print('Most Frequent Combination of start station and end station trip:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration in seconds."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is:', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The average travel time in seconds is:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    """Counts occurences for each value in the column."""
    user_types = df['User Type'].value_counts()
    print('The number of users by type is:', user_types)

    # TO DO: Display counts of gender
    """Determines if user input for city is washington to handle differently than chicago or new york city."""
    if df['City'].eq("washington").all():
            print ("We do not have gender data for washington.")
    else:
            """Counts occurences for each value in the column."""
            gender = df['Gender'].value_counts()
            print('The number of users by gender is:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    """Determines if user input for city is washington to handle differently than chicago or new your city."""
    if df['City'].eq("washington").all():
            print ("We do not have age data for washington.")
    else:
            """Converts Birth Year to integer when completing calculation."""
            oldest_user = df['Birth Year'].min().astype(int)
            youngest_user = df['Birth Year'].max().astype(int)
            most_common_age_user = df['Birth Year'].mean().astype(int)
            print('The oldest user was born in:', oldest_user)
            print('The youngest user was born in:', youngest_user)
            print('The most common year of birth is:', most_common_age_user)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #print('Would you')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            """Asks user to input whether or not to show data."""
            raw_data_request = input("Would you like to see 5 rows of raw data? Valid answers are yes or no. ")
            """Converts input to lower case to enable case insensitive data entry."""
            """Iterates through file as long as row number (index) is smaller than total number of rows in file and prints 5 rows at a time."""
            #print(raw_data_request)
            pd.set_option('display.max_columns',200)
            if raw_data_request.lower() == 'yes':
                """ Create iterator to go to through dataframe"""
                def track_row(x):
                    i = 0
                    while i < x:
                        yield i
                        i += 5
                """Define action when iterator is called, in this case, printing of data and asking user if they want to see more data."""
                for row_num in track_row(len(df)):
                    print(df.iloc[row_num:(row_num+5)])
                    more_raw_data = input('\nWould you like to see 5 more rows? Enter yes or no.\n')
                    if more_raw_data.lower() =='yes':
                        print(df.iloc[row_num:(row_num+5)])
                        row_num += 5
                            #show_more_values = list(display_raw(len(df)-1))
                            #print(show_more_values)
                    elif more_raw_data.lower() == 'no':
                        print("Thank you for using bikeshare.")
                        return
                    else:
                        """ Provides instructions to user should input be invalid."""
                        print("I'm sorry, that is an invalid. Please try again.")
                        return

            elif raw_data_request.lower() == 'no':
                print("Thank you for using bikeshare.")
                break
            else:
                """ Provides instructions to user should input be invalid."""
                print("I'm sorry, that is an invalid. Please enter either yes or no.")

        except ValueError:
            """ Provides instructions to user should input be invalid."""
            print("That is not a valid value. Please enter either yes or no.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
