import numpy as np

def NumpyToList(dictionary):
    outdict = {}
    for keys, values in dictionary.items():
        if type(values) == np.ndarray:
            outdict[keys] = values.tolist()
        else:
            outdict[keys] = values
    return outdict
            
