# Generated by Django 4.1 on 2023-04-14 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(default=15)),
                ('exam_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ConstValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('english_title', models.CharField(max_length=255)),
                ('theory_units', models.PositiveSmallIntegerField(default=0)),
                ('practical_units', models.PositiveSmallIntegerField(default=0)),
                ('course_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Course_course_type', to='amuzeshyar.constvalue')),
                ('degree_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Course_degree_level', to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.building')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.department')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('english_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('national_id', models.CharField(db_column='national_id', db_index=True, max_length=10, primary_key=True, serialize=False)),
                ('father_name', models.CharField(max_length=50)),
                ('gender', models.BooleanField(default=0)),
                ('birth_date', models.DateField()),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_member', models.BooleanField(default=False)),
                ('research_area', models.CharField(max_length=255)),
                ('academic_rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Professor_academic_rank', to='amuzeshyar.constvalue')),
                ('contract_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Professor_contract_type', to='amuzeshyar.constvalue')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.department')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.person')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_start_date', models.DateField()),
                ('registration_end_date', models.DateField()),
                ('classes_start_date', models.DateField()),
                ('classes_end_date', models.DateField()),
                ('registration_modification_start_date', models.DateField(blank=True, null=True)),
                ('registration_modification_end_date', models.DateField(blank=True, null=True)),
                ('exams_start_date', models.DateField()),
                ('exams_end_date', models.DateField()),
                ('year', models.PositiveSmallIntegerField()),
                ('semester_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('entry_date', models.DateField()),
                ('student_id', models.CharField(db_column='student_id', db_index=True, max_length=10, primary_key=True, serialize=False)),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('entry_semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
                ('field_of_study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.major')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.person')),
                ('registration_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('creation_date', models.DateField()),
                ('is_payed', models.BooleanField(default=False)),
                ('indebtedness', models.IntegerField()),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('payment_gateway', models.CharField(max_length=50)),
                ('reference_code', models.CharField(blank=True, max_length=255, null=True)),
                ('is_succeeded', models.BooleanField(default=True)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.studentinvoice')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='amuzeshyar.semester')),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('after_appeal_grade', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.class')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.student')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('english_title', models.CharField(max_length=50)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.major')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterCourseTuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuition_per_unit', models.IntegerField()),
                ('course_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SemesterCourseTuition_course_type', to='amuzeshyar.constvalue')),
                ('field_of_study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.major')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
                ('unit_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SemesterCourseTuition_unit_type', to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('code', models.CharField(db_column='code', max_length=10, primary_key=True, serialize=False)),
                ('floor', models.SmallIntegerField()),
                ('block', models.CharField(blank=True, max_length=1, null=True)),
                ('title', models.CharField(max_length=50)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.building')),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorEvaluationParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('evaluation_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.PositiveSmallIntegerField(default=5)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.professor')),
                ('parameter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.professorevaluationparameter')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.class')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.student')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.person')),
                ('phone_number_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='MajorSpecializationDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.department')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='GradeAppeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeal_description', models.CharField(max_length=1000)),
                ('reply_description', models.CharField(max_length=1000)),
                ('submission_datetime', models.DateTimeField(auto_now=True)),
                ('reply_datetime', models.DateTimeField(blank=True, null=True)),
                ('class_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.studentclass')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
            ],
        ),
        migrations.CreateModel(
            name='FixedTuitionFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('field_of_study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.major')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.person')),
            ],
        ),
        migrations.CreateModel(
            name='CoursePrerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_prerequisite', models.BooleanField(default=False)),
                ('is_concurrent', models.BooleanField(default=False)),
                ('c1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CoursePrerequisite_c1', to='amuzeshyar.course')),
                ('c2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CoursePrerequisite_c2', to='amuzeshyar.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.specialization'),
        ),
        migrations.AddField(
            model_name='course',
            name='units_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Course_units_type', to='amuzeshyar.constvalue'),
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.PositiveSmallIntegerField()),
                ('start_at', models.TimeField()),
                ('end_at', models.TimeField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.room')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.class')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_number', models.PositiveSmallIntegerField()),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.class')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.student')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.course'),
        ),
        migrations.AddField(
            model_name='class',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.professor'),
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester'),
        ),
        migrations.AddField(
            model_name='building',
            name='building_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue'),
        ),
        migrations.CreateModel(
            name='AnnouncementText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.person')),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('expiration_datetime', models.DateTimeField(blank=True, null=True)),
                ('announcement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.announcementtext')),
                ('specific_degree_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.constvalue')),
                ('specific_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.department')),
                ('specific_entry_semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.semester')),
                ('specific_major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.major')),
                ('specific_specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.specialization')),
                ('specific_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amuzeshyar.student')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('is_default', models.BooleanField(default=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amuzeshyar.person')),
            ],
        ),
    ]
