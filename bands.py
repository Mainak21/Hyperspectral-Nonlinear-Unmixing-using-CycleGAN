import scipy.io as spio
import pysptools.eea as eea
import pysptools.abundance_maps as amp
import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(__file__)
bands_dir = os.path.join(script_dir, 'Urban/UrbanBands/')

urban = spio.loadmat('Urban_R162.mat', squeeze_me=True)       

urban_data = urban['Y']
urban_data = urban_data.T.reshape(307,307,162)
print(urban_data.shape)

my_dpi = 227
urban_data = (255 * (urban_data.astype(np.float32) - urban_data.min())/(urban_data.max() - urban_data.min())).astype(np.uint8)

for i in range(162):
    plt.figure(figsize=(307/my_dpi, 307/my_dpi), dpi=my_dpi)
    plt.imshow(urban_data[:,:,i], cmap='gray')
    plt.axis('off')
    plt.savefig(bands_dir + f'Band{i+1}.jpg', dpi=my_dpi, bbox_inches='tight',pad_inches = 0)
    plt.show()