# coding:utf-8

import os
import pickle

import numpy as np
from osgeo import gdal
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def get_dir_file_names(dir_name=""):
    """
    获得指定目录下的所有文件名称
    :param dir_name: str
    :return: list
    """
    out=[]
    for file_root,dirs,files in os.walk(dir_name):
        for file in files:
            out.append(file)
    return out
    


def get_tif_bands(tif_file=r""):
    """
    获取图像像元点波段值
    """
    out=[]
    dataset=gdal.Open(tif_file,gdal.GA_ReadOnly)
    tif_x_size=dataset.RasterXSize
    tif_y_size=dataset.RasterYSize
    im_data=dataset.ReadAsArray(0,0,tif_x_size,tif_y_size)
    band1=dataset.GetRasterBand(1)
    band2=dataset.GetRasterBand(2)
    band3=dataset.GetRasterBand(3)
    band4=dataset.GetRasterBand(4)
    im_data1=band1.ReadAsArray(0,0,tif_x_size,tif_y_size)
    im_data2=band2.ReadAsArray(0,0,tif_x_size,tif_y_size)
    im_data3=band3.ReadAsArray(0,0,tif_x_size,tif_y_size)
    im_data4=band4.ReadAsArray(0,0,tif_x_size,tif_y_size)
    # print(im_data1.shape,im_data2.shape,im_data3.shape,im_data4.shape,im_data.shape)
    for i in range(tif_x_size):
        for j in range(tif_y_size):
            out.append([im_data1[j][i],im_data2[j][i],im_data3[j][i],im_data4[j][i]])
    del dataset
    return out
    


if __name__=="__main__":
    water_tif_list=get_dir_file_names(dir_name=r"D:/杂物/RS/train data/水体/")
    other_tif_list=get_dir_file_names(dir_name=r"D:/杂物/RS/train data/非水体/")
    for i in water_tif_list:
        water_data_vec=get_tif_bands(r"D:/杂物/RS/train data/水体/"+i)
    # print("water data shape:"+str(np.array(water_data_vec).shape))
    for i in other_tif_list:
        other_data_vec=get_tif_bands(r"D:/杂物/RS/train data/非水体/"+i)
    # print("other data shape:"+str(np.array(other_data_vec).shape))
    x=np.array(water_data_vec+other_data_vec)
    y=np.concatenate((np.ones(len(water_data_vec)),np.zeros(len(other_data_vec))))
    X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=3)

    rs_mod=SVC(kernel="rbf",C=0.8)
    rs_mod.fit(X_train,Y_train)
    print(rs_mod.score(X_test,Y_test))

    with open('./train mod/RS_SVM-1.pickle','wb') as file_pickle:
        pickle.dump(rs_mod,file_pickle)
