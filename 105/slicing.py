from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

another_text = """Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""

def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    lines = text.split('\n')
    for item in lines:
        piss=item.lstrip()
        if item == '':
            pass
        elif piss[0].islower():
            split = item.split(' ')
            for elem in split[-1:]:
                print(elem)
                if elem[-1:] == '.':
                    results.append(elem.rstrip('.'))
                elif elem[-1:] == '!':
                    results.append(elem.rstrip('!'))
                else:
                    results.append(elem)
    return results

if __name__ == '__main__':
    #slice_and_dice(text)
    slice_and_dice(another_text)
