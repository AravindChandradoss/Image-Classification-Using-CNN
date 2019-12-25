# ImageClassificationUsingCNN
The objective is to create variety of CNN networks and to compare their performance.

# Refer to [report](https://github.com/AravindChandradoss/Image-Classification-Using-CNN/blob/master/ImageClassificationUsingCNN/Aravind_Chandradoss/ML_Final_Project.pdf) for more details. You can also viz the result using TensorBoard.

To run the log file in TensorBoard. You need TensorFlow to be install in your computer. 

Once you have TensorFlow, you can run the following command on you terminal to start the TensorBoard.

Be sure that you are in the right directory before running the following command. 

For CIFAR DATASET:
#######################################################################################
$ tensorboard --logdir='logsCIFAR/'   
#######################################################################################

For AR DATASET:
#######################################################################################
$ tensorboard --logdir='logsAR/'
#######################################################################################

After you run the command you will get something similar to this,
#######################################################################################
aravinddoss@aravinddoss-Inspiron-5558:~/Documents/ML_Proj$ tensorboard --logdir='logs/'
TensorBoard 1.12.0 at http://aravinddoss-Inspiron-5558:6006 (Press CTRL+C to quit)
#######################################################################################

Once you get this, you can open the link in you browser and access the tensorboard as you want. 

Plz, WAIT FOR SOME TIME in order to load all the data. It will take few minutes to load all the data.
In some case, it might not show all the selected items. make sure to REFRESH THE TENSORBOARD using the refereh buttom on top right within the tensorboard.

To see the network, click graph at the top next to TensorBoard logo. You can see the flow of the computation in the graph.

The naming I used is straight forward:

zzz-x-conv-with-p-nodes-and-y-dense-with-q-nodes-zzxxyy 
	
	where, x and y represent the number of layer
	       p and q represent the filter count and number of nodes
	       zzz represents some special cases like change in optimizer, activation or inclusion of dropout 
	       zzxxxyy represents the time stamp (to avoid overwritting)
For eg:
	conv_size-7-adam-3-conv-with-24-nodes-and-3-dense-with-64-nodes-1543736436	
	
	represent,
		a network with convolutional size of 7*7, with adam optimizer
		with 3 convolutional layer (24 filter) followed by 3 dense layer (64 nodes) and finally the timestamp.	
