import emoji

insertword = str(input("Input: ")).strip()
emojiword = emoji.emojize(insertword, language='alias')

print(emojiword)
