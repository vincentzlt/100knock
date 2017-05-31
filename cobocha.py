import sys

class cabocha_morph(object):
    def __init__(self, f_name):
        self.sentences=[]
        
        
    def get_sentence_block(self, f_name):
        
        sentence_block=[]
        for line in open(f_name,"r",encoding="UTF-8"):
            if not sentence_block:
                sentence_block.append(line)
            if line.startswith("EOS"):
                yield sentence_block
                sentence_block[:]=[]