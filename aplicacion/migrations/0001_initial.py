# Generated by Django 2.2.12 on 2020-07-06 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreColaborador', models.CharField(max_length=40, verbose_name='Colaborador')),
                ('link', models.URLField(max_length=500, null=True)),
                ('logo', models.ImageField(null=True, upload_to='Colaborador/')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEntidad', models.CharField(max_length=40, null=True, verbose_name='Entidad')),
                ('link', models.URLField(max_length=500, null=True)),
                ('logo', models.ImageField(null=True, upload_to='Entidades/')),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Impacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Impacto Social')),
                ('texto', models.CharField(max_length=150, verbose_name='Descripción')),
                ('dato', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Impacto_Social',
                'verbose_name_plural': 'Impacto_Social',
            },
        ),
        migrations.CreateModel(
            name='Nosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('description', models.TextField(max_length=250, verbose_name='Descripción')),
                ('video', models.FileField(blank=True, upload_to='', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProyecto', models.CharField(max_length=40, null=True, verbose_name='Nombre del Proyecto')),
                ('año', models.DateTimeField(auto_now_add=True, verbose_name='Año del Proyecto')),
                ('descripcion', models.CharField(max_length=300, null=True, verbose_name='Descripción')),
                ('logros', models.CharField(max_length=300, null=True, verbose_name='Logros')),
                ('imagen', models.ImageField(upload_to='imagesProyecto/', verbose_name='Imagen General')),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='Video')),
                ('entidades', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Entidad', verbose_name='Entidades Vinculado')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['año'],
            },
        ),
        migrations.CreateModel(
            name='ProyectoAnual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, null=True, verbose_name='Título del Proyecto del Año')),
                ('año', models.DateTimeField(auto_now_add=True, verbose_name='Año del Proyecto Anual')),
                ('descripcion', models.CharField(max_length=300, null=True, verbose_name='Descripción')),
                ('videofile', models.FileField(blank=True, upload_to='videoProyectoAnual/', verbose_name='Video del Proyecto Anual')),
                ('status', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'Proyecto_Anual',
                'verbose_name_plural': 'Proyectos_Anuales',
                'ordering': ['año'],
            },
        ),
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('texto', models.CharField(max_length=300, verbose_name='Testimonio')),
                ('foto', models.ImageField(upload_to='fotoTestimonio/', verbose_name='Foto')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('entidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Entidad', verbose_name='Entidad Vinculada')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Proyecto', verbose_name='Proyecto Vinculado')),
            ],
            options={
                'verbose_name': 'Testimonio',
                'verbose_name_plural': 'Testimonios',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRecurso', models.CharField(max_length=40, verbose_name='Nombre de la Transferencia')),
                ('archivo', models.FileField(null=True, upload_to='transferencias/')),
                ('link', models.URLField(blank=True, null=True)),
                ('imagen', models.ImageField(default='descarga.jpg', upload_to='recursos/')),
                ('status', models.BooleanField(default=True, verbose_name='Si activa esta opción será público')),
                ('entidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Entidad', verbose_name='Entidad vinculada')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AddField(
            model_name='proyecto',
            name='proyectoAnual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.ProyectoAnual', verbose_name='Proyecto Anual Vinculado'),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('link', models.URLField(blank=True, max_length=500)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='TÍtulo de la Noticia')),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción de la Noticia')),
                ('imagen', models.ImageField(default='noticia.jpg', upload_to='noticia/', verbose_name='Imagen')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Contenido de la Noticia')),
                ('destacados', models.BooleanField(default=False)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Imagen_Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloProyecto', models.CharField(blank=True, max_length=400, null=True)),
                ('images', models.FileField(upload_to='imagesProyecto/')),
                ('imagenes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Proyecto', verbose_name='Imagenes Extras')),
            ],
            options={
                'verbose_name': 'Imagen_Proyecto',
                'verbose_name_plural': 'Imagenes_Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Imagen_Nosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=400, null=True)),
                ('images', models.FileField(upload_to='images/')),
                ('imagenes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Nosotros')),
            ],
            options={
                'verbose_name': 'Imagen_Nosotros',
                'verbose_name_plural': 'Imagenes_Nosotros',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProyecto',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombreProyecto', models.CharField(max_length=40, null=True, verbose_name='Nombre del Proyecto')),
                ('año', models.DateTimeField(blank=True, editable=False, verbose_name='Año del Proyecto')),
                ('descripcion', models.CharField(max_length=300, null=True, verbose_name='Descripción')),
                ('logros', models.CharField(max_length=300, null=True, verbose_name='Logros')),
                ('imagen', models.TextField(max_length=100, verbose_name='Imagen General')),
                ('videofile', models.TextField(max_length=100, null=True, verbose_name='Video')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('entidades', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='aplicacion.Entidad', verbose_name='Entidades Vinculado')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('proyectoAnual', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='aplicacion.ProyectoAnual', verbose_name='Proyecto Anual Vinculado')),
            ],
            options={
                'verbose_name': 'historical Proyecto',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
