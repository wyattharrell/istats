# Uses gather.py, finds max, min, and average characters
# Along with the mode of the phone numbers
import statistics as st
import emojis
import gather


class Elements:
    def __init__(self, value, counter, precedence):     # values if the char/word, counter is how many found
        self.value = value                          # so far, precedence's the order that that letter/word first came in
        self.counter = counter
        self.__precedence = precedence

    def __lt__(self, other):                # less then, checks precedence and count if count is equal
        if self.counter == other.counter:
            if self.__precedence < other.__precedence:
                return False
            else:
                return True

        if self.counter < other.counter:
            return True

        return False

    def __gt__(self, other):                # greater than operator
        if self.counter == other.counter:
            if self.__precedence > other.__precedence:
                return False
            else:
                return True

        if self.counter > other.counter:
            return True
        return False

    def __repr__(self):
        return "({self.counter})".format(self=self)

    def __str__(self):              # returns string as value counter precedence
        return "{}\t{}".format(self.value, self.counter)

    def increment(self):            # increase counter
        self.counter += 1


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


''' Containers for words, characters and their top 10s '''
letters = {}                    # dictionary to store 'element' objects
words = {}
emojies = {}
top10_letters = []              # only store 10 values at a time
top10_words = []
top10_emojies = []


def count_words(w, itr):
    if w in words:
        words[w].increment()
    else:
        itr += 1
        words[w] = Elements(w, 1, itr)

    isin = False
    for j in range(0, len(top10_words)):  # check all the top 10 so far to change the counter
        if top10_words[j].value == w:
            top10_words[j].counter = words[w].counter
            isin = True

    if len(top10_words) < 10 and isin is False:
        top10_words.append(words[w])
    elif words[w].counter >= top10_words[-1].counter and isin is False:
        # if current 'w' is now greater then or equal to the lowest element add it to the list
        top10_words.append(words[w])
        top10_words.sort(reverse=True)  # sort the list to put it in its correct place
        top10_words.pop()  # pop one element off to keep at 10 total elements
        isin = True

    top10_words.sort(reverse=True)

    if len(top10_words) > 10:
        top10_words.pop()


def count_letters(chars, itr):
    for c in chars:
        if c in letters:  # here we add or increment the operator
            letters[c].increment()
        else:
            itr += 1
            letters[c] = Elements(c, 1, itr)

        isin = False
        for j in range(0, len(top10_letters)):  # cheak all the top 10 so far to change the counter
            if top10_letters[j].value == c:
                top10_letters[j].counter = letters[c].counter
                isin = True

        if len(top10_letters) < 10 and isin is False:
            top10_letters.append(letters[c])
        elif letters[c].counter >= top10_letters[-1].counter and isin is False:
            # if current 'char' is now greater then or equal to the lowest element add it to the list
            top10_letters.append(letters[c])
            top10_letters.sort(reverse=True)  # sort the list to put it in its correct place
            top10_letters.pop()  # pop one element off to keep at 10 total elements
            isin = True

        top10_letters.sort(reverse=True)

        if len(top10_letters) > 10:
            top10_letters.pop()


def get_emojis(s, itr):
    emoji_list = s[:]
    emoji_list = emojis.get(s)                  # set of emojies in this string
    emoji_list = list(emoji_list)               # list of that set

    if len(emoji_list) > 0:

        for element in emoji_list:
            if element in emojies:
                emojies[element].increment()
            else:
                itr += 1
                emojies[element] = Elements(element, 1, itr)

            isin = False
            for j in range(0, len(top10_emojies)):  # check all the top 10 so far to change the counter
                if top10_emojies[j].value == element:
                    top10_emojies[j].counter = emojies[element].counter
                    isin = True

            if len(top10_emojies) < 10 and isin is False:
                top10_emojies.append(emojies[element])
            elif emojies[element].counter >= top10_emojies[-1].counter and isin is False:
                # if current 'w' is now greater then or equal to the lowest element add it to the list
                top10_emojies.append(emojies[element])
                top10_emojies.sort(reverse=True)  # sort the list to put it in its correct place
                top10_emojies.pop()  # pop one element off to keep at 10 total elements
                isin = True

            top10_emojies.sort(reverse=True)

            if len(top10_emojies) > 10:
                top10_emojies.pop()


def get_entire_emoji_list():
    retEmoji = []
    retCounter = []
    for i in emojies:
        retEmoji.append(emojies[i].value)
        retCounter.append(emojies[i].counter)
    return retEmoji, retCounter


def make_separate(lst):
    strings = []
    counts = []
    for i in range(len(lst)):
        strings.append(lst[i].value)
        counts.append(lst[i].counter)

    return strings, counts


def get_letters_and_words(lst):
    itr = 0  # iterator for the precedence value
    for i in range(0, 5):    # iterate through every line of the test file of nd-array
        # at that index
        messages = lst.split()   # creates a list of separate words

        for w in messages:
            w = w.lower()
            if not ((w[-1] >= 'A' and w[-1] <= 'Z') or (w[-1] >= 'a' and w[-1] <= 'z')):    # catch punctuation
                w = w[:-1]
            count_words(w, itr)

            chars = list(w)
            count_letters(chars, itr)

            get_emojis(w, itr)


def get_input():                     # users enters word or phrase they want to find
    user_str = input("Enter a word or phrase you would like to find: ")
    return user_str


def find_msg(s):                     # return the message if the word or phrase found in message
    if input_phrase in s:
        return s
    else:
        return ' '


def get_word(s):                     # returns the number of times a word/char appears or a message that is it not used
    s = s.lower()
    if s in words:
        return words[s].counter
    elif s in letters:
        return letters[s].counter
    else:
        return "Word no found"
    
    
def date_df(day, value):
    df = gather.populate_frame(gather.path)
    df = gather.clean_null(df)
    df = gather.on_date(df, day, value)
    df = df[['text', 'handle_id', 'date']]
    return len(df)


def get_days_of_week():
    ret = []
    for i in range(7):
        ret.append(date_df('wday', i))
    return ret


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

    gather.df['text'].apply(get_letters_and_words)

    val, coun = get_entire_emoji_list()
    print(val)
    print(coun)

    print("About to print to 10 characters")
    for i in range(0, len(top10_letters)):
        print(str(i+1) + ": " + str(top10_letters[i]))

    print("About to print 10 emojies")
    for i in range(0, len(top10_emojies)):
        print(str(i + 1) + ": " + str(top10_emojies[i]))

    print("About to print 10 words")
    for i in range(0, len(top10_words)):
        print(str(i+1) + ": " + str(top10_words[i]))

    p = date_df('wday', 1)

    print(p)
    p = get_days_of_week()
    print(p)


    p1, p2 = make_separate(top10_words)

    print(p1)
    print(p2)

    print("Getting a specific word")
    print(get_word(get_input()))
    print("Printing dict of words")

    input_phrase = get_input()
    msg_df = gather.df
    msg_df['text'] = msg_df['text'].apply(find_msg)                 # new df of messages containing user's input
    print()
    print("Messages with your specified word or phrase:")
    print(msg_df.loc[msg_df['text'] != ' '])                        # prints only the found messages

