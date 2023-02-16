def choose(n, k):
    '''
        Función para calcular el número combinatorio n sobre k
    '''
    import math
    if (n >= k and k >= 0):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    else:
        return 'No se puede calcular el número factorial indicado'
    
def pascal_triangle(n = 1):
    print(1)
    for i in range(1, n + 1):
        for k in range(i + 1):
            print(choose(i, k), end = ' ')
        print('')

pascal_triangle(5)