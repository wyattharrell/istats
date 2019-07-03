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
    return max(df)


def min_char(df):                    # prints min character count
    return min(df)


def avg(df):                         # prints average char count
    num = st.mean(df)
    num = format(num, '.2f')         # 2 decimal places
    return num


def common_txt():                    # mode of the phone numbers
    phone = st.mode(gather.df['handle_id'])
    return phone


if __name__ == '__main__':
    count_df = gather.df
    count_df = count_df['text'].apply(find_count)       # new df of char counts
    print(count_df)
    print("Statistics on messages from you:")
    print()
    print("Max char count: " + str(max_char(count_df)) + " characters")
    print("Min char count: " + str(min_char(count_df)) + " characters")
    print("Avg. char count: " + str(avg(count_df)) + " characters")
    print("You most commonly text: " + str(common_txt()))
