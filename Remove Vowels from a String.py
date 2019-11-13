
class Solution:
def removeVowels1(S):
    S = S.replace('a', '')
    S = S.replace('e', '')
    S = S.replace('i', '')
    S = S.replace('o', '')
    S = S.replace('u', '')
    return S

def removeVowels2(S):
    vowels = set('aeiou')
    return ''.join(letters for letters in S if letters not in vowels)



# The difference between set() and list() is that unlike lists, sets cannot have multiple instances of the same element.