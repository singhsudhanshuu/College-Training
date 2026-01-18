def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

result = count_vowels("Hello World")
print("Number of vowels:", result)
