import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    data = np.array(list).reshape(3,3)
    output = {
        'mean': [
            np.mean(data, axis=1).tolist(),
            np.mean(data, axis =0).tolist(),
            np.mean(data).tolist()
        ],
        'varience': [
            np.var(data, axis =1).tolist(),
            np.var(data, axis = 0).tolist(),
            np.var(data).tolist()
        ]
    }
    print(output)


calculate([1,2,3,4,5,6,7,8,9])