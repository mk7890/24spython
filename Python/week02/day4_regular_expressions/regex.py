# Regular Expressions are used for matching patterns -> regex
# moducle -> re

# BASIC REGEX patterns.
"""  
    ^  matches the beginning of a line or string
    $  matches the end of the line or string
    .   matches any character except newline
    \s  matches any whitespace (tab, newline, return, space) // \t  \n  \r  \f
    \S  matches any non-whitespace character
    +   repeats a character zero or more times
    +?  repeats a character zero or more times (non-greedy)
    *   repeats a character zero or more times
    *?  repeats a character zero or more times (non-greedy)
    [aeiou] matches a single character in the listed set
    [^XYZ]  matches a single character not in the listed set
    [a-z0-9] the set of characters can inlude a range
    (   indicates where string extraction is to start
    )   indicates where string extraction is to end
    \d  matches any digital character  (0-9)
    \w  matches any word character (a-z, A-Z, 0-9, _)
    \b  boundary between a word and non-word (@....)

    []  matches a set of characters e.g a,b,c = abc
    \   to match
"""