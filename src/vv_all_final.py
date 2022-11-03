
import pandas as pd
import argparse

def fn_CE(tok,tag,c_or_e):
    tok = tok[1:-1].split(" ")
    tag = tag[1:-1].split(",")

    ret = []

    if(len(tok)==len(tag)):
        strt_tag = "'B-C'"
        ins_tag = "'I-C'"
        if(c_or_e=='e'):
            strt_tag = "'B-E'"
            ins_tag = "'I-E'"
        
        i=0
        while(i<len(tok)):
            cur = ""
            cur_tok = tag[i].strip()
            if(tag[i].strip() == strt_tag):
                cur=cur+" "+tok[i]
                i=i+1
                while(i<len(tok) and tag[i].strip()==ins_tag):
                    cur=cur+" "+tok[i]
                    i=i+1
                ret.append(cur)
                
            else:
                i=i+1
        return ret


parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument(
    "--dataset_name",
    type=str,
    default='altlex_test',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
args = parser.parse_args()

dataset_name = args.dataset_name
file_name = f"/home/vv2116/capstone_data/{dataset_name}_subtask3.csv"
df = pd.read_csv(file_name)
print(df.head())


cols = ["corpus",	"doc_id"	,"sent_id",	"eg_id",	"index",	"text"	,"text_w_pairs"	,"seq_label"	,"pair_label",	"context",	"num_sents"]
df_labels = pd.read_csv(f"./results/subtask3_{dataset_name}_predictions.txt",sep="\t")
df["pair_label"] = df_labels["pair_pred"]

df.to_csv( f"./results/FINAL_{dataset_name}.csv",index=False)








