from django.db import models


class Node(models.Model):

    FOLDER_TYPE = 'folder'
    DOCUMENT_TYPE = 'document'

    NODE_TYPES = (
        (FOLDER_TYPE, 'folder'),
        (DOCUMENT_TYPE, 'document')
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=256)
    type = models.CharField(
        max_length=8,
        choices=NODE_TYPES,
        default=DOCUMENT_TYPE
    )
