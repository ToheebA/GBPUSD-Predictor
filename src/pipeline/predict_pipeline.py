import os
import sys
import pandas as pd
from exception import CustomException
from utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Open: float,
        High: float,
        Low: float,
        Weekday: str):

        self.Open = Open

        self.High = High

        self.Low = Low

        self.Weekday = Weekday


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Open": [self.Open],
                "High": [self.High],
                "Low": [self.Low],
                "Weekday": [self.Weekday]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)