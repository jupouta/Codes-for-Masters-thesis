import re

## RULES

class Tokenized:

    def __init__(self, sent):
        self.sent = sent

    def process(self):
        self.removeTags()
        self.splitWithSmileys()
        self.splitWithApostrophe()
        self.splitWithPunctuation()
        return self.sent

    # 1
    def removeTags(self):
        current = self.sent
        sentWithoutTags = re.sub(r"<.[^(><.)]+>", "", current)
        self.sent = ' '.join(sentWithoutTags.split())
        return self.sent

    # 2
    def splitWithSmileys(self):
        eyes, noses, mouths = r":;8BX=<\^", r"-~'", r")(/\|DdPp3\^"
        pattern1 = "([%s][%s]?[%s]+)" % tuple(map(re.escape, [eyes, noses, mouths]))
        sentWithSmileySpaced = re.sub(pattern1, r" \1 ", self.sent)
        self.sent = ' '.join(sentWithSmileySpaced.split())
        return self.sent

    # 3
    def splitWithApostrophe(self):
        splitted = re.sub("(\w')", r"\1 ", self.sent)
        self.sent = ' '.join(splitted.split())
        return self.sent

    # 4
    def splitWithPunctuation(self):
        splitted = re.sub(r"(\w)?([\.\,?!]+|[:;]^[pPdD])", r"\1 \2 ", self.sent)
        self.sent = ' '.join(splitted.split())
        return self.sent
