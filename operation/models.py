from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course

# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    mobile = models.CharField(max_length=11,verbose_name='手机')
    course_name = models.CharField(max_length=50,verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户: {0} 手机号: {1}'.format(self.name, self.mobile)


class CourseComments(models.Model):
    # 课程评论 涉及到两个外键
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    comment = models.CharField(max_length=200,verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.course)


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    fav_id = models.IntegerField(default=0,verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1,'课程'),(2,'课程机构'),(3,'讲师')),default=1,verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})收藏了{1} '.format(self.user, self.fav_type)


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name='接受用户')
    message = models.CharField(max_length=500,verbose_name='消息内容')
    has_read = models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})接受了{1}'.format(self.user,self.message)


class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="学习时间")

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})学习了{1} '.format(self.user, self.course)