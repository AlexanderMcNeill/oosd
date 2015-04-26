__author__ = 'alexmcneill'


#Factorial method
factorial = lambda input: reduce(lambda x, y: x + y, range(input + 1))  #input + 1 ensures that it includes the input

print("Factorial result: " + str(factorial(2)))

#Remove char from string method
remove_char = lambda input_char, input_string: filter(lambda c: c != input_char, input_string)

print("Remove character result: " + str(remove_char('c', 'call me captain')))

#Count char in string method
count_char = lambda input_char, input_string: len(filter(lambda c: c == input_char, input_string))

print("Count character result: " + str(count_char('h',"who the hell are you")))

#Number of words that start with char method
count_words_starting_char = lambda c, s: len(filter(lambda word: word.startswith(c), s.split(" ")))

print(count_words_starting_char('c', 'cancel the meeting'))

#Method that to uppers characters that match the input character
to_upper_char = lambda c, s: "".join(map(lambda x: x.upper() if x == c else x, s))

print(to_upper_char('c', 'cancel the meeting'))

#Map method using a loop
def my_map(f, input_list):
    output = []

    for i in range(0, len(input_list)):
        output.append(f(input_list[i]))

    return output

#Need to add map method that uses recursion

