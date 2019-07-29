# Opens SQL database chat.db and loads into panda
# Returns formated pandas dataframe
# Needs to open messages, handle, and chat?
# IN messages, replace handle with numbers from handle table. (ROWID, ID)

import sqlite3
import pandas as pd
import time
import datetime

path = "/Users/wyattaharrell/Desktop/chat.db"


def populate_frame(file): # IF handle is zero, it is sent from you
    conn = sqlite3.connect(file)
    frame =\
        pd.read_sql_query\
            ("select datetime(date + strftime('%s','2001-01-01'), 'unixepoch') as date_utc, * from message;", conn)
    handle = pd.read_sql_query("select ROWID, id from handle;", conn)
    frame = clean_null(frame)
    row = 0
    for message in frame["handle_id"]:  # changes handle id to phone number
        if message != 0:
            temp = handle.loc[handle['ROWID'] == message]
            temp = temp.to_dict('list')
            frame.iloc[row, frame.columns.get_loc('handle_id')] = temp['id'][0]
        row += 1
    row = 0
    frame['date'] = frame['date'].astype(object)
    for message in frame["date"]:  # puts date field into struct time format
        dateSent = message
        dateSent = dateSent // 1000000000
        dateSent += 978307200
        now = datetime.datetime.fromtimestamp(dateSent)
        # struct time format year, mon, mday, hour, min, sec, wday, yday, isdst
        frame.iloc[row, frame.columns.get_loc('date')] = time.struct_time(now.timetuple())
        row += 1
    frame = frame.query('is_corrupt == 0')  # Makes sure no messages are corrupt
    return frame


def clean_null(df):  # Removes Null text cells from DataFrame
    df = df.dropna(subset=['text'])
    return df


''' To use on_ date function: df is populated data frame. type is what division of time you want, with the value being
    the int that you are looking for valid options:
            - year(int): returns all messages from that year 
            - mon(int [1,12)) all messages within that month, where jan = 1
            - mday (int [1,31]) all messages from the month day, ie the 4th
            - hour(int[0,23]) where 0 is midnight
            - wday(int [0,6] weekdays where monday is 0
            - min(int[0,59] minutes. 
'''


def on_date(df, type, value):  # pass in dataframe, field: Returns all messages that are equal to the value.
    temp = pd.DataFrame()
    row = 0
    for message in df['date']:
        if type == 'year':  # By Year
            if message.tm_year == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        elif type == 'mon':  # By Month [1,12]
            if message.tm_mon == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        elif type == 'mday':  # By Month day [1,31]
            if message.tm_mday == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        elif type == 'hour':  # By Hour [0,23]
            if message.tm_hour == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        elif type == 'wday':  # By Weekday [0,6] Monday is 0
            if message.tm_wday == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        elif type == 'min':  # By minute [0,59]
            if message.tm_min == value:
                df.iloc[row, df.columns.get_loc('is_corrupt')] = 1
        row += 1
    return df.query('is_corrupt == 1')


def date_count(df):
    month = [0] * 12
    day = [0] * 7
    hour = [0] * 24

    for date in df['date']:
        month[date.tm_mon-1] += 1
        day[date.tm_wday-1] += 1
        hour[date.tm_hour] += 1
    return hour, day, month


def is_me(df):  # returns dateframe of text sent by you
    return df.query('is_from_me == 1')


def is_emote(df): # returns dataframe of emotes
    return df.query('is_emote == 1')


def find_convo(df, number):  # returns text conversation with number, where number includes the country code
    return df.query('handle_id == @number')


def is_groupchat(df, roomname=''):  # returns a specified group chat if roomname is available, else returns df with all
    # group chats.
    df = df.query('cache_roomname != NULL')
    if not roomname:
        return df.query('cache_roomname == @roomname')
    else:
        return df


#if __name__ == '__main__':
df = populate_frame(path)
df = clean_null(df)
    #df = on_date(df, 'wday', 1)
    #df = df[['text', 'handle_id', 'date']]
    #print(df)
print(date_count(df))

