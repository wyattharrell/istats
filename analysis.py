# Uses gather.py, finds max, min, and average characters
# Along with the mode of the phone numbers

import statistics as st
import gather


def find_count(s):                  # finds char count of each message passed in
    count = 0
    if len(s) > count:
        count = len(s) - 1
    return count


def max_char(df):                    # prints max character count
    print("The max number of characters found in a text: " + str(max(df)) + " characters")
    print()


def min_char(df):                    # prints min character count
    print("The min number of characters found in a text: " + str(min(df)) + " characters")
    print()


def avg(df):                         # prints average char count
    num = st.mean(df)
    num = format(num, '.2f')         # 2 decimal places
    print("Average character count for messages sent by you: " + str(num) + " characters")
    print()


def common_txt():                    # mode of the phone numbers
    phone = st.mode(gather.df['handle_id'])
    print("You most commonly text: " + str(phone))
    print()


if __name__ == '__main__':
    count_df = gather.df
    count_df = count_df['text'].apply(find_count)       # new df of char counts
    print(count_df)
    print("Statistics on messages from you:")
    max_char(count_df)
    min_char(count_df)
    avg(count_df)
    common_txt()
