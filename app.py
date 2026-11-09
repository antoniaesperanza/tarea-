import streamlit as st

st.title("Mi primera aplicacion de Streamlit")
st.subheader("¡Hola, Streamlit!")


#Inicio de la barra lateral
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.text("¡Hola, Barra lateral!")

#    Area principal
st.text("Esta es una aplicacion simple")
st.image("https://researches.uss.cl/skin/footerIcon/", width=250)

#Boton de area principal 
if st.button("haz clicl"):
  st.write("¡Boton precionado!")

#Campo de texto del area principal
nombre_texto = st.text_input("Escribe algo:")
st.write(f"Escribiste: {nombre_texto}")


#  Barra Lateral
st.sidebar.text("Esto es una barra lateral")
st.sidebar.image("https://researches.uss.cl/skin/footerIcon/", width=200)

#Boton de la barra lateral
if st.sidebar.button("Haz clicl pero en la barra lateral"):
  st.sidebar.write("¡Boton de la barra presionado!")

  #Campo de texto de la barra lateral
  texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
  st.sidebar.write(f"Escribiste en la barra: {texto_barra}")
  
                
