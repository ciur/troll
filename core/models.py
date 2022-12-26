from django.db import models


FOLDER_TYPE = 'folder'
DOCUMENT_TYPE = 'document'

NODE_TYPES = (
    (FOLDER_TYPE, 'folder'),
    (DOCUMENT_TYPE, 'document')
)


class Node(models.Model):

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=256)
    type = models.CharField(
        max_length=8,
        choices=NODE_TYPES,
        default=DOCUMENT_TYPE,
        null=False,
        blank=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'title'], name='unique title per parent'
            ),
            models.CheckConstraint(
                name="Node can be either document or folder only",
                check=(models.Q(type__in=(FOLDER_TYPE, DOCUMENT_TYPE)))
            )
        ]
