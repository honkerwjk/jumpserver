# -*- coding: utf-8 -*-
#

from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from common import api as capi
from .. import api


app_name = 'orgs'
router = DefaultRouter()

router.register(r'orgs', api.OrgViewSet, 'org')
router.register(r'org-memeber-relation', api.OrgMemberRelationBulkViewSet, 'org-memeber-relation')

old_version_urlpatterns = [
    re_path('(?P<resource>org)/.*', capi.redirect_plural_name_api)
]

urlpatterns = router.urls + old_version_urlpatterns
