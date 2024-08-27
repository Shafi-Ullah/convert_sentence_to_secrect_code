

import random
choose = ["dog","gyj","hjk","fgy","eft","sry","yzx","vwh","hyd","ynd","heo","vuy","joy","ban","has"]

string = (input("Enter Some things:  " ))
list = string.split(" ")
coded_value = []
coding = True

if (coding):
   for word in list:
       if (len(word) >= 3):
          r1 = random.choice(choose)
          r2 = random.choice(choose)
          secret_words = r1 + word[-1] + word[1:-1]+word[0] + r2
          coded_value.append(secret_words)
       else:
           coded_value.append(word[::-1])
   print("")
   print(" ".join(coded_value))

else:   
    for word in list:
       if (len(word) >= 3):
          unordered_word = word[3:-3]
          natural_word = unordered_word[-1] + unordered_word[1:-1] + unordered_word[0]
          coded_value.append(natural_word)
       else:
           coded_value.append(word[::-1])
    print("")
    print(" ".join(coded_value))
print("\n          😎 Coded by Shafi 😎           ")    
    

