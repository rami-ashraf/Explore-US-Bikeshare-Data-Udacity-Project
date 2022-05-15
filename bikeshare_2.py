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
    city =''
    city=str(input("Please type one of this cities (chicago, new york city, washington):").lower())

    # make a while loop to check if the user meets the right cities 
    while not(city == 'chicago' or city =='new york city' or city =='washington') :
        city=str(input("Please make sure you chooce one of this cities (chicago, new york city, washington):").lower())


    # get user input for month (all, january, february, ... , june)
    month=''
    # make a user input for month
    month=str(input("Please type the month you want to check (january , february , march , april , may , june ) \n or type ( all ) to include all months :").lower())

    # make a while loop to check if the user meets the right month 
    while not(month == 'january' or month =='february' or month =='march'or month =='april'or month =='may'or month =='june' or month =='all') :
        month=str(input("Please make sure you chooce the month you want to check (january , february , march , april , may , june ) \n or type ( all ) to include all months :").lower())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    day=str(input("Please type the day you want (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) \n or type ( all ) to include all the week :").lower())

    # make a while loop to check if the user meets the right day
    while not(day == 'monday' or day =='tuesday' or day =='wednesday'or day =='thursday'or day =='friday'or day =='saturday'or day =='sunday' or day =='all') :
        day=str(input("Please make sure you type the day you want (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) \n or type ( all ) to include all the week :").lower())

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_moth=df['month'].mode()[0]
    print('the most common month:' ,most_common_moth)
    print()
    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('Most common day:', most_common_day)
    print()
    # display the most common start hour:
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station=df['Start Station'].mode()[0]
    print('Most commonly used Start Station :',most_used_start_station)
    print()
    # display most commonly used end station
    most_used_start_station=df['End Station'].mode()[0]
    print('Most commonly used End Station :',most_used_start_station)
    print()
    # display most frequent combination of start station and end station trip
    df['Combinat Start & End Station']= 'Start Station : '+df['Start Station']+'       End Station : ' + df['End Station']
    most_frequent_combination=df['Combinat Start & End Station'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station trip:\n',most_frequent_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tota_trip_time=df['Trip Duration'].sum()
    print('Total Travel Time is {} seconds'.format(tota_trip_time))
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\nThe Average Travel Time is {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df:
        user_types = df['User Type'].value_counts()
        print('The Count of each User Type:\n',user_types)
    else:
        print('there is no user type in this city')
    # Display counts of gender
    if 'Gender' in df:
        genders=df['Gender'].value_counts()
        print('\nThe Count of each Gender:\n',genders)
    else:
        print('there is no gender in this city')
    # Display earliest, most recent, and most common year of birth
    # Find the Oldest User:
    if 'Birth Year' in df:
        the_oldest=int(df['Birth Year'].min())
        #finding the youngest user:
        the_youngest=int(df['Birth Year'].max())
        #find the most comment year (mode) of users :
        the_comment_year=int(df['Birth Year'].mode()[0])
        print('\nThe oldest user birth year is {} \nthe youngest user birth year is {} \nThe most comment birth year of users is {}'.format(the_oldest ,the_youngest,the_comment_year))
    else:
        print('there is no Birth year in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Display data for the data frame if the user
    wish for that 

    Disaplaying 5 lines of data in each turn 
    """
    ''' Your script should prompt the user if they want to see 5 lines of raw data,

    Display that data if the answer is 'yes',

    Continue iterating these prompts and displaying the next 5 lines
    of raw data at each iteration,

    Stop the program when the user says 'no' or there is no more raw data to display.'''
    
    

    # count the number of rows in the data frame
    count_of_rows= df.shape[0]-1

    #user input to check if he wish to see 5 rows of data:
    check_input=str(input('Do you wish to display 5 rows of the main data (yes or no): ').lower())
    #make sure that user type only yes or no :
    while check_input!='yes':
        check_input=str(input("Please make sure that you right (yes) or (no)\n Do you wish to display 5 rows of the main data (yes or no):").lower())

    # n represent the number of the growing row in the data
    n=0
    
       
        #check that the user not exceed the number of rows in the data frame
    while n < count_of_rows :

        if check_input=='yes':
            if n==0 :
                n+=5
                data_displayed=df.iloc[:n, -n:]
                n+=5
                print(data_displayed)
                check_input=str(input('Do you wish to display 5 more rows of the main data (yes or no): ').lower())
                while not(check_input=='yes' or check_input=='no'):
                    check_input=str(input("Please make sure that you right (yes) or (no)\n Do you wish to display 5 more rows of the main data (yes or no):").lower())
            else:
                data_displayed=df.iloc[n-5:n, -n:n-5]
                n+=5
                print(data_displayed)
                check_input=str(input('Do you wish to display 5 more rows of the main data (yes or no): ').lower())                
                while not(check_input=='yes' or check_input=='no'):
                    check_input=str(input("Please make sure that you right (yes) or (no)\n Do you wish to display 5 more rows of the main data (yes or no):").lower())
        else:
            n=0
            break
    
        #continue 
        #check_input=str(input('Do you wish to display 5 more rows of the main data (yes or no): ').lower())
     






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
