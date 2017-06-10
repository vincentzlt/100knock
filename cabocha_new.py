
# coding: utf-8

# In[1]:

from pprint import pprint
import sys


# In[2]:

def gen_sent_cabocha(f_name):
    with open(f_name, "r", encoding="utf-8") as f:
        output = []
        for line in f:
            if line.startswith("EOS"):

                if len(output) > 0:
                    yield output
                output = []
            else:
                output.append(line)
        yield output


# In[3]:

class Word():
    def __init__(self, line):
        self.surface, attr = line.split("\t")
        self.pos, self.pos1, self.pos2, self.pos3, self.hy1, self.hy2, self.rt, *self.rd = attr.split(
            ",")
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return self.surface


# In[59]:

class Phrase():
    def __init__(self, lines):
        self.words = []
        self.childs = []
        for line in lines:
            if line.startswith("*"):
                _, self.index, father, head_func, self.dep_value = line.split()
                self.father = int(father[:-1])
                self.head_id, self.particle_id = (
                    int(i) for i in head_func.split("/"))
            else:
                self.words.append(Word(line))
    def __repr__(self):
        return str(self.__dict__)

    @property
    def __str__(self):
        output="".join(w.surface for w in self.words)
        return output


# In[60]:

class Sentence():
    def __init__(self, lines):
        phrase_lines = []
        self.phrases = []
        self.temp = 1

        for line in lines:
            if line.startswith("*"):
                if len(phrase_lines) == 0:
                    phrase_lines.append(line)
                else:
                    #pprint(phrase_lines)
                    self.phrases.append(Phrase(phrase_lines))
                    phrase_lines = []
                    phrase_lines.append(line)
            else:
                phrase_lines.append(line)
        #pprint(phrase_lines)
        self.phrases.append(Phrase(phrase_lines))
        for ind, p in enumerate(self.phrases):
            if p.father != -1:
                self.phrases[p.father].childs.append(ind)

    def __repr__(self):
        return str(self.__dict__)

    @property
    def __str__(self):
        str_list=[p.__str__ for p in self.phrases]
        return str("".join(str_list))


# In[ ]:

def knock_40(Sent):
    # print morpheme list of a sentence with pos information
    for p in Sent.phrases:
        for w in p.words:
            print("{surface}:\tbase:\t{base}\tpos:\t{pos}\tpos1\t{pos1}".
                  format(surface=w.surface, base=w.rt, pos=w.pos, pos1=w.pos1))


# In[ ]:

def knock_41(Sent):
    # print the father_id and phrase
    for p in Sent.phrases:
        father_id = p.father
        phrase = p.__str__
        print("father_id:", str(father_id), "phrase:", phrase, sep="\t")


# In[52]:

def knock_42(Sent):
    # print phrase and its father phrase
    #print(Sent.phrases)
    for p in Sent.phrases:
        #print(p.father)
        if p.father!=-1:
            print(p)
            print(Sent.phrases[p.father])


# In[61]:

for ind, sent in enumerate(gen_sent_cabocha("./neko.txt.cabocha")):
    if ind == 6:
        print("sentence {number}:".format(number=ind + 1), end="\n")
        #knock_42(Sentence(sent))
        tt=Sentence(sent)
        #print(Sentence(sent))
        #pprint(sent)


# In[63]:

tt.phrases[0]


# In[65]:

print(tt.phrases[0].words[0])


