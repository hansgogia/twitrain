import android
import os
import sys
import tweepy
import tweet
import timeline
droid = android.Android()

main_layout = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical"
    android:background="#000000" >

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="100dp"
        android:layout_gravity="center_horizontal"
        android:text="Twitrain Alpha 0.1"
        android:textSize="15dp" />

    <Button
        android:id="@+id/loginbutton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Login" />

    <Button
        android:id="@+id/timelinebutton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="timeline" />

    <Button
        android:id="@+id/tweetmain"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Tweet" />

    <Button
        android:id="@+id/exit"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="exit" />

</LinearLayout>
"""
def main_loop():
    while True:
        event = droid.eventWait().result
        print event
        if event["name"] == "click":
            id = event["data"]["id"]
            if id == "tweetmain":
                tweet.post()
            elif id == "timelinebutton":
                timeline.tl()
            elif id == "exit":
                exit(0)
        elif event["name"]=="screen":
            if event["data"]=="destroy":
                return
print main_layout
print droid.fullShow(main_layout)
main_loop()
