import streamlit as st
import pandas as pd
import numpy as np
# import plotly_express as px
from PIL import Image
# import matplotlib.pyplot as plt
from fwhr import *

from PIL import Image
# sys.modules['Image'] = Image 

def main():
    st.subheader("Heal - Food Analyzer")
    data = st.file_uploader('')
    if data == None:
        st.write('Please Upload Photo of Food')
    else:
        img = Image.open(data)
        newsize = (280, 230)
        image = img.resize(newsize)
        # guy_url = 'RAT.jpg'
        output = get_fwhr(image, url=False,top = 'eyebrow')
        st.image(output)


if __name__=='__main__':
    main()