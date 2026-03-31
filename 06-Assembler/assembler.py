#!/usr/bin/env python3

file_input = input('Type assembly source filename (no extention): ')
file = f'{file_input}.asm'
output = f'{file_input}.hack'

table = {
        'R0': 0,
        'R1': 1,
        'R2': 2,
        'R3': 3,
        'R4': 4,
        'R5': 5,
        'R6': 6,
        'R7': 7,
        'R8': 8,
        'R9': 9,
        'R10': 10,
        'R11': 11,
        'R12': 12,
        'R13': 13,
        'R14': 14,
        'R15': 15,
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
        'SCREEN': 16384,
        'KBD': 24576,
        }

translation = {}

next_mem = 16
position = 0

def clean_line(line):
    line = line.strip()

    if line == '':
        return None

    if line[:2] == '//':
        return None

    return line

def instructionType(line):
    if line[0] == '@':
        return 'A'

    elif line[0] == '(' and line[-1] == ')':
        return 'L'

    else:
        return 'C'

def symbol(data):
    if data[0] == '@':
        return data[1:]
    else:
        return data[1:-1]

def destination(value):
    table = {
            None: '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
            }
    return table[value]

def compute(value):
    table = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101'
            }
    if 'M' in value:
        value = value.replace('M', 'A')
        value = table[value]
        return f'1{value}'
    else:
        return f'0{table[value]}'

def jump(value):
    table =  {
            None: '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
            }
    return f'{table[value]}'

def split_line(line, data):
    if '=' in line and ';' in line:
        data['dest'], data['comp'], data['jmp'] = line.split('=', ';')
        return data
    elif '=' in line:
        data['dest'], data['comp'] = line.split('=')
        return data
    elif ';' in line:
        data['comp'], data['jmp'] = line.split(';')
        return data

with open(file, 'r') as f:
    for line in f:
        line = clean_line(line)

        if line is None:
            continue

        _type = instructionType(line)

        if _type == 'A' or _type == 'C':
            position += 1

        if _type == 'L':
            value = symbol(line)
            # position += 1
            table[value] = position

with open(output, 'w') as w:
    with open(file, 'r') as f:
        for line in f:
            value = None

            line = clean_line(line)

            if line is None:
                continue

            _type = instructionType(line)

            if _type == 'L':
                continue

            if _type == 'A':
                value = symbol(line)
                
                if value == '32':
                    print(value, type(value))
                if value.isdigit():
                    value = int(value)
                    w.write(f'{format(value, '016b')}\n')
                elif value in table:
                    w.write(f'{format(table[value], '016b')}\n')

                if value not in table and not isinstance(value, int):
                    table[value] = next_mem
                    w.write(f'{format(table[value], '016b')}\n')
                    next_mem += 1

            if _type == 'C':
                values = {}
                split = split_line(line, values)

                if 'dest' in values:
                    dest = destination(values['dest'])
                else:
                    dest = destination(None)
                if 'comp' in values:
                    comp = compute(values['comp'])
                if 'jmp' in values:
                    jmp = jump(values['jmp'])
                else:
                    jmp = jump(None)

                w.write(f'111{comp}{dest}{jmp}\n')
