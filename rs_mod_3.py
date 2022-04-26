# coding:utf-8

import pickle
import rs_mod_1
import numpy as np


def get_water_cover_level(mod_path="",data_dir_name=""):
    """
    计算水体覆盖率
    """
    out=[]
    with open(mod_path,'rb') as file_pickle:
        rs_mod=pickle.load(file_pickle)
    year_tif_file_names=rs_mod_1.get_dir_file_names(dir_name=data_dir_name)
    for file_name in year_tif_file_names:
        pixel_list=rs_mod_1.get_tif_bands(tif_file=data_dir_name+file_name)
        predict_list=rs_mod.predict(pixel_list)
        water_cover_level=len([x for x in predict_list if int(x)==1])/len(predict_list)
        out.append({file_name:water_cover_level/0.6115410378097966})
    # pixel_list=rs_mod_1.get_tif_bands(tif_file=r"D:/杂物/RS/Image/Wuhan RS data/2013.tif")
    # print(np.array(pixel_list).shape)
    # predict_list=rs_mod.predict(pixel_list)
    # water_cover_level=len([x for x in predict_list if int(x)==1])/len(predict_list)
    # out.append({"2013":water_cover_level})
    return out


if __name__=="__main__":
    years_path=r"D:/杂物/RS/Image/Wuhan RS data/"
    mod_path=r"D:/杂物/RS/Script/train mod/RS_SVM-1.pickle"
    res_list=get_water_cover_level(mod_path=mod_path,data_dir_name=years_path)
    for year_data in res_list:
        print(year_data)
