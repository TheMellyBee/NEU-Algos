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
    for begin_marker in range(LENGTH -1, -1, -1):
        for end_marker in range(begin_marker + 1, LENGTH):
            if str[begin_marker] == str[end_marker]:
                # see if it's in the table
                marker_distance = end_marker - begin_marker
                if marker_distance == 1 or memo_table[begin_marker+1][end_marker-1]:
                    memo_table[begin_marker][end_marker] = True
                    if max_length < marker_distance + 1:
                        max_length = marker_distance + 1  # for the off by one of the 0 start
                        longest = str[begin_marker:end_marker + 1]
    return longest


# so this is using a greedy algo, but it isn't optimal. We need to do something iwth tables to do this correctly
def printNeatly(text: str, max: int) -> str:
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
            current_char += len(word) + 1 # for the space
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
    ('Dynamic programming is not that difficult', 15, 'Dynamic\nprogramming\nis not that\ndifficult.'),
    #('Algorithm is my favorite subject.', 16, "Algorithm is\nmy favorite\nsubject."),
])
def test_printNeatly(text, max, expected):
    assert printNeatly(text, max) == expected


if __name__ == '__main__':
    pytest.main()
