
def count_vowels(s: str, vowels: int, consonants: int) -> bool:
    if len(s) == 0: return vowels > consonants

    if s[0].lower() in 'aeiuy':
        return count_vowels(s[1:], vowels + 1, consonants)

    elif not s[0].lower() in 'aeiuy' and s[0] != " ":
        return count_vowels(s[1:], vowels, consonants + 1)

    else:
        return count_vowels(s[1:], vowels, consonants)


