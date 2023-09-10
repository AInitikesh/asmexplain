from enum import Enum

class Instruction(Enum):
    LDR = "ldr"
    STI = "sti"

class Size(Enum):
    BYTE = 'b'
    HALF_WORD = 'h'
    WORD = 'w'
    SIGNED_BYTE = 'sb'
    SIGNED_HALF_WORD = 'sh'
    SIGNED_WORD = 'sw'
    DOUBLE_WORD = 'x'

class Comment(Enum):
    COMMENT_START = '/*'
    COMMENT_STOP = '*/'
    COMMENT = '//'

def stripLine(line):
    return line.strip().split(Comment.COMMENT.value)[0].strip()    

lines = []
with open('input.S') as f:
    lines = f.readlines()


comment = False

for line in lines:
    
    rightLine = None
    if not comment and Comment.COMMENT_START.value in line:
        line, rightLine = line.split(Comment.COMMENT_START.value, 1)
        comment = True
    if comment:
        if rightLine and Comment.COMMENT_STOP.value in rightLine:
            line += rightLine
            comment = False
        elif '*/' in line:
            line = line.split(Comment.COMMENT_STOP.value, 1)[1]
            comment = False
        elif not rightLine:
            continue
        
    splitted = line.split(';')
    codeLine = []
    for sLine in splitted:
        sLine = stripLine(sLine)
        if sLine != '':
            codeLine.append(sLine)
    if len(codeLine) == 0:
        continue
    print(codeLine)