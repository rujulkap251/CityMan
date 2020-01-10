# from django.test import TestCase
# import unittest
# import json
# from unittest import skipIf, mock
# #from django.urls import reverse
# from django.utils import timezone
# from django.apps.registry import Apps
# from django.apps import AppConfig, apps
# from django import forms
# from django.core.checks import Tags, run_checks
# from django.core.checks.registry import CheckRegistry
# from django.contrib import admin
# from django.contrib.admin.decorators import register
# from django.contrib.admin.sites import site
# from django.core.exceptions import ImproperlyConfigured
# from django.db import connection, models
# from django.test import SimpleTestCase, override_settings
# from django.contrib.admin.models import LogEntry
# from django.db import transaction
# from django.core.checks.caches import E001
# from django.test.utils import override_settings
# from . import views
# from . import apps as de_app
# from .apps import  MyappConfig
# from .models import Station,Rtstation,Luastations, Rtdart, Rtluas, Rtstation1
#
# class URLTest(TestCase):
#
#     def test_root_url_shows_links_to_all_polls(self):
#         response = self.client.get('/form/')
#         # check we've used the right template
#         self.assertTemplateUsed(response, 'myapp/form.html')
#
#    # def test_calendar_url_shows_links_to_all_polls(self):
#     #    response = self.client.get('/calendar/')
#         # check we've used the right template
#      #   self.assertTemplateUsed(response, 'myapp/calendar.html')
#
#     def test_homepage_url_shows_links_to_all_polls(self):
#         response = self.client.get('/')
#         # check we've used the right template
#         self.assertTemplateUsed(response, 'myapp/homepage.html')
#
#     def test_amartest_url_shows_links_to_all_polls(self):
#         response = self.client.get('/test/')
#         # check we've used the right template
#         self.assertTemplateUsed(response, 'myapp/amartest.html')
#
#     def test_luas_url_shows_links_to_all_polls(self):
#         response = self.client.get('/luas/')
#         # check we've used the right template
#         self.assertTemplateUsed(response, 'myapp/homepage_luas.html')
#
#     def test_dart_url_shows_links_to_all_polls(self):
#         response = self.client.get('/dart/')
#         # check we've used the right template
#         self.assertTemplateUsed(response, 'myapp/homepage_dart.html')
#
#    # def test_map_url_shows_links_to_all_polls(self):
#        # response = self.client.get('/map/')
#         # check we've used the right template
#        # self.assertEqual(response.status_code, 200)
#
# class CheckCacheSettingsAppDirsTest(SimpleTestCase):
#     VALID_CACHES_CONFIGURATION = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         },
#     }
#     INVALID_CACHES_CONFIGURATION = {
#         'other': {
#             'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         },
#     }
#
#     @property
#     def func(self):
#         from django.core.checks.caches import check_default_cache_is_configured
#         return check_default_cache_is_configured
#
#     @override_settings(CACHES=VALID_CACHES_CONFIGURATION)
#     def test_default_cache_included(self):
#         """
#         Don't error if 'default' is present in CACHES setting.
#         """
#         self.assertEqual(self.func(None), [])
#
#     @override_settings(CACHES=INVALID_CACHES_CONFIGURATION)
#     def test_default_cache_not_included(self):
#         """
#         Error if 'default' not present in CACHES setting.
#         """
#         self.assertEqual(self.func(None), [E001])
#
# SOME_INSTALLED_APPS = [
#     'apps.MyappConfig',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
#
# SOME_INSTALLED_APPS_NAMES = [
#     'django.contrib.admin',
#     'django.contrib.auth',
# ] + SOME_INSTALLED_APPS[2:]
#
# class APPTest(TestCase):
#
#     def test_singleton_master(self):
#         """
#         Only one master registry can exist.
#         """
#         with self.assertRaises(RuntimeError):
#             Apps(installed_apps=None)
#
#    # def test_app_config(self):
#        # with self.settings(INSTALLED_APPS=['myapp.apps']):
#           #  config = apps.get_app_config('apps')
#       #  self.assertIsInstance(config, MyappConfig)
#
# class DatabaseCheckTests(TestCase):
#     databases = {'default', 'other'}
#
#     @property
#     def func(self):
#         from django.core.checks.database import check_database_backends
#         return check_database_backends
#
#     def test_database_checks_not_run_by_default(self):
#         """
#         `database` checks are only run when their tag is specified.
#         """
#         def f1(**kwargs):
#             return [5]
#
#         registry = CheckRegistry()
#         registry.register(Tags.database)(f1)
#         errors = registry.run_checks()
#         self.assertEqual(errors, [])
#
#         errors2 = registry.run_checks(tags=[Tags.database])
#         self.assertEqual(errors2, [5])
#
# class NameAdmin(admin.ModelAdmin):
#
#     list_display = ['name']
#     save_on_top = True
#
# class CustomSite(admin.AdminSite):
#     pass
#
# class TestRegistration(SimpleTestCase):
#     def setUp(self):
#         self.site = admin.AdminSite()
#
# class TestRegistrationDecorator(SimpleTestCase):
#
#     def setUp(self):
#         self.default_site = site
#         self.custom_site = CustomSite()
#
# class TextFieldTests(TestCase):
#
#     def test_max_length_passed_to_formfield(self):
#         """
#         TextField passes its max_length attribute to form fields created using
#         their formfield() method.
#         """
#         tf1 = models.TextField()
#         tf2 = models.TextField(max_length=2345)
#         self.assertIsNone(tf1.formfield().max_length)
#         self.assertEqual(2345, tf2.formfield().max_length)
#
#     def test_choices_generates_select_widget(self):
#         """A TextField with choices uses a Select widget."""
#         f = models.TextField(choices=[('A', 'A'), ('B', 'B')])
#         self.assertIsInstance(f.formfield().widget, forms.Select)
#
#     def test_to_python(self):
#         """TextField.to_python() should return a string."""
#         f = models.TextField()
#         self.assertEqual(f.to_python(1), '1')
#
# @skipIf(connection.vendor == 'mysql', 'Running on MySQL requires utf8mb4 encoding (#18392)')
# class Luasstations_TextfieldTest(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Luastations_stopid
#         self.assertEqual(Luastations.objects.filter(stopid=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#    	#Luastations_sname
#         self.assertEqual(Luastations.objects.filter(name=5).count(), 0)
#
#
# class Luasstations_TextfieldTest_2(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#     	#Luastations_abbr
#         self.assertEqual(Luastations.objects.filter(abbr=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#     	#Luastations_lineid
#         self.assertEqual(Luastations.objects.filter(lineid=5).count(), 0)
#
# class Luasstations_TextfieldTest_3(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#     	#Luastations_sortorder
#         self.assertEqual(Luastations.objects.filter(sortorder=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#     	#Luastations_isenabled
#         self.assertEqual(Luastations.objects.filter(isenabled=5).count(), 0)
#
# class Luasstations_TextfieldTest_4(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#     	#Luastations_isparkandride
#         self.assertEqual(Luastations.objects.filter(isparkandride=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_iscycleandride
#         self.assertEqual(Luastations.objects.filter(iscycleandride=5).count(), 0)
#
# class Luasstations_TextfieldTest_5(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_zonecounta
#         self.assertEqual(Luastations.objects.filter(zonecounta=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_zonecountb
#         self.assertEqual(Luastations.objects.filter(zonecountb=5).count(), 0)
#
# class Luasstations_TextfieldTest_6(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_lat
#         self.assertEqual(Luastations.objects.filter(lat=5).count(), 0)
#
# class Luasstations_TextfieldTest_7(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_long
#         self.assertEqual(Luastations.objects.filter(long=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
# 	#Luastations_irishname
#         self.assertEqual(Luastations.objects.filter(irishname=5).count(), 0)
#
# class Rtdart_Textfieldtests(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_tation_mhide
#         self.assertEqual(Rtdart.objects.filter(station_mhide=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_pmnck
#         self.assertEqual(Rtdart.objects.filter(station_pmnck=5).count(), 0)
#
# class Rtdart_Textfieldtests_2(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_grgrd
#         self.assertEqual(Rtdart.objects.filter(station_grgrd=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_suttn
#         self.assertEqual(Rtdart.objects.filter(station_suttn=5).count(), 0)
#
# class Rtdart_Textfieldtests_3(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_bysde=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_hwthj=5).count(), 0)
#
# class Rtdart_Textfieldtests_4(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_howth=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_hkbrck=5).count(), 0)
#
# class Rtdart_Textfieldtests_5(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_rahny=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_htcwn=5).count(), 0)
#
# class Rtdart_Textfieldtests_6(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_klstr=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_ctarf=5).count(), 0)
#
# class Rtdart_Textfieldtests_7(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_cnlly=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_rahny=5).count(), 0)
#
# class Rtdart_Textfieldtests_8(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_tara_field=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_perse=5).count(), 0)
#
# class Rtdart_Textfieldtests_9(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_gcdk_field=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_ldwne=5).count(), 0)
#
# class Rtdart_Textfieldtests_10(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_smont=5).count(), 0)
#
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_sidny=5).count(), 0)
#
# class Rtdart_Textfieldtests_11(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_btstn=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_hrock=5).count(), 0)
#
# class Rtdart_Textfieldtests_12(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_seapt=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_shill=5).count(), 0)
#
# class Rtdart_Textfieldtests_13(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_dlery=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_scove=5).count(), 0)
#
# class Rtdart_Textfieldtests_14(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_glgry=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_dlkey=5).count(), 0)
#
# class Rtdart_Textfieldtests_15(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_kilny=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_skill=5).count(), 0)
#
# class Rtdart_Textfieldtests_16(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_bray_field=5).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Rtdart.objects.filter(station_kcool=5).count(), 0)
#
# class BasicIntegerFieldTest(TestCase):
#
#     def test_documented_range(self):
#         """
#         Values within the documented safe range pass validation, and can be
#         saved and retrieved without corruption.
#         """
#         min_value, max_value = self.documented_range
#
#         instance = self.model(value=min_value)
#         instance.full_clean()
#         instance.save()
#         qs = self.model.objects.filter(value__lte=min_value)
#         self.assertEqual(qs.count(), 1)
#         self.assertEqual(qs[0].value, min_value)
#
#         instance = self.model(value=max_value)
#         instance.full_clean()
#         instance.save()
#         qs = self.model.objects.filter(value__gte=max_value)
#         self.assertEqual(qs.count(), 1)
#         self.assertEqual(qs[0].value, max_value)
#
# class BigIntegerFieldTests(BasicIntegerFieldTest):
#
# 	model = Rtstation
# 	documented_range = (-9223372036854775808, 9223372036854775807)
#
# class BigIntegerFieldTests_Rtstation1(BasicIntegerFieldTest):
#
# 	model = Rtstation1
# 	documented_range = (-9223372036854775808, 9223372036854775807)
#
# class Rtweather_Textfieldtest(TestCase):
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Station.objects.filter(address=10).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Station.objects.filter(contract_name=10).count(), 0)
#
#     def test_lookup_integer_in_textfield(self):
#         #Rtdart_station_bysde
#         self.assertEqual(Station.objects.filter(name=10).count(), 0)
#
# class Station_BigIntegerTest(TestCase):
#
#         model = Station
#         documented_range = (-9223372036854775808, 9223372036854775807)
#
# class BooleanFieldTests(TestCase):
#
#     def _test_get_prep_value(self, f):
#         self.assertIs(f.get_prep_value(True), True)
#         self.assertIs(f.get_prep_value('1'), True)
#         self.assertIs(f.get_prep_value(1), True)
#         self.assertIs(f.get_prep_value(False), False)
#         self.assertIs(f.get_prep_value('0'), False)
#         self.assertIs(f.get_prep_value(0), False)
#         self.assertIsNone(f.get_prep_value(None))
#
#     def test_booleanfield_to_python(self):
#         self._test_to_python(models.BooleanField())
#
#
# class TestFloatField(TestCase):
#
#     def test_float_validates_object(self):
#         instance = Station(size=2.5)
#         # Try setting float field to unsaved object
#         instance.size = instance
#         with transaction.atomic():
#             with self.assertRaises(TypeError):
#                 instance.save()
#         # Set value to valid and save
#         instance.size = 2.5
#         instance.save()
#         self.assertTrue(instance.id)
#         # Set field to object on saved instance
#         instance.size = instance
#         msg = (
#             'Tried to update field model_fields.FloatModel.size with a model '
#             'instance, %r. Use a value compatible with FloatField.'
#         ) % instance
#         with transaction.atomic():
#             with self.assertRaisesMessage(TypeError, msg):
#                 instance.save()
#         # Try setting field to object on retrieved object
#         obj = Station.objects.get(pk=instance.id)
#         obj.size = obj
#         with self.assertRaisesMessage(TypeError, msg):
#             obj.save()
#
# class TestCharField(TestCase):
#
#     def test_max_length_passed_to_formfield(self):
#         """
#         CharField passes its max_length attribute to form fields created using
#         the formfield() method.
#         """
#         cf1 = models.CharField()
#         cf2 = models.CharField(max_length=1234)
#         self.assertIsNone(cf1.formfield().max_length)
#         self.assertEqual(1234, cf2.formfield().max_length)
#
# @override_settings(ROOT_URLCONF='myapp.urls')
# class JsonResponseTests(SimpleTestCase):
#
#     def test_json_response(self):
#         response = self.client.get('/json/response/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             response['content-type'], 'application/json')
#         self.assertEqual(json.loads(response.content.decode()), {
#             'a': [1, 2, 3],
#             'foo': {'bar': 'baz'},
#             'timestamp': '2019-04-07T20:00:00',
#             'value': '3.14',
#         })
#
