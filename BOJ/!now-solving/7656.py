# 7656

import re

text = input()
queries = re.findall("What is.*?[?]", text)

for query in queries:
  query = re.sub("What", "Forty-two", query)
  query = re.sub("[?]", ".", query)
  print(query)
