# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:39:50 2020

@author: bhara
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:01:15 2020

@author: bhara
"""

from hierarchical_kmeans import hierarchical_kmeans as hkmeans
import numpy as np
import matplotlib.pyplot as plt
from hierarchical_kmeans import tree

count = 1
def plotClustering(nodes,customData):
    global count
    count += 1
    plt.figure()
    plt.scatter(customData[0,:],customData[1,:])
    children = np.array([])
    for node in nodes:
        children = np.append(children,node.children)
    means = np.array([[]]).reshape(2,-1)
    for child in children:
        mean = np.array(child.data).reshape(2,-1)
        means = np.append(means,mean,axis=1)
    x = np.linspace(-10,10,100)
    for i in range(0,means.shape[1],2):
        points = means[:,i:(i+2)]
        print("points:",points)
        point = np.mean(points,axis =1)
        m = -(np.diff(points,axis=1)[0]/np.diff(points,axis=1)[1])
        y = m*((x-point[0]))+point[1]
        axes = plt.gca()
        axes.set_xlim([-15,15])
        axes.set_ylim([-15,15])
        plt.plot(x,y)
        plt.scatter(points[0,:],points[1,:])
    if(children[0].is_leaf_node()):
        return
    else:
        plotClustering(children,customData)
        

def saveHashMap(hk,hashMap):
    leafNodes = []
    hk.root.gather_leaves(leafNodes)
    leafNodes = np.array(leafNodes)
    for node in leafNodes:
        hashMap[node.name] = node.get_additional_data()
        

def generateClusterStructure(depth,desiredDepth,parent):
    parentId = '' if parent.name == 'root' else parent.name
    if(depth>desiredDepth):
            return parent
    depth += 1
    for j in range(2):
        childId = parentId + str(j)
        child = tree(childId)
        child = generateClusterStructure(depth,desiredDepth,child)
        parent.add_child(child)
    return parent


def getDataFromEllipse():
    data = np.empty((2,1))
    a,b = 5,2
    n = 500
    pi = np.pi
    theta = [0,pi/4,pi/2,3*pi/4,pi,5*pi/4,3*pi/2,7*pi/4]
    center = np.array([5,0]).reshape(2,-1)
    centers = np.empty((2,1))
    for t in theta:
        rotation = np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]]).reshape(2,2)
        centers = np.append(centers,np.matmul(rotation,center).reshape(2,1),axis=1)
    centers = np.array(centers,dtype='int').reshape(2,-1)[:,1:]
    for index,t in enumerate(theta):
        for i in range(n):
            rotation = np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]]).reshape(2,2)
            phi = 2*np.pi* np.random.rand()
            rho = np.random.rand()
            pt = np.array([rho*np.cos(phi)*a/2,rho*np.sin(phi)*b/2]).reshape(2,-1)
            rotatedPt = np.matmul(rotation,pt)
            translatedPt = centers[:,index].reshape(2,-1)+rotatedPt.reshape(2,-1)
            data = np.append(data,translatedPt,axis = 1)
    return data[:,1:]
    

plt.close('all')
customData = getDataFromEllipse()
plt.scatter(customData[0,:],customData[1,:])
testClusterStructure = tree('root')
generateClusterStructure(1,3,testClusterStructure)
hk2 = hkmeans(testClusterStructure)
hk2.cluster(customData.T, only_store_id=False, iteration=1)
testTreeRoot = hk2.root
plotClustering([testTreeRoot],customData)










