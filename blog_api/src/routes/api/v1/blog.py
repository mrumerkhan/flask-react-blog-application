from flask import Blueprint

from views.blog import BlogListView, BlogDetailView

blog = Blueprint("blog", __name__)
blog.add_url_rule(
    "/items", view_func=BlogListView.as_view("blog-list"), methods=["GET", "POST"]
)
blog.add_url_rule(
    "/items/<int:id>",
    view_func=BlogDetailView.as_view("blog-detail"),
    methods=["GET", "PUT", "PATCH", "DELETE"],
)
