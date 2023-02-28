from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Users must have a unique username')
        # username = self.username
        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        return user




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True,null=True,blank=True)
    username = models.CharField(max_length=40,unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []



    objects = UserManager()

    # def get_absolute_url(self):
    #     return "/users/%i/" % (self.pk)

    def __str__(self):
        return self.username



    '''     relationship_methods    '''
    def add_relationship(self, user, status):
        relationship, created = Relationship.objects.get_or_create(
            from_user=self,
            to_user=user,
            status=status)
        return relationship

    def remove_relationship(self, user, status):
        Relationship.objects.filter(
            from_user=self,
            to_user=user,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_user__status=status,
            to_user__from_user=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_user__status=status,
            from_user__to_user=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)

    # def do_i_follow(self,user):
    #     if Relationship.objects.filter(from_user=self,to_user=user).exists():
    #         return True
    #     else:return False


    '''     tweet methods   

             user.tweets.all() to get users tweets
                tweet.replies.all() to get a tweets replies
                                                            '''

    def create_tweet(self,text):
        return Tweet.objects.create(user=self,text=text)

    def create_reply(self,text,tweet_obj):
        return Tweet.objects.create(
            user=self,
            text=text,
            is_reply=True,
            reply_to_tweet=tweet_obj,
        )

    def create_quote(self, text, tweet_obj):
        return Tweet.objects.create(
            user=self,
            text=text,
            is_quote=True,
            reply_to_quote=tweet_obj,
        )

    def delete_tweet(self,tweet_obj):
        id = tweet_obj.id
        Tweet.objects.filter(
            user=self,
            id=id
        ).delete()
        return

    #get tweets and likes and retweets??
    def get_the_shit(self):
        following_qs = self.get_following()
        data = {}

        for flwr in following_qs:
            data['tweets'] = [i for i in Tweet.objects.filter(user=flwr)]
            data['likes'] = [i for i in Like.objects.filter(user=flwr) if i.tweet.user != self]
            data['retweets'] = [i for i in Retweet.objects.filter(user=flwr)]


        return data

    # def get_tweet_comments(self,)




RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)



class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user',on_delete=models.CASCADE)
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status_for_print = 'follows' if self.status == 1 else 'blocked'
        return '{} {} {}'.format(self.from_user,status_for_print,self.to_user)



class Tweet(models.Model):
    user = models.ForeignKey(User,related_name='tweets',on_delete=models.CASCADE)
    text = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reply = models.BooleanField(default=False)
    is_quote = models.BooleanField(default=False)

    # TODO this ondelete should be changed
    reply_to_tweet = models.ForeignKey('self',related_name='replies',null=True,blank=True,on_delete=models.CASCADE)
    quote_to_tweet = models.ForeignKey('self',related_name='quotes',null=True,blank=True,on_delete=models.CASCADE)



    def __str__(self):
        return '"{}" by {} at {}'.format(self.text,self.user,self.created_at)

    # def get_all_replies(self):
    #     reply_set = self.replies
    #     [ [i.replies] if i.replies for i in reply_set]

    def tweet_count(self):
        return self.likes_of_tweet.all().count()






class Retweet(models.Model):
    user = models.ForeignKey(User, related_name='retweets_by_user',on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='retweets',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User,related_name='likes_of_user',on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,related_name='likes_of_tweet',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} liked tweet id:{} by {}'.format(self.user,self.tweet.id,self.tweet.user)


class Hashtag(models.Model):
    name = models.CharField(max_length=100)
    tweet = models.ManyToManyField(Tweet,related_name='tweets_with_this_hashtag')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name