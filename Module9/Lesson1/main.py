def apply_all_func(int_list, *functions):
    ret = {}
    for f in functions:
        ret[f.__name__] = f(int_list)
    return ret

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
