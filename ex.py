import pickle
import streamlit as st
import sqlite3
import pandas as pd

df=pd.read_csv("C:/Users/annad/OneDrive/Documents/project/set/finaldata(1).csv")


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
X_train, X_test, y_train, y_test = train_test_split(df['symptom'], df['disease'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

cancer_model = pickle.load(open('C:/Users/annad/Downloads/webpage/cancer_model.sav', 'rb'))


conn=sqlite3.connect('data.db',check_same_thread=False)
cur=conn.cursor()

st.set_page_config(page_title="cancer identification", page_icon=":minidisc:", layout="wide")

with st.container():
    st.markdown("""
<style>
.big-font {
    font-size:50px;
    font-weight:bold;
    font-family:SANS-SERIF;
    
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">cancer identification</p>', unsafe_allow_html=True)
st.markdown("""
<style>
.small-font {
    font-size:15px;
   
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="small-font">based on your symptoms it will give the type of cancer your are suffering with.Consult the doctor to confirm it.</p>', unsafe_allow_html=True)


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
with st.container():
    st.write("___")
    st.write("Give your symptom here below!")
    st.write("___")

def adddata(a,b,c):
    cur.execute("""CREATE TABLE IF NOT EXISTS sym(NAME TEXT(50),AGE TEXT(50),SYMPTOM TEXT(500));""")
    cur.execute("INSERT INTO sym VALUES(?,?,?)",(a,b,c))
    
    
    conn.commit()
st.markdown("""
<style>
.big2-font {
    font-size:25px;
    height:150px;
    text-align:center;
    color:white;
    font-style:bold;
   
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big3-font {
    font-size:15px;
    height:150px;
    text-align:center;
    color:white;
    font-style:bold;
   
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    with st.form(key="Information form"):
        name=st.text_input("ENTER FULL NAME")
        age=st.text_input("ENTER YOUR AGE")
        symp=st.text_area("ENTER YOUR SYMPTOM")
        submission=st.form_submit_button("Submit")
    if submission==True:
            adddata(name, age, symp)
            can_prediction = cancer_model.predict(count_vect.transform([symp]))
            st.write("MR/MRS/MISS",name)
            st.write(f'<p class="big2-font">probably suffering with this: {can_prediction} </p>',unsafe_allow_html=True)
            res = can_prediction[0]
            result = df[df.disease == res].head(1)
            treatmen=result['treatment']
            treatment1=list(treatmen)
            treatment=treatment1[0]
            diag1=result['diagnosis']
            diag2=list(diag1)
            diag=diag2[0]
            st.write(f'<p class="big3-font">DIAGONSIS: {diag} </p>',unsafe_allow_html=True)
            st.write(f'<p class="big3-font">TREATMENT: {treatment} </p>',unsafe_allow_html=True) 
                      
            
            
            
    
    
with col3:
    st.write(' ')

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
    

with col2:
    
    raw_code="SELECT COUNT(NAME) as TOTALVIEWS FROM sym"
    def sql_executor(raw_code):
        cur.execute(raw_code)
        data=cur.fetchall()
        l=[]
        for i in data:
            l.append(i)
        a=list(l)
        return a[0][0]
    query_res=sql_executor(raw_code)
    conn.close()
    st.markdown("""
<style>
.big1-font {
    font-size:15px;
    height:150px;
    text-align:center;
    color:white;
   
}
</style>
""", unsafe_allow_html=True)
    st.write(f'<p class="big1-font">TOTAL VIEWS: {query_res} </p>',unsafe_allow_html=True)
with col3:
    st.write(' ')
    