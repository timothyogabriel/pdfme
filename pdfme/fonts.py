import abc
from io import BytesIO
from pathlib import Path

helvetica = {'\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278, '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278, '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278, '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278, '\x1f': 278, ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944, 'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556, '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 222, '\x83': 556, '\x84': 333, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333, '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 222, '\x92': 222, '\x93': 333, '\x94': 333, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000, '\x9a': 500, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '¡': 333, '¢': 556, '£': 556, '¤': 556, '¥': 556, '¦': 260, '§': 556, '¨': 333, '©': 737, 'ª': 370, '«': 556, '¬': 584, '\xad': 333, '®': 737, '¯': 333, '°': 400, '±': 584, '²': 333, '³': 333, '´': 333, 'µ': 556, '¶': 537, '·': 278, '¸': 333, '¹': 333, 'º': 365, '»': 556, '¼': 834, '½': 834, '¾': 834, '¿': 611, 'À': 667, 'Á': 667, 'Â': 667, 'Ã': 667, 'Ä': 667, 'Å': 667, 'Æ': 1000, 'Ç': 722, 'È': 667, 'É': 667, 'Ê': 667, 'Ë': 667, 'Ì': 278, 'Í': 278, 'Î': 278, 'Ï': 278, 'Ð': 722, 'Ñ': 722, 'Ò': 778, 'Ó': 778, 'Ô': 778, 'Õ': 778, 'Ö': 778, '×': 584, 'Ø': 778, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 667, 'Þ': 667, 'ß': 611, 'à': 556, 'á': 556, 'â': 556, 'ã': 556, 'ä': 556, 'å': 556, 'æ': 889, 'ç': 500, 'è': 556, 'é': 556, 'ê': 556, 'ë': 556, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 556, 'ñ': 556, 'ò': 556, 'ó': 556, 'ô': 556, 'õ': 556, 'ö': 556, '÷': 584, 'ø': 611, 'ù': 556, 'ú': 556, 'û': 556, 'ü': 556, 'ý': 500, 'þ': 556, 'ÿ': 500}
helveticaB = {'\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278, '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278, '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278, '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278, '\x1f': 278, ' ': 278, '!': 333, '"': 474, '#': 556, '$': 556, '%': 889, '&': 722, "'": 238, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 333, ';': 333, '<': 584, '=': 584, '>': 584, '?': 611, '@': 975, 'A': 722, 'B': 722, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 556, 'K': 722, 'L': 611, 'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944, 'X': 667, 'Y': 667, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 584, '_': 556, '`': 333, 'a': 556, 'b': 611, 'c': 556, 'd': 611, 'e': 556, 'f': 333, 'g': 611, 'h': 611, 'i': 278, 'j': 278, 'k': 556, 'l': 278, 'm': 889, 'n': 611, 'o': 611, 'p': 611, 'q': 611, 'r': 389, 's': 556, 't': 333, 'u': 611, 'v': 556, 'w': 778, 'x': 556, 'y': 556, 'z': 500, '{': 389, '|': 280, '}': 389, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 278, '\x83': 556, '\x84': 500, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333, '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 278, '\x92': 278, '\x93': 500, '\x94': 500, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000, '\x9a': 556, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '¡': 333, '¢': 556, '£': 556, '¤': 556, '¥': 556, '¦': 280, '§': 556, '¨': 333, '©': 737, 'ª': 370, '«': 556, '¬': 584, '\xad': 333, '®': 737, '¯': 333, '°': 400, '±': 584, '²': 333, '³': 333, '´': 333, 'µ': 611, '¶': 556, '·': 278, '¸': 333, '¹': 333, 'º': 365, '»': 556, '¼': 834, '½': 834, '¾': 834, '¿': 611, 'À': 722, 'Á': 722, 'Â': 722, 'Ã': 722, 'Ä': 722, 'Å': 722, 'Æ': 1000, 'Ç': 722, 'È': 667, 'É': 667, 'Ê': 667, 'Ë': 667, 'Ì': 278, 'Í': 278, 'Î': 278, 'Ï': 278, 'Ð': 722, 'Ñ': 722, 'Ò': 778, 'Ó': 778, 'Ô': 778, 'Õ': 778, 'Ö': 778, '×': 584, 'Ø': 778, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 667, 'Þ': 667, 'ß': 611, 'à': 556, 'á': 556, 'â': 556, 'ã': 556, 'ä': 556, 'å': 556, 'æ': 889, 'ç': 556, 'è': 556, 'é': 556, 'ê': 556, 'ë': 556, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 611, 'ñ': 611, 'ò': 611, 'ó': 611, 'ô': 611, 'õ': 611, 'ö': 611, '÷': 584, 'ø': 611, 'ù': 611, 'ú': 611, 'û': 611, 'ü': 611, 'ý': 556, 'þ': 611, 'ÿ': 556}
times = {'\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250, '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250, '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250, '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250, '\x1f': 250, ' ': 250, '!': 333, '"': 408, '#': 500, '$': 500, '%': 833, '&': 778, "'": 180, '(': 333, ')': 333, '*': 500, '+': 564, ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500, '7': 500, '8': 500, '9': 500, ':': 278, ';': 278, '<': 564, '=': 564, '>': 564, '?': 444, '@': 921, 'A': 722, 'B': 667, 'C': 667, 'D': 722, 'E': 611, 'F': 556, 'G': 722, 'H': 722, 'I': 333, 'J': 389, 'K': 722, 'L': 611, 'M': 889, 'N': 722, 'O': 722, 'P': 556, 'Q': 722, 'R': 667, 'S': 556, 'T': 611, 'U': 722, 'V': 722, 'W': 944, 'X': 722, 'Y': 722, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 469, '_': 500, '`': 333, 'a': 444, 'b': 500, 'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500, 'h': 500, 'i': 278, 'j': 278, 'k': 500, 'l': 278, 'm': 778, 'n': 500, 'o': 500, 'p': 500, 'q': 500, 'r': 333, 's': 389, 't': 278, 'u': 500, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 444, '{': 480, '|': 200, '}': 480, '~': 541, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333, '\x83': 500, '\x84': 444, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333, '\x8c': 889, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 444, '\x94': 444, '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 980, '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 444, '\x9f': 722, '\xa0': 250, '¡': 333, '¢': 500, '£': 500, '¤': 500, '¥': 500, '¦': 200, '§': 500, '¨': 333, '©': 760, 'ª': 276, '«': 500, '¬': 564, '\xad': 333, '®': 760, '¯': 333, '°': 400, '±': 564, '²': 300, '³': 300, '´': 333, 'µ': 500, '¶': 453, '·': 250, '¸': 333, '¹': 300, 'º': 310, '»': 500, '¼': 750, '½': 750, '¾': 750, '¿': 444, 'À': 722, 'Á': 722, 'Â': 722, 'Ã': 722, 'Ä': 722, 'Å': 722, 'Æ': 889, 'Ç': 667, 'È': 611, 'É': 611, 'Ê': 611, 'Ë': 611, 'Ì': 333, 'Í': 333, 'Î': 333, 'Ï': 333, 'Ð': 722, 'Ñ': 722, 'Ò': 722, 'Ó': 722, 'Ô': 722, 'Õ': 722, 'Ö': 722, '×': 564, 'Ø': 722, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 722, 'Þ': 556, 'ß': 500, 'à': 444, 'á': 444, 'â': 444, 'ã': 444, 'ä': 444, 'å': 444, 'æ': 667, 'ç': 444, 'è': 444, 'é': 444, 'ê': 444, 'ë': 444, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 500, 'ñ': 500, 'ò': 500, 'ó': 500, 'ô': 500, 'õ': 500, 'ö': 500, '÷': 564, 'ø': 500, 'ù': 500, 'ú': 500, 'û': 500, 'ü': 500, 'ý': 500, 'þ': 500, 'ÿ': 500}
timesB = {'\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250, '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250, '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250, '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250, '\x1f': 250, ' ': 250, '!': 333, '"': 555, '#': 500, '$': 500, '%': 1000, '&': 833, "'": 278, '(': 333, ')': 333, '*': 500, '+': 570, ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500, '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 570, '=': 570, '>': 570, '?': 500, '@': 930, 'A': 722, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 778, 'I': 389, 'J': 500, 'K': 778, 'L': 667, 'M': 944, 'N': 722, 'O': 778, 'P': 611, 'Q': 778, 'R': 722, 'S': 556, 'T': 667, 'U': 722, 'V': 722, 'W': 1000, 'X': 722, 'Y': 722, 'Z': 667, '[': 333, '\\': 278, ']': 333, '^': 581, '_': 500, '`': 333, 'a': 500, 'b': 556, 'c': 444, 'd': 556, 'e': 444, 'f': 333, 'g': 500, 'h': 556, 'i': 278, 'j': 333, 'k': 556, 'l': 278, 'm': 833, 'n': 556, 'o': 500, 'p': 556, 'q': 556, 'r': 444, 's': 389, 't': 333, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 444, '{': 394, '|': 220, '}': 394, '~': 520, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333, '\x83': 500, '\x84': 500, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333, '\x8c': 1000, '\x8d': 350, '\x8e': 667, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 500, '\x94': 500, '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 1000, '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 444, '\x9f': 722, '\xa0': 250, '¡': 333, '¢': 500, '£': 500, '¤': 500, '¥': 500, '¦': 220, '§': 500, '¨': 333, '©': 747, 'ª': 300, '«': 500, '¬': 570, '\xad': 333, '®': 747, '¯': 333, '°': 400, '±': 570, '²': 300, '³': 300, '´': 333, 'µ': 556, '¶': 540, '·': 250, '¸': 333, '¹': 300, 'º': 330, '»': 500, '¼': 750, '½': 750, '¾': 750, '¿': 500, 'À': 722, 'Á': 722, 'Â': 722, 'Ã': 722, 'Ä': 722, 'Å': 722, 'Æ': 1000, 'Ç': 722, 'È': 667, 'É': 667, 'Ê': 667, 'Ë': 667, 'Ì': 389, 'Í': 389, 'Î': 389, 'Ï': 389, 'Ð': 722, 'Ñ': 722, 'Ò': 778, 'Ó': 778, 'Ô': 778, 'Õ': 778, 'Ö': 778, '×': 570, 'Ø': 778, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 722, 'Þ': 611, 'ß': 556, 'à': 500, 'á': 500, 'â': 500, 'ã': 500, 'ä': 500, 'å': 500, 'æ': 722, 'ç': 444, 'è': 444, 'é': 444, 'ê': 444, 'ë': 444, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 500, 'ñ': 556, 'ò': 500, 'ó': 500, 'ô': 500, 'õ': 500, 'ö': 500, '÷': 570, 'ø': 500, 'ù': 556, 'ú': 556, 'û': 556, 'ü': 556, 'ý': 500, 'þ': 556, 'ÿ': 500}
timesBI = {'\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250, '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250, '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250, '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250, '\x1f': 250, ' ': 250, '!': 389, '"': 555, '#': 500, '$': 500, '%': 833, '&': 778, "'": 278, '(': 333, ')': 333, '*': 500, '+': 570, ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500, '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 570, '=': 570, '>': 570, '?': 500, '@': 832, 'A': 667, 'B': 667, 'C': 667, 'D': 722, 'E': 667, 'F': 667, 'G': 722, 'H': 778, 'I': 389, 'J': 500, 'K': 667, 'L': 611, 'M': 889, 'N': 722, 'O': 722, 'P': 611, 'Q': 722, 'R': 667, 'S': 556, 'T': 611, 'U': 722, 'V': 667, 'W': 889, 'X': 667, 'Y': 611, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 570, '_': 500, '`': 333, 'a': 500, 'b': 500, 'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500, 'h': 556, 'i': 278, 'j': 278, 'k': 500, 'l': 278, 'm': 778, 'n': 556, 'o': 500, 'p': 500, 'q': 500, 'r': 389, 's': 389, 't': 278, 'u': 556, 'v': 444, 'w': 667, 'x': 500, 'y': 444, 'z': 389, '{': 348, '|': 220, '}': 348, '~': 570, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333, '\x83': 500, '\x84': 500, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333, '\x8c': 944, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 500, '\x94': 500, '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 1000, '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 389, '\x9f': 611, '\xa0': 250, '¡': 389, '¢': 500, '£': 500, '¤': 500, '¥': 500, '¦': 220, '§': 500, '¨': 333, '©': 747, 'ª': 266, '«': 500, '¬': 606, '\xad': 333, '®': 747, '¯': 333, '°': 400, '±': 570, '²': 300, '³': 300, '´': 333, 'µ': 576, '¶': 500, '·': 250, '¸': 333, '¹': 300, 'º': 300, '»': 500, '¼': 750, '½': 750, '¾': 750, '¿': 500, 'À': 667, 'Á': 667, 'Â': 667, 'Ã': 667, 'Ä': 667, 'Å': 667, 'Æ': 944, 'Ç': 667, 'È': 667, 'É': 667, 'Ê': 667, 'Ë': 667, 'Ì': 389, 'Í': 389, 'Î': 389, 'Ï': 389, 'Ð': 722, 'Ñ': 722, 'Ò': 722, 'Ó': 722, 'Ô': 722, 'Õ': 722, 'Ö': 722, '×': 570, 'Ø': 722, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 611, 'Þ': 611, 'ß': 500, 'à': 500, 'á': 500, 'â': 500, 'ã': 500, 'ä': 500, 'å': 500, 'æ': 722, 'ç': 444, 'è': 444, 'é': 444, 'ê': 444, 'ë': 444, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 500, 'ñ': 556, 'ò': 500, 'ó': 500, 'ô': 500, 'õ': 500, 'ö': 500, '÷': 570, 'ø': 500, 'ù': 556, 'ú': 556, 'û': 556, 'ü': 556, 'ý': 444, 'þ': 500, 'ÿ': 444}
timesI = {'\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250, '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250, '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250, '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250, '\x1f': 250, ' ': 250, '!': 333, '"': 420, '#': 500, '$': 500, '%': 833, '&': 778, "'": 214, '(': 333, ')': 333, '*': 500, '+': 675, ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500, '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 675, '=': 675, '>': 675, '?': 500, '@': 920, 'A': 611, 'B': 611, 'C': 667, 'D': 722, 'E': 611, 'F': 611, 'G': 722, 'H': 722, 'I': 333, 'J': 444, 'K': 667, 'L': 556, 'M': 833, 'N': 667, 'O': 722, 'P': 611, 'Q': 722, 'R': 611, 'S': 500, 'T': 556, 'U': 722, 'V': 611, 'W': 833, 'X': 611, 'Y': 556, 'Z': 556, '[': 389, '\\': 278, ']': 389, '^': 422, '_': 500, '`': 333, 'a': 500, 'b': 500, 'c': 444, 'd': 500, 'e': 444, 'f': 278, 'g': 500, 'h': 500, 'i': 278, 'j': 278, 'k': 444, 'l': 278, 'm': 722, 'n': 500, 'o': 500, 'p': 500, 'q': 500, 'r': 389, 's': 389, 't': 278, 'u': 500, 'v': 444, 'w': 667, 'x': 444, 'y': 444, 'z': 389, '{': 400, '|': 275, '}': 400, '~': 541, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333, '\x83': 500, '\x84': 556, '\x85': 889, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 500, '\x8b': 333, '\x8c': 944, '\x8d': 350, '\x8e': 556, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 556, '\x94': 556, '\x95': 350, '\x96': 500, '\x97': 889, '\x98': 333, '\x99': 980, '\x9a': 389, '\x9b': 333, '\x9c': 667, '\x9d': 350, '\x9e': 389, '\x9f': 556, '\xa0': 250, '¡': 389, '¢': 500, '£': 500, '¤': 500, '¥': 500, '¦': 275, '§': 500, '¨': 333, '©': 760, 'ª': 276, '«': 500, '¬': 675, '\xad': 333, '®': 760, '¯': 333, '°': 400, '±': 675, '²': 300, '³': 300, '´': 333, 'µ': 500, '¶': 523, '·': 250, '¸': 333, '¹': 300, 'º': 310, '»': 500, '¼': 750, '½': 750, '¾': 750, '¿': 500, 'À': 611, 'Á': 611, 'Â': 611, 'Ã': 611, 'Ä': 611, 'Å': 611, 'Æ': 889, 'Ç': 667, 'È': 611, 'É': 611, 'Ê': 611, 'Ë': 611, 'Ì': 333, 'Í': 333, 'Î': 333, 'Ï': 333, 'Ð': 722, 'Ñ': 667, 'Ò': 722, 'Ó': 722, 'Ô': 722, 'Õ': 722, 'Ö': 722, '×': 675, 'Ø': 722, 'Ù': 722, 'Ú': 722, 'Û': 722, 'Ü': 722, 'Ý': 556, 'Þ': 611, 'ß': 500, 'à': 500, 'á': 500, 'â': 500, 'ã': 500, 'ä': 500, 'å': 500, 'æ': 667, 'ç': 444, 'è': 444, 'é': 444, 'ê': 444, 'ë': 444, 'ì': 278, 'í': 278, 'î': 278, 'ï': 278, 'ð': 500, 'ñ': 500, 'ò': 500, 'ó': 500, 'ô': 500, 'õ': 500, 'ö': 500, '÷': 675, 'ø': 500, 'ù': 500, 'ú': 500, 'û': 500, 'ü': 500, 'ý': 444, 'þ': 500, 'ÿ': 444}
symbol = {'\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250, '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250, '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250, '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250, '\x1f': 250, ' ': 250, '!': 333, '"': 713, '#': 500, '$': 549, '%': 833, '&': 778, "'": 439, '(': 333, ')': 333, '*': 500, '+': 549, ',': 250, '-': 549, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500, '7': 500, '8': 500, '9': 500, ':': 278, ';': 278, '<': 549, '=': 549, '>': 549, '?': 444, '@': 549, 'A': 722, 'B': 667, 'C': 722, 'D': 612, 'E': 611, 'F': 763, 'G': 603, 'H': 722, 'I': 333, 'J': 631, 'K': 722, 'L': 686, 'M': 889, 'N': 722, 'O': 722, 'P': 768, 'Q': 741, 'R': 556, 'S': 592, 'T': 611, 'U': 690, 'V': 439, 'W': 768, 'X': 645, 'Y': 795, 'Z': 611, '[': 333, '\\': 863, ']': 333, '^': 658, '_': 500, '`': 500, 'a': 631, 'b': 549, 'c': 549, 'd': 494, 'e': 439, 'f': 521, 'g': 411, 'h': 603, 'i': 329, 'j': 603, 'k': 549, 'l': 549, 'm': 576, 'n': 521, 'o': 549, 'p': 549, 'q': 521, 'r': 549, 's': 603, 't': 439, 'u': 576, 'v': 713, 'w': 686, 'x': 493, 'y': 686, 'z': 494, '{': 480, '|': 200, '}': 480, '~': 549, '\x7f': 0, '\x80': 0, '\x81': 0, '\x82': 0, '\x83': 0, '\x84': 0, '\x85': 0, '\x86': 0, '\x87': 0, '\x88': 0, '\x89': 0, '\x8a': 0, '\x8b': 0, '\x8c': 0, '\x8d': 0, '\x8e': 0, '\x8f': 0, '\x90': 0, '\x91': 0, '\x92': 0, '\x93': 0, '\x94': 0, '\x95': 0, '\x96': 0, '\x97': 0, '\x98': 0, '\x99': 0, '\x9a': 0, '\x9b': 0, '\x9c': 0, '\x9d': 0, '\x9e': 0, '\x9f': 0, '\xa0': 750, '¡': 620, '¢': 247, '£': 549, '¤': 167, '¥': 713, '¦': 500, '§': 753, '¨': 753, '©': 753, 'ª': 753, '«': 1042, '¬': 987, '\xad': 603, '®': 987, '¯': 603, '°': 400, '±': 549, '²': 411, '³': 549, '´': 549, 'µ': 713, '¶': 494, '·': 460, '¸': 549, '¹': 549, 'º': 549, '»': 549, '¼': 1000, '½': 603, '¾': 1000, '¿': 658, 'À': 823, 'Á': 686, 'Â': 795, 'Ã': 987, 'Ä': 768, 'Å': 768, 'Æ': 823, 'Ç': 768, 'È': 768, 'É': 713, 'Ê': 713, 'Ë': 713, 'Ì': 713, 'Í': 713, 'Î': 713, 'Ï': 713, 'Ð': 768, 'Ñ': 713, 'Ò': 790, 'Ó': 790, 'Ô': 890, 'Õ': 823, 'Ö': 549, '×': 250, 'Ø': 713, 'Ù': 603, 'Ú': 603, 'Û': 1042, 'Ü': 987, 'Ý': 603, 'Þ': 987, 'ß': 603, 'à': 494, 'á': 329, 'â': 790, 'ã': 790, 'ä': 786, 'å': 713, 'æ': 384, 'ç': 384, 'è': 384, 'é': 384, 'ê': 384, 'ë': 384, 'ì': 494, 'í': 494, 'î': 494, 'ï': 494, 'ð': 0, 'ñ': 329, 'ò': 274, 'ó': 686, 'ô': 686, 'õ': 686, 'ö': 384, '÷': 384, 'ø': 384, 'ù': 384, 'ú': 384, 'û': 384, 'ü': 494, 'ý': 494, 'þ': 494, 'ÿ': 0}
zapfdingbats = {'\x00': 0, '\x01': 0, '\x02': 0, '\x03': 0, '\x04': 0, '\x05': 0, '\x06': 0, '\x07': 0, '\x08': 0, '\t': 0, '\n': 0, '\x0b': 0, '\x0c': 0, '\r': 0, '\x0e': 0, '\x0f': 0, '\x10': 0, '\x11': 0, '\x12': 0, '\x13': 0, '\x14': 0, '\x15': 0, '\x16': 0, '\x17': 0, '\x18': 0, '\x19': 0, '\x1a': 0, '\x1b': 0, '\x1c': 0, '\x1d': 0, '\x1e': 0, '\x1f': 0, ' ': 278, '!': 974, '"': 961, '#': 974, '$': 980, '%': 719, '&': 789, "'": 790, '(': 791, ')': 690, '*': 960, '+': 939, ',': 549, '-': 855, '.': 911, '/': 933, '0': 911, '1': 945, '2': 974, '3': 755, '4': 846, '5': 762, '6': 761, '7': 571, '8': 677, '9': 763, ':': 760, ';': 759, '<': 754, '=': 494, '>': 552, '?': 537, '@': 577, 'A': 692, 'B': 786, 'C': 788, 'D': 788, 'E': 790, 'F': 793, 'G': 794, 'H': 816, 'I': 823, 'J': 789, 'K': 841, 'L': 823, 'M': 833, 'N': 816, 'O': 831, 'P': 923, 'Q': 744, 'R': 723, 'S': 749, 'T': 790, 'U': 792, 'V': 695, 'W': 776, 'X': 768, 'Y': 792, 'Z': 759, '[': 707, '\\': 708, ']': 682, '^': 701, '_': 826, '`': 815, 'a': 789, 'b': 789, 'c': 707, 'd': 687, 'e': 696, 'f': 689, 'g': 786, 'h': 787, 'i': 713, 'j': 791, 'k': 785, 'l': 791, 'm': 873, 'n': 761, 'o': 762, 'p': 762, 'q': 759, 'r': 759, 's': 892, 't': 892, 'u': 788, 'v': 784, 'w': 438, 'x': 138, 'y': 277, 'z': 415, '{': 392, '|': 392, '}': 668, '~': 668, '\x7f': 0, '\x80': 390, '\x81': 390, '\x82': 317, '\x83': 317, '\x84': 276, '\x85': 276, '\x86': 509, '\x87': 509, '\x88': 410, '\x89': 410, '\x8a': 234, '\x8b': 234, '\x8c': 334, '\x8d': 334, '\x8e': 0, '\x8f': 0, '\x90': 0, '\x91': 0, '\x92': 0, '\x93': 0, '\x94': 0, '\x95': 0, '\x96': 0, '\x97': 0, '\x98': 0, '\x99': 0, '\x9a': 0, '\x9b': 0, '\x9c': 0, '\x9d': 0, '\x9e': 0, '\x9f': 0, '\xa0': 0, '¡': 732, '¢': 544, '£': 544, '¤': 910, '¥': 667, '¦': 760, '§': 760, '¨': 776, '©': 595, 'ª': 694, '«': 626, '¬': 788, '\xad': 788, '®': 788, '¯': 788, '°': 788, '±': 788, '²': 788, '³': 788, '´': 788, 'µ': 788, '¶': 788, '·': 788, '¸': 788, '¹': 788, 'º': 788, '»': 788, '¼': 788, '½': 788, '¾': 788, '¿': 788, 'À': 788, 'Á': 788, 'Â': 788, 'Ã': 788, 'Ä': 788, 'Å': 788, 'Æ': 788, 'Ç': 788, 'È': 788, 'É': 788, 'Ê': 788, 'Ë': 788, 'Ì': 788, 'Í': 788, 'Î': 788, 'Ï': 788, 'Ð': 788, 'Ñ': 788, 'Ò': 788, 'Ó': 788, 'Ô': 894, 'Õ': 838, 'Ö': 1016, '×': 458, 'Ø': 748, 'Ù': 924, 'Ú': 748, 'Û': 918, 'Ü': 927, 'Ý': 928, 'Þ': 928, 'ß': 834, 'à': 873, 'á': 828, 'â': 924, 'ã': 924, 'ä': 917, 'å': 930, 'æ': 931, 'ç': 463, 'è': 883, 'é': 836, 'ê': 836, 'ë': 867, 'ì': 867, 'í': 696, 'î': 696, 'ï': 874, 'ð': 0, 'ñ': 874, 'ò': 760, 'ó': 946, 'ô': 771, 'õ': 865, 'ö': 771, '÷': 888, 'ø': 967, 'ù': 888, 'ú': 831, 'û': 873, 'ü': 927, 'ý': 970, 'þ': 918, 'ÿ': 0}
courier = {chr(i): 600 for i in range(256)}

STANDARD_FONTS = {
    'Helvetica': {
        'n': { 'base_font': 'Helvetica', 'widths': helvetica },
        'b': { 'base_font': 'Helvetica-Bold', 'widths': helveticaB },
        'i': { 'base_font': 'Helvetica-Oblique', 'widths': helvetica},
        'bi': { 'base_font': 'Helvetica-BoldOblique', 'widths': helveticaB }
    },
    'Times': {
        'n': { 'base_font': 'Times-Roman', 'widths': times },
        'b': { 'base_font': 'Times-Bold', 'widths': timesB },
        'i': { 'base_font': 'Times-Italic', 'widths': timesI },
        'bi': { 'base_font': 'Times-BoldItalic', 'widths': timesBI }
    },
    'Courier': {
        'n': { 'base_font': 'Courier', 'widths': courier },
        'b': { 'base_font': 'Courier-Bold', 'widths': courier },
        'i': { 'base_font': 'Courier-Oblique', 'widths': courier },
        'bi': { 'base_font': 'Courier-BoldOblique', 'widths': courier }
    },
    'Symbol': {'n': {'base_font': 'Symbol', 'widths': symbol}},
    'ZapfDingbats': {'n': {'base_font': 'ZapfDingbats', 'widths': zapfdingbats}}
}

def get_tounicode_cmap(cmap_mappings):
    '''Method returns cmap for Unicode mappings.'''
    def cmap_hex_format(hex_str: str) -> str:
        if hex_str.startswith('0x'):
            hex_str = hex_str[2:]
        if len(hex_str) != 4:
            hex_str = hex_str.zfill(4)
        return f'<{hex_str.upper()}>'

    mappings = []
    for (cid, gid) in cmap_mappings.items():
        mappings.append(
            f'{cmap_hex_format(hex(int(gid)))} {cmap_hex_format(hex(int(cid)))}')

    return f'''/CIDInit /ProcSet findresource begin
        12 dict begin
        begincmap
        /CIDSystemInfo
         <</Registry (Adobe)
           /Ordering (UCS)
           /Supplement 0
        >> def
        /CMapName /Adobe-Identity-UCS def
        /CMapType 2 def
        1 begincodespacerange
        <0000> <FFFF>
        endcodespacerange
        {len(mappings)} beginbfchar
        {'\n'.join(mappings)}
        endbfchar
        endcmap
        CMapName currentdict /CMap defineresource pop
        end
        end'''.encode('latin')


class PDFFont(abc.ABC):
    """Abstract class that represents a PDF font.

    Args:
        ref (str): the name of the font, included in every paragraph and page
            that uses this font.
    """

    registered_fonts = {}
    loaded_fonts = []

    def __init__(self, ref: str) -> None:
        self._ref = ref

    @property
    def ref(self) -> str:
        """Property that returns the name (ref) of this font.

        Returns:
            str: the name of this font
        """
        return self._ref

    @staticmethod
    def register(font_family: str, mode: str, path: str):
        '''
        This is useful for registering user defined custom fonts. The registered 
        font would be loaded when required in the document.

        Args:
            font_family: The font family name.
            mode: The font mode. One of n, b, i, bi.
            path: Font file path.
        '''
        PDFFont.registered_fonts[(font_family, mode)] = path

    @abc.abstractproperty
    def base_font(self) -> str:
        """Abstract property that should return this font's base font name.

        Returns:
            str: the base font name
        """
        pass

    @abc.abstractmethod
    def get_char_width(self, char: str) -> float:
        """Abstract method that should return the width of ``char`` character
        in this font.

        Args:
            char (str): the character.

        Returns:
            float: the character's width.
        """
        pass

    @abc.abstractmethod
    def get_text_width(self, text: str) -> float:
        """Abstract method that should return the width of the ``text`` string
        in this font.

        Args:
            text (str): the sentence to measure.

        Returns:
            float: the sentence's width.
        """
        pass

    @abc.abstractmethod
    def add_font(self, base: 'PDFBase') -> 'PDFObject':
        """Abstract method that should add this font to the PDFBase instance,
        passed as argument.

        Args:
            base (PDFBase): the base instance to add this font.
        """
        pass

class PDFStandardFont(PDFFont):
    """This class represents a standard PDF font.

    Args:
        ref (str): the name of this font.
        base_font (str): the base font name of this font.
        widths (dict): the widths of each character in this font.
    """
    def __init__(self, ref: str, base_font: str, widths: dict) -> None:
        super().__init__(ref)
        self._base_font = base_font
        self.widths = widths

    @property
    def base_font(self) -> str:
        """See :meth:`pdfme.fonts.PDFFont.base_font`"""
        return self._base_font

    def get_char_width(self, char: str) -> float:
        """See :meth:`pdfme.fonts.PDFFont.get_char_width`"""
        return self.widths[char] / 1000

    def get_text_width(self, text) -> float:
        """See :meth:`pdfme.fonts.PDFFont.get_text_width`"""
        return sum(self.widths[char] for char in text) / 1000

    def add_font(self, base: 'PDFBase') -> 'PDFObject':
        """See :meth:`pdfme.fonts.PDFFont.add_font`"""
        font = base.add({
            'Type': b'/Font',
            'Subtype': b'/Type1',
            'BaseFont': subs('/{}', self.base_font),
            'Encoding': b'/WinAnsiEncoding'
        })
        if self.base_font not in ['Symbol', 'ZapfDingbats']:
            font['Encoding'] = b'/WinAnsiEncoding'
        return font

class PDFTrueTypeFont(PDFFont):
    """This class represents a TrueType PDF font.

    Args:
        ref (str): the name of this font.
        base_font (str): the base font name of this font.
        widths (dict): the widths of each character in this font.
    """
    def __init__(self, ref: str, filename:str=None) -> None:
        super().__init__(ref)
        self._base_font = None
        if filename is not None:
            self.load_font(filename)

    @property
    def base_font(self) -> str:
        """See :meth:`pdfme.fonts.PDFFont.base_font`"""
        return self._base_font

    def _get_char_width(self, char: str) -> float:
        """Method to get the width of the ``char`` character string.

        Args:
            char (str): the character.

        Returns:
            float: the character's width.
        """
        index = ord(char)
        if index in self.cmap:
            glyph = self.cmap[index]
            if glyph in self.glyph_set:
                return self.glyph_set[self.cmap[ord(char)]].width

        return self.glyph_set['.notdef'].width

    def get_char_width(self, char: str) -> float:
        """See :meth:`pdfme.fonts.PDFFont.get_char_width`"""
        return self._get_char_width(char) / self.units_per_em

    def get_text_width(self, text) -> float:
        """See :meth:`pdfme.fonts.PDFFont.get_text_width`"""
        return sum(self._get_char_width(c) for c in text) / self.units_per_em

    def load_font(self, filename: str) -> None:
        """Method to extract information needed by the PDF document about this
        font, from font file in ``filename`` path.

        Args:
            filename (str): font file path.

        Raises:
            ImportError: if ``fonttools`` library is not installed.
        """
        try:
            from fontTools import ttLib
        except:
            raise ImportError(
                'You need to install library fonttools to add new fonts: '
                'pip install fonttools'
            )
        self.filename = str(Path(filename))
        font = self.font = ttLib.TTFont(self.filename)

        cmap = self.cmap = self.font['cmap'].getBestCmap()

        self.glyph_set = self.font.getGlyphSet()

        self.font_descriptor = self._get_font_descriptor()
        cids2gids = self.cids2gids = {}
        for c in cmap:
            cids2gids[c] = font.getGlyphID(cmap[c])


    def _get_font_descriptor(self) -> dict:
        """Method to extract information needed by the PDF document from the
        font file, to build a PDF object called "font descriptor".

        Raises:
            Exception: if font file has copyright restrictions.

        Returns:
            dict: dict representing this font's "font descriptor".
        """
        self._base_font = self.font['name'].names[6].toStr()
        head = self.font["head"]
        self.units_per_em = head.unitsPerEm
        scale = self.scale = 1000 / self.units_per_em
        xMax = head.xMax * scale
        xMin = head.xMin * scale
        yMin = head.yMin * scale
        yMax = head.yMax * scale

        hhea = self.font.get('hhea')

        if hhea:
            ascent = hhea.ascent * scale
            descent = hhea.descent * scale

        os2 = self.font.get('OS/2')

        if os2:
            usWeightClass = os2.usWeightClass
            fsType = os2.fsType
            if (fsType == 0x0002 or (fsType & 0x0300) != 0):
                error = 'Font file in {} has copyright restrictions.'
                raise Exception(error.format(self.filename))

            if hhea is None:
                ascent = os2.sTypoAscender * scale
                descent = os2.sTypoDescender * scale
            capHeight = os2.sCapHeight * scale if os2.version > 1 else ascent
        else:
            usWeightClass = 500
            if hhea is None:
                ascent = yMax
                descent = yMin
            capHeight = self.ascent

        stemV = 50 + int(pow((usWeightClass / 65.0),2))

        post = self.font['post']
        italicAngle = post.italicAngle

        flags = 4
        if (italicAngle!= 0):
            flags = flags | 64
        if (usWeightClass >= 600):
            flags = flags | 262144
        if (post.isFixedPitch):
            flags = flags | 1

        return {
            'Type': b'/FontDescriptor',
            'FontName': subs('/{}', self.base_font),
            'Flags': flags,
            'FontBBox': [xMin, yMin, xMax, yMax],
            'ItalicAngle': italicAngle,
            'Ascent': ascent,
            'Descent': descent,
            'CapHeight': capHeight,
            'StemV': stemV
        }

    def add_font(self, base: 'PDFBase') -> 'PDFObject':
        """See :meth:`pdfme.fonts.PDFFont.add_font`"""
        font_file = BytesIO()
        self.font.save(font_file)
        font_file_bytes = font_file.getvalue()
        font_file_stream = base.add({
            'Filter': b'/FlateDecode',
            '__stream__': font_file_bytes,
            'Length1': len(font_file_bytes)
        })

        font_descriptor = base.add(self.font_descriptor)
        font_descriptor['FontFile2'] = font_file_stream.id

        font_cid = base.add({
            'Type': b'/Font',
            'FontDescriptor': font_descriptor.id,
            'BaseFont': subs('/{}', self.base_font),
            'Subtype': b'/CIDFontType2',
            'CIDToGIDMap': b'/Identity',
            'CIDSystemInfo': {
                'Registry': 'Adobe',
                'Ordering': 'Identity',
                'Supplement': 0
            },
            'W': self.compute_char_widths()
        })

        to_unicode_stream = base.add({
            'Filter': b'/FlateDecode',
            '__stream__': get_tounicode_cmap(self.cids2gids)
        })

        return base.add({
            'Type': b'/Font',
            'Subtype': b'/Type0',
            'BaseFont': subs('/{}', self.base_font),
            'Encoding': b'/Identity-H',
            'DescendantFonts': [font_cid.id],
            'ToUnicode': to_unicode_stream.id
        })

    def encode_text(self, text: str):
        return ''.join(as_hex(chr(self.cids2gids[ord(c)])) for c in text)

    def compute_char_widths(self):
        glyph_set = self.glyph_set
        cmap = self.cmap
        font = self.font
        scale = self.scale

        widths = []
        current_width_group = []

        prev_glyph_id = None
        for c in cmap:
            current_glyph_id = font.getGlyphID(cmap[c])
            if not widths:
                widths.append(current_glyph_id)
                prev_glyph_id = current_glyph_id
            elif (current_glyph_id - prev_glyph_id) != 1:
                widths.append(current_width_group)
                widths.append(current_glyph_id)
                current_width_group = []
                prev_glyph_id = current_glyph_id

            current_width_group.append(glyph_set[cmap[c]].width * scale)

        widths.append(current_width_group)

        return widths

class PDFFonts:
    """Class that represents the set of all the fonts added to a PDF document.
    """
    def __init__(self) -> None:
        self.fonts = {}
        self.index = 1
        for font_family, modes in STANDARD_FONTS.items():
            self.fonts[font_family] = {}
            for mode, font in modes.items():
                self.fonts[font_family][mode] = PDFStandardFont(
                    'F'+str(self.index), font['base_font'], font['widths']
                )
                self.index += 1

    def get_font(self, font_family: str, mode: str) -> PDFFont:
        """Method to get a font from its ``font_family`` and ``mode``.

        Args:
            font_family (str): the name of the font family
            mode (str): the mode of the font you want to get. ``n``, ``b``,
                ``i`` or ``bi``.

        Returns:
            PDFFont: an object that represents a PDF font.
        """
        if font_family in STANDARD_FONTS:
            family = self.fonts[font_family]
        else:
            font_type = (font_family, mode)
            if font_type in PDFFont.registered_fonts:
                if font_type not in PDFFont.loaded_fonts:
                    self.load_font(PDFFont.registered_fonts[font_type],
                        font_family,
                        mode)
                    PDFFont.loaded_fonts.append(font_type)
                family = self.fonts[font_family]
            else:
                raise ValueError('Unknown font family requested!')
            
        return family['n'] if mode not in family else family[mode]

    def load_font(self, path: str, font_family: str, mode: str='n') -> None:
        """Method to add a TrueType font to this instance.

        Args:
            path (str): the location of the font file.
            font_family (str): the name of the font family
            mode (str, optional): the mode of the font you want to get.
                ``n``, ``b``, ``i`` or ``bi``.
        """
        font = PDFTrueTypeFont('F'+str(self.index), path)
        if not font_family in self.fonts:
            self.fonts[font_family] = {'n': font}
        self.fonts[font_family][mode] = font
        self.index += 1

from .parser import PDFObject
from .base import PDFBase
from .utils import as_hex, subs
