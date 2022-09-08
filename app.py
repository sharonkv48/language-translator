from optparse import Option
import streamlit as st
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

# setting the api key
api_key = 'MhOj3a_u0V-rbrptfRLr6kk5toWx5KxHN4ew4PfivJBd'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/5db23956-e51e-4ce6-960f-3fa08d6ff0d1'

authenticator = IAMAuthenticator(apikey= api_key)

langtranslator = LanguageTranslatorV3(version='2018-05-01', authenticator = authenticator)

langtranslator.set_service_url(url)

st.title("Language Translator")

# setting the dropdown list of the languages

option = st.selectbox(
    'which language would you like to type',
    ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))

option1 = st.selectbox('Which language would you like to translate to',
                       ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))


sent = "Enter the text in "+option+" language in the text-area provided below"

# setting up the dictionary of languages to their keywords


language_lib = {'English': 'en', 'Arabic': 'ar',
                'Hindi': 'hi', 'Spanish': 'es', 'German': 'de', 'Korean': 'ko'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select different Language for Translation")

        else:

            translate_code = language_lib[option]+'-'+language_lib[option1]

            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write("Please do cross check if text-area is filled with sentences or not")
