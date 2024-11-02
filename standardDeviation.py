import numpy as np


def calculate(input_list):
    list = input_list
    # print(len(list))
    if (len(list) != 9):
        raise ValueError('Number should be more than 9 numbers')
    new_array  = np.array(list).reshape(3,3)
    print(new_array)
    output = {
        "mean": [
            np.mean(new_array, axis = 1).tolist(),
            np.mean(new_array, axis = 0).tolist(),
            np.mean(new_array).tolist() 
        ],
        "varience": [
            np.var(new_array, axis = 1).tolist(),
            np.var(new_array, axis = 0).tolist(),
            np.var(new_array).tolist()
        ],
        "Standard devoiation":[

            np.std(new_array, axis = 1).tolist(),
            np.std(new_array, axis = 0).tolist(),
            np.std(new_array).tolist()
        ],
        'Max':[
            np.max(new_array, axis = 1).tolist(),
            np.max(new_array, axis = 0).tolist(),
            np.max(new_array).tolist()
        ],
        'Min':[
            np.min(new_array, axis = 1).tolist(),
            np.min(new_array, axis = 0).tolist(),
            np.min(new_array).tolist()
        ],
        'Sum':[
            np.sum(new_array, axis = 1).tolist(),
            np.sum(new_array, axis = 0).tolist(),
            np.sum(new_array).tolist()
        ]
    }
    print(output)


calculate([1,2,3,4,5,6,7,8,9])