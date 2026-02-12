first = input("Enter your first name: ").title()
last = input("Enter your last name: ").title()
birth = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ")

age = 2026 - birth

print("=" * 30)
print("USER PROFILE CARD")
print("=" * 30)
print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("\nThank you for creating your profile!")



sentence = input("Enter a sentence: ")

total_with_spaces = len(sentence)
total_without_spaces = len(sentence.replace(" ", ""))
words = len(sentence.split())

vowels = sum(1 for ch in sentence.lower() if ch in "aeiou")

print("\nAnalysis Results ---")
print(f"Total characters (with spaces): {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words: {words}")
print(f"Number of vowels: {vowels}")
print(f"Uppercase version: {sentence.upper()}")
print(f"Lowercase version: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Starts with capital: {'Yes' if sentence[0].isupper() else 'No'}")
print(f"Ends with punctuation: {'Yes' if sentence[-1] in '.!?' else 'No'}")