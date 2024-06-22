# 콘솔창에 'pip install pandas' 입력 후 실행
import pandas   # 파이썬에서 행렬을 계산하는 프로그램 : pandas
from sklearn import svm,metrics
csv=pandas.read_csv("py\iris.csv")
data=csv[["sepal.length","sepal.width","petal.length","petal.width"]]
label=csv["variety"]
# print(label)

clf=svm.SVC()
clf.fit(data,label)
results=clf.predict([
    [4.6,3.6,1.4,.2],
    [4.6,3.1,1.5,.2],
    [5.6,3.6,1.5,.4],
    [4.6,3.1,1.4,.2],
    [5.9,3,5.1,1.8],
    [3.5,3.1,2.4,1.1]])

print(results)