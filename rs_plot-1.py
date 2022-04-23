import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

import rs_mod_1

if __name__=="__main__":
    water_tif_list=rs_mod_1.get_dir_file_names(dir_name=r"D:/杂物/RS/train data/水体/")
    other_tif_list=rs_mod_1.get_dir_file_names(dir_name=r"D:/杂物/RS/train data/非水体/")
    for i in water_tif_list:
        water_data_vec=rs_mod_1.get_tif_bands(r"D:/杂物/RS/train data/水体/"+i)
    # print("water data shape:"+str(np.array(water_data_vec).shape))
    for i in other_tif_list:
        other_data_vec=rs_mod_1.get_tif_bands(r"D:/杂物/RS/train data/非水体/"+i)
    # print("other data shape:"+str(np.array(other_data_vec).shape))
    pca_tool=PCA(n_components=3)
    pca_tool.fit(water_data_vec)
    x1_points=pca_tool.transform(water_data_vec)
    x0_points=pca_tool.transform(other_data_vec)
    # plot.style.use("seaborn")
    # plot.scatter([i[0] for i in x1_points],[i[1] for i in x1_points],c='red',s=10)
    # plot.scatter([i[0] for i in x0_points],[i[1] for i in x0_points],c='blue',s=10)
    # plot.show()
    fig=plot.figure()
    ax=Axes3D(fig)
    ax.scatter([i[0] for i in x1_points],[i[1] for i in x1_points],[i[2] for i in x1_points],c='red')
    ax.scatter([i[0] for i in x0_points],[i[1] for i in x0_points],[i[2] for i in x0_points],c='blue')
    plot.show()