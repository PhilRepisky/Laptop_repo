import numpy as np
import cv2
import os

from matplotlib import pyplot as plt
import matplotlib.animation as animation



class img_proc():

    def __init__(self, save_file,end):

        self.var_dict_ = {}
        self.var_dict_["save_file"] = save_file

        self.data_dict_ = {}
        self.data_dict_["var_0"] = np.zeros((end), dtype=float)
        self.data_dict_["var_1"] = np.zeros((end), dtype=float)

        self.data_dict_["mean_0"] = np.zeros((end), dtype=float)
        self.data_dict_["mean_1"] = np.zeros((end), dtype=float)
        
        self.data_dict_["var_diff"] = np.zeros((end), dtype=float)
        self.data_dict_["mean_diff"] = np.zeros((end), dtype=float)

        self.fig, self.cxs = plt.subplots(3,1, facecolor='w', edgecolor='k' )
        '''
        for i in range(2):
            self.cxs[i] = plt.gca()
        '''
        self.var_array = np.zeros((end), dtype = float)
        
        self.trial = np.linspace(0,end,end)

    def var_mean(self, index, end):

        for cam in range(2):
            curr_file = self.var_dict_["save_file"]  + str(cam)

            img_array = np.genfromtxt(curr_file, skip_header = index-1, skip_footer = end-index , delimiter = ',', dtype = str)

            
            img_array = np.array(img_array, dtype = float)
            self.data_dict_["var_"+str(cam)][index] = np.var(img_array)

            self.data_dict_["mean_"+str(cam)][index] = np.mean(img_array)

            
    def plot(self, end):

        self.data_dict_["var_diff"] = self.data_dict_["var_0"] - self.data_dict_["var_1"] 

        self.data_dict_["mean_diff"] = self.data_dict_["mean_0"] - self.data_dict_["mean_1"] 
        
        for cam in range(2):
            #self.cxs[cam].set_ylim( [0,300] )
            self.cxs[0].plot(self.trial, self.data_dict_["var_" + str(cam)] )
            self.cxs[1].plot(self.trial, self.data_dict_["mean_" + str(cam)] )

        self.cxs[-1].plot(self.trial, self.data_dict_["var_diff"] )
        self.cxs[-1].plot(self.trial, self.data_dict_["mean_diff"] )

if __name__ == "__main__":

    save_file = 'trial_9_26_3_noise_'

    end = 500
    exe = img_proc(save_file,end)

    for i in range(0, end):
        exe.var_mean(i, end)
        print i
    exe.plot(end)

    plt.show()
