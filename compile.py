# Compile a .dotrun file to interpretable format
#
# -------- Example ---------
# Input string: "print (hello world)\nprint hey there"
# Output: [[print, [hello, world]], [print, hey, there]]
# 1:= 
# 

space_bounds = [
    ['(', ')'],
    ['\"', '\"'],
]
def compile(f: str) -> list:
    spaces = get_spaces(f)

def get_spaces(f: str, exit_on: str = ''):
    spaces = []
    pointer = 0
    while pointer < len(f):
        if f[pointer] == exit_on:
            return spaces, pointer
        if f[pointer] == "(":
            space, length = get_spaces(f[pointer + 1:], ")")
            spaces.append(space)
            pointer += length + 2
        if pointer >= len(f):
            return spaces, pointer
        if len(spaces) > 0 and isinstance(spaces[len(spaces) - 1], str):
            spaces[len(spaces) - 1] += f[pointer]
        else:
            spaces.append(f[pointer])
        pointer += 1


    return spaces, pointer

print(get_spaces('print (hello world) (oh yeah)')[0])

def get_std():
    return 'print:= fn (in:="") (mem:0:= in)'
    # return 'Clamydia'