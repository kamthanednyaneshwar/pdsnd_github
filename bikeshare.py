import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["january", "february", "march","april","may","june","july","august","september","october","november","december"]

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Test comment added - 1
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city data would you like to explore? Chicago, New York, or Washington? Enter "all" to explore data for all cities.\n').lower()
        if city == "":
            print("Please enter a city name or 'all'")
            continue
        elif city == "all":
            break
        elif city not in ["chicago", "new york", "washington"]:
            print("Invalid city name. Please enter either Chicago, New York, Washington or 'all'.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month data would you like to explore? Enter "all" to explore data for all months.\n').lower()
        if month == "":
            print("Please enter a month name or 'all'")
            continue
        elif month == "all":
            break
        elif month not in ["january", "february", "march","april","may","june","july","august","september","october","november","december"]:
            print("Invalid month name. Please enter again")
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day data would you like to explore? Enter "all" to explore data for all days.\n').lower()
        if day == "":
            print("Please enter a day or 'all'")
            continue
        elif day == "all":
            break
        elif day not in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
            print("Invalid day. Please enter again")
            continue
        else:
            break

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
    if city == 'all':
        df = pd.concat([pd.read_csv(CITY_DATA['chicago']),
                        pd.read_csv(CITY_DATA['new york']),
                        pd.read_csv(CITY_DATA['washington'])], sort=True)
    else:
        filename = CITY_DATA[city]
        df = pd.read_csv(filename)

     # Convert start time to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != "all":
        month_num = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month_num]

    # Filter by day of week if applicable
    if day != "all":
        day_num = days.index(day)
        df = df[df['Start Time'].dt.dayofweek == day_num]

    #print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    month_mode = df['month'].mode()[0]
    month_name = pd.date_range(start='1/1/2021', periods=12, freq='M').strftime('%B')[month_mode-1]
    print('Most Common Month:', month_name)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    day_mode = df['day_of_week'].mode()[0]
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day_mode]
    print('Most Common Day of Week:', day_name)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_mode = df['hour'].mode()[0]
    print('Most Common Start Hour:', hour_mode)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    start_time = time.time()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f'The most frequent combination of start station and end station trip is from {common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {} seconds".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("Counts of User Types:")
    print(user_types)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print("\nCounts of Gender:")
        print(gender_counts)
    else:
        print("\nGender data is not available for this city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth_year = int(df["Birth Year"].min())
        recent_birth_year = int(df["Birth Year"].max())
        common_birth_year = int(df["Birth Year"].mode()[0])
        print("\nEarliest Birth Year:", earliest_birth_year)
        print("Most Recent Birth Year:", recent_birth_year)
        print("Most Common Birth Year:", common_birth_year)
    else:
        print("\nBirth year data is not available for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Ask & displey if executer want to see 5 rows of data ."""

    start_time = time.time()

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == "yes":
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue to view another 5 rows of individual trip data ? Enter yes or no \n ").lower()
        if view_data != "yes":
            break



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
