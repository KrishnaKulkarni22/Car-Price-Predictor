import streamlit as st

import numpy as np 

import pickle

from streamlit_lottie import st_lottie
import requests



## Importing the Dataset

df = pickle.load(open('Df.pkl','rb'))
model = pickle.load(open('Model1.pkl','rb'))



## Creating the necessary parameters in order to deploy the model

st.set_page_config(page_title= "Car Price Predictor" , 
                   layout='wide')

## Creating a user defined function

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


## Loading assets
lottie_1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_nyk1qdpg.json")





### Title 

### Deploying animation

with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie_1, height=400)
        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
            
            
            
    
    

## Title and subtitle
st.title(' Car Price Predictor')

st.write("---") 

st.text('Accuracy of this Model is 95 % ')


with st.container():
   
   ### Columns of the dataset 
   ## 1) Make

    Make = st.selectbox('Make(Car Brand)',df['Make'].unique())

    ## 2) Type

    Type = st.selectbox('Type( Vehicle Type)', df['Type'].unique())


    ## 3) Origin

    Origin = st.selectbox('Origin(Region)',df['Origin'].unique())

    ## 4) Drivetrain

    DriveTrain = st.selectbox('DriveTrain(Drivetrain)',df['DriveTrain'].unique())


    ## 5) Engine Size 

    EngineSize = st.number_input('EngineSize(Cubic Capacity Ranege 1.3 - 6.2 Litres)')


    ## 6) Cylinders

    Cylinders = st.selectbox('Cylinders(No of Cylinders)',[3,4,5,6,8,9])


    ## 7) Horsepower

    HorsePower = st.number_input('HorsePower(HP Range is in between 73 - 390)')


    ## 8) Miles Per Gallon(City)

    MPG_city = st.number_input('MPG_City(Fuel Economy(Range 10 - 27 Miles per gallon)')



    ## 9) Miles Per Gallon (Highway)

    MPG_Highway = st.number_input('MPG_Highway(Fuel Economy(Highway range 16 - 36 Miles per gallon)')


    ## 10) Weight

    Weight = st.number_input('Weight(Kerb Weight range 1850 - 5288 Pounds)')


    ## 11) Wheelbase 

    Wheelbase = st.number_input('Wheelbase(Wheelbase range 89 - 125)')


    ## 12) Length

    Length = st.number_input('length(Length range 154 - 218)')


    ## 13) Convertible

    Convertible = st.selectbox('Convertible(Convertible Yes or No)',['No', 'Yes'])


    ## 14) Door 4 or 2

    Doors = st.selectbox('Doors(Two Doors)',['No', 'Yes'])

    ## 15) Model Name

    ModelName = st.selectbox('Model Name(Model)',df['Model Name'].unique())
    




## Animation for price prediction

lottie_final = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_58tsmdsb.json")

## Model Prediction



if st.button('Price'):
    if Convertible == 'Yes':
        Convertible = 1
    else:
        Convertible = 0
        
    if Doors == 'Yes':
        Doors = 1
    else:
        Doors = 0
    group = np.array([Make,Type,Origin,DriveTrain,EngineSize,Cylinders,HorsePower,MPG_city,MPG_Highway,Weight,Wheelbase,Length,Convertible,Doors,ModelName])
    group = group.reshape(1,15)
    st.title("Predicted Price " + str(int((model.predict(group)[0]))))
    st_lottie(lottie_final, height=275)    
           
                
            
    

    
  
        
         
st.subheader(('By: Krishna Kulkarni'))





