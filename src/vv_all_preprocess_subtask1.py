import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument(
    "--dataset_name",
    type=str,
    default='altlex_test',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
parser.add_argument(
    "--file_loc",
    type=str,
    default='altlex_test',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
parser.add_argument(
    "--type",
    type=str,
    default='altlex_test',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
args = parser.parse_args()

dataset_name = args.dataset_name
file_loc = args.file_loc
df = pd.read_csv(file_loc)
print(df.columns)

#The columns we need [corpus	doc_id	sent_id	eg_id	index	text	text_w_pairs	seq_label	pair_label	context	num_sents]
cols = ["corpus",	"doc_id"	,"sent_id",	"eg_id",	"index",	"text"	,"text_w_pairs"	,"seq_label"	,"pair_label",	"context",	"num_sents"]

if(args.type=='polusa'):
    df["corpus"] = "polusa"
    df["doc_id"] = dataset_name
    df["sent_id"] = df["id"]    
    df["eg_id"] = 0
    df["index"] = df["id"]
    df["text"] = df["body"].str.lower()
    df["text_w_pairs"] = ""
    df["seq_label"] = 0
    df["pair_label"] = -1
    df["context"] = ""
    df["num_sents"] =2

df[cols].to_csv( f"/home/vv2116/capstone_data/{dataset_name}_subtask1.csv",index=False)
print(df.head())



