"""
Creates two lists of lists—data and scores. The data list holds ages, heights,
and weights for 12 athletes. The scores list holds three exam scores for 12
students. The data list is put directly into df1, and the scores list is put
directly into df2. Averages are computed and displayed.
"""
import pandas as pd
import numpy as np
if __name__ == "__main__":
    data = [
        [41, 72, 180], [27, 66, 140],
        [18, 59, 101], [57, 72, 160],
        [21, 59, 112], [29, 77, 250],
        [55, 60, 120], [28, 72, 110],
        [19, 59, 99], [32, 68, 125],
        [31, 79, 322], [36, 69, 111]
    ]
    scores = [
        [99, 90, 88], [77, 66, 81], [78, 77, 83],
        [75, 72, 79], [88, 77, 93], [88, 77, 94],
        [100, 99, 93], [94, 74, 90], [98, 97, 99],
        [73, 68, 77], [55, 50, 68], [36, 77, 90]
    ]
    n = 3
    key1 = ['age', 'height', 'weight']
    df1 = pd.DataFrame(data, columns=key1)
    print('df1 slice:\n', df1.head(n))


    print('\naverage by columns:')
    avg_cols = df1.apply(np.mean, axis=0)
    print(avg_cols)

    print('\naverage weight')
    avg_wt = df1[['weight']].apply(np.mean, axis="index")
    print(avg_wt)

    key2 = ['exam1', 'exam2', 'exam3']
    df2 = pd.DataFrame(scores, columns=key2)
    print('\ndf2 slice:\n', df2.head(n))
    avg_scores = df2.apply(np.mean, axis=1)

    print('\naverage scores for 1st', n, 'students (rows):')
    print(avg_scores.head(n))

    avg_slice = df2[['exam1', 'exam3']].apply(np.mean, axis="columns")
    print('\naverage "exam1" & "exam3" 1st', n, 'students (rows):')
    print(avg_slice[0:n])
