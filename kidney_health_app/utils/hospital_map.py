# utils/hospital_map.py
import streamlit as st
import geocoder
import pandas as pd

def show_nearby_hospitals():
    # Get user's approximate location using IP
    g = geocoder.ip('me')
    lat, lon = g.latlng if g.ok else (20.5937, 78.9629)  # Default to India center if location fails

    # Fake hospital data near user location (you can replace with real hospital data later)
    hospitals = [
        {"name": "City Kidney Hospital", "lat": lat + 0.01, "lon": lon + 0.01},
        {"name": "NephroCare Clinic", "lat": lat - 0.01, "lon": lon - 0.01},
        {"name": "Renal Health Center", "lat": lat + 0.015, "lon": lon - 0.008},
    ]

    df = pd.DataFrame(hospitals)

    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))
    for h in hospitals:
        st.markdown(f"**{h['name']}** - 📍 Location: ({h['lat']:.4f}, {h['lon']:.4f})")

    st.info("Showing sample hospital locations near your IP address.")
