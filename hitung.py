import streamlit as st

x = st.number_input('Masukkan angka')
sx = st.selectbox('Satuan asal', ['C', 'R', 'F', 'K'], key='sx')
st.write("Anda memasukkan", x, ' ', sx)
sy = st.selectbox('Dikonversi ke', ['C', 'R', 'F', 'K'], key='sy')
y = 0

if sx == 'C':
    if sy == 'C':
        y = x
    elif sy == 'R':
        y = (x * 4 / 5)
    elif sy == 'F':
        y = (x * 9 / 5) + 32
    elif sy == 'K':
        y = x + 273.15
elif sx == 'R':
    if sy == 'C':
        y = x * 5 / 4
    elif sy == 'R':
        y = x
    elif sy == 'F':
        y = (x * 9 / 4) + 32
    elif sy == 'K':
        y = (x * 5 / 4) + 273.15
elif sx == 'F':
    if sy == 'C':
        y = (x - 32) * 5 / 9
    elif sy == 'R':
        y = (x - 32) * 4 / 9
    elif sy == 'F':
        y = x
    elif sy == 'K':
        y = (x - 32) * 5 / 9 + 273.15
elif sx == 'K':
    if sy == 'C':
        y = x - 273.15
    elif sy == 'R':
        y = (x - 273.15) * 4 / 5
    elif sy == 'F':
        y = (x - 273.15) * 9 / 5 + 32
    elif sy == 'K':
        y = x

st.write(x, ' ', sx, ' = ', y, ' ', sy)
