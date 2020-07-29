from django.db import models
from passlib.hash import pbkdf2_sha256
# Create your models here.

class Clue(models.Model):
    clue_no = models.IntegerField(default=0)
    question = models.TextField()
    ans1 = models.CharField(max_length = 300)
    ans2 = models.CharField(max_length = 300)
    ans3 = models.CharField(max_length = 300)
    ans4 = models.CharField(max_length = 300)

    def __str__(self):
        return str(self.clue_no)

    def verify(self, ans):
        if(pbkdf2_sha256.verify(ans,self.ans1) or pbkdf2_sha256.verify(ans,self.ans2) or pbkdf2_sha256.verify(ans,self.ans3) or pbkdf2_sha256.verify(ans,self.ans4)):
            return True