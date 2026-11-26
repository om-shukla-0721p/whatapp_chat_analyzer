# this is the parser code 
# when the code first comes its not readable 
# we correct that here

import re # re for matching pattern and text manipulation
import pandas as pd # pandas to convert dict into dataframe

# reading the file
def read_chat(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        data=file.read()

    return data


# pattern
# pattern = r'^(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2}(?::\d{2})?)\s*([APap][Mm]) - (.*)$'
# the pattern of the data in the raw data which we will use to encod the raw_data
# this splits the data into 4 groups
# 1) date 
# 2) time
# 3) period
# 4) content



def parse_chat(messages):
    # pattern = r'^(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2}(?::\d{2})?)(?:\s*([APap][Mm]))? - (.*)$'
    mobile_pattern = r'^(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}(?::\d{2})?)(?:\s*([APap][Mm]))? - (.*)$'
    # pc_pattern = r'^\[(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2}:\d{2})\s*([APap][Mm])\] (.*)$'
    parsed_chat=[] # this stores the parsed chat
    unparsed_chat=[] # the chat which cant be parsed 
    current_message=None # the current message we will store

    for line in messages.splitlines():
        match=re.match(mobile_pattern,line)
        if match:
            if current_message is not None:
                parsed_chat.append(current_message)
            date,time,period,content=match.groups()
            if period is None:
                period=""
            
            current_message={
                "date":date,
                "time":time,
                "period":period,
                "content":content
            } 
            # making the next message
        else: # if not mathed meaning maybe the continuation of prev message
            if current_message is not None:
                current_message["content"]+="\n"+ line
            elif line.strip(): # empty string->False /else->True
                unparsed_chat.append(line) # as it has no prev continuation and 
    if current_message is not None:
        parsed_chat.append(current_message)

    return parsed_chat,unparsed_chat


# STAGE 2
# converting our parsed data  into a pandas dataframe

def create_df(parsed_chat):
    df=pd.DataFrame(parsed_chat)
    return df






    
