formatter = '%r %r %r %r'

print(formatter % (1, 2, 3, 4))
print(formatter % ("uno", "dos", "tres", "quatro"))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (True, False, False, True))
