from django.db import models


# [payer, reciever,amount]
# Create your models here.
class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    members = models.JSONField(default=list)
    totalmembers = models.IntegerField(default=0)
    payments = models.JSONField(default=list)
    totalpayment = models.IntegerField(default=0)
    paymentpermember = models.IntegerField(default=0)
    dues = models.JSONField(default=list)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.members:
            # Calculate fields before saving
            self.totalmembers = len(self.members)
            self.totalpayment = sum([payment['amount'] for payment in self.payments])
            self.paymentpermember = self.totalpayment / self.totalmembers

        # Call the parent class's save method, passing the arguments
        super(Trip, self).save(*args, **kwargs)

    def newmember(self,member):
        for me in self.members:
            self.dues.append([member,me,0,False])
        self.members.append(member)
        self.totalmembers = len(self.members)
        self.save()

    def newpayment(self,member,amount,shop):
        self.payments.append(
        {
            "shop": shop,
            "member": member,
            "amount":amount
        }
        )
        for due in self.dues:
            if due[0] == member:
                due[2] -= amount/self.totalmembers
                due[3] = False
            elif due[1] == member:
                due[2] += amount/self.totalmembers
                due[3] = False
        self.save()
