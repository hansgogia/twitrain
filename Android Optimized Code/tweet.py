import sys
import android
import tweepy
import re
from OAuth import *
import os
droid = android.Android()
def tweet_post():
    while True:
        event = droid.eventWait().result
        print event
        if event["name"] == "click":
            id = event["data"]["id"]
            if id == "tweetbutton":
                status_temp = droid.fullQueryDetail("editText2").result
                status_extract = re.search('u\'text\': u\'(.+?)\'', str(status_temp))
                status_post = ''
                if status_extract:
                    status_post = status_extract.group(1)
                if len(status_post) <= 140:
                    answer = droid.dialogGetInput('','in reply to last mention? y/n').result
                    if answer == 'n':
                        api.update_status(status_post)
                        droid.makeToast("Check Timeline, tweet posted")
                    elif answer == 'y':
                        for mention in api.mentions(count = 1):
                            api.update_status(status_post, in_reply_to_status_id = mention.id)
                            droid.makeToast("Check Timeline, reply posted")
            elif id == "backbutton":
                droid.fullDismiss()
        elif event["name"]=="screen":
            if event["data"]=="destroy":
                return

    
tweet_layout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical"
    android:background="#000000" >

    <EditText
        android:id="@+id/editText2"
        android:layout_width="match_parent"
        android:layout_height="160dp"
        android:ems="10" />

    <Button
        android:id="@+id/tweetbutton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="right"
        android:text="Tweet" />

    <Button
        android:id="@+id/backbutton"
        android:layout_width="90dp"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        android:text="back" />

    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        android:text="Twitrain Alpha 0.1"
        android:textAppearance="?android:attr/textAppearanceSmall"
        android:textSize="14dp" />

</LinearLayout>
"""
def post():
    print tweet_layout
    print droid.fullShow(tweet_layout)
    return tweet_post()
