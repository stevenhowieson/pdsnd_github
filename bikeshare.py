import time
import pandas as pd
import numpy as np
import pdb

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    acceptable_cities = ["washington","new york city","chicago"]

    while True:
        try:
            city = input('Would you like to see data for Chicago,Washington or New York City?').lower()
            if city in acceptable_cities:
                break
        except:
            print('That is not a valid city')
        
    print(city)
    # TO DO: get user input for month (all, january, february, ... , june)
    acceptable_months = ["all","january", "february", "march", "april", "may", "june"]
    
    while True:
        try:
            month = input('Which month would you like to filter by?January to June.').lower()
            if month in acceptable_months:
                break
        except:
            print('That is not a valid month')
        
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    acceptable_days = ["all","monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]
    
    while True:
        try:
            day = input('Which day would you like to filter by?').lower()
            if day in acceptable_days:
                break
        except:
            print('That is not a valid day')
        
    print(day)

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
    #pdb.set_trace()
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month was {}".format(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("The most popular month was {}".format(popular_month))
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour was {}".format(popular_hour))
          
    print("\nThis took {}s seconds.".format( time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most popular start station was {}".format(start_station))
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most popular end station was {}".format(end_station))
    # TO DO: display most frequent combination of start station and end station trip
    #pdb.set_trace()
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Route'].mode()[0]
    print("The most popular trip was {}".format(most_common_trip))
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #pdb.set_trace()
    Total_travel_time = df['Trip Duration'].sum()
    print("The total travel time was {}".format(Total_travel_time))

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time was {}".format(Mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    #pdb.set_trace()
    # TO DO: Display counts of gender
     
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no data available for gender')
  
       
        
            

    # TO DO: Display earliest, most recent, and most common year of birt
   
    if 'Birth Year' in df.columns: 
        earliest_dob = df['Birth Year'].min()
        latest_dob = df['Birth Year'].max()
        popular_dob = df['Birth Year'].mode()[0]
        print('The earliest birth year is {}'.format(earliest_dob)) 
        print('The most recent birth year is {}'.format(latest_dob))
        print('most common birth year is {}'.format(popular_dob))
    else:
        print('There is no data available for birth year')           
     
            
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #pdb.set_trace()
def raw_data(df):
    """Ask user if they want to see the  5 rows of the table at a time
    Returns:
    -5 consecutive rows """
    def iterate_rows(iterable):
                for i in range(0, len(iterable),5):
                    yield df.iloc[i:i+5]
                
    row_iterator = iterate_rows(df)

    while True:
        raw_data = input('\nWould you like to see raw data?Enter yes or no.')
        if raw_data.lower() == 'yes':
            print(next(row_iterator))
        elif raw_data.lower() == 'no':
            print("Exiting the loop.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()