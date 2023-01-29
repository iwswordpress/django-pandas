from django.db import models

class Project(models.Model):

    run_id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
    run_date = models.DateField()
    mlr_dataset = models.CharField(max_length=255)
    feature_set = models.CharField(max_length=255)
    split = models.FloatField()
    tuned = models.BooleanField()
    setup = models.CharField(max_length=1000)
    best = models.CharField(max_length=1000)
    holdout_acc = models.FloatField()
    metrics_dict = models.CharField(max_length=1000)
    accuracy = models.FloatField()
    roc_auc = models.FloatField()
    recall = models.FloatField()
    precision = models.FloatField()
    f1 = models.FloatField()
    kappa = models.FloatField()
    mcc = models.FloatField()
  
    def __str__(self):
        return self.run_id

