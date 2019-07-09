# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib

string = zlib.compress(
    bytes("hello world!hello world!hello world!hello world!".encode("utf-8")))

print(string)

print(zlib.decompress(string))
