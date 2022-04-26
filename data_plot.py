# coding:utf-8

import matplotlib.pyplot as plot
import json
import pandas as pd


def make_water_GDP(water_data_list=[],gdp_data_list=[],year=[]):
    """
    制作水体覆盖率与GDP的关系
    """
    fig,ax1=plot.subplots()
    ax1.grid()
    ax1.set_title("Water coverage and GDP")
    ax1.plot(year,water_data_list,c="red",label=" Water coverage")
    ax1.scatter(year,water_data_list,s=50,c="red")
    ax1.set_ylabel("Water coverage")
    plot.legend(loc=2)
    ax2=ax1.twinx()
    ax2.plot(year,gdp_data_list,c="green",label="GDP")
    ax2.scatter(year,gdp_data_list,s=50,c="green")
    ax2.set_ylabel("GDP of Wuhan")
    plot.legend(loc=1)
    plot.show()


def make_water_population(water_data_list=[],people_data_list=[],year=[]):
    """
    制作水体覆盖率与人口的关系
    """
    fig,ax1=plot.subplots()
    ax1.grid()
    ax1.set_title("Water coverage and Population")
    ax1.plot(year,water_data_list,c="red",label=" Water coverage")
    ax1.scatter(year,water_data_list,s=50,c="red")
    ax1.set_ylabel("Water coverage")
    plot.legend(loc=2)
    ax2=ax1.twinx()
    ax2.plot(year,people_data_list,c="green",label="Population")
    ax2.scatter(year,people_data_list,s=50,c="green")
    ax2.set_ylabel("Population of Wuhan")
    plot.legend(loc=1)
    plot.show()


if __name__=="__main__":
    water_cover_path="D:/杂物/RS/Script/result.json"
    gdp_path="D:/杂物/RS/Script/Wuhan GDP.json"
    people_path="D:/杂物/RS/Script/Wuhan people.json"
    with open(gdp_path) as file_json:
        gdp_json_data=json.load(file_json)
    with open(people_path) as file_json:
        people_json_data=json.load(file_json)
    with open(water_cover_path) as file_json:
        water_json_data=json.load(file_json)
    year=["2013","2014","2015","2016","2017","2018","2019"]
    gdp_data_list=[]
    people_data_list=[]
    water_data_list=[]
    for i in year:
        gdp_data_list.append(gdp_json_data[0][i])
        people_data_list.append(people_json_data[0][i])
        water_data_list.append(water_json_data[0][i])
    
    # make_water_population(water_data_list=water_data_list,people_data_list=people_data_list,year=year)
    data=pd.DataFrame({"Water coverage":water_data_list,"Population":people_data_list,"GDP":gdp_data_list})
    print(data.corr())
    
    