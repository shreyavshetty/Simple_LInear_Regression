#importing csv module
import csv
#reading the csv file
from random import randrange
dataset = []
dataset1 = []
test_set = []
train_set = []

def load_dataset(filename):
	with open(filename,'r') as csvfile:
		csvreader = csv.reader(csvfile)
		csvreader.next()
		for row in csvreader:
		   c_row = [float(x) for x in row]
		   dataset.append(c_row)
	return dataset
	
def simple_linear_regression(dataset):
	sum_x = 0
	sum_y = 0
	mean_x = 0
	mean_y = 0
	var = 0
	covar = 0
	dataset_length = len(dataset)
	training_length = int(0.6*dataset_length)
	test_set = dataset
	while len(train_set) < training_length:
		i = randrange(len(test_set))
		train_set.append(test_set.pop(i))
	print "train_set"
	print train_set
	print "test_set"
	print test_set
	for row in train_set:
		sum_x = sum_x + row[0]
		sum_y = sum_y + row[1]
	mean_x = sum_x/training_length
	mean_y = sum_y/training_length
	for row in train_set:
		var = var + ((row[0] - mean_x) ** 2)
		covar = covar +((row[0] - mean_x) * (row[1] - mean_y))
	b1 = covar/var
	b0 = mean_y - b1*mean_x
	print "predicted values as: x,ypredicted,ytarget"
	sum_error = 0
	for row in test_set:
		y = b0 + b1*(row[0])
		print(row[0] , y , row[1], y-row[1])
		sum_error = sum_error + ((y - row[1])**2)
	mean_error = sum_error / len(test_set)
	print (mean_error ** 0.5)
#dataset file name
filename = 'Cryogenic_Flow_Meter.csv'
dataset = load_dataset(filename)
simple_linear_regression(dataset)

			

