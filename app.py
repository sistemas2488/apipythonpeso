from flask import Flask, jsonify, request

from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd



app=Flask(__name__ )


@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({"message":"Funciona"})


@app.route('/data/<string:product_name>',methods=['Get'])
def getProduct(product_name):
    clf = tree.DecisionTreeClassifier()
    datos=pd.read_csv('encuesta.csv')
    dato=product_name
    info=dato.split("-")
    estarura=int(info[0])
    peso=int(info[1])
    print(estarura)
    print(peso)
    XX=datos[['Estatura (cm) solo numero y sin coma','Peso (Kg)']]
    YY=datos['Estado']
    ##variables de entrenamiento y de prueba
    X_train, X_test, y_train, y_test=train_test_split(XX, YY, test_size=0.3, random_state=42)

    clf=clf.fit(X_train,y_train)
    print(clf.score(X_train, y_train))
    dato=[estarura,peso]
    prediccion=clf.predict([dato])
    print(prediccion)
    
    return jsonify({"resultado": prediccion[0]})
    




if __name__=='__main__':
    app.run(debug=True, port=4000)