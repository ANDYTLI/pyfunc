def slrfunc(x,y):
    #Simple Linear Regression
    import pandas as pd
    X = pd.DataFrame(x)
    Y = pd.DataFrame(y)
        
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X,Y)
    
    Y2 = model.predict(X)
 
    import matplotlib.pyplot as plt
    plt.figure(figsize=(3,3))
    plt.plot(X,Y,'k.')
    plt.plot(X,Y2,'g-')
    plt.show()
    
    model = print('Model: y = ', round(float(model.intercept_),2) , '+', round(float(model.coef_),2), 'x')
    return model