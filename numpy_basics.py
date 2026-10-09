import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# my_array = np.array([5, 10, 15, 20, 25])
# result = my_array + 10
# print (result)

my_2d_array = np.array([
    [25, 50000, 0],
    [35, 60000, 1],
    [45, 75000, 1]
])

# print (my_2d_array.shape)

# print (my_2d_array[0])
# print (my_2d_array[:, 1])
# print (my_2d_array[-1, -1])

# print (my_2d_array * 2)
# print (np.mean(my_2d_array[:, 0]))
# print (np.sum(my_2d_array[:, 2]))

# my_2d_array_2 = np.array([10, 100, 5])

# result = my_2d_array - my_2d_array_2
# print(result) 

# my_2d_array_of_0 = np.zeros((3, 3))
# my_range_array = np.arange(0, 9)
# my_rand_array = np.random.rand(2, 4)

# print (my_2d_array_of_0)
# print (my_range_array)
# print (my_rand_array)

print ("=====Pandas======")
# df = pd.DataFrame(my_2d_array, columns=["Age", "Salary", "Risk"])
# print (df)
# print ()
# print (df['Age'])
# print ()
# print (df.loc[[0,1]])
# print ()
# print (df.describe())

# df = pd.read_csv('iris.data.csv')

# print (df.head())
# print (df.shape)
# print (df.info())


# print (df[df["PetalLength"] > 2.0].shape[0])
# print (np.mean(df['SepalLength']))
# print (len(df[df["Name"] == 'Iris-setosa']))

print ("======Matplotlib======")

# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]

# plt.plot(x, y)
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Simple Line Plot")
# plt.show()

# df = pd.read_csv("iris.data.csv")
# plt.hist(df['SepalLength'])
# plt.xlabel ('X Axis')
# plt.ylabel ('Y Axis')
# plt.title ('Histogram of SepalLength')
# plt.show()

# x = df['SepalLength']
# y = df['PetalLength']

# plt.scatter(x,y)
# plt.xlabel ('SepalLength')
# plt.ylabel ('PetalLength')
# plt.title ('Relationship between SepalLength and PetalLength')
# plt.show()

# print ("===Dot product===")
# v1 = np.array([1,2,3])
# v2 = np.array([2,0,1])

# print (np.dot(v1,v2))
# print (v1 @ v2)

# matrix1 = np.array([[2, 3, 7],
#                    [4, 5, 6]])

# matrix2 = np.array([[3, 2],
#                    [1, 9],
#                    [5, 9]])

# result = matrix1 @ matrix2

# print (result)
# print (result.shape)

# print (matrix1.T.shape)
# print (matrix1.T.T.shape)

# m = np.array(
#     [[4, 7],
#      [2, 6]])

# i = np.eye(2)
# print (m @ i)

# inverse = np.linalg.inv(m)
# print (m @ inverse)

# dataset = pd.read_csv('iris.data.csv')
# x = dataset['SepalWidth']
# y = dataset['PetalLength']

# plt.scatter(x, y)
# plt.xlabel('SepalWidth')
# plt.ylabel('PetalLength')
# plt.title('Relationship between sapal width and patel length')
# plt.show()

# df = pd.read_csv('iris.data.csv')
# print (f"Mean: {np.mean(df['SepalLength'])}")
# print (f"Variance: {np.var(df['SepalLength'])}")
# print (f"Standard deviation: {np.std(df['SepalLength'])}")

# print (f"Mean: {np.mean(df['PetalLength'])}")
# print (f"Variance: {np.var(df['PetalLength'])}")
# print (f"Standard deviation: {np.std(df['PetalLength'])}")

# print (f"Correlation:\n {np.corrcoef(df['SepalLength'], df['PetalLength'])}")

# plt.hist(df['SepalLength'])
# plt.show()

df = pd.read_csv('iris.data.csv')
print (f"Shape: {df.shape}")
print (f"Missing values: \n {df.isnull().sum()}")
print ()
print (f"Data type: {df.dtypes}")
print ()
print (df.head())
print ()
print (df.describe())

plt.subplot(1,3,1)
plt.hist(df['PetalLength'])

plt.subplot(1,3,2)
plt.scatter(df['SepalLength'], df['PetalLength'])

x = df['Name'].value_counts()
plt.subplot(1,3,3)
plt.bar(x.index, x.values)

plt.show()