# Generated by Django 4.2.14 on 2024-08-14 11:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "real_estate_app_customuser_type",
                    models.CharField(
                        choices=[
                            ("individual", "Individual"),
                            ("agent", "Agent"),
                            ("developer", "Developer"),
                        ],
                        default="individual",
                        max_length=20,
                    ),
                ),
                (
                    "real_estate_app_customuser_phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "real_estate_app_customuser_agree_terms",
                    models.BooleanField(default=False),
                ),
                (
                    "real_estate_app_client_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "real_estate_app_client_email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "real_estate_app_category_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "real_estate_app_category_name",
                    models.CharField(max_length=100, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "real_estate_app_property_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_property_title", models.CharField(max_length=100)),
                (
                    "real_estate_app_property_description",
                    models.TextField(default="No description provided"),
                ),
                (
                    "real_estate_app_property_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("real_estate_app_property_location", models.CharField(max_length=100)),
                (
                    "real_estate_app_property_street",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "real_estate_app_property_city",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "real_estate_app_property_additional_details",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "real_estate_app_property_thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
                ),
                (
                    "real_estate_app_property_agent",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="properties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "real_estate_app_property_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="real_estate_app.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "real_estate_app_report_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_report_name", models.CharField(max_length=255)),
                ("real_estate_app_report_content", models.TextField()),
                (
                    "real_estate_app_report_created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "real_estate_app_userprofile_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "real_estate_app_userprofile_user_type",
                    models.CharField(
                        choices=[
                            ("individual", "Individual"),
                            ("agent", "Agent"),
                            ("developer", "Developer"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "real_estate_app_userprofile_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "real_estate_app_userprofile_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "real_estate_app_userprofile_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "real_estate_app_transaction_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_transaction_date", models.DateField()),
                (
                    "real_estate_app_transaction_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "real_estate_app_transaction_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "real_estate_app_transaction_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="real_estate_app.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "real_estate_app_review_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_review_text", models.TextField()),
                ("real_estate_app_review_date", models.DateField()),
                (
                    "real_estate_app_review_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "real_estate_app_review_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="real_estate_app.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyImage",
            fields=[
                (
                    "real_estate_app_propertyimage_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "real_estate_app_propertyimage_image",
                    models.ImageField(upload_to="property_images/"),
                ),
                (
                    "real_estate_app_propertyimage_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="real_estate_app.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "real_estate_app_message_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_message_subject", models.CharField(max_length=255)),
                ("real_estate_app_message_body", models.TextField()),
                (
                    "real_estate_app_message_sent_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                ("real_estate_app_message_read", models.BooleanField(default=False)),
                (
                    "real_estate_app_message_receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "real_estate_app_message_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inquiry",
            fields=[
                (
                    "real_estate_app_inquiry_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("real_estate_app_inquiry_date", models.DateField()),
                (
                    "real_estate_app_inquiry_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "real_estate_app_inquiry_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="real_estate_app.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "real_estate_app_favorite_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "real_estate_app_favorite_created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "real_estate_app_favorite_property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorites",
                        to="real_estate_app.property",
                    ),
                ),
                (
                    "real_estate_app_favorite_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorites",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
