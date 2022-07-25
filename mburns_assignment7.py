# author: Melanie Burns
# Due: July 21, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 6, but everything else is my own
import pytest


# oh no this doens't get the subsequence where you ignore some of the ones in between
def longestPalindromeSubsequence(str: str) -> str:
    # 1 make a table (nxn for each n character in str)
    LENGTH = len(str)
    memo_table = [[0] * LENGTH for _ in range(LENGTH)]
    longest = ""

    # the diagonal is *always* a palindrome
    for diagonal in range(LENGTH):
        memo_table[diagonal][diagonal] = True

    # right now the largest is one on the diagonal
    longest = str[0]
    max_length = 1
    for begin_marker in range(LENGTH - 1, -1, -1):
        for end_marker in range(begin_marker + 1, LENGTH):
            if str[begin_marker] == str[end_marker]:
                # see if it's in the table
                marker_distance = end_marker - begin_marker
                if marker_distance == 1 or memo_table[begin_marker + 1][end_marker - 1]:
                    memo_table[begin_marker][end_marker] = True
                    if max_length < marker_distance + 1:
                        max_length = marker_distance + 1  # for the off by one of the 0 start
                        longest = str[begin_marker:end_marker + 1] # this only does it in direct sequential .. not what we want
    return longest


# I played with a couple different wayof of doing the costs, and max together through forwards and backwards
# I finally got it somewhat working, but it wants to put everthing on a seperate line. You can see the cost table and everything though
def printNeatly(text: str, max: int) -> str:
    words = text.split(" ")
    NUM_WORDS = len(words)
    SPACE = 1
    cost_table = [[0] * NUM_WORDS for _ in range(NUM_WORDS)]
    finished = [0] * NUM_WORDS
    totals = [0] * NUM_WORDS

    # 1 populate the table
    for i, first_word in enumerate(words):
        cost_table[i][i] = max - len(first_word)
        for j, next_word in enumerate(words[i+1:], start=i+1):
            cost_table[i][j] = cost_table[i][j-1] - len(next_word)

    # 2 adjust to be the percentage
    for i in range(NUM_WORDS):
        for j in range(NUM_WORDS):
            if cost_table[i][j] < 0:
                # instead of a negative (it was too large) let's make it false
                cost_table[i][j] = False
            else:
                # I'm going to use the percentage of the line used as the
                cost_table[i][j] = (cost_table[i][j]/max)**2

    # 3 find the max percentages
    for i in range(NUM_WORDS-1, -1, -1):
        totals[i] = cost_table[i][NUM_WORDS-1]
        finished[i] = NUM_WORDS
        for j in range(NUM_WORDS-1, i, -1):
            if not cost_table[i][j-1]:
                continue
            if not totals[i] or totals[i] < totals[j] + cost_table[i][j-1]:
                totals[i] = totals[j] + cost_table[i][j - 1]
                finished[i] = j

    # 4. build the list
    curr_line = []
    lines = []
    result_index = 0
    for index in finished:
        for i in range(result_index, index):
            curr_line.append(words[i])
        lines.append(" ".join(curr_line))
        curr_line = []
        result_index = index

    return "\n".join(lines)


# so this is using a greedy algo, but it isn't optimal. We need to do something iwth tables to do this correctly
def printNeatlyGreedy(text: str, max: int) -> str:
    ## Write Your Code Here ##
    # break on spaces (keep punctuation as part of the word
    # greedy, we can grab the next word if we can fit it
    original = text.split(" ")
    formatted = []
    current_line = []
    current_char = 0

    for word in original:
        if current_char + len(word) < max:
            current_line.append(word)
            current_char += len(word) + 1  # for the space
        elif current_char + len(word) == max:
            current_line.append(word)
            current_char += len(word) + 1
            formatted.append(" ".join(word for word in current_line))
            current_line = []
            current_char = 0
        else:
            formatted.append(" ".join(word for word in current_line))
            current_line = []
            current_char = 0
            current_line.append(word)
            current_char += len(word)
    if current_line:
        formatted.append(" ".join(word for word in current_line))

    finished = "\n".join(line for line in formatted)
    print(finished)
    return finished


@pytest.mark.parametrize("target,expected", [
    ('character', 'carac'),
    ('racecar', 'racecar'),
    ("abcdefg", 'a')
])
def test_longestPalindromeSubsequence(target, expected):
    assert longestPalindromeSubsequence(target) == expected


@pytest.mark.parametrize("text,max,expected", [
    ('Dynamic programming is not that difficult.', 15, 'Dynamic\nprogramming\nis not that\ndifficult.'),
    # ('Algorithm is my favorite subject.', 16, "Algorithm is\nmy favorite\nsubject."),
])
def test_printNeatly(text, max, expected):
    assert printNeatly(text, max) == expected


if __name__ == '__main__':
    pytest.main()
