from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ClientRegister_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=3000)),
                ('gender', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Email_Type_Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMail_Message', models.CharField(max_length=30000)),
                ('Prediction', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_accuracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_ratio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
    ]
