import tweepy
from OAuth import *
import os

def main():
    def error():
        print 'Enter some value or the value entered by you is incorrect'

    def post():
        status_post = raw_input('Enter 140 Character Status:\n')
        if len(status_post) <= 140:
            answer = raw_input('in reply to last mention? y/n\n')
            if answer == 'n':
                api.update_status(status_post)
            elif answer == 'y':
                for mention in api.mentions(count = 1):
                    api.update_status(status_post, in_reply_to_status_id = mention.id)
            print 'Check Timeline'
            
        else:
            print 'Length of tweet is over 140 characters or some other error may have occured, try again'
        
    def friends_tl():
        user = raw_input('Enter the name of the user:\n')
        if len(user) > 0:
            for status in tweepy.api.user_timeline(user, count=10):
                print '-->  ', status.author.screen_name,':', status.text, '\n\n'
        else :
            print 'User not specified'

    def my_tl():
        for status in api.home_timeline():
            print '-->  ', status.author.screen_name, ':' ,status.text, '\n'

    def mentions():
        for mention in api.mentions():
            print '-->  ', mention.author.screen_name, ':' ,mention.text, '\n'

    def retweet():
        def retweets_by_me():
            for retweet in api.retweeted_by_me():
                print '-->  ', retweet.author.screen_name, ':' ,retweet.text, '\n'
                
        def retweets_to_me():
            for retweet in api.retweeted_to_me():
                print '-->', retweet.author.screen_name, ':' ,retweet.text, '\n'

        def retweets_of_me():
            for retweet in api.retweets_of_me():
                print '-->  ', retweet.author.screen_name, ':' ,retweet.text, '\n'

        while True:
#            option = {'0' : retweets_by_me,
#                      '1' : retweets_to_me,
#                      '2' : retweets_of_me,
#                      '3' : break
#                      }
            print "Enter:\n 0:retweets by me,\n 1:retweet to me,\n 2:retweet of me,\n 3:back\n\n "
            no = raw_input("OPTION ---> ")
#            option.get(no)()
            if no == '0':
                retweets_by_me()
            elif no == '1':
                retweets_to_me()
            elif no == '2':
                retweets_of_me()
            elif no == '3':
                break

    def direct():
        def dm():
            for messages in api.direct_messages():
                print '-->', messages.sender.screen_name,':',messages.text,'\nsent at :',messages.created_at, '\n'

        def sent_dm():
            for messages in api.sent_direct_messages():
                print '-->', messages.sender.screen_name,':',messages.text,'\nsent at :',messages.created_at, '\n'

        def send_dm():
            direct_msg = raw_input('Enter 140 Character Message:\n')
            to = raw_input('enter screen name\nTo: ')
            if len(direct_msg) <= 140:
                api.send_direct_message(screen_name = to, text = direct_msg)
            else:
                print 'Length of message is over 140 characters or some other error may have occured, try again'
            print "DM sent\n\n"

        while True:
            print "Enter:\n 0:dm,\n 1:send dm,\n 2:sent dm,\n 3:back\n\n "
            value = raw_input("OPTION ---> ")
            if value == '0':
                dm()
            elif value == '1':
                send_dm()
            elif value == '2':
                sent_dm()
            elif value == '3':
                break
    user_name = api.me()
    def followers():
        for user in api.followers():
            print '-->' , user.screen_name,':', user.name, '\n'
    def following():
        for user in api.friends():
            print '-->', user.screen_name, ':', user.name ,'\n'
    def follow():
        get = raw_input("Follow a user? Enter the screen name:\n")
        chck = api.exists_friendship(user_name.screen_name,get)
        if chck == False:
            friend = api.create_friendship(get)
            print '-->', friend.name, 'followed'
        else:
            ans = raw_input("Already following, Unfollow(y/n)?")
            if ans == 'y':
                unfriend = api.destroy_friendship(get)
                print '-->', unfriend.name, 'unfollowed'
                    
    def logout():
        os.remove(".twitrain_oauth")
        exit

    while True:
        options = {'0' : post,
                   '1' : friends_tl,
                   '2' : my_tl,
                   '3' : mentions,
                   '4' : retweet,
                   '5' : direct,
                   '6' : followers,
                   '7' : following,
                   '8' : follow,
                   '9' : exit,
                   '10': logout,
                   }
        print "Enter:\n 0: post,\n 1: friends timeline\n 2: your timeline\n 3: mentions\n 4: Retweets\n 5: dm\n 6: followers\n 7: following\n 8: follow\n 9: exit\n 10: logout\n\n"
        num = raw_input("OPTION --->  ")
        options.get(num,error)()

if __name__ == '__main__':
    main()
