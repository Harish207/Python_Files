def anti_vowel(text):
    vowels='aeiou'
    vowels_u=vowels.upper()
    str1 =''
    str2=''
    str3=''
    for i in text:
        if i in vowels or i in vowels_u:
            str2 = str2 + i
        else:
            str1 = str1 + i
    for letter in str1:
        str3 = str3 + letter
    return str3