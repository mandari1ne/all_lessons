# import os
#
# class FileObject:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#         words = ['trulala\n', 'kukuku\n', 'opopoop\n', 'eheheh\n', 'wawaway\n']
#
#         self.file = open(self.file_name, 'w+')
#         self.file.writelines(words)
#
#     def read_file(self):
#         self.file.seek(0)
#
#         return self.file.read()
#
#     def __del__(self):
#         self.file.close()
#
#         os.remove(self.file_name)
#
# file_obj = FileObject('words.txt')
# print(file_obj.read_file())

# from functools import total_ordering
#
# @total_ordering
# class Word(str):
#     def __new__(cls, word):
#         if ' ' in word:
#             word = word[:word.index(' ')]
#         return str.__new__(cls, word)
#
#     def __gt__(self, other):
#         return len(self) > len(other)
#
# exmpl = Word('Один два')
# print(exmpl > 'два')
# print(exmpl < 'два')
# print(exmpl == 'два')
# print(exmpl != 'два')


