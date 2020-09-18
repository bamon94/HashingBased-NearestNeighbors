# HashingBased-NearestNeighbors
Hashing is a method of representing a collection of higher dimensional data by a lowerdimensional hash. The primary motivation behind is the reduction of time complexity in-volved in searching and finding the nearest neighbors of a particular data, for example animage.  The image (usually a very high dimensional data) can be represented by its hashvalue and similar images can be found out by comparing the hash values associated withthe images in the database.One  of  the  methods  of  generating  hash  involves  hierarchical  clustering.   Here  hashingusing Hierarchical 2-means is illustrated.The training dataset is employed to generate atree,which involves clustering the data into 2 clusters at each node, the cluster mean and the associated data (stored as additional info) are stored in the respective node.The com-plete tree is thus generated whose number of levels are determined by required dimensionof the hash value.  To determine the hash value for a particular test data, a complete treetraversal upto the leaf node is carried out,of which the path traversed determines the hashvalue.<br/> <br/>

![Alt text](Hashing_Tree.PNG?raw=true "Title")

# Dataset
http://yann.lecun.com/exdb/mnist/<br/> <br/>
# Generated Output
![Alt text](output.PNG?raw=true "Title")

