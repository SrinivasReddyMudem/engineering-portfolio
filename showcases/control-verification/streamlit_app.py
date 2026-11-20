"""Public recorded control demonstration; live engineering remains local."""
from pathlib import Path
import streamlit as st
from replay_page import load_page

st.set_page_config(page_title='Embedded Control & Verification',page_icon='⚙️',layout='wide',initial_sidebar_state='collapsed')
folder=Path(__file__).resolve().parent/'presentation'
try:
 page=load_page(folder)
except (OSError,ValueError,KeyError) as error:
 st.error('Recorded evidence could not be verified: '+str(error))
 st.stop()
st.iframe(page,height='content',width='stretch',alt='Recorded PLC/C operating and verification walkthrough')
with st.expander('Download the readable walkthrough and evidence'):
 for name,label,mime in [('review.md','Readable walkthrough','text/markdown'),('evidence.json','Operating evidence','application/json'),('verification-evidence.json','Defect and repair verification','application/json')]:
  st.download_button(label,(folder/name).read_bytes(),file_name=name,mime=mime,key=name)
