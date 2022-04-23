import rs_plot_2
import rs_mod_1


if __name__=="__main__":
    train_dir_name_1=r"D:/杂物/RS/train data/水体/"
    train_dir_name_0=r"D:/杂物/RS/train data/非水体/"
    test_dir_name_1=r"D:/杂物/RS/test dataset/水体/"
    test_dir_name_0=r"D:/杂物/RS/test dataset/非水体/"
    train_tif_list_1=rs_mod_1.get_dir_file_names(train_dir_name_1)
    train_tif_list_0=rs_mod_1.get_dir_file_names(train_dir_name_0)
    test_tif_list_1=rs_mod_1.get_dir_file_names(test_dir_name_1)
    test_tif_list_0=rs_mod_1.get_dir_file_names(test_dir_name_0)
    train_data_vec_1=[]
    train_data_vec_0=[]
    test_data_vec_1=[]
    test_data_vec_0=[]
    for name in train_tif_list_1:
        train_data_vec_1+=rs_mod_1.get_tif_bands(train_dir_name_1+name)
    for name in train_tif_list_0:
        train_data_vec_0+=rs_mod_1.get_tif_bands(train_dir_name_0+name)
    for name in test_tif_list_1:
        test_data_vec_1+=rs_mod_1.get_tif_bands(test_dir_name_1+name)
    for name in test_tif_list_0:
        test_data_vec_0+=rs_mod_1.get_tif_bands(test_dir_name_0+name)
    rs_plot_2.show_plot3D(train_list_1=train_data_vec_1,train_list_0=train_data_vec_0,test_list_1=test_data_vec_1,test_list_0=test_data_vec_0)