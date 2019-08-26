from csv import reader
from random import randrange

def GetDataset(filename='SPECT.csv'):
	dataset = []
	data=open(filename,'r')
	file = reader(data)
	for i in file:
		if not i:
			continue
		dataset.append(i)
	for j in range(len(dataset[0])):
		for i in range(len(dataset)):
			dataset[i][j]=float(dataset[i][j])

	return dataset

def Metrics(actual, predicted):
	tp = tn = fp = fn = 0
	ans = 0

	for i in range(len(actual)):
		if actual[i] == 0 and predicted[i] == 0: tn += 1
		if actual[i] == 0 and predicted[i] == 1: fn += 1
		if actual[i] == 1 and predicted[i] == 1: tp += 1
		if actual[i] == 1 and predicted[i] == 0: fp += 1

	ans = tp+tn

	return ans/float(len(actual))*100.0,tp,tn,fp,fn

def ValidationSplit(dataset, n_folds):
	split = []
	dataset_copy = list(dataset)
	fold_size = int(len(dataset)/n_folds)
	for i in range(n_folds):
		fold = []
		while len(fold)<fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		split.append(fold)
	return split
  
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	if activation >= 0.0:
		return 1.
	
	return 0.

def Perceptron(train, test, alpha, epoch):
	predictions = []
	weights = Update(train, alpha, epoch)
	for row in test:
		prediction = predict(row, weights)
		predictions.append(prediction)

	return(predictions)
 
def Train(dataset, n_folds, alpha, epochs):
	folds = ValidationSplit(dataset, n_folds)
	scores = []
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = []
		
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None

		predicted = Perceptron(train_set, test_set,alpha,epochs)
		actual = [row[-1] for row in fold]
		accuracy,tp,tn,fp,fn = Metrics(actual, predicted)
		print('Precision: ',tp/(tp+fp))
		print('Recall: ',tp/(tp+fn))
		print('Accuracy: ',accuracy)
		print('---------------------------------------')
		scores.append(accuracy)

	return scores
 
def Update(train, alpha, epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(epoch):
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			weights[0] = weights[0] + alpha * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + alpha * error * row[i]

	return weights

 
# filename = 'SPECT.csv'
# filename = 'IRIS.csv'

filename = 'SPECT.csv'
dataset = GetDataset(filename)
n_folds = 10
alpha = 0.2
epoch = 50
print("folds %d, l_rate %f, epochs %d"%(n_folds,alpha,epoch))
scores = Train(dataset, n_folds, alpha, epoch)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))