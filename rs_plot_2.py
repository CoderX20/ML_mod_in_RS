import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

import rs_mod_1


def show_plot2D(train_list_1=[],train_list_0=[],test_list_1=[],test_list_0=[]):
    """
    制作分布的二维可视化
    """
    pca_tool=PCA(n_components=2)
    pca_tool.fit(train_list_1)
    train_points_1=pca_tool.transform(train_list_1)
    train_points_0=pca_tool.transform(train_list_0)
    test_points_1=pca_tool.transform(test_list_1)
    test_points_0=pca_tool.transform(test_list_0)
    plot.style.use("seaborn")
    plot.scatter([i[0] for i in train_points_1],[i[1] for i in train_points_1],c='red',s=10)
    plot.scatter([i[0] for i in train_points_0],[i[1] for i in train_points_0],c='blue',s=10)
    plot.scatter([i[0] for i in test_points_1],[i[1] for i in test_points_1],c='yellow',marker="s",s=10)
    plot.scatter([i[0] for i in test_points_0],[i[1] for i in test_points_0],c='green',marker="s",s=10)
    plot.show()


def show_plot3D(train_list_1=[],train_list_0=[],test_list_1=[],test_list_0=[]):
    """
    制作分布的三维可视化
    """
    pca_tool=PCA(n_components=3)
    pca_tool.fit(train_list_1)
    train_points_1=pca_tool.transform(train_list_1)
    train_points_0=pca_tool.transform(train_list_0)
    test_points_1=pca_tool.transform(test_list_1)
    test_points_0=pca_tool.transform(test_list_0)
    fig=plot.figure()
    ax=Axes3D(fig)
    ax.scatter([i[0] for i in train_points_1],[i[1] for i in train_points_1],[i[2] for i in train_points_1],c='red',s=10)
    ax.scatter([i[0] for i in train_points_0],[i[1] for i in train_points_0],[i[2] for i in train_points_0],c='blue',s=10)
    ax.scatter([i[0] for i in test_points_1],[i[1] for i in test_points_1],[i[2] for i in test_points_1],c='yellow',s=10)
    ax.scatter([i[0] for i in test_points_0],[i[1] for i in test_points_0],[i[2] for i in test_points_0],c='red',s=10)
    plot.show()



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
    show_plot2D(train_list_1=train_data_vec_1,train_list_0=train_data_vec_0,test_list_1=test_data_vec_1,test_list_0=test_data_vec_0)
    # show_plot3D(train_list_1=train_data_vec_1,train_list_0=train_data_vec_0,test_list_1=test_data_vec_1,test_list_0=test_data_vec_0)
