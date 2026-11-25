# Case Study 36: Repeated Word and Phrase Detection
text = input("Enter a sentence or paragraph: ").lower()

for mark in ".,!?;:":
    text = text.replace(mark, " ")

words = text.split()
found = []

print("Repeated words:")
for word in words:
    count = words.count(word)
    if count > 1 and word not in found:
        print(f"{word}: {count} times")
        found.append(word)

if not found:
    print("No repeated words found.")
