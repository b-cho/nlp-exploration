import fugashi
import argparse
from pathlib import Path
from tqdm import tqdm

parser = argparse.ArgumentParser(description="MeCab-based tokenizer. MeCabを使用している形態素解析器。")
parser.add_argument('files', metavar='files', nargs='*', default=[], help='Files to convert to .txt format.')
args = parser.parse_args()

tagger = fugashi.Tagger() # Initialize MeCab tagger

def tokenize(text):
    tokens = tagger(text) # Get tokens, see documentation for fields

    def format_output(tokens):
        output_string = ''
        output_string += '{:　<10s}{:　<10s}{:　<10s}{:　<10s}{:　<10s}{:　<10s}\n'.format('言葉', '発音形出現形', '語彙素', '品詞大分類', '品詞中分類', '語種')
        output_string += '-' * 85 + '\n'
        for token in tqdm(tokens):
            output_string += '{:　<10s}{:　<10s}{:　<10s}{:　<10s}{:　<10s}{:　<10s}\n'.format(token.surface, token.feature.pron or '', token.feature.lemma or '', token.feature.pos1 or '', token.feature.pos2 or '', token.feature.goshu or '')

        return output_string

    return format_output(tokens)

for fl in args.files:
    input_path = Path(fl)
    input_file = open(input_path, mode='r', encoding='utf-8')
    input_text = input_file.read()

    tokenized_text = tokenize(input_text)

    output_path = input_path.parent / (input_path.stem + '.tkf.txt')
    output_file = open(output_path, mode='w', encoding='utf-8')

    output_file.write(tokenized_text)

    