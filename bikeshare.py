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
    print('---------------------------------------------\n \n  --------- WELCOME TO BIKESHARE ---------\n')
    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('---------------------------------------------')
    while True:
        #creating a list of cities
        cities_ = ['chicago','new york city','washington']
        
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('1. Enter the city of your choice(HINT: chicago, new york city, washington): ').lower()
        if city in cities_:
               break 
        else:      
            print('\nThe input you entered is not recognized (Please follow the HINT)\n')
   
    while True:
        #creating a list of months
        months_ = ['january','february','march','april','may','june','all']
         
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('2. Enter the month of your choice(HINT:all, january, february, ... , june): ').lower()
        if month in months_:
            break    
        else:       
            print('\nThe input you entered is not recognized (Please follow the HINT)\n')
    while True:
        #creating a list of days
        days_ = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('3. Enter the day of your choice(HINT:all, monday, tuesday, ... sunday): ').lower()
        if day in days_:
            break
        else:       
            print('\nThe input you entered is not recognized (Please follow the HINT)\n')

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
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):                    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('The most common month is: ', months[df['month'].mode()[0] - 1])

    # TO DO: display the most common day of week
    print('The most common day of the week is: ', df['day_of_week'].mode()[0])

    ## extract hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common start hour
    print('The most common start hour is:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):         
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common used start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most common used end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: |--START STATION--|', (df['Start Station'] + ' |--END STATION--|' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Finding the total trip duration
    total_travel = df['Trip Duration'].sum()

    #Finding the travel time in minutes and seconds format
    minutes_,seconds_= divmod(total_travel,60)

    #Finding the travel time in hours and minutes
    hours_,minutes_ = divmod(minutes_,60)

    # TO DO: display total travel time
    print('The total travel time is: {} hours {} minutes {} seconds'.format(hours_,minutes_,seconds_))

    #Finding the mean trip duration
    mean_travel = df['Trip Duration'].mean()

    #Finding the travel time in minutes and seconds format
    minutes_m,seconds_m = divmod(mean_travel,60) 

    #Finding the travel time in hours and minutes format
    hours_m,minutes_m = divmod(minutes_m,60)

    # TO DO: display mean travel time
    print('The mean of the travel time is: {} hours {} minutes {} seconds'.format(hours_m,minutes_m,seconds_m))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):                                        
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types is:\n',user_types)
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender_ = df['Gender'].value_counts()
        print('The counts of gender is:\n',gender_)

        # TO DO: Display earliest year of birth
        early_birth = df['Birth Year'].min()
        print('Earliest year of birth is:',early_birth)

        # Display most recent year of birth
        most_recent = df['Birth Year'].max()
        print('Most recent year of birth is:',most_recent)

        # Display most common year of birth
        most_common = df['Birth Year'].mode()[0]
        print('Most common year of birth is:',most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def display_info(df):                                   
    """ A function to display information of an individual trip."""
    while True:
        print('--------HELLO USER, GET READY TO VIEW OUR INDIVIDUAL\'S TRIP INFORMATION--------\n')
        print('-'*80)
        #creating a list of answers
        answer_=['yes','no']
        #accepting user input
        action_1= input("Do you want to display atleast 5 entries of our individual trip information? (HINT:Type 'yes' or 'no'): ").lower()
        #Condition to locate the information to be displayed
        if action_1 in answer_:
            if action_1=='yes':
                start=0
                end=5
                info_ = df.iloc[start:end,:9]
                print(info_)
            break     
        else:
            print("The input you entered is not valid(Please follow the HINT)")
    if  action_1=='yes':       
            while True:
                #accepting user input
                action_2= input("Do you want to display more individual trip information? (HINT: Type 'yes' or 'no'): ").lower()
                #condition to locate more information to be displayed
                if action_2 in answer_:
                    if action_2=='yes':
                        start+=5
                        end+=5
                        info_ = df.iloc[start:end,:9]
                        print(info_)
                    else:    
                        break  
                else:
                    print("The input you entered is not valid(Please follow the HINT)")      


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_info(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
