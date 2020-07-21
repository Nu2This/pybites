INDENTS = 4
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    inn = []
    out = []
    previous = None
    for item in poem.split('\n'):
        inn.append(item)
    l = len(inn)
    for index, obj in enumerate(inn):
        if index > 0:
            previous = inn[index - 1]
        if index < (l - 1):
            next_ = inn[index + 1]
        if previous == None:
            pass
        else:
            if previous == '':
                out.append(obj.strip())
            else:
                if obj != '':
                    out.append(INDENTS * ' ' + obj.strip())




      #  if previous == '':
      #      next_ = next_.strip()
      #      out.append(obj.strip())
      #      out.append((INDENTS * ' ') + next_)
      #  else:
      #      out.append((INDENTS * ' ') + obj.strip())
    for line in out:
        print(line)










if __name__ == '__main__':
    print_hanging_indents(rosetti_unformatted)
