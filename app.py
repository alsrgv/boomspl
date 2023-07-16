import math

import streamlit as st


voltage = st.number_input("Voltage", min_value=0.01, max_value=160.0, step=0.01)
pressure_pa = voltage / 10 ** (-56.0 / 20)
spl = 20 * math.log(pressure_pa / (20 * 1e-6), 10)
st.info(f"SPL: {spl:.2f} db")
