"""
	two parameters to tune
	k-nearest neighbors
	sample number
"""

import numpy as np
import random 
class RelieF:
	def __init__(self,data,label):
		self.data = np.array(data)
		self.label = np.array(label)
		self.item_num = len(label)
		self.labelset = list(set(self.label))
		self.num_label = len(self.labelset)
		self.label_freq = np.zeros(self.num_label)
		for l in self.label:
			for idx,la in enumerate(self.labelset):
				if l == la:
					self.label_freq[idx] += 1
					break




	def find_nearest_data(self, pivot):
		"""
			Return the index of the k nearest hits and mits, respectively
		"""
		R = self.data[pivot]
		k = 7

		d = abs(np.sum(R-self.data,axis=1))
		# sorted_dist = [(dist,index,label)]
		sorted_dist = sorted(zip(d,np.arange(0,self.item_num),self.label,),cmp=lambda x,y:cmp(x[0],y[0]))
		num_D = [0 for x in range(self.num_label)]
		num_D_total = 0
		D = [[] for x in range(self.num_label)]
		i = 0

		while num_D_total<self.num_label*k:
			current_label = sorted_dist[i][2]
			if num_D[current_label]<k:
				D[current_label].append(sorted_dist[i][1])
				num_D[current_label] += 1
				num_D_total += 1
			i += 1

			if(i>=self.item_num):
				break

		return D

	def gen_rand_sample(self):
		
		pivot = random.randint(0,self.item_num-1)
		return pivot

	def compute_sum_diff(self,feature,pivot,neighbors):
		"""
			Compute the sum of the distance from the k nearest neighbors to the selected
			pivot.
		"""
		k = len(neighbors)
		if k == 0 :
			return 0
		pivot_value = self.data[pivot]
		sum_diff = 0
		feature_column = self.data[:,feature]
		feature_max = max(feature_column)
		feature_min = min(feature_column)

		for nidx in neighbors:
			sum_diff += abs(feature_column[nidx]-feature_column[pivot])*1.0/(feature_max-feature_min)
		return sum_diff*1.0/k



	def select(self,samples):
		feature_num = len(self.data[0])
		#print feature_num
		weights = np.zeros(feature_num)
		for i in range(samples):
			pivot = self.gen_rand_sample()
			D = self.find_nearest_data(pivot)

			#print Dh, Dm
			for f in range(feature_num):
				for idx, Dn in enumerate(D): # index is the index for labels in label_set
					#print idx,Dn,self.label[pivot],pivot
					dist = self.compute_sum_diff(f,pivot,Dn)
					if idx != self.label[pivot]:
						dist *= self.label_freq[idx]/(self.item_num-self.label_freq[idx])	
					weights[f] += dist*1.0/samples
				#print ""
	
		return weights

	def select_feature(self, weights):
		sigma = 0
		return [idx for idx,v in enumerate(weights) if v>sigma ]





if __name__=='__main__':
	"""
	loadfn = "wpbc/wpbc.data"
	x_vals = np.genfromtxt(loadfn, delimiter=',')

	data = np.delete(x_vals,[0,1,2,34],1).astype(np.float32)
	y_vals = np.genfromtxt(loadfn, delimiter=',',usecols=(1),dtype=str)
	labels = [1 if y == 'R' else 0 for y in y_vals]
	wpbc_rf = RelieF(data,labels)
	weights = wpbc_rf.select(1000)
	
	print sorted(enumerate(weights),cmp=lambda x,y: cmp(x[1],y[1]))
	
	
	"""
	from sklearn.datasets import load_iris
	iris = load_iris()
	iris_rf = RelieF(iris.data,iris.target)
	iris_weights = iris_rf.select(100)
	print iris_weights
	
