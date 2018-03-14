guy1 = input('Guy1: ')
guy2 = input('Guy2: ')
guy3 = input('Guy3: ')

def bigger_guy(guy1, guy2, guy3):
    if guy1 >= guy2 and guy1 >= guy3:
        return guy1
    elif guy2 >= guy3:
        return guy2
    else:
        return guy3

print(bigger_guy(guy1, guy2, guy3))
