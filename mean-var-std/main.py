import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr1 = list[0:3]
    arr2 = list[3:6]
    arr3 = list[6:]
    matrix = np.array([arr1, arr2, arr3])

    axis0_mean = matrix.mean(axis=0)
    axis1_mean = matrix.mean(axis=1)

    axis0_var = matrix.var(axis=0)
    axis1_var = matrix.var(axis=1)

    axis0_std = matrix.std(axis=0)
    axis1_std = matrix.std(axis=1)

    axis0_max = matrix.max(axis=0)
    axis1_max = matrix.max(axis=1)

    axis0_min = matrix.min(axis=0)
    axis1_min = matrix.min(axis=1)

    axis0_sum = matrix.sum(axis=0)
    axis1_sum = matrix.sum(axis=1)

    mean = [[axis0_mean[0], axis0_mean[1], axis0_mean[2]], [axis1_mean[0], axis1_mean[1], axis1_mean[2]], matrix.mean()]
    variance = [[axis0_var[0], axis0_var[1], axis0_var[2]], [axis1_var[0], axis1_var[1], axis1_var[2]], matrix.var()]
    standard_deviation = [[axis0_std[0], axis0_std[1], axis0_std[2]], [axis1_std[0], axis1_std[1], axis1_std[2]], matrix.std()]
    max = [[axis0_max[0], axis0_max[1], axis0_max[2]], [axis1_max[0], axis1_max[1], axis1_max[2]], matrix.max()]
    min = [[axis0_min[0], axis0_min[1], axis0_min[2]], [axis1_min[0], axis1_min[1], axis1_min[2]], matrix.min()]
    sum = [[axis0_sum[0], axis0_sum[1], axis0_sum[2]], [axis1_sum[0], axis1_sum[1], axis1_sum[2]], matrix.sum()]

    results = {
        'mean': 0, 
        'variance': 0, 
        'standard deviation': 0,
        'max': 0,
        'min': 0,
        'sum': 0
    }

    results['mean'] = mean
    results['variance'] = variance
    results['standard deviation'] = standard_deviation
    results['max'] = max
    results['min'] = min
    results['sum'] = sum

    #return results

    for key,value in results.items():
        print(key, ':', value)  

calculate([0,1,2,3,4,5,6,7,8])