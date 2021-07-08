# Installation

## Installing MeCab (with UniDic) on Python3

1. Run `python3 -m pip install mecab-python3 unidic-lite`, as described by the MeCab documentation on [pip](https://pypi.org/project/mecab-python3/).
2. Install [Visual Studio 2015-2019](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0), as directed.
3. ~~Download MeCab from [the MeCab website](https://taku910.github.io/mecab/#install). See [here](https://stackoverflow.com/questions/44829179/mecab-importerror-dll-load-failed-the-specified-module-could-not-be-found) for more information, especially the comment under the original question.~~
   1. ~~Make sure to select `UTF-8` as the dictionary encoding.~~
4. Locate where your Python installation is, then copy the `libmecab.dll` file from `Python\lib\site-packages\MeCab` to `Python\Python{VERSION}\site-packages\MeCab`.

## Installing Fugashi (with UniDic) on Python3

1. Run `python3 -m pip install fugashi unidic-lite`, as described by the MeCab documentation on [pip](https://pypi.org/project/mecab-python3/).
2. Install [Visual Studio 2015-2019](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0), as directed.
3. Locate where your Python installation is, then copy the `libmecab.dll` file from `Python\lib\site-packages\fugashi` to `Python\Python{VERSION}\site-packages\fugashi`.

# Comments and Resources

I prefer using `fugashi` because it has a more Pythonic interface relative to `mecab-python3` and is better maintained. See [here](https://www.dampfkraft.com/nlp/fugashi.html) for more details. In particular, a nice walkthrough of the `fugashi` library can be found [here](https://www.dampfkraft.com/nlp/how-to-tokenize-japanese.html).

More information on UniDic's official field names can be found [here](https://unidic.ninjal.ac.jp/faq#col_name), and are used in `fugashi` as well.

Information on 表記ゆれ (*hyouki-yure*, orthographical variants) can be found [here](https://ja.wikipedia.org/wiki/%E8%A1%A8%E8%A8%98%E3%82%86%E3%82%8C). (Japanese-language Wikipedia)