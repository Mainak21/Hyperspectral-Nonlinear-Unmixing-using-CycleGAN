# Hyperspectral-Nonlinear-Unmixing-using-GAN
Hyperspectral images have huge number of bands (usually above 100), which is able to give the continuous spectrum of reflectances. So the datasets exist as a cube with dimensions of length, width and number of bands. 

Hyperspectral unmixing is the method of decomposing an image cube into the pure spectral signatures found in a scene, which are called **endmembers**. 
The proportion of each endmember can be found in each pixel as pure pixel and mixed pixels. Pure pixels are those pixels which have only one endmember and mixed pixels have multiple endmembers.
The endmembers can be represented in an image with only pure pixels. These images are called **Abundance Maps** of each endmembers.

## Linear Unmixing
Hyperspectral unmixing can be done in different linear methods. In this project, I have used **Pixel Purity Index (PPI)** algorithm to find the spectral signatures, and applied Fully Constrained Least Squares **(FCLS)** method which follows linear mixing model to estimate the abundance maps.

![spectra](https://github.com/Mainak21/Hyperspectral-Nonlinear-Unmixing-using-GAN/Urban_spectralProfile.png)

## Nonlinear Unmixing
This project is generally focused on Nonlinear Unmixing methods. So, here I have a Deep Learning Generative Adversarial Network **CycleGAN**. Here
