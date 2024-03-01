import pickle
import streamlit as st

#Loading Model Here
model = pickle.load(open('main/Internship_1/Heart-Disease-Check/model.pkl', 'rb'))


#Making Streamlit Widgets
name = st.text_area(label="Your Name")
age = st.text_area(label="Age")
rbp = st.text_area(label="RestingBP")
ch = st.text_area(label="Cholesterol")
fbs = st.text_area(label="FastingBS")
mhr = st.text_area(label="MaxHR")
ea = st.text_area(label="ExerciseAngina")
op = st.text_area(label="Oldpeak")
slope = st.selectbox("ST Slope",('Up', 'Flat', 'Down'))
cpt = st.selectbox("Chest Pain Type",('ATA', 'NAP', 'ASY', 'TA'))
r_ecg = st.selectbox("Resting ECG",('Normal', 'ST', 'LVH'))
sex = st.selectbox("Sex",('Male', 'Female'))

#Main Processing
try:
    if st.button("Check"):
        with st.spinner():
            female = 0
            lvh = 0
            str = 0
            asy = 0
            ata = 0
            nap = 0
            down = 0
            up = 0
            if sex == "Female":
                female += 1

            if cpt == 'ATA':
                ata += 1
            if cpt == 'NAP':
                nap += 1
            if cpt == 'ASY':
                asy += 1

            if r_ecg == "ST":
                str += 1
            if r_ecg == "LVH":
                lvh += 1

            if slope == "Up":
                up += 1
            if slope == "Down":
                down += 1

            #Prediction
            y_pred = model.predict([[float(age), float(rbp), float(ch), float(fbs), float(mhr), float(ea), float(op), lvh, str, asy, ata, nap, down, up, female]])

            #Results
            st.markdown("### Results")
            if y_pred == 1:
                st.write("Sorry to Inform You But You Have Heart Problem, You should consult to a Doctor As Soon As Possible")
            else:
                st.write("Bingo! You are Perfectly Fine. No need to worry!")
except:
    st.write("### First Enter Details")
