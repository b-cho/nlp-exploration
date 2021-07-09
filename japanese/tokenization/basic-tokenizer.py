import MeCab
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="MeCab-based tokenizer.")
parser.add_argument('files', metavar='files', nargs='*', default=[], help='Files to convert to .txt format.')
args = parser.parse_args()

wakachi = MeCab.Tagger('-Owakati')

def tokenize(text):
    return ' '.join(wakachi.parse(text).split())

for fl in args.files:
    input_path = Path(fl)
    input_file = open(input_path, mode='r', encoding='utf-8')
    input_text = input_file.read()

    tokenized_text = tokenize(input_text)

    output_path = input_path.parent / (input_path.stem + '.tk.txt')
    output_file = open(output_path, mode='w', encoding='utf-8')

    output_file.write(tokenized_text)

    