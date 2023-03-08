'''
This file defines how the script is meant to be utilized
'''

import argparse

def encrypt():
    pass

def decrypt():
    pass

'''
We have to pass arguments within the commandline execution in order to get an output

1. Whether to encrypt or decrypt
2. The text to be encrypted or decrypted
3. The algorithm to use for encryption or decryption
'''
argparser = argparse.ArgumentParser()
argparser.add_argument("-e", "--encrypt", help="flag to use to specify encryption", action='store_true' )
argparser.add_argument("-d", "--decrypt", help="flag to use to specify decryption", action='store_true' )
argparser.add_argument("-t", "--text", help="text to be encrypted or decrypted" )
argparser.add_argument("-f", "--file", help="file whose text is to be encrypted or decrypted" )
argparser.add_argument("-a", "--algo", type=str, help="algorithm to be used for encryption/decryption")

args = argparser.parse_args()

algo = ''

if args.algo:
    algo = str.lower(args.algo)

text = ''

if args.text and args.file:
    raise Exception("Please specify a single source text")
elif args.text:
   text = args.text
elif args.file:
    # TODO: Read file content and assign it to text
    text = ''
else:
    raise Exception("Please specify a source text to encrypt or decrypt")


if(args.encrypt and args.decrypt):
    raise Exception("You cannot use the encrypt and decrypt flags together. Please choose either one!")
elif args.encrypt:
    encrypt()
elif args.decrypt:
    decrypt()
else:
    raise Exception("You must specify either -e or -d flag to proceed")
