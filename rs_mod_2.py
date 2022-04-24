# coding: utf-8

import rs_mod_1
import pickle

def test_mod(mod_path=r"",test_dataset=[]):
    """
    对模型进行精度测试
    :param test_data:list[dict]
    """
    dataset_true_count=len([value for value in test_dataset if value["class"]==1])
    dataset_false_count=len([value for value in test_dataset if value["class"]==0])
    true_count=0
    count_1=0
    false_count=0
    count_0=0
    with open(mod_path,'rb') as file_pickle:
        mod=pickle.load(file_pickle)
    for value in test_dataset:
        pre_result=int(mod.predict([value['value']])[0])
        if pre_result==1:
            count_1+=1
            if pre_result==value['class']:
                true_count+=1
        else:
            count_0+=1
            if pre_result==value['class']:
                false_count+=1
    
    Accuracy=(true_count+false_count)/(dataset_true_count+dataset_false_count)
    Precision=true_count/count_1
    Recall=true_count/dataset_true_count
    F1=0
    if (Precision+Recall)!=0:
        F1=2*(Precision*Recall)/(Precision+Recall)
    return {"Accuracy":Accuracy,"Precision":Precision,"Recall":Recall,"F1":F1}


def make_test_dataset(test_dir_path_1="",test_dir_path_0=""):
    """
    制作测试数据集
    """
    out=[]
    test_data_1=rs_mod_1.get_dir_file_names(dir_name=test_dir_path_1)
    tets_data_0=rs_mod_1.get_dir_file_names(dir_name=test_dir_path_0)
    test_data_vec_1=[]
    test_data_vec_0=[]
    for file_name in test_data_1:
        test_data_vec_1+=rs_mod_1.get_tif_bands(tif_file=test_dir_path_1+file_name)
    for test_value in test_data_vec_1:
        out.append({"value":test_value,"class":1})
    for file_name in tets_data_0:
        test_data_vec_0+=rs_mod_1.get_tif_bands(tif_file=test_dir_path_0+file_name)
    for test_value in test_data_vec_0:
        out.append({"value":test_value,"class":0})
    return out


if __name__=="__main__":
    mod_path='D:/杂物/RS/Script/train mod/RS_SVM-1.pickle'
    test_path_1='D:/杂物/RS/test dataset/水体/'
    test_path_0='D:/杂物/RS/test dataset/非水体/'
    test_dataset=make_test_dataset(test_dir_path_1=test_path_1,test_dir_path_0=test_path_0)
    test_result=test_mod(mod_path=mod_path,test_dataset=test_dataset)
    for key,value in test_result.items():
        print(key,value)

    