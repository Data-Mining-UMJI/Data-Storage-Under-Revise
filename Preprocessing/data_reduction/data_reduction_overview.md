＃ Data Reduction (more details)

*** Overview ***

- data redcution can be devided into 3 categories
	* dimension reduction
	* sample numerosity reduction
	* cardinality reduction
- dimension reduction (DR):
	* why we need it? the curse of dimension
	 number of training samples should grows linearly or even exponentially with the dimensions. For exaample, when dealing with non-parametric learners, such as decision tree.
	
    * PCA: normalize the input data, get the principal components by calculating the eigenvalues-eigenvectors of the covariance matrix of the original data, sort by the eigenvalues, reduce weaker components
    * Factor Analysis: Discover hiddeen factos in the current variables. Assume that there is a set of latent varaibels that generate the original data. Major method is using PCA. (, the eigenvalues of PCA are inflated component loadings, i.e., contaminated with error variance, from wikipedia)
    Therefore in my opinion, this maybe that factor analysis introduce an error item and it will estimate it recursively until it converge(it may not!) before hand.
    * Mutidimensional scaling: it reduces the data into a space that the distance between each other is minimized. Too much mathematics. 
    * Locally linear embedding: Assume data lies in a manifold with dimension d < D like a line in a plain. Each point can be revcovered by its neightbor. It preserve the invariance to rotation and scaling. Then we can use the weight to get the d-dimensional coordinate by fixing the weight and finding the d-dimensional coordinate to minimize teh sqarue distances of all points.

- data sampling 
	* why?
		+ reduce the number of instances submitted to the data mining algorithm. Predictive learning often can have 10%-20% of data to learn without the dererioration of performance.
		+ balancing the data, like oversampling the rare case and undersampling the common case
		+ partition into training , validation and testing sets.
	* method
		+ simple random sample without replacement
		+ simple random sample with replacement
		+ balanced sample
		+ clusters sample, like samples in geographically separated areas.
		+ stratified ssample
	* data condensation: selection of small representatives
	* data squashing: use a compressed set of data such that hte staistical properties are preserved
	* data clustering: use the cluster instead of the data itself

- bining and reduction of cardinality
bining is discretize the continuous data into discrete ones which cover different ranges.
combine different categories into one indicator variable, reducing the possibility that original category has trivially almost all 0 or 1.