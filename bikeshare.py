import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_data = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}

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
    while True :
        try :
            city=str(input('enter the city (chicago, new york city, washington)	')).lower()
            if city not in CITY_DATA.keys() :
                raise Exception("Sorry, the city name must be correct")
            month=str(input('enter the month ( january, february, ... , june) ')).lower()
            if month not in month_data.keys():
                raise Exception("Sorry, the month name must be correct")
            day =str(input(' enter the day of week (all, monday, tuesday, ... sunday) '))
            break
        except Exception:
            print('Sorry, the city and the month name must be correct')
            
    return city, month, day
            
           
        
    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    #print('-'*40)
    #return city, month, day
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
    
    
    while True :
        try :
            
            
            
            a1=input('if you need to filter the data by the city only enter yes if not enter no:   ')
            if a1.title()== 'Yes':
                df = pd.read_csv(CITY_DATA[str(city)])
                break
            a2=input('if u want to filter  the data by the city and the month enter yes if not enter no:  ')
            
            if a2.title()=='Yes' :
                
                df = pd.read_csv(CITY_DATA[str(city)])
                df['month'] = pd.DatetimeIndex(df['Start Time']).month
                df = df[df['month'] == month_data[str(month)]]
                break
            print('filtering the data by city and month and  the day')
            if a1.title()!= 'Yes' and a2.title()!='Yes':
                                
                df = pd.read_csv(CITY_DATA[str(city)])
                df['month'] = pd.DatetimeIndex(df['Start Time']).month
                
                df = df[df['month'] == month_data[str(month)]]
                df['Start Time'] = pd.to_datetime(df['Start Time'])
                df['day_of_week'] = df['Start Time'].dt.weekday_name
                df = df[df['day_of_week'] == day.title()]
                break
            
             
              
                  
        except():
                  print('please try again')
        #df = df[df['month'] == month_data[str(month)]]
        #df = df[df['day_of_week'] == day.title()]
        
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
                
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour']= df['Start Time'].dt.hour
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].value_counts().idxmax()

    # TO DO: display the most common day of week
    popular_day =df['day_of_week'].value_counts().idxmax()

    # TO DO: display the most common start hour
    popular_day=df['hour'].value_counts().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_Start_Station =df['Start Station'].value_counts().idxmax()
    print(f"The most commonly used start station: {popular_Start_Station}")

    # TO DO: display most commonly used end station
    popular_End_Station =df['End Station'].value_counts().idxmax()
    print(f"The most commonly used end station: {popular_End_Station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    Popular_Start_end_station= df['Start To End'].value_counts().idxmax()
    print(f"The most commonly used stat-end station: {Popular_Start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =df['Trip Duration'].sum()
    print(f'the total travel time {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    
    print(f'the maen travel time {mean_travel_time}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    # TO DO: Display counts of gender
    try:
        
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
        
    except:
        print("\nThere is no 'Gender' column in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    #because the dataset washington not have columns called Year
    #while  city !='washington' :
    try:
        df['Birth Year']=df['Birth Year'].dropna().astype(np.int)
        earliest=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].value_counts().idxmax()
    except:
        print("\nThere is no 'Birth Year' column in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def desplay_data(df) :
	#Display the data if the user want 
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data== 'yes' :
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_data = input("Do you wish to continue?: ").lower()
    print('thank you')
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        desplay_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
