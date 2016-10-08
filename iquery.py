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
  result_dir='/home/lw/dgd_person_reid_old/external/exp/results/jstl/img_jstl_dgd_fc7_bn'
  #features = np.r_[np.load(osp.join(result_dir, 'train_features.npy')),np.load(osp.join(result_dir, 'val_features.npy')),np.load(osp.join(result_dir, 'test_probe_features.npy')),np.load(osp.join(result_dir, 'test_gallery_features.npy'))]
  #features=np.asarray(features)
  #u=np.load(osp.join(result_dir, 'gallery_features.npy'))
  #v=np.load(osp.join(result_dir, 'probe_features.npy')) 
  w=np.load(osp.join(result_dir,'img_features.npy'))
  #k=np.zeros((u.shape[0],u.shape[0]))
  #D = pairwise_distances(u, v, metric='euclidean',  n_jobs=-2)
  #l={}
  
  #for i in range(u.shape[0]):
	#D = pairwise_distances(features[i].reshape(1,-1), features, metric='euclidean',  n_jobs=-2)
	#resultid=np.argsort(D)[0][1]
	#l[i]=resultid
	#min=1000
	#for j in range(u.shape[0]):
	  #if j!=i:
		#k[i][j]=euclidean(u[i],u[j])
		#if k[i][j] < min:
			#min=k[i][j]
			#index=i
			#resultid=j
	#l[index]=resultid
  
  

  kdt=KDTree(w)
  #fin1 = open('/home/lw/dgd_person_reid_old/reiddata2/P1/gallery.txt', 'r')
  #fin2 = open('/home/lw/dgd_person_reid_old/reiddata2/P1/probe.txt','r')  
  fin3= open('/home/lw/dgd_person_reid_old/img.txt','r')
  fs1=[]
  fs2=[]
  fs3=[]
  #for line1 in fin1.readlines():
	#line1=line1.strip()
	#fs1.append(line1)
  #fin1.close()
  #n=len(fs1)
  #fs1=np.asarray(fs1)
	
  #for line2 in fin2.readlines():
	#line2=line2.strip()
  	#fs2.append(line2)
  #fin2.close()
  #m=len(fs2)
  #fs2=np.asarray(fs2)

  for line3 in fin3.readlines():
	line3=line3.strip()
	fs3.append(line3)
  fin3.close()
  n=len(fs3)
  fs3=np.asarray(fs3)

  #query
  while True:
	index = raw_input('please input a number between 0 and %d, input done to exit :  '%(n-1))
	try:
		index = int(index)
		assert(index>=0 and index<n)
	except:
		print 'Hi man, you just input a mess......'
		continue
	dist, ind = kdt.query(w[index].reshape(1, -1), k=3)
	
	dist, ind = dist[0], ind[0]
	query_id=index
	#result_id1=np.argsort(D[query_id])[0]
	#result_id2=np.argsort(D[query_id])[1]
	#result_id=l[index]
	result_id=ind[1]
	
	query_img=cv2.imread(fs3[query_id])
	result_img=cv2.imread(fs3[result_id])
	#result_img1=cv2.imread(fs2[result_id1])
	#result_img2=cv2.imread(fs2[result_id2])
	cv2.imwrite(str(query_id)+'.jpg',query_img)
	cv2.imwrite(str(result_id)+'first.jpg',result_img)
	#cv2.imwrite(str(result_id2)+'second.jpg',result_img2)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  #parser.add_argument('-i', '--input_txt', type=str,default='/home/lw/dgd_person_reid_old/img.txt', help='input text')
  args = parser.parse_args()
  main(args)
