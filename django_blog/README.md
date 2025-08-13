# Blog Post CRUD

Routes:
- /posts/ → list all posts
- /posts/new/ → create (login required)
- /posts/<pk>/ → detail
- /posts/<pk>/edit/ → update (author only)
- /posts/<pk>/delete/ → delete (author only)

Permissions:
- Anyone can view list & details.
- Only authenticated users can create posts.
- Only the post author can edit or delete.

Notes:
- Set `LOGIN_URL` in settings (e.g. '/accounts/login/') so `LoginRequiredMixin` redirects properly.
- If you use the provided custom `PostForm.save(..., author=...)` call in views, ensure `form.save()` in views is invoked accordingly or default to using `form.instance.author = request.user`.
