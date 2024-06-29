# from django.db import models

# # Create your models here.

# # Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=30)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

#     def __str__(self):
#         return self.title


# class Expenses(models.Model):
#     title = models.CharField(max_length=30, )
#     costs = models.IntegerField(verbose_name='total cost', default=0)
#     description = models.TextField(null=True, blank=True, )
#     date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
#     timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     receipt = models.FileField(upload_to='receipts/', null=True, blank=True)

#     def __str__(self):
#         return self.title


# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)


# class Friend(models.Model):
#     user1 = models.ForeignKey(User, related_name='friends1', on_delete=models.CASCADE)
#     user2 = models.ForeignKey(User, related_name='friends2', on_delete=models.CASCADE)


# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     created_by = models.ForeignKey(User, related_name='groups_created', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class GroupMember(models.Model):
#     group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='group_memberships', on_delete=models.CASCADE)

# class GroupExpense(models.Model):
#     group = models.ForeignKey(Group, related_name='expenses', on_delete=models.CASCADE)
#     added_by = models.ForeignKey(User, related_name='group_expenses_added', on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     total_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     division_percent = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
#     file_upload = models.FileField(upload_to='bills/', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class GroupHistory(models.Model):
#     group = models.ForeignKey(Group, related_name='history', on_delete=models.CASCADE)
#     expense = models.ForeignKey(GroupExpense, related_name='history', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
