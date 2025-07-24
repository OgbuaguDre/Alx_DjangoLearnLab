# Permissions & Groups Setup

## Custom Permissions (defined in Book model)
- can_view: View book list/details
- can_create: Create a new book
- can_edit: Edit an existing book
- can_delete: Delete a book

## Groups (created via Admin)
- Viewers: Only `can_view`
- Editors: `can_view`, `can_create`, `can_edit`
- Admins: All permissions

## Usage in Views
All views are decorated with `@permission_required` to restrict access.
Example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    ...
