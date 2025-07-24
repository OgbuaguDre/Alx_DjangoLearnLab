# Django Permissions and Groups Setup

This Django project demonstrates how to use **custom permissions** and **user groups** to control access to actions like viewing, creating, editing, and deleting model instances.

---

## Custom Permissions

Defined in `Book` model (`bookshelf/models.py`):

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
