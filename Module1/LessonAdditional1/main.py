# Task 1
str1 = "мадам"
str2 = "слово"
str3 = "заказ"

str = str1;
strrev = str[::-1]

if str == strrev:
    print(f"Строка '{str}' палиндром.")
else:
    print(f"Строка '{str}' не палиндром.")
    
# Task 2
str1 = "abcdef"    
str2 = "abcgdef"    

print("\nСтрока 1: " + str1) 
print("Строка 2: " + str2) 

for c in str1: 
	str2 = str2.replace(c, "", 1) 
print("Лишний символ: " + str2) 
