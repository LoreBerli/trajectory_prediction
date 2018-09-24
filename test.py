import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image


def load_data(file):
    dic={}
    dic_names={}
    with open(file,"r") as dt:
        lns=dt.readlines()
        for l in lns:
            as_arr=l.replace("\n","").split(",")
            if(dic.get(as_arr[2].replace(" ",""))==None):
                dic[as_arr[2].replace(" ","")]=[]
            if(dic_names.get(as_arr[2].replace(" ",""))==None):
                dic_names[as_arr[2].replace(" ","")]=[]

            tot=as_arr[10:]
            dic_names[as_arr[2].replace(" ","")].append(as_arr[1])
            dic[as_arr[2].replace(" ","")].append(tot)
    return dic,dic_names

def to_baricenter(bbox):
    bbox=np.asarray(bbox,dtype=np.float32)
    return bbox[2]-bbox[0],bbox[3]-bbox[1]

def main():
    data,names = load_data("filtered_data")
    for k in data.keys():
        if(len(data[k])>8):
            print([to_baricenter(i) for i in data[k][0:10]])

            #plot_me(data[k],names[k])

def plot_me(bbox,name):
    bbox=np.asarray(bbox,dtype=np.float32)
    fig,ax=plt.subplots(len(name))
    fig.set_size_inches((16,16))
    for i in range(len(name)-1,0,-1):

            n=name[i]
            j=i
            im = np.array(Image.open("data/frames/"+n.replace(" ","")), dtype=np.uint8)
            #im.resize((320,240))
            ax[j].set_axis_off()
            ax[j].imshow(im)

            x=bbox[i,0]*im.shape[1]
            y=bbox[i,1]*im.shape[0]
            rect=patches.Rectangle((x,y),(bbox[i,2]-bbox[i,0])*im.shape[1],(bbox[i,3]-bbox[i,1])*im.shape[0],facecolor='none',linewidth=1,edgecolor='r')
            ax[j].add_patch(rect)
            ax[j].set_axis_off()

    plt.axis('off')
    plt.savefig("prova"+str(name[0])+".png",dpi=600)
    # plt.scatter(bbox[:,0],bbox[:,1])
    # plt.scatter(bbox[:, 2], bbox[:, 3])
    print(name)

main()