from cmath import exp, pi
import json

def convert_json_to_array(json_arr,key):
    Y = []
    X = []
    for point in json_arr:
#        print point['y']
        Y.append(point[key])
    return Y

# Fast Fourier Transform 

def FFT(X):
    n = len(X)
    w = exp(-2*pi*1j/n)
    if n > 1:
        X = FFT(X[::2])+FFT(X[1::2])
        for k in xrange(n/2):
            xk = X[k]
            X[k] = xk + w**k*X[k+n/2]
            X[k+n/2] = xk - w**k*X[k+n/2]
    return X

def fft_intensity (X):
    I = []
    for x in X:
        I.append(abs(x))
    return I

def time_to_freq(X,factor):
    F = []
    for x in X:
        F.append(x*factor)
    return F

def FFT_json(json_arr):
    I = fft_intensity(FFT(convert_json_to_array(json_arr,'y')))
    F = time_to_freq(convert_json_to_array(json_arr,'x'),1000)
    points = []
    for i in xrange(len(I)):
        points.append({'x':F[i], 'y':I[i]})
    return json.dumps(points)
