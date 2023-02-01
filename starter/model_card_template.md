# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
It is a `RandomForestClassifier` from `scikit-learn` library used for classification model. Applied the default hyperparameters
## Intended Use
The model is used for classifying employees' salary into `<=50K` and `>50K`, based on employees's information.

Users can apply this model to their information about the employees in the predefined format and get the prediction for the salary type.

## Training Data
Publicly available dataset "Census Bureau" is used for training and evaluating the model. 

For both training and evaluation, categorical features of the data are encoded using `OneHotEncoder` and the target is transformed using `LabelBinarizer`

## Evaluation Data
The original dataset is first preprocessed and then split into training and evaluation data with evaluation data size of 20\%

## Metrics
The model achieves the following result:
* precision: 0.7351145038167939
* recall: 0.6233009708737864
* fbeta: 0.6746059544658494

## Ethical Considerations
The misuse of these census information can cause consequences to the lives of people surveyed and (possibly) other people in some related populations

## Caveats and Recommendations
The used data to train the model is mostly from USA, predicting for other regions might need different feature distributions.