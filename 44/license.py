import string
import random

def gen_key(parts=4, chars_per_part=8):
    sections = []
    out = ''
    for _ in range(parts):
        sections.append(part_gen(chars_per_part))
    print('-'.join(sections))
    return '-'.join(sections)

def part_gen(length = 8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == '__main__':
    gen_key()
