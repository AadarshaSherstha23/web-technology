phrase = "Ram is a student of Herald College . He is a widely placed in college and is a good student ."
words = []
words= phrase.lower().split()
print(words)
count=0
for i in words:
    count+=words.count(i)
print(count)
count = [words.count(i) for i in words]
print(zip(words,count))
result = dict(zip(words,count))
print(result)