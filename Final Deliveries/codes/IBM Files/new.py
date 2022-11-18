# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:39:30 2022

@author: SAI SRI  BHOGADI
"""
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "GlV1T6Yw4bjdsiYVvGckVU2Jh2VgkmcKLStQ3TJ0o5WR"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["having_IPhaving_IP_Address"," URLURL_Length" , "Shortining_Service ", "having_At_Symbol " ," double_slash_redirecting ",  " Prefix_Suffix  ", "having_Sub_Domain ", "SSLfinal_State ", "Domain_registeration_length","Favicon" ,"port ", "HTTPS_token","Request_URL ","URL_of_Anchor","Links_in_tags ","SFH","Submitting_to_email","Abnormal_URL", "Redirect ","on_mouseover", "RightClick ","popUpWidnow","Iframe ","age_of_domain", "DNSRecord","web_traffic","Page_Rank ","Google_Index ", "Links_pointing_to_page","Statistical_report"]], "values": [[-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/76aaa647-636d-4953-812d-217381b612c9/predictions?version=2022-08-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
pred=predictions['predictions'][0]['values'][0][0]
if(pred==-1):
    print("You are on fake website")
else:
    print("You are on legitimate website")