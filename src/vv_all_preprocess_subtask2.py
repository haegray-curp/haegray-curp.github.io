import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument(
    "--dataset_name",
    type=str,
    default='semeval2010t8_train',
    help='List of datasets to include in run. Dataset must be available under "data/splits" folder and presplitted.'
)
args = parser.parse_args()

dataset_name = args.dataset_name
file_name = f"/home/vv2116/capstone_data/{dataset_name}_subtask1.csv"
df = pd.read_csv(file_name)
print(df.head())

cols = ["corpus",	"doc_id"	,"sent_id",	"eg_id",	"index",	"text"	,"text_w_pairs"	,"seq_label"	,"pair_label",	"context",	"num_sents"]
df_labels = pd.read_csv(f"./results/subtask1_{dataset_name}_predictions.txt", sep="\t")

df['seq_label'] = df_labels['seq_pred'].astype('int')
# df = df[~pd.isnull(df['seq_label'])]
df['seq_label'] = df['seq_label'].astype('int')

print(df[df['seq_label']==1].shape)
df["text_w_pairs"] = df["text"]
df["pair_label"] = 1

df[df['seq_label']==1][cols].to_csv( f"/home/vv2116/capstone_data/{dataset_name}_subtask2.csv",index=False)

