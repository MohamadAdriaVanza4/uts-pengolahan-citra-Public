import streamlit as st

from camera_input_live import camera_input_live # type: ignore

image = camera_input_live()

if image:
  st.image(image)
