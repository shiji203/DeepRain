import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def generate_stuff(dim, p=0.01, pad=5, sigma=3, scale=True):
    array = np.zeros(dim)
    array = np.random.choice([0,1],size=dim,p=[1-p, p])
    array = add_padding_border(array, pad_value=0, size=pad)
    array = gaussian_filter(array,sigma=sigma)

    if scale:
        array = array/np.max(array)

    return array

def add_padding_border(array, pad_value=0, size=2):
    pad = np.zeros((array.shape[0],size))
    pad.fill(pad_value)
    array = np.concatenate((array,pad), axis=1) #rechter Rand
    array = np.concatenate((pad,array), axis=1) #linker Rand
    pad = np.zeros((size, array.shape[1]))
    pad.fill(pad_value)
    array = np.concatenate((array,pad), axis = 0) #unterer Rand
    array = np.concatenate((pad,array), axis = 0) #oberer Rand
    return array

#nur rechtsbewegung beachtet!
#noch keine schrittweite/speed einstellbar!
def generate_one_sample(_dim, n_input, schrittweite=2, pad=5):
    internPAD = 5
    n = n_input+1
    dim = (_dim[0]-2*pad, _dim[1]-2*pad)
    dim2 = (dim[0]-2*internPAD,dim[1]+n*schrittweite-2*internPAD)
    img = generate_stuff(dim2, p=0.01, pad=internPAD, sigma=3, scale=True)
    samplelist=[]
    for i in range(n):
        tmp = img[0:dim[0],schrittweite*i:schrittweite*i+dim[1]]
        tmp = add_padding_border(tmp, pad_value=0, size=pad)
        if i == n_input:
            label = tmp
        else:
            samplelist.append(tmp)
    return np.array(samplelist), label

def plot_6_images(data, label):
    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
    f.suptitle('Data and Labels')
    ax1.imshow(data[0])
    ax2.imshow(data[1])
    ax3.imshow(data[2])
    ax4.imshow(data[3])
    ax5.imshow(data[4])
    ax6.imshow(label)
    plt.show()
    return

if __name__ == '__main__':

    if True:
        data, label = generate_one_sample((100,100), 5, schrittweite=10)
        print(data.shape, label.shape)
        #Shape von Data = (n,x,y)
        plot_6_images(data, label)
    else:
        a = generate_stuff(dim=(100,200))
        print(a.shape)
        plt.imshow(a, vmin=0, vmax=1, cmap='gray')
        plt.show()