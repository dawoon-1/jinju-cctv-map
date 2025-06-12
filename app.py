import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("진주시 CCTV 지도")

# 샘플 CCTV 위치 데이터 (위도, 경도)
data = pd.DataFrame({
    'lat': [35.1803, 35.1853, 35.1702],
    'lon': [128.1076, 128.1126, 128.1151],
    '설명': ['진주시청 앞', '진주중앙시장', '진주역 근처']
})

# 지도 그리기
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v11',
    initial_view_state=pdk.ViewState(
        latitude=35.1803,
        longitude=128.1076,
        zoom=13,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_color='[255, 0, 0, 160]',
            get_radius=100,
        ),
        pdk.Layer(
            "TextLayer",
            data=data,
            get_position='[lon, lat]',
            get_text='설명',
            get_size=16,
            get_color=[0, 0, 0],
            get_angle=0,
            get_alignment_baseline="'bottom'"
        )
    ]
))
