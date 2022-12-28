import pytest

from core.models import (
    Node,
    Document,
    Folder,
    NODE_TYPE_FOLDER,
    NODE_TYPE_DOCUMENT,
    OCR_STATUS_UNKNOWN
)

from core.utils import get_descendants

@pytest.mark.django_db
def test_nodes_creation():
    doc = Document(title="mydoc.pdf")
    doc.save()

    folder = Folder(title="My Documents")
    folder.save()

    doc1 = Document(title="doc1.pdf", parent=folder)
    doc2 = Document(title="doc2.pdf", parent=folder)

    doc1.save()
    doc2.save()

    assert Folder.objects.count() == 1
    assert Document.objects.count() == 3
    assert Node.objects.count() == 4


@pytest.mark.django_db
def test_nodes_type():
    doc = Document(title="mydoc.pdf")
    doc.save()

    folder = Folder(title="My Documents")
    folder.save()

    # get a node which we know for fact that is a folder
    node1 = Node.objects.get(title="My Documents")
    assert node1.is_folder is True
    assert node1.type == NODE_TYPE_FOLDER

    # get a node which we know for fact that is a document
    node2 = Node.objects.get(title="mydoc.pdf")
    assert node2.is_folder is False
    assert node2.is_document is True
    assert node2.type == NODE_TYPE_DOCUMENT
    assert node2.document.ocr_status == OCR_STATUS_UNKNOWN


