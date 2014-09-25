from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from mock import MagicMock

from esef_auth.models.managers import filtered_model_manager
from esef_auth.services.auth_service import AuthService

from esef_auth.tests.models import TestModel2
from esef_auth.tests.models.testmodel1 import TestModel1


__author__ = 'ahmetdal'


class FilteredModelManagerTest(TestCase):
    fixtures = ['filtered_model_manager_test.json']

    def setUp(self):
        super(FilteredModelManagerTest, self).setUp()


    def test_filter(self):
        user = get_user_model().objects.get(pk=2001)
        permission11 = Permission.objects.get(codename='add_%s' % TestModel1._meta.module_name)
        permission12 = Permission.objects.get(codename='change_%s' % TestModel1._meta.module_name)

        permission21 = Permission.objects.get(codename='add_%s' % TestModel2._meta.module_name)
        permission22 = Permission.objects.get(codename='change_%s' % TestModel2._meta.module_name)

        filtered_model_manager.get_current_user = MagicMock(return_value=user)

        self.assertEqual(1, TestModel1.objects.filter().count())
        self.assertEqual(0, TestModel1.objects.filter(data_filter_on='').count())

        self.assertEqual(1, TestModel2.objects.filter().count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='').count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='test_model1').count())


        # Register wrong permission not change one.
        AuthService.register_user_object_permissions(user, TestModel1.objects.get(pk=3001), permission11)

        self.assertEqual(1, TestModel1.objects.filter().count())
        self.assertEqual(0, TestModel1.objects.filter(data_filter_on='').count())

        self.assertEqual(1, TestModel2.objects.filter().count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='').count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='test_model1').count())


        # Register change permission
        AuthService.register_user_object_permissions(user, TestModel1.objects.get(pk=3001), permission12)

        self.assertEqual(1, TestModel1.objects.filter().count())
        self.assertEqual(1, TestModel1.objects.filter(data_filter_on='').count())

        self.assertEqual(1, TestModel2.objects.filter().count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='').count())
        self.assertEqual(1, TestModel2.objects.filter(data_filter_on='test_model1').count())


        # Register wrong permission not change one.
        AuthService.register_user_object_permissions(user, TestModel2.objects.get(pk=4001), permission21)

        self.assertEqual(1, TestModel1.objects.filter().count())
        self.assertEqual(1, TestModel1.objects.filter(data_filter_on='').count())

        self.assertEqual(1, TestModel2.objects.filter().count())
        self.assertEqual(0, TestModel2.objects.filter(data_filter_on='').count())
        self.assertEqual(1, TestModel2.objects.filter(data_filter_on='test_model1').count())

        # Register wrong permission not change one.
        AuthService.register_user_object_permissions(user, TestModel2.objects.get(pk=4001), permission22)

        self.assertEqual(1, TestModel1.objects.filter().count())
        self.assertEqual(1, TestModel1.objects.filter(data_filter_on='').count())

        self.assertEqual(1, TestModel2.objects.filter().count())
        self.assertEqual(1, TestModel2.objects.filter(data_filter_on='').count())
        self.assertEqual(1, TestModel2.objects.filter(data_filter_on='test_model1').count())




