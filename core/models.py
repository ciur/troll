from django.db import models


NODE_TYPE_FOLDER = 'folder'
NODE_TYPE_DOCUMENT = 'document'

OCR_STATUS_SUCCEEDED = 'succeeded'
OCR_STATUS_RECEIVED = 'received'
OCR_STATUS_STARTED = 'started'
OCR_STATUS_FAILED = 'failed'
OCR_STATUS_UNKNOWN = 'unknown'

OCR_STATUS_CHOICES = [
    ('unknown', 'Unknown'),
    ('received', 'Received'),
    ('started', 'Started'),
    ('succeeded', 'Succeeded'),
    ('failed', 'Failed'),
]


class Node(models.Model):

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True
    )

    title = models.CharField(max_length=256)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'title'], name='unique title per parent'
            ),
        ]

    @property
    def type(self):
        try:
            self.folder
        except Folder.DoesNotExist:
            return NODE_TYPE_DOCUMENT
        return NODE_TYPE_FOLDER

    @property
    def is_folder(self):
        return self.type == NODE_TYPE_FOLDER

    @property
    def is_document(self):
        return self.type == NODE_TYPE_DOCUMENT


class Document(Node):
    ocr_status = models.CharField(
        choices=OCR_STATUS_CHOICES,
        default=OCR_STATUS_UNKNOWN,
        max_length=32
    )

    def __str__(self):
        return f"Document({self.id}, {self.title})"


class Folder(Node):

    def __str__(self):
        return f"Folder({self.id}, {self.title})"
