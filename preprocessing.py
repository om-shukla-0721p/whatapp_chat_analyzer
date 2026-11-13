# module 2) To preprocess the data as required for better further use
# aim-->
# 1) divide content into ->sender ,message
# 2) have type and subtype for classification

def preprocess_messages(parsed_message):
    new_parse=[]

    for msg in parsed_message:
        date=msg["date"]
        time=msg["time"]
        period=msg["period"]
        content=msg["content"]

    # spliting sender and message from content
        if ":" in content:
            sender,message=content.split(":",1)
            sender=sender.strip()
            message=message.strip()
        else:
            sender=None
            message=content.strip()

        # now assigning type of messages to data

        # Classification
        if sender is not None and message == "": # call
            msg_type = "Call"
            subtype = "Unspecified"

        elif sender is None: # system
            msg_type="System_Notification"
            subtype="Unknown"

        else: # media and others
            if "https://" in message or "http://" in message:
                msg_type="Link"
                subtype="URL"
        
            elif "(file attached)" in message:
                msg_type="Media"
                if "STK-" in message:
                    subtype="Sticker"
                elif "AUD" in message:
                    subtype="Audio"
                elif "PTT-" in message:
                    subtype="Voice_message"
                elif "IMG" in message:
                    subtype="Image"
                elif "VID" in message:
                    subtype="Video"
                elif ".pdf" in message:
                    subtype="PDF"
                else:
                    subtype="Other"
                    
            else:
                msg_type="Text"
                subtype="Text"
                

        # Build dictionary and append it here
        current={
            "date":date,
            "time":time,
            "period":period,
            "content":content,
            "sender":sender,
            "message":message,
            "type":msg_type,
            "subtype": subtype ,
        }
        new_parse.append(current)

    return new_parse



    
    


