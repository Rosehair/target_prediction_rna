import numpy as np
from src import deepTarget_utils as bio_utils

# rewritting one source functions to act as I want
def make_train_pair(mirna_ids, mirna_seqs, mrna_ids, mrna_seqs, query_ids, target_ids, labels):
    X_query_ids = []
    X_query_seqs = []
    X_target_ids = []
    X_target_seqs = []
    Y = []
    for i in range(len(query_ids)):
        try:
           j = mirna_ids.index(query_ids[i])
           k = mrna_ids.index(target_ids[i])
        except:
            continue
            
        query_seqs, target_seqs = bio_utils.make_pair(mirna_seqs[j], mrna_seqs[k])
        nb_pairs = len(query_seqs)
        if nb_pairs > 0:
            querys = [query_ids[i] for k in range(nb_pairs)]
            X_query_ids.extend(querys)
            X_query_seqs.extend(query_seqs)
            targets = [target_ids[i] for k in range(nb_pairs)]
            X_target_ids.extend(targets)
            X_target_seqs.extend(target_seqs)
            y = [labels[i] for k in range(nb_pairs)]
            Y.extend(y)

    Y = np.array([[Y[i]] for i in range(len(Y))], 'uint8')
    return X_query_ids, X_query_seqs, X_target_ids, X_target_seqs, Y

def comp(seq):
    wc_pairs = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    rc_seed = ''
    for i in seq:
        rc_seed += wc_pairs[i]
    return rc_seed
