text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
words = text.split()
fin_words = []
for word in words:
    if word[-1] == ',':
        transformed = word[:-1] + 'ing' + word[-1]
        fin_words.append(transformed)
    else:
        transformed = word + 'ing'
        fin_words.append(transformed)
print(' '.join(fin_words))
