from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericView

urlpatterns = [
    # path('article/', article_list, name=''), #--function_based
    path('article/', ArticleAPIView.as_view(), name=''), # --Class_based
                                                    # --- used to get object by id and delete that obejct...
    path('generic/article/<int:id>/', GenericView.as_view(), name='generic_based'),
    # path('generic/article/', GenericView.as_view(), name='generic_based'),
                                                    # --- remove this if ou want to
                                                    # --- this will give functionality of listig the data presnt in Model .
                                                    # --- used to post and get method.
    # path('detail/<int:Pk>/', article_detail, name='function_based'),
    path('detail/<int:id>/', ArticleDetails.as_view(), name='Class_based'),

]
