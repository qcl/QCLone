QCLone
========

Clone of @qcl, or qcl-one, it will try to post something (e.g. 廢文) on [qcl's Facebook newsfeed](http://facebook.com/qingchengli.tw) 
during 2014/10/09 - 2014/10/24, which is the 新訓 of 研發替代役. 

#Setup
##Access Token
Put your access token in the file ``fb.json``, the format is

    {
        "access_token":"YOUR ACCESS TOKEN"
    }

##Status
Put the message in the file ``status.json``, it's a array of objects, the format is

    [{
        "message","message you want to say"
    },{
        "messsage":"or you want to share a link",
        "link":"http://blog.qcl.tw/"
    }]

##Setup conrtab

    $ crontab -e

Add line:

    15 20 * * * python fb.py
