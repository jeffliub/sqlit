import jfutils
import jfutils.dbutils
import streamlit as st

db='postgres'
sc=jfutils.dbutils.DBUtils(db,st.secrets[db]['server'],st.secrets[db]['port'],st.secrets[db]['user'],st.secrets[db]['password'],st.secrets[db]['database'])
data=sc.get_query_rows('select * from tcommodity limit 10')
st.title('Streamlit App with PostgreSQL')
st.write('This is a simple Streamlit app that connects to PostgreSQL and displays data.')
st.write('Data from PostgreSQL:')
if data:
    st.table(data)