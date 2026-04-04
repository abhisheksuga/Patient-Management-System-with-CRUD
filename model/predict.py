import pickle
import pandas  as pd

with open('model/model.pkl','rb') as f :
    model = pickle.load(f)

#In prod we usually extract the version from the model registry /MLflow
MODEL_VERSION = '1.0.0'


class_labels = model.classes_.tolist()

def predict_output(userinput :dict):
    df = pd.DataFrame([userinput])

    predicted_class = model.predict(df)[0]

    probablities = model.predict_proba(df)[0]
    confidence = max(probablities)
    class_probs = dict(zip(class_labels,map(lambda p : round(p,4),probablities)))

    return{
        "predicted_category" : predicted_class,
        "confidence" : round(confidence,4) ,
        "class_probabilities" :class_probs
    }

