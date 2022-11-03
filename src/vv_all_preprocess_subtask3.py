import pandas as pd
import argparse
import logging
# import datetime
from utils.files import set_seeds, make_dir
from utils.logger import get_logger
from datetime import datetime
import itertools



def fn_CE(tok,tag):

    tok = tok[1:-1].split(" ")
    tag = tag[1:-1].split(",")
    
    if(len(tok)==len(tag)):

        i=0
        while(i<len(tok)):

                
            if(tag[i].strip().strip("'") == "B-C" or tag[i].strip().strip("'") == "I-C"):
                
                tok.insert(i,"<ARG0>")
                tag.insert(i,"<ARG0>")
                i=i+2
                while(i<len(tok) and tag[i].strip().strip("'")=="I-C"):
                    i=i+1
                tok.insert(i,"</ARG0>")
                tag.insert(i,"</ARG0>")
                
            else:
                i=i+1

        i=0
        while(i<len(tok)):

            if(tag[i].strip().strip("'") == "B-E" or tag[i].strip().strip("'") == "I-E"):
                
                tok.insert(i,"<ARG1>")
                tag.insert(i,"<ARG1>")
                i=i+2
                while(i<len(tok) and tag[i].strip().strip("'")=="I-E"):
                    i=i+1
                tok.insert(i,"</ARG1>")
                tag.insert(i,"</ARG1>")
                
            else:
                i=i+1

        tok = [x.strip().strip("'") for x in tok]
        return " ".join(tok)
    else:
        with open("results/notags_.txt", "w") as writer:
            writer.write(f"\t{tok}\t{tag}\n")


def fn_CE2(tok,tag):
    try:
        tok = tok[1:-1].split(" ")
        tag = tag[1:-1].split(",")
    except:
        print(tok,tag)

    c = []
    e = []
    if(len(tok)==len(tag)):

        i=0
        while(i<len(tok)):   
            if(tag[i].strip().strip("'") == "B-C" or tag[i].strip().strip("'") == "I-C"):
                start = i
                i = i+1
                while(i<len(tok) and tag[i].strip().strip("'")=="I-C"):
                    i = i+1
                end =i-1
                c.append((start,end))
                
            else:
                i = i+1

        i=0
        while(i<len(tok)):
            if(tag[i].strip().strip("'") == "B-E" or tag[i].strip().strip("'") == "I-E"):
                start = i
                i = i+1
                while(i<len(tok) and tag[i].strip().strip("'")=="I-E"):
                    i = i+1
                end =i-1
                e.append((start,end))  
            else:
                i = i+1


        tok = [x.strip().strip("'") for x in tok]
        # print(c,e)
    else:
        pass

    ce_pairs = list(itertools.product(c,e))
    res = []
    for pair in ce_pairs:
        tok_cpy = tok[:]
        tok_cpy[pair[0][0]] = "<ARG0> "+tok_cpy[pair[0][0]]
        tok_cpy[pair[0][1]] = tok_cpy[pair[0][1]]+" </ARG0>"
        tok_cpy[pair[1][0]] = "<ARG1> "+tok_cpy[pair[1][0]]
        tok_cpy[pair[1][1]] = tok_cpy[pair[1][1]]+" </ARG1>"
        res.append(" ".join(tok_cpy))
    return res


parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument(
    "--dataset_name",
    type=str,
    default='altlex_test',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
args = parser.parse_args()

dataset_name = args.dataset_name

file_name = f"/home/vv2116/capstone_data/{dataset_name}_subtask2.csv"
df = pd.read_csv(file_name)
print(df.head())

df_labels = pd.read_csv(f"./results/subtask2_{dataset_name}_predictions.txt", sep="\t")
df_tokens = pd.read_csv(f"./results/subtask2_{dataset_name}_tokens.csv")

cols = ["corpus",	"doc_id"	,"sent_id",	"eg_id",	"index",	"text"	,"text_w_pairs"	,"seq_label"	,"pair_label",	"context",	"num_sents"]
df["tags"] = df_labels["pred"]
df["tokens"] = df_tokens["text"]

text_w_pairs = pd.Series(df.apply(lambda x: fn_CE2(x["tokens"],x["tags"]),axis=1))
df["repeat"] = text_w_pairs.apply(lambda x : len(x))
df[df["repeat"]>1]["tags"].head()
df = df.loc[df.index.repeat(df['repeat'])].reset_index(drop=True).drop('repeat', axis=1)
df["text_w_pairs"] = text_w_pairs.apply(pd.Series).stack().reset_index(drop=True) 

# df["text_w_pairs"] = df.apply(lambda x: fn_CE(x["tokens"],x["tags"]),axis=1)

# print(df.shape)

df[cols].to_csv( f"/home/vv2116/capstone_data/{dataset_name}_subtask3.csv",index=False)




