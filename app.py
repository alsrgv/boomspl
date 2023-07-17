import math

import streamlit as st


st.title("Boom SPL")

st.markdown("This app helps to measure [sound pressure level](https://en.wikipedia.org/wiki/Sound_pressure) of loud noises.")

st.markdown("Illustration from Wikipedia:")
st.write("<img style='background-color:white;width:100%' src='https://upload.wikimedia.org/wikipedia/commons/7/7a/Sound_pressure_diagram.svg'/>", unsafe_allow_html=True)
st.markdown("(1) silence; (2) audible sound; (3) atmospheric pressure; (4) sound pressure")

st.markdown("Connect a high-SPL dynamic microphone to an oscilloscope, and record a waveform that would resemble the illustration above. One example is [Shure SM57](https://en.wikipedia.org/wiki/Shure_SM57).")

microphone_sensitivity_dbv_pa = st.number_input("Microphone sensitivity (dBV/Pa)", value=-56.0)
voltage = st.number_input("Measured voltage (V)", value=1.0, min_value=0.01, max_value=160.0, step=0.01)

pressure_pa = voltage / 10 ** (microphone_sensitivity_dbv_pa / 20)
reference_pressure_pa = 20 * 1e-6
spl = 20 * math.log(pressure_pa / reference_pressure_pa, 10)
st.metric(label="Calculated SPL", value=f"{spl:.2f} dB", delta=f"{spl-140:.2f} dB vs hearing damage threshold", delta_color="inverse")
