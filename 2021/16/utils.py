
from typing import List, Tuple

DEBUG = False

class Stream():
    VERSION_LENGTH = 3
    TYPEID_LENGTH = 3
    GROUP_LENGTH = 5

    ID_SUM = 0
    ID_PRODUCT = 1
    ID_MINIMUM = 2
    ID_MAXIMUM = 3
    ID_LITERAL_VALUE = 4
    ID_GREATER_THAN = 5
    ID_LESS_THAN = 6
    ID_EQUAL = 7

    TYPE_ID_MAP = {ID_SUM:'Sum',ID_PRODUCT:'Product',ID_MINIMUM:'Minimum',
               ID_MAXIMUM:'Maximum',ID_LITERAL_VALUE:'Literal',
               ID_GREATER_THAN:'Greater',ID_LESS_THAN:'Less', ID_EQUAL:'Equal'}

    PADDING_SPACE = '\u2502   '
    PADDING_JOIN_HEADER = '\u251c\u2500\u2500\u2500'
    PADDING_JOIN_VALUE = '\u2514\u2500\u2500\u2500'

    def __init__(self, stream:str) -> None:
        tmp = bin(int(stream, 16))[2:]
        packs = len(stream)

        self.m_stream = tmp.zfill(packs*4)
        self.m_version_sum = 0
        self.m_value = 0
        self.m_idx = 0
        self.m_padding = -2
    

    def parse(self):
        self.m_value, _ = self.__parse_packet()

        print('Ver Sum: {}{}{}'.format('\033[1m' + '\033[96m', self.m_version_sum, '\033[0m'))
        print('Pkg Value: {}{}{}'.format('\033[1m' + '\033[92m', self.m_value, '\033[0m'))


    def __read_bits(self, num:int) -> int:
        tmp = int(self.m_stream[self.m_idx:self.m_idx + num], 2)
        self.m_idx += num

        return tmp

    def __parse_packet(self) -> Tuple[List[int], int]:

        first_idx = self.m_idx
        self.m_padding += 1

        version = self.__read_bits(Stream.VERSION_LENGTH)
        self.m_version_sum += version
        if DEBUG: print(Stream.PADDING_SPACE*self.m_padding + Stream.PADDING_JOIN_HEADER + 'Version = {};'.format(version), end='')

        type_id = self.__read_bits(Stream.TYPEID_LENGTH)
        if DEBUG:print(' Type ID = {} ({});'.format(type_id, Stream.TYPE_ID_MAP[type_id]))

        match type_id:
            case Stream.ID_LITERAL_VALUE:
                value = self.__parse_literal()
            case _:
                value = self.__parse_operator(type_id)

        if DEBUG: print(Stream.PADDING_SPACE*(self.m_padding + 1) + Stream.PADDING_JOIN_VALUE + 'Value = {};'.format(value))

        last_idx = self.m_idx
        self.m_padding -= 1

        return (value, last_idx - first_idx)




    def __parse_literal(self) -> int:
        run = True
        value = 0
        while run:
            tmp = self.__read_bits(1)
            value = (value << (Stream.GROUP_LENGTH - 1)) + self.__read_bits(Stream.GROUP_LENGTH - 1)

            if tmp == 0:
                run = False
        
        return value


    def __parse_operator(self, type_id:int) -> int:
        I = self.__read_bits(1)

        values = []
        if I == 0:
            L = 15
            subpacket_length = self.__read_bits(L)

            consumed = 0
            while consumed < subpacket_length:
                value, cons = self.__parse_packet()
                values.append(value)
                consumed += cons

        else:
            L = 11
            packets_num = self.__read_bits(L)

            for _ in range(packets_num):
                value, cons = self.__parse_packet()
                values.append(value)
                
        match type_id:
            case Stream.ID_SUM:
                return sum(values)

            case Stream.ID_PRODUCT:
                val = 1
                for v in values:
                    val *= v

                return val
                
            case Stream.ID_MINIMUM:
                return min(values)
                
            case Stream.ID_MAXIMUM:
                return max(values)
                
            case Stream.ID_GREATER_THAN:
                return (values[0] > values[1])*1
                
            case Stream.ID_LESS_THAN:
                return (values[0] < values[1])*1
                
            case Stream.ID_EQUAL:
                return (values[0] == values[1])*1
                
