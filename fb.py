# -*- coding: utf-8 -*-
# qcl

import facebook
import json
from datetime import datetime

def postStatusOnFacebook(accessToken):
    
    # get stored status.
    status = json.load(open("./status.json","r"))
    
    today = datetime.now()
    postIndex = today.day - 8

    if postIndex < 0 or postIndex >= len(status):
        print "There is no content."
        return

    post = status[postIndex]

    # create facebook GraphAPI
    graph = facebook.GraphAPI(accessToken)
    if "link" in post:
        result = graph.put_object("me","feed",message=post["message"],link=post["link"])
        pass
    else:
        result = graph.put_object("me","feed",message=post["message"])
        pass
    
    print "Posted, result=",result

if __name__ == "__main__":
    fbSetting = json.load(open("./fb.json","r"))
    postStatusOnFacebook(fbSetting["access_token"])
