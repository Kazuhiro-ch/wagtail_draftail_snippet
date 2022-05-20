from django.urls import path, re_path


from wagtail.snippets.views import chooser

from .views import choose_snippet_link_model, choose_snippet_embed_model


app_name = "wagtaildraftailsnippet"

urlpatterns = [
    re_path(
        r"^choose-link-model/$",
        choose_snippet_link_model,
        name="choose-snippet-link-model",
    ),
    re_path(
        r"^choose-embed-model/$",
        choose_snippet_embed_model,
        name="choose-snippet-embed-model",
    ),
    path(
        "choose/", chooser.ChooseView.as_view(), name="choose_generic"
    ),  # This exists only to get the additional URL params added via JS in wagtail-draftail-snippet.js line 50
]
