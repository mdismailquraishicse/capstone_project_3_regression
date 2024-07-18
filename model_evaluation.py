from sklearn.metrics import r2_score, mean_squared_error
def showMetrics(ytrain,ytest, pred_train, pred_test):
    print('train mean squared error : ',mean_squared_error(ytrain, pred_train))
    print('test mean squared error : ',mean_squared_error(ytest, pred_test))
    print()
    print('train r2score: ',r2_score(ytrain, pred_train))
    print('test r2score : ',r2_score(ytest, pred_test))