# 콘솔창에 'pip install scikit-learn' 입력 후 실행
from sklearn import svm,metrics     # 머신러닝을 위한 라이브러리 : sklearn

#학습시킬 데이터
datas=[[0,0],[1,0],[0,1],[1,1]]
#학습시킬 데이터에 대한 답안
labels=[0,1,1,1]
#질의할 데이터
examples=[[0,0],[1,0]]
#질의 데이터 정답
examples_label=[0,1]

clf =svm.SVC()
clf.fit(datas,labels)
results=clf.predict(examples)
print(results)

score=metrics.accuracy_score(examples_label,results)
print("정답률",score)


