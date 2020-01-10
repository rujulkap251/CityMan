# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dartstations(models.Model):
    index = models.BigIntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    stationid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dartstations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Form(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    des = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form'


class Luastations(models.Model):
    index = models.BigIntegerField(primary_key=True)
    stopid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    lineid = models.TextField(blank=True, null=True)
    sortorder = models.TextField(blank=True, null=True)
    isenabled = models.TextField(blank=True, null=True)
    isparkandride = models.TextField(blank=True, null=True)
    iscycleandride = models.TextField(blank=True, null=True)
    zonecounta = models.TextField(blank=True, null=True)
    zonecountb = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)
    irishname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'luastations'


class Rtdart(models.Model):
    index = models.BigIntegerField(primary_key=True)
    station_mhide = models.TextField(db_column='station_MHIDE', blank=True, null=True)  # Field name made lowercase.
    station_pmnck = models.TextField(db_column='station_PMNCK', blank=True, null=True)  # Field name made lowercase.
    station_grgrd = models.TextField(db_column='station_GRGRD', blank=True, null=True)  # Field name made lowercase.
    station_suttn = models.TextField(db_column='station_SUTTN', blank=True, null=True)  # Field name made lowercase.
    station_bysde = models.TextField(db_column='station_BYSDE', blank=True, null=True)  # Field name made lowercase.
    station_hwthj = models.TextField(db_column='station_HWTHJ', blank=True, null=True)  # Field name made lowercase.
    station_howth = models.TextField(db_column='station_HOWTH', blank=True, null=True)  # Field name made lowercase.
    station_kbrck = models.TextField(db_column='station_KBRCK', blank=True, null=True)  # Field name made lowercase.
    station_rahny = models.TextField(db_column='station_RAHNY', blank=True, null=True)  # Field name made lowercase.
    station_htown = models.TextField(db_column='station_HTOWN', blank=True, null=True)  # Field name made lowercase.
    station_klstr = models.TextField(db_column='station_KLSTR', blank=True, null=True)  # Field name made lowercase.
    station_ctarf = models.TextField(db_column='station_CTARF', blank=True, null=True)  # Field name made lowercase.
    station_cnlly = models.TextField(db_column='station_CNLLY', blank=True, null=True)  # Field name made lowercase.
    station_tara_field = models.TextField(db_column='station_TARA ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    station_perse = models.TextField(db_column='station_PERSE', blank=True, null=True)  # Field name made lowercase.
    station_gcdk_field = models.TextField(db_column='station_GCDK ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    station_ldwne = models.TextField(db_column='station_LDWNE', blank=True, null=True)  # Field name made lowercase.
    station_smont = models.TextField(db_column='station_SMONT', blank=True, null=True)  # Field name made lowercase.
    station_sidny = models.TextField(db_column='station_SIDNY', blank=True, null=True)  # Field name made lowercase.
    station_btstn = models.TextField(db_column='station_BTSTN', blank=True, null=True)  # Field name made lowercase.
    station_brock = models.TextField(db_column='station_BROCK', blank=True, null=True)  # Field name made lowercase.
    station_seapt = models.TextField(db_column='station_SEAPT', blank=True, null=True)  # Field name made lowercase.
    station_shill = models.TextField(db_column='station_SHILL', blank=True, null=True)  # Field name made lowercase.
    station_dlery = models.TextField(db_column='station_DLERY', blank=True, null=True)  # Field name made lowercase.
    station_scove = models.TextField(db_column='station_SCOVE', blank=True, null=True)  # Field name made lowercase.
    station_glgry = models.TextField(db_column='station_GLGRY', blank=True, null=True)  # Field name made lowercase.
    station_dlkey = models.TextField(db_column='station_DLKEY', blank=True, null=True)  # Field name made lowercase.
    station_kilny = models.TextField(db_column='station_KILNY', blank=True, null=True)  # Field name made lowercase.
    station_skill = models.TextField(db_column='station_SKILL', blank=True, null=True)  # Field name made lowercase.
    station_bray_field = models.TextField(db_column='station_BRAY ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    station_gstns = models.TextField(db_column='station_GSTNS', blank=True, null=True)  # Field name made lowercase.
    station_kcool = models.TextField(db_column='station_KCOOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rtdart'


class Rtluas(models.Model):
    index = models.BigIntegerField(primary_key=True)
    station_tal = models.TextField(db_column='station_TAL', blank=True, null=True)  # Field name made lowercase.
    station_hos = models.TextField(db_column='station_HOS', blank=True, null=True)  # Field name made lowercase.
    station_coo = models.TextField(db_column='station_COO', blank=True, null=True)  # Field name made lowercase.
    station_bel = models.TextField(db_column='station_BEL', blank=True, null=True)  # Field name made lowercase.
    station_kin = models.TextField(db_column='station_KIN', blank=True, null=True)  # Field name made lowercase.
    station_red = models.TextField(db_column='station_RED', blank=True, null=True)  # Field name made lowercase.
    station_kyl = models.TextField(db_column='station_KYL', blank=True, null=True)  # Field name made lowercase.
    station_blu = models.TextField(db_column='station_BLU', blank=True, null=True)  # Field name made lowercase.
    station_bla = models.TextField(db_column='station_BLA', blank=True, null=True)  # Field name made lowercase.
    station_dri = models.TextField(db_column='station_DRI', blank=True, null=True)  # Field name made lowercase.
    station_gol = models.TextField(db_column='station_GOL', blank=True, null=True)  # Field name made lowercase.
    station_sui = models.TextField(db_column='station_SUI', blank=True, null=True)  # Field name made lowercase.
    station_ria = models.TextField(db_column='station_RIA', blank=True, null=True)  # Field name made lowercase.
    station_fat = models.TextField(db_column='station_FAT', blank=True, null=True)  # Field name made lowercase.
    station_jam = models.TextField(db_column='station_JAM', blank=True, null=True)  # Field name made lowercase.
    station_heu = models.TextField(db_column='station_HEU', blank=True, null=True)  # Field name made lowercase.
    station_mus = models.TextField(db_column='station_MUS', blank=True, null=True)  # Field name made lowercase.
    station_smi = models.TextField(db_column='station_SMI', blank=True, null=True)  # Field name made lowercase.
    station_fou = models.TextField(db_column='station_FOU', blank=True, null=True)  # Field name made lowercase.
    station_jer = models.TextField(db_column='station_JER', blank=True, null=True)  # Field name made lowercase.
    station_abb = models.TextField(db_column='station_ABB', blank=True, null=True)  # Field name made lowercase.
    station_bus = models.TextField(db_column='station_BUS', blank=True, null=True)  # Field name made lowercase.
    station_con = models.TextField(db_column='station_CON', blank=True, null=True)  # Field name made lowercase.
    station_sts = models.TextField(db_column='station_STS', blank=True, null=True)  # Field name made lowercase.
    station_har = models.TextField(db_column='station_HAR', blank=True, null=True)  # Field name made lowercase.
    station_cha = models.TextField(db_column='station_CHA', blank=True, null=True)  # Field name made lowercase.
    station_ran = models.TextField(db_column='station_RAN', blank=True, null=True)  # Field name made lowercase.
    station_bee = models.TextField(db_column='station_BEE', blank=True, null=True)  # Field name made lowercase.
    station_cow = models.TextField(db_column='station_COW', blank=True, null=True)  # Field name made lowercase.
    station_mil = models.TextField(db_column='station_MIL', blank=True, null=True)  # Field name made lowercase.
    station_win = models.TextField(db_column='station_WIN', blank=True, null=True)  # Field name made lowercase.
    station_dun = models.TextField(db_column='station_DUN', blank=True, null=True)  # Field name made lowercase.
    station_bal = models.TextField(db_column='station_BAL', blank=True, null=True)  # Field name made lowercase.
    station_kil = models.TextField(db_column='station_KIL', blank=True, null=True)  # Field name made lowercase.
    station_sti = models.TextField(db_column='station_STI', blank=True, null=True)  # Field name made lowercase.
    station_san = models.TextField(db_column='station_SAN', blank=True, null=True)  # Field name made lowercase.
    station_cpk = models.TextField(db_column='station_CPK', blank=True, null=True)  # Field name made lowercase.
    station_gle = models.TextField(db_column='station_GLE', blank=True, null=True)  # Field name made lowercase.
    station_gal = models.TextField(db_column='station_GAL', blank=True, null=True)  # Field name made lowercase.
    station_leo = models.TextField(db_column='station_LEO', blank=True, null=True)  # Field name made lowercase.
    station_baw = models.TextField(db_column='station_BAW', blank=True, null=True)  # Field name made lowercase.
    station_rcc = models.TextField(db_column='station_RCC', blank=True, null=True)  # Field name made lowercase.
    station_cck = models.TextField(db_column='station_CCK', blank=True, null=True)  # Field name made lowercase.
    station_bre = models.TextField(db_column='station_BRE', blank=True, null=True)  # Field name made lowercase.
    station_lau = models.TextField(db_column='station_LAU', blank=True, null=True)  # Field name made lowercase.
    station_che = models.TextField(db_column='station_CHE', blank=True, null=True)  # Field name made lowercase.
    station_bri = models.TextField(db_column='station_BRI', blank=True, null=True)  # Field name made lowercase.
    station_fet = models.TextField(db_column='station_FET', blank=True, null=True)  # Field name made lowercase.
    station_cvn = models.TextField(db_column='station_CVN', blank=True, null=True)  # Field name made lowercase.
    station_cit = models.TextField(db_column='station_CIT', blank=True, null=True)  # Field name made lowercase.
    station_for = models.TextField(db_column='station_FOR', blank=True, null=True)  # Field name made lowercase.
    station_sag = models.TextField(db_column='station_SAG', blank=True, null=True)  # Field name made lowercase.
    station_gdk = models.TextField(db_column='station_GDK', blank=True, null=True)  # Field name made lowercase.
    station_mys = models.TextField(db_column='station_MYS', blank=True, null=True)  # Field name made lowercase.
    station_sdk = models.TextField(db_column='station_SDK', blank=True, null=True)  # Field name made lowercase.
    station_tpt = models.TextField(db_column='station_TPT', blank=True, null=True)  # Field name made lowercase.
    station_dep = models.TextField(db_column='station_DEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rtluas'


class Rtstation(models.Model):
    station_no_10 = models.BigIntegerField(blank=True, null=True)
    station_no_100 = models.BigIntegerField(blank=True, null=True)
    station_no_101 = models.BigIntegerField(blank=True, null=True)
    station_no_102 = models.BigIntegerField(blank=True, null=True)
    station_no_103 = models.BigIntegerField(blank=True, null=True)
    station_no_104 = models.BigIntegerField(blank=True, null=True)
    station_no_105 = models.BigIntegerField(blank=True, null=True)
    station_no_106 = models.BigIntegerField(blank=True, null=True)
    station_no_107 = models.BigIntegerField(blank=True, null=True)
    station_no_108 = models.BigIntegerField(blank=True, null=True)
    station_no_109 = models.BigIntegerField(blank=True, null=True)
    station_no_11 = models.BigIntegerField(blank=True, null=True)
    station_no_110 = models.BigIntegerField(blank=True, null=True)
    station_no_111 = models.BigIntegerField(blank=True, null=True)
    station_no_112 = models.BigIntegerField(blank=True, null=True)
    station_no_113 = models.BigIntegerField(blank=True, null=True)
    station_no_114 = models.BigIntegerField(blank=True, null=True)
    station_no_115 = models.BigIntegerField(blank=True, null=True)
    station_no_12 = models.BigIntegerField(blank=True, null=True)
    station_no_13 = models.BigIntegerField(blank=True, null=True)
    station_no_14 = models.BigIntegerField(blank=True, null=True)
    station_no_15 = models.BigIntegerField(blank=True, null=True)
    station_no_16 = models.BigIntegerField(blank=True, null=True)
    station_no_17 = models.BigIntegerField(blank=True, null=True)
    station_no_18 = models.BigIntegerField(blank=True, null=True)
    station_no_19 = models.BigIntegerField(blank=True, null=True)
    station_no_2 = models.BigIntegerField(blank=True, null=True)
    station_no_21 = models.BigIntegerField(blank=True, null=True)
    station_no_22 = models.BigIntegerField(blank=True, null=True)
    station_no_23 = models.BigIntegerField(blank=True, null=True)
    station_no_24 = models.BigIntegerField(blank=True, null=True)
    station_no_25 = models.BigIntegerField(blank=True, null=True)
    station_no_26 = models.BigIntegerField(blank=True, null=True)
    station_no_27 = models.BigIntegerField(blank=True, null=True)
    station_no_28 = models.BigIntegerField(blank=True, null=True)
    station_no_29 = models.BigIntegerField(blank=True, null=True)
    station_no_3 = models.BigIntegerField(blank=True, null=True)
    station_no_30 = models.BigIntegerField(blank=True, null=True)
    station_no_31 = models.BigIntegerField(blank=True, null=True)
    station_no_32 = models.BigIntegerField(blank=True, null=True)
    station_no_33 = models.BigIntegerField(blank=True, null=True)
    station_no_34 = models.BigIntegerField(blank=True, null=True)
    station_no_35 = models.BigIntegerField(blank=True, null=True)
    station_no_36 = models.BigIntegerField(blank=True, null=True)
    station_no_37 = models.BigIntegerField(blank=True, null=True)
    station_no_38 = models.BigIntegerField(blank=True, null=True)
    station_no_39 = models.BigIntegerField(blank=True, null=True)
    station_no_4 = models.BigIntegerField(blank=True, null=True)
    station_no_40 = models.BigIntegerField(blank=True, null=True)
    station_no_41 = models.BigIntegerField(blank=True, null=True)
    station_no_42 = models.BigIntegerField(blank=True, null=True)
    station_no_43 = models.BigIntegerField(blank=True, null=True)
    station_no_44 = models.BigIntegerField(blank=True, null=True)
    station_no_45 = models.BigIntegerField(blank=True, null=True)
    station_no_46 = models.BigIntegerField(blank=True, null=True)
    station_no_47 = models.BigIntegerField(blank=True, null=True)
    station_no_48 = models.BigIntegerField(blank=True, null=True)
    station_no_49 = models.BigIntegerField(blank=True, null=True)
    station_no_5 = models.BigIntegerField(blank=True, null=True)
    station_no_50 = models.BigIntegerField(blank=True, null=True)
    station_no_51 = models.BigIntegerField(blank=True, null=True)
    station_no_52 = models.BigIntegerField(blank=True, null=True)
    station_no_53 = models.BigIntegerField(blank=True, null=True)
    station_no_54 = models.BigIntegerField(blank=True, null=True)
    station_no_55 = models.BigIntegerField(blank=True, null=True)
    station_no_56 = models.BigIntegerField(blank=True, null=True)
    station_no_57 = models.BigIntegerField(blank=True, null=True)
    station_no_58 = models.BigIntegerField(blank=True, null=True)
    station_no_59 = models.BigIntegerField(blank=True, null=True)
    station_no_6 = models.BigIntegerField(blank=True, null=True)
    station_no_60 = models.BigIntegerField(blank=True, null=True)
    station_no_61 = models.BigIntegerField(blank=True, null=True)
    station_no_62 = models.BigIntegerField(blank=True, null=True)
    station_no_63 = models.BigIntegerField(blank=True, null=True)
    station_no_64 = models.BigIntegerField(blank=True, null=True)
    station_no_65 = models.BigIntegerField(blank=True, null=True)
    station_no_66 = models.BigIntegerField(blank=True, null=True)
    station_no_67 = models.BigIntegerField(blank=True, null=True)
    station_no_68 = models.BigIntegerField(blank=True, null=True)
    station_no_69 = models.BigIntegerField(blank=True, null=True)
    station_no_7 = models.BigIntegerField(blank=True, null=True)
    station_no_70 = models.BigIntegerField(blank=True, null=True)
    station_no_71 = models.BigIntegerField(blank=True, null=True)
    station_no_72 = models.BigIntegerField(blank=True, null=True)
    station_no_73 = models.BigIntegerField(blank=True, null=True)
    station_no_74 = models.BigIntegerField(blank=True, null=True)
    station_no_75 = models.BigIntegerField(blank=True, null=True)
    station_no_76 = models.BigIntegerField(blank=True, null=True)
    station_no_77 = models.BigIntegerField(blank=True, null=True)
    station_no_78 = models.BigIntegerField(blank=True, null=True)
    station_no_79 = models.BigIntegerField(blank=True, null=True)
    station_no_8 = models.BigIntegerField(blank=True, null=True)
    station_no_80 = models.BigIntegerField(blank=True, null=True)
    station_no_81 = models.BigIntegerField(blank=True, null=True)
    station_no_82 = models.BigIntegerField(blank=True, null=True)
    station_no_83 = models.BigIntegerField(blank=True, null=True)
    station_no_84 = models.BigIntegerField(blank=True, null=True)
    station_no_85 = models.BigIntegerField(blank=True, null=True)
    station_no_86 = models.BigIntegerField(blank=True, null=True)
    station_no_87 = models.BigIntegerField(blank=True, null=True)
    station_no_88 = models.BigIntegerField(blank=True, null=True)
    station_no_89 = models.BigIntegerField(blank=True, null=True)
    station_no_9 = models.BigIntegerField(blank=True, null=True)
    station_no_90 = models.BigIntegerField(blank=True, null=True)
    station_no_91 = models.BigIntegerField(blank=True, null=True)
    station_no_92 = models.BigIntegerField(blank=True, null=True)
    station_no_93 = models.BigIntegerField(blank=True, null=True)
    station_no_94 = models.BigIntegerField(blank=True, null=True)
    station_no_95 = models.BigIntegerField(blank=True, null=True)
    station_no_96 = models.BigIntegerField(blank=True, null=True)
    station_no_97 = models.BigIntegerField(blank=True, null=True)
    station_no_98 = models.BigIntegerField(blank=True, null=True)
    station_no_99 = models.BigIntegerField(blank=True, null=True)
    index = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rtstation'


class Rtweather(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    main = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pressure = models.BigIntegerField(blank=True, null=True)
    humidity = models.BigIntegerField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    rain = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtweather'


class Station(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    banking = models.BooleanField(blank=True, null=True)
    bike_stands = models.BigIntegerField(blank=True, null=True)
    bonus = models.BooleanField(blank=True, null=True)
    contract_name = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    number = models.BigIntegerField(primary_key=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class UserProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'user_profile'
