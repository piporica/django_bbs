from django.db import models
"""
if 게시판을 만든다면? 
글 : id/제목/작성자/날짜/조회수/좋아요/싫어요/내용
댓글 : id/글아이디/내용/작성자
"""


class Post (models.Model):
    title = models.CharField('제목', max_length=100)
    author = models.CharField('글쓴이', max_length=15, null=True)
    date = models.DateTimeField('작성날짜', auto_now_add=True)
    views = models.IntegerField('조회수', default=0)
    likes = models.IntegerField('좋아요', default=0)
    dislikes = models.IntegerField('싫어요', default=0)
    contents = models.TextField('글내용')

    def __str__(self):
        return self.title


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.TextField('댓글내용')
    author = models.CharField('글쓴이', max_length=15)

    def __str__(self):
        return self.contents

# Create your models here.
