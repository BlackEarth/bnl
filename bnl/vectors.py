
import numpy

def similarity(v1, v2):
    return numpy.dot(v1, v2) / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2))

def average(vectors):
    if len(vectors)==0:
        return vectors
    elif len(vectors)==1: 
        return vectors[0]
    else:
        s = vectors[0]
        for v in vectors[1:]:
            s = s + v
        return s / len(vectors)

