#!/usr/bin/env python2.7
# coding: utf-8

import os.path as osp
import pickle
import argparse
import cv2
import numpy as np
from sklearn.neighbors import KDTree
from scipy.spatial.distance import euclidean
from sklearn.metrics.pairwise import pairwise_distances
def main(args):
  result_dir='/home/lw/dgd_person_reid_old/external/exp/results/dgd/ilids_jstl_dgd_fc7_bn'
  #features = np.r_[np.load(osp.join(result_dir, 'train_features.npy')),np.load(osp.join(result_dir, 'val_features.npy')),np.load(osp.join(result_dir, 'test_probe_features.npy')),np.load(osp.join(result_dir, 'test_gallery_features.npy'))]
  
  v=np.load(osp.join(result_dir, 'test_probe_features.npy'))
  u=np.load(osp.join(result_dir, 'test_gallery_features.npy'))
  k=np.zeros((u.shape[0],v.shape[0]))
  D = pairwise_distances(u, v, metric='euclidean',  n_jobs=-2)
  
  #l={}
  #for i in range(u.shape[0]):
	#min=euclidean(u[i],v[0])
	#index=i
	#resultid=0
	#for j in range(v.shape[0]):
		#k[i][j]=euclidean(u[i],v[j])
		#if k[i][j] < min:
			#min=k[i][j]
			#index=i
			#resultid=j
	#l[index]=resultid
  

  #kdt=KDTree(features)
  fin1 = open('test_gallery1.txt', 'r')
  fin2 = open('test_probe1.txt','r')  
  fs1=[]
  fs2=[]
  for line1 in fin1.readlines():
	line1=line1.strip()
	fs1.append(line1)
  fin1.close()
  n=len(fs1)
  fs1=np.asarray(fs1)
	
  for line2 in fin2.readlines():
	line2=line2.strip()
  	fs2.append(line2)
  fin2.close()
  m=len(fs2)
  fs2=np.asarray(fs2)
  #query
  while True:
	index = raw_input('please input a number between 0 and %d, input done to exit :  '%(n-1))
	try:
		index = int(index)
		assert(index>=0 and index<n)
	except:
		print 'Hi man, you just input a mess......'
		continue
	#dist, ind = kdt.query(features[index].reshape(1, -1), k=6)
	
	#dist, ind = dist[0], ind[0]
	query_id=index
	result_id=np.argsort(D[query_id])[0]
	#result_id=l[index]
	#result_id=ind[1]
	query_img=cv2.imread(fs1[query_id])
	result_img=cv2.imread(fs2[result_id])
	cv2.imwrite(osp.join('/home/lw',str(query_id)+'.jpg'),query_img)
	cv2.imwrite(osp.join('/home/lw',str(result_id)+'result.jpg'),result_img)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  #parser.add_argument('-i', '--input_txt', type=str,default='ilids.txt', help='input text')
  args = parser.parse_args()
  main(args)
