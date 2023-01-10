# # # ex1
# pattern = ["o", "O"]
#
# password_correct = False
# while not password_correct:
#     Inp = input("Enter 'O' letter: ")
#     for letter in Inp:
#         if letter in pattern:
#             print("Your password is correct")
#             password_correct = True
#             break
#
# # ex2
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2 = []
# for item in lst1:
#
#     if type(item) is str:
#         lst2.append(item)
#         print(item)
# ex3
pattern = ["o", "O"]
counter = 0
pre_letter = None
and_word_pattern = [" ", ",", ".", "!", "?"]
text = 'Hello, loremo ? Ipsum'
for letter in text:
    if pre_letter in pattern and letter in and_word_pattern:
        counter = counter+1

    pre_letter = letter

if pre_letter in pattern:
    counter = counter + 1
print(counter)
