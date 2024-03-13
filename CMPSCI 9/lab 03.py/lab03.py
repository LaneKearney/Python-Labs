def int_division(num, div):
    if num < div:
        return 0
    elif num == div:
        return 1
    else:
        return 1 + int_division((num - div), div)

def get_even_ints(int_list):
    if not int_list:
        return []
    if int_list[0]%2 == 0:
        return [int_list[0]] + get_even_ints(int_list[1:])
    else:
        return get_even_ints(int_list[1:])
        
def count_vowels(text):
    if not text:
        return 0
    if text[0] in ('AaEeIiOoUu'):
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])

def reverse_str(text):
    if not text:
        return ""
    return text[-1] + reverse_str(text[:-1])

def remove_seq(text, seq):
    if not text:
        return ""
    if text.startswith(seq):
        return remove_seq(text[len(seq):], seq)
    else:
        return text[0] + remove_seq(text[1:], seq)

print(remove_seq("CmpscicmpsciCmpsci", "Cmpsci"))
