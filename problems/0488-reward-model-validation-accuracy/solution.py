import numpy as np

def reward_model_validation(
    chosen_scores: np.ndarray,
    rejected_scores: np.ndarray,
    margin_thresholds: list[float]
) -> dict:
    """
    Compute validation metrics for a reward model on held-out preference pairs.

    Args:
        chosen_scores: 1D array of reward scores for preferred responses.
        rejected_scores: 1D array of reward scores for rejected responses.
        margin_thresholds: List of thresholds for margin-based accuracy.

    Returns:
        Dictionary with 'accuracy', 'mean_margin', 'concordance', 'margin_accuracy'.
    """
    accuracy=0
    mean_margin=0
    mt=len(margin_thresholds)
    margin_acc_val=[0]*mt
    concordance=0
    t=0
    n=len(chosen_scores)
    a=0
    b=0
    c=0
    margins=np.zeros(n)
    for i in range(n):
        
        margins[i]=chosen_scores[i]-rejected_scores[i]

        for j in range(mt):
            if(margins[i]>=margin_thresholds[j]):
               margin_acc_val[j]+=1

        mean_margin+=margins[i]

        if(margins[i]>0):
            accuracy+=1
        elif(margins[i]==0):
            t+=1
    for i in range(mt):
        margin_acc_val[i]/=n
        margin_acc_val[i]=round(margin_acc_val[i],4)
    mean_margin/=n
    accuracy/=n
    concordance=(accuracy*n+0.5*t)/n
    margin_accuracy=dict(zip(margin_thresholds,margin_acc_val))
    dic={}
    dic['accuracy']=round(accuracy,4)
    dic['mean_margin']=mean_margin
    dic['concordance']=concordance
    dic['margin_accuracy']=margin_accuracy
    return dic
    pass