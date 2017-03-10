Foundation of feature selection 

***feature relevance***
In terms of an ideal Bayes classifier
1. strongly relevant if remove the feature X will result in the deterioration of the classification results
2. weakly relevant if there exisits a set S that performance is better when using S U {X} than S.
3. irrelevant if neither weakly or strong relevant
*Note: The difference between stong and weakly is that one is for  all set and one only requires existence.

***feature selection method***
* indivisual searching vs subset searching
* filters, wrappers and embedded methods
* Filter method
	+ chi-Sqaured: univariate, the higher teh chi-squared, the more relkevant the feature with tespect to the class.
	+ information gain: entorpy orginal - entropy psterior
	+ Correlea=ation-Based Feature Selection.: multivariate, the more the fetaure related with the class and the less with the orther feature, the more it is selected.
	+ ReliefF: improved version of Relief algorithm. The attributes that separate the same class is insisgificant and the attributes that separate different calsses is desirable.

 