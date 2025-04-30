import streamlit as st

containers = {
    # size: [(length, width, height),(door_height,door_width), weight]
    # 尺寸：[(内长,内宽,内高),(门高,门宽)，重量]

    # size unit: mm, weight unit: tons
    # 尺寸单位：毫米，重量单位：吨

    '20GP': [(5898,2352,2385),(2280,2340),18],
    '40GP': [(12032,2352,2385),(2280,2340),26],
    '40HQ': [(12032,2352,2690),(2585,2340),26],
    '45HQ': [(13556,2352,2698),(2585,2340),29],
}

box = st.selectbox('选择柜子：',['20GP','40GP','40HQ','45HQ'])
box_info = containers[box]
LxWxH = '+'.join(box_info[0])
st.write(LxWxH)
