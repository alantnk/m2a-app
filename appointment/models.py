from django.db import models

STATUS_CHOICES = [
    ("1", "Agendado"),
    ("2", "Concluído"),
    ("3", "Cancelado"),
]


class Schedule(models.Model):
    date_time = models.DateTimeField()
    professional = models.ForeignKey(
        "record.Professional", null=True, on_delete=models.SET_NULL
    )  # noqa E501
    service = models.ForeignKey(
        "record.Service", null=True, on_delete=models.SET_NULL
    )  # noqa E501
    customer = models.ForeignKey(
        "record.Customer", null=True, on_delete=models.SET_NULL
    )
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="1"
    )  # noqa E501

    class Meta:
        unique_together = ("date_time", "professional")
        indexes = [
            models.Index(
                fields=["date_time", "status"], name="idx_schedule_data_status"
            ),
        ]

    def __str__(self):
        return f"{self.date_time} - {self.professional.name} with {self.customer.name} for {self.service.title}"  # noqa E501
