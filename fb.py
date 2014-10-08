# -*- coding: utf-8 -*-
# qcl

import facebook
import json

def postStatusOnFacebook(accessToken):
   
    graph = facebook.GraphAPI(accessToken)

    status = json.load(open("./status.json","r"))

    result = graph.put_object("me","feed",message=status[0]["message"])


if __name__ == "__main__":
    fbSetting = json.load(open("./fb.json","r"))
    postStatusOnFacebook(fbSetting["access_token"])
