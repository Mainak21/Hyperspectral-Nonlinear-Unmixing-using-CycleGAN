import scipy.io as spio
import pysptools.eea as eea
import pysptools.abundance_maps as amp
import matplotlib.pyplot as plt
import numpy as np
import os
import torch

script_dir = os.path.dirname(__file__)
abundance_dir = os.path.join(script_dir, 'Urban/UrbanAbundance/')
#ppnm_dir = os.path.join(script_dir, 'UrbanPPNM/')
#bilinear_dir = os.path.join(script_dir, 'UrbanBilinear/')

urban = spio.loadmat('Urban_R162.mat', squeeze_me=True)       
#pines_gt = spio.loadmat('Indian_pines_gt.mat', squeeze_me=True)

urban_data = urban['Y']
urban_data = urban_data.T.reshape(307,307,162)
print(urban_data.shape)

ppi = eea.PPI()
urban_ppi = ppi.extract(urban_data, 4, numSkewers=10000, normalize=True, mask=None)                   #U is a numpy array with dimensions (16,200)
indexes =  ppi.get_idx()
print(indexes)
ppi.display()

my_dpi = 227
urban_data = (255 * (urban_data.astype(np.float32) - urban_data.min())/(urban_data.max() - urban_data.min())).astype(np.uint8)

fcls_ppi = amp.FCLS()          #FCLS abundance estimation
amap_ppi = fcls_ppi.map(urban_data, urban_ppi, normalize=False, mask=None)
print(amap_ppi.shape)
#fcls_ppi.display(mask=None, interpolation='none', colorMap='viridis', columns=5, suffix=None)

for i in range(4):
    plt.figure(figsize=(307/my_dpi, 307/my_dpi), dpi=my_dpi)
    plt.imshow(amap_ppi[:,:,i], cmap='gray')
    plt.axis('off')
    plt.savefig(abundance_dir + f'{i+1}.jpg', dpi=my_dpi, bbox_inches='tight',pad_inches = 0)
    plt.show()
'''
## PPNM

h = torch.Tensor(amap_ppi)
j = torch.Tensor(urban_ppi)


ppnm = torch.sigmoid(torch.matmul(h, j))
ppnm = ppnm*256
print(ppnm.max())


for i in range(162):
    plt.figure(figsize=(307/my_dpi, 307/my_dpi), dpi=my_dpi)
    plt.imshow(ppnm[:,:,i], cmap='gray')
    plt.axis('off')
    plt.savefig(ppnm_dir + f'BandPpnm{i+1}.jpg', dpi=my_dpi)
    plt.show()


## Bilinear
bilinear = torch.matmul(h, j) +  0.5 * torch.matmul((h * h), (j * j))   # Hadamard Product
bilinear = bilinear*256
print(bilinear.max())

for i in range(162):
    plt.figure(figsize=(307/my_dpi, 307/my_dpi), dpi=my_dpi)
    plt.imshow(bilinear[:,:,i], cmap='gray')
    plt.axis('off')
    #plt.savefig(bilinear_dir + f'BandBilinear{i+1}.jpg', dpi=my_dpi)
    plt.show()
'''