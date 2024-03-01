
# Attack Detection Project - detection of malicious PE files

### Created by:
- Yehonatan Baruchson
- itamar 

### Abstract:
In the past few years, malware has become one of the most significant threats to computer security. In this project we implemented a new detection model to classify PE files based on the article: “Investigation of Malicious Portable Executable File Detection on the Network using Supervised Learning Techniques”. Our implementation includes new data features for model training and uses a newer dataset. The returned results showed that the proposed system can achieve 99.55% detection rates, 0.0494 false positive rate, and by that we improve the detection part significantly.


### System Workflow and Model Architecture:
Our system flow starts by uploading a PE file to the UI, then the file moves to the extraction process to fetch all features, and so moves all features into the trained model. eventually the classification results presented to the user in the interface.
The classification model architecture is based on a Random Forest classification with 10 trees.
We used the DSC-CLASS dataset from kaggle, to train the model and then to test it. The dataset was splitted into two parts: 70% - training and 30% - testing.




### dataset 
https://www.kaggle.com/datasets/dscclass/malware


## Screenshots

![GUI](Snapshot/GUI.png)

![App project_workflow](Snapshot/project_workflow.png)

