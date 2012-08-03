import tweepy
from urllib import urlencode
from urllib2 import urlopen
import android
from OAuth import *
import os
import sys
droid = android.Android()

timeline_layout = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical"
    android:background="#000000" >

    <TextView
        android:id="@+id/text1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text3"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text4"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text5"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text6"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text7"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <TextView
        android:id="@+id/text8"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="5sp"
        android:layout_marginRight="5sp"
        android:layout_marginTop="3sp"
        android:layout_weight="0.00"
        android:gravity="left"
        android:textSize="10sp" />
    <Button
        android:id="@+id/refreshbutton"
        android:layout_width="180dp"
        android:layout_marginTop="10sp"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        android:text="Refresh" />

    <Button
        android:id="@+id/backbutton"
        android:layout_width="90dp"
        android:layout_marginTop="10sp"
        android:layout_height="wrap_content"
        android:layout_gravity="center_horizontal"
        android:text="Back" />
                                                        
</LinearLayout>
"""

def timeline_loop():
    while True:
        event = droid.eventWait().result
        print event
        if event["name"] == "click":
            id = event["data"]["id"]
            if id == "refreshbutton":
                timeline_view()
            elif id == "backbutton":
                droid.fullDismiss()
        elif event["name"]=="screen":
            if event["data"]=="destroy":
                return


def timeline_view():
    i = 0
    for status in api.home_timeline(count=7):
        i = i + 1
        text_id = 'text' + str(i)
        tweet_displayed = status.author.screen_name + '  :  ' + status.text
        droid.fullSetProperty(text_id,"text",tweet_displayed)


def tl():
    print timeline_layout
    print droid.fullShow(timeline_layout)
    return timeline_view(), timeline_loop()
