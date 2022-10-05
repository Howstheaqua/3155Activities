# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  threes = {}
  for char in n:
    if int(char)%3==0:
      if char in threes:
        threes[char] += 1
      else:
        threes[char] = 1
    else:
      pass
  return int(max(threes, key=threes.get))


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  dictionary = {}
  currentCount = 0
  latestchar = ''

  for char in s:
      if char == latestchar:
          currentCount += 1
          if char in dictionary:
              if currentCount > dictionary[char]:
                  dictionary[char]=currentCount
      else:
          currentCount = 1
          dictionary.update({char: currentCount})
          latestchar = char
  maxvalue = dictionary[max(dictionary, key=dictionary.get)]
  listofmax = []
  for k,v in dictionary.items():
    if v == maxvalue:
      listofmax.append(k)
  return listofmax


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  return s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")
