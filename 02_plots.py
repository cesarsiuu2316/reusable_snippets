import matplotlib.pyplot as plt

# General configs: 
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

def histograms(data_frame): 
    data_frame.hist(bins=50, figsize=(20,15))
    plt.show()

