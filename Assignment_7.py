#1. What is the name of the feature responsible for generating Regex objects?
 The re. compile() function returns Regex objects.
#2. Why do raw strings often appear in Regex objects?
 Backslashes do not have to be escaped. 
#3. What is the return value of the search() method?
re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the
 matching part of the string.
#4. From a Match item, how do you get the actual strings that match the pattern?
The group() method returns strings of the matched text.
#5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.
#6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
Periods and parentheses can be escaped with a backslash: \., \(, and \).
#7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.
#8. In standard expressions, what does the | character mean?
Define "either, or" between two groups.
#9. In regular expressions, what does the character stand for?
 mean "match zero or one of the preceding group" or be used to signify nongreedy matching.
#10.In regular expressions, what is the difference between the + and * characters?
The + matches one or more. The * matches zero or more.
#11. What is the difference between {4} and {4,5} in regular expression?
#12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?
It matches any single digit (same as [0-9] ).
word character) matches any single letter, number or underscore (same as [a-zA-Z0-9_] )
 “whitespace character”. Again, which characters this actually includes,
#13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
It match a single character that is not a digit, word, or space character, respectively.
#14. What is the difference between .*? and .*?
It is the difference between greedy and non-greedy quantifiers. .*? is non-greedy & * is greedy.
#15. What is the syntax for matching both numbers and lowercase letters with a character class?
the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
#16. What is the procedure for making a normal expression in regax case insensitive?
#17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
re.IGNORECASE : This flag allows for case-insensitive matching of the Regular Expression with the given string 
i.e. expressions like [A-Z] will match lowercase letters, too. Generally, It’s passed as an optional argument to re.compile().
#18. If numReg = re.compile(r'\d+'), what will numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
X drummers, X pipers, five rings, X hen
#19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
To ignore whitespace and comments inside the regular expression string.
# 20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
#'42'
#'1,234'
#'6,368,745'
#but not the following:
#'12,34,567' (which has only two digits between the commas)
#'1234' (which lacks commas)
numCommas = re.compile(r'(^\d{1,3})(,\d{3})*$') numCommas.search('12,34,567').group()

#21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
#'Haruto Watanabe'
#'Alice Watanabe'
#'RoboCop Watanabe'
#but not the following:
#'haruto Watanabe' (where the first name is not capitalized)
#'Mr. Watanabe' (where the preceding word has a nonletter character)
#'Watanabe' (which has no first name)
#'Haruto watanabe' (where Watanabe is not capitalized)
fullName = re.compile(r'[A-Z]\w [A-Z]\w') 
mo = fullName.findall('Satoshi Nakamoto, satoshi Nakamoto, Alice Nakamoto, Nakamoto, Satoshi nakamoto, Robocop Nakamoto') mo.group()

#22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
#'Alice eats apples.'
#'Bob pets cats.'
#'Carol throws baseballs.'
#'Alice throws Apples.'
#'BOB EATS CATS.'
#but not the following:
#'RoboCop eats apples.'
#'ALICE THROWS FOOTBALLS.'
#'Carol eats 7 cats.'
senRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.I|re.DOTALL)
senRegex.findall('''Alice eats apples.''Bob pets cats.''Carol throws baseballs.''Alice throws Apples.''BOB EATS CATS.'
but not the following:
'Robocop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.''')
Test result: [('Alice', 'eats', 'apples'), ('Bob', 'pets', 'cats'), ('Carol', 'throws', 'baseballs'), 
('Alice', 'throws', 'Apples'), ('BOB', 'EATS', 'CATS')]