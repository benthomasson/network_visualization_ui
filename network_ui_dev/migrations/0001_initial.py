# Generated by Django 2.0.8 on 2018-08-23 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CodeUnderTest',
            fields=[
                ('code_under_test_id', models.AutoField(primary_key=True, serialize=False)),
                ('version_x', models.IntegerField()),
                ('version_y', models.IntegerField()),
                ('version_z', models.IntegerField()),
                ('commits_since', models.IntegerField()),
                ('commit_hash', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('coverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('coverage_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('id', models.IntegerField()),
                ('device_type', models.CharField(blank=True, max_length=200)),
                ('interface_id_seq', models.IntegerField(default=0)),
                ('process_id_seq', models.IntegerField(default=0)),
                ('host_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventTrace',
            fields=[
                ('event_trace_id', models.AutoField(primary_key=True, serialize=False)),
                ('trace_session_id', models.IntegerField(default=0)),
                ('event_data', models.TextField()),
                ('message_id', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FSMTrace',
            fields=[
                ('fsm_trace_id', models.AutoField(primary_key=True, serialize=False)),
                ('fsm_name', models.CharField(blank=True, max_length=200)),
                ('from_state', models.CharField(blank=True, max_length=200)),
                ('to_state', models.CharField(blank=True, max_length=200)),
                ('message_type', models.CharField(blank=True, max_length=200)),
                ('trace_session_id', models.IntegerField(default=0)),
                ('order', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('x1', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('x2', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('group_type', models.CharField(blank=True, max_length=200)),
                ('inventory_group_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GroupDevice',
            fields=[
                ('group_device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Device')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('interface_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('id', models.IntegerField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('link_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('from_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_link', to='network_ui_dev.Device')),
                ('from_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_link', to='network_ui_dev.Interface')),
                ('to_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_link', to='network_ui_dev.Device')),
                ('to_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_link', to='network_ui_dev.Interface')),
            ],
        ),
        migrations.CreateModel(
            name='MessageType',
            fields=[
                ('message_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('process_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('process_type', models.CharField(blank=True, max_length=200)),
                ('id', models.IntegerField(default=0)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('stream_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=200)),
                ('id', models.IntegerField(default=0)),
                ('from_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_stream', to='network_ui_dev.Device')),
                ('to_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_stream', to='network_ui_dev.Device')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('test_case_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('test_case_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('test_result_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('id', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Client')),
                ('code_under_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.CodeUnderTest')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Result')),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.TestCase')),
            ],
        ),
        migrations.CreateModel(
            name='Toolbox',
            fields=[
                ('toolbox_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ToolboxItem',
            fields=[
                ('toolbox_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField()),
                ('toolbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Toolbox')),
            ],
        ),
        migrations.CreateModel(
            name='Topology',
            fields=[
                ('topology_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('scale', models.FloatField()),
                ('panX', models.FloatField()),
                ('panY', models.FloatField()),
                ('device_id_seq', models.IntegerField(default=0)),
                ('link_id_seq', models.IntegerField(default=0)),
                ('group_id_seq', models.IntegerField(default=0)),
                ('stream_id_seq', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TopologyHistory',
            fields=[
                ('topology_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_id', models.IntegerField()),
                ('message_data', models.TextField()),
                ('undone', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Client')),
                ('message_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.MessageType')),
                ('topology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Topology')),
            ],
        ),
        migrations.CreateModel(
            name='TopologyInventory',
            fields=[
                ('topology_inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_id', models.IntegerField()),
                ('topology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Topology')),
            ],
        ),
        migrations.CreateModel(
            name='TopologySnapshot',
            fields=[
                ('topology_snapshot_id', models.AutoField(primary_key=True, serialize=False)),
                ('topology_id', models.IntegerField()),
                ('trace_session_id', models.IntegerField()),
                ('snapshot_data', models.TextField()),
                ('order', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Client')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='topology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Topology'),
        ),
        migrations.AddField(
            model_name='device',
            name='topology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.Topology'),
        ),
        migrations.AddField(
            model_name='coverage',
            name='test_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_ui_dev.TestResult'),
        ),
    ]