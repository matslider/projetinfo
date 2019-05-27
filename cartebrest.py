try:
    from PIL import Image
except ImportError:
    import Image
import numpy as np
carte = Image.open('/Users/matheosacaze/Documents/projet info/image2.png')
cartemat = np.asarray(carte)
#cartemat.setflags(write=1)
(n1,n2,n3) = np.shape(cartemat)
map = np.zeros((n1,n2))
for i in range(n1):
    for k in range(n2):
        if cartemat[i,k,2] <= cartemat[i,k,1] + 5 and cartemat[i,k,2] <= cartemat[i,k,0] + 5:
            map[i,k] = 1