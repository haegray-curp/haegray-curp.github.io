# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_preprocess_subtask1.py
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/1run_seqbase.py;

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_preprocess_subtask2.py;
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/2run_tokbase.py;

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_preprocess_subtask3.py;
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/3run_pairbase.py;

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------altlex_dedup-------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask1.py --dataset_name "altlex_train" --file_loc "/home/vv2116/capstone/UniCausal/data/grouped/splits/altlex_train.csv"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/1run_seqbase.py --dataset_id "altlex_train" --seq_val_file "/home/vv2116/capstone_data/altlex_train_subtask1.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask2.py --dataset_name "altlex_train"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/2run_tokbase.py --dataset_id "altlex_train" --span_val_file "/home/vv2116/capstone_data/altlex_train_subtask2.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask3.py --dataset_name "altlex_train"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/3run_pairbase.py --dataset_id "altlex_train" --pair_val_file "/home/vv2116/capstone_data/altlex_train_subtask3.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_final.py --dataset_name "altlex_train"

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------semeval2010t8_train-------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask1.py --dataset_name "semeval2010t8_train" --file_loc "/home/vv2116/capstone/UniCausal/data/splits/semeval2010t8_train.csv"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/1run_seqbase.py --dataset_id "semeval2010t8_train" --seq_val_file "/home/vv2116/capstone_data/semeval2010t8_train_subtask1.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask2.py --dataset_name "semeval2010t8_train"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/2run_tokbase.py --dataset_id "semeval2010t8_train" --span_val_file "/home/vv2116/capstone_data/semeval2010t8_train_subtask2.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask3.py --dataset_name "semeval2010t8_train"
# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/3run_pairbase.py --dataset_id "semeval2010t8_train" --pair_val_file "/home/vv2116/capstone_data/semeval2010t8_train_subtask3.csv"

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_final.py --dataset_name "semeval2010t8_train"

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------2017_1-------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

# /ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask1.py --type "polusa" --dataset_name "2017_1_3s" --file_loc="/home/vv2116/capstone/UniCausal/capstone/capstone_data/2017_1_3s.csv" 
/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/1run_seqbase.py --dataset_id "2017_1_3s" --seq_val_file "/home/vv2116/capstone_data/2017_1_3s_subtask1.csv"

/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask2.py --dataset_name "2017_1_3s"
/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/2run_tokbase.py --dataset_id "2017_1_3s" --span_val_file "/home/vv2116/capstone_data/2017_1_3s_subtask2.csv"

/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_preprocess_subtask3.py --dataset_name "2017_1_3s"
/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/3run_pairbase.py --dataset_id "2017_1_3s" --pair_val_file "/home/vv2116/capstone_data/2017_1_3s_subtask3.csv"

/ext3/conda/bootcamp/bin/python /home/vv2116/capstone/UniCausal/vv_all_final.py --dataset_name "2017_1_3s"