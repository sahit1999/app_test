import streamlit as st
import base64
from PIL import Image
import json 
import requests 
from streamlit_lottie import st_lottie 
##lottie animation
url = requests.get( 
    "https://lottie.host/a6e625b0-a2bf-46a1-bb43-fdd2072d7ff9/pofMSCoB1h.json") 
# Creating a blank dictionary to store JSON file, 
# as their structure is similar to Python Dictionary 
url_json = dict() 
  
if url.status_code == 200: 
    url_json = url.json() 
else: 
    print("Error in the URL") 
  
  
#st.title("Adding Lottie Animation in Streamlit WebApp") 
  
st_lottie(url_json,height=250,width=250,reverse=True)
st.title('Resource Finder')
sub_list=('MACHINE LEARNING','DATA ANALYTICS','STATISTICS FOR ANALYTICS')
select=st.selectbox(':blue[**please select your subject**] :point_down:',sub_list)
da,ml,nlp,tsf=0,0,0,0
if select=='DATA ANALYTICS':
    #st.write(':violet[**you have selected**] - :orange[**DATA ANALYTICS**]')
    ml+=1
    st.subheader(':red[Youtube Resources] :bulb:',divider='rainbow')
    st.write(':orange[**1.Excel**]: - :green[**by Simplilearn**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=8Ob8Hre_SnI')
    print('\n'*2)
    st.write(':orange[**2.Data Visualization,Dashboarding and portfolio projects**]: - :green[**by Data Tutorials**:] :point_down:')
    st.write('https://www.youtube.com/@datatutorials1/playlists')
    print('\n'*2)
    st.write(':orange[**3.Excel,Dashboards**]: - :green[**by Chandoo**:] :point_down:')
    st.write('https://www.youtube.com/@chandoo_/videos')
    print('\n'*2)
    st.write(':orange[**4.PowerBI full course**]: - :green[**by Pawan Lalwani**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=UXhGRVTndQA&t=4s')
    print('\n'*2)
    st.write(':orange[**5.Analytics Playlist**]: - :green[**by Great Learning**:] :point_down:')
    st.write('https://www.youtube.com/@greatlearning/playlists')
    st.divider()
    with st.container():
        st.subheader(':red[**Web Resources**] :bulb:',divider='rainbow')
        st.write(':orange[**1.Excel**]: - :green[**by W3Schools**:] :point_down:')
        st.write('https://www.w3schools.com/EXCEL/index.php')
        print('\n'*2)
        st.write(':orange[**2.Advanced Excel**]: - :green[**by Tutorialspoint**:] :point_down:')
        st.write('https://www.tutorialspoint.com/advanced_excel/index.htm')
        st.write(':orange[**3.SQL for Beginners**]: - :green[**by guru99**:] :point_down:')
        st.write('https://www.guru99.com/sql.html')
        st.divider()
    with st.container():
        st.subheader(':red[**Roadmap**] :bulb:',divider='rainbow')
        image = Image.open('data_analytics.png')
        st.image(image, caption='Road to Data Analyst',width=700)
    with open("data_analytics.png", "rb") as file:
            btn = st.download_button(
            label=":red[**Download image**]",
            data=file,
            file_name="data_analytics.png",
            #mime="image/jpg"
          )
    st.divider()
dic={}
#s.write('most requested subject is:',max(array))
#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
#@st.cache_data(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    st.App {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('data_analytics.png')
##3
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
##
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    }
   </style>
    """,
    unsafe_allow_html=True
)
# Insert the CSS into the Streamlit app
#s.markdown(background_image, unsafe_allow_html=True)
#image = Image.open('images.jpg')
#s.image(image, caption='Sunrise by the mountains')
#####Machine Learning
if select=='MACHINE LEARNING':
    ml+=1
    st.subheader(':red[Youtube Resources] :bulb:',divider='rainbow')
    st.write(':orange[**1.Machine Learning Playlist**]: - :green[**by Krish Naik**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=z8sxaUw_f-M&list=PLZoTAELRMXVPjaAzURB77Kz0YXxj65tYz')
    print('\n'*2)
    st.write(':orange[**2.ML**]: - :green[**by StatQuest**:] :point_down:')
    st.write('https://www.youtube.com/@statquest/playlists')
    print('\n'*2)
    st.write(':orange[**3.Data Science**]: - :green[**by Unfold DataScience**:] :point_down:')
    st.write('https://www.youtube.com/@UnfoldDataScience/playlists')
    print('\n'*2)
    st.write(':orange[**4.Complete ML**]: - :green[**by Krish Naik**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=JxgmHe2NyeY')
    print('\n'*2)
    st.write(':orange[**5.ML course for beginners**]: - :green[**by FreeCodeCamp**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=NWONeJKn6kc&t=13683s')
    st.write(':orange[**6.Feature Engineering Playlist**]: - :green[**by CampusX**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=sluoVhT0ehg&list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7')
    st.divider()
    with st.container():
        st.subheader(':red[**Web Resources**] :bulb:',divider='rainbow')
        st.write(':orange[**1.Foundational Courses**]: - :green[**by Google**:] :point_down:')
        st.write('https://developers.google.com/machine-learning/foundational-courses')
        print('\n'*2)
        st.write(':orange[**2.Articles for ML**]: - :green[**by AnalyticsVidhya**:] :point_down:')
        st.write('https://www.analyticsvidhya.com/blog/2022/01/machine-learning-algorithms/')
        st.write(':orange[**3.Machine Learning Tutorial**]: - :green[**by Medium**:] :point_down:')
        st.write('https://medium.com/edureka/machine-learning-tutorial-f2883412fba1')
        st.divider()
    with st.container():
        st.subheader(':red[**Roadmap**] :bulb:',divider='rainbow')
        image = Image.open('ml.jpeg')
        st.image(image, caption='Road to ML',width=700)
    with open("ml.jpeg", "rb") as file:
            btn = st.download_button(
            label=":red[**Download image**]",
            data=file,
            file_name="ml.jpeg",
            #mime="image/jpg"
          )
    st.divider()
##statistics
##for analytics
if select=='STATISTICS FOR ANALYTICS':
    ml+=1
    st.subheader(':red[Youtube Resources] :bulb:',divider='rainbow')
    st.write(':orange[**1.Statistics**]: - :green[**ZedStatistics**:] :point_down:')
    st.write('https://www.youtube.com/@zedstatistics/playlists')
    print('\n'*2)
    st.write(':orange[**2.Stats for Analysts**]: - :green[**by Krish Naik**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=7y3XckjaVOw&list=PLTDARY42LDV6YHSRo669_uDDGmUEmQnDJ')
    print('\n'*2)
    st.write(':orange[**3.Statistics for Beginners**]: - :green[**by FreeCodeCamp**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=xxpc-HPKN28')
    print('\n'*2)
    st.write(':orange[**4.Business Math**]: - :green[**by CodeBasics**:] :point_down:')
    st.write('https://www.youtube.com/watch?v=npgbI8KYvN8')
    #print('\n'*2)
    #st.write(':orange[**5.Analytics Playlist**]: - :green[**by Great Learning**:] :point_down:')
    #st.write('https://www.youtube.com/@greatlearning/playlists')
    st.divider()
