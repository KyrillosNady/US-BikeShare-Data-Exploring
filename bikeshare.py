import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("\nWhich city would you like to check out ?"
                  "New York City, Chicago or Washington ?\n")
        city = city.lower().strip()
        if city not in ('new york city', 'chicago' , 'washington') :
            print('sorry, your input is wrong. Please, Try again.\n')
            continue
        else :
            break

    # get user input for month (all, january, february, ... , june)
    while True :
        month = input('Would you prefer to look for a specific month ? '
                       'January, February, March, April, May, June '
                       'or you can type "all" if you don\'t have any preference.\n')
        month = month.lower().strip()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all') :
            print('sorry, your input is wrong. Please, Try again.\n')
            continue
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('Are you looking for a specific day ? '
                     'If so, please enter your specific day as follows: '
                     'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday '
                     'or you can type "all" if you don\'t have any preference.\n')
        day = day.lower().strip()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                         'saturday', 'sunday','all') :
            print('sorry, your input is wrong. Please, Try again.\n')
            continue
        else :
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day of week'] = df['Start Time'].dt.day_name()

    if month != 'all' :
        df= df[df['month'] == month.title()]

    if day != 'all' :
        df= df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month to travel is : ', common_month , '\n')

    # display the most common day of week
    common_day = df['day of week'].mode()[0]
    print('the most common day of the week to travel is : ', common_day, '\n')
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    common_hour = df['hour'].mode()[0]
    print('the most common start hour to travel is : ', common_hour, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('the most common used start station is : ', start_station , '\n')

    # display most commonly used end station
    End_station = df['End Station'].mode()[0]
    print('the most common used end station is : ', End_station , '\n')

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " : " + df["End Station"]
    print('the most frequent combination of start station and end station trip is', 
            df['combination'].mode()[0] , '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('the total travel time is : ', total_duration , '\n')

    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    print('the average travel time is : ', average_duration , '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the counts of user types is :\n', user_types, '\n')

    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    if city != 'washington' :
        gender = df['Gender'].value_counts()
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('the counts of each gender is :\n', gender ,'\n')
        print('the earliest year of birth is :\n ', earliest_birth, '\n')
        print('the most recent year of birth is :\n ', recent_birth, '\n')
        print('the most common year of birth is :\n ', common_birth, '\n')
    elif  city == 'washington' :
        print('sorry, Washington dataset doesn\'t include the gender or the birth year.')     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city) :
    df = pd.read_csv(CITY_DATA[city])
    start = 0
    raw_display = input('To take a look on the avaliable data , type (y) for yes or (n) to exit\n')
    while True :
        raw_display = raw_display.lower().strip()
        if raw_display not in ('y', 'n') :
            print('sorry, your input is wrong. please, Try again\n')
            continue
        elif raw_display == 'y' :
            print(df.iloc[start : start+5])
            start += 5
            raw_display = input('Do you want to check another 5 raws ? type (y) for yes or (n) to exit\n')
        elif raw_display == 'n' :
            print('Thank you')
            break
        
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
