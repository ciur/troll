import pytest

from core.models import (
    Document,
    Folder,
)

from core.utils import get_descendants, get_ancestors


@pytest.mark.django_db
def test_get_descendants_depth_1():
    folder = Folder(title="My Documents")
    folder.save()

    for i in range(0, 10):
        doc = Document(title=f"mydoc-{i}.pdf", parent=folder)
        doc.save()

    count = len(
        get_descendants(folder.id, include_self=False)
    )

    assert count == 10


@pytest.mark.django_db
def test_get_descendants_depth_2():
    folder = Folder(title="My Documents")
    folder.save()

    inv = Folder(title="My Invoices", parent=folder)
    inv.save()
    receipts = Folder(title="My Receipts", parent=folder)
    receipts.save()

    # 5 in invoice
    for i in range(0, 5):
        doc = Document(title=f"inv-{i}.pdf", parent=inv)
        doc.save()

    # 5 in receipts
    for i in range(0, 5):
        doc = Document(title=f"receipts-{i}.pdf", parent=receipts)
        doc.save()

    # 5 invoice docs + 5 receipts docs + My Receipts folder +
    # + My Invoices folder
    count = len(
        get_descendants(folder.id, include_self=False)
    )

    assert count == 12


@pytest.mark.django_db
def test_get_ancestors():
    folder = Folder(title="My Documents")
    folder.save()

    inv = Folder(title="My Invoices", parent=folder)
    inv.save()
    receipts = Folder(title="My Receipts", parent=folder)
    receipts.save()

    # 5 in invoice
    for i in range(0, 5):
        doc = Document(title=f"inv-{i}.pdf", parent=inv)
        doc.save()

    # 5 in receipts
    for i in range(0, 5):
        doc = Document(title=f"receipts-{i}.pdf", parent=receipts)
        doc.save()

    doc = Document.objects.get(title="receipts-1.pdf")
    # self, My Receipts, My Documents
    count = len(get_ancestors(doc.id))

    assert count == 3
