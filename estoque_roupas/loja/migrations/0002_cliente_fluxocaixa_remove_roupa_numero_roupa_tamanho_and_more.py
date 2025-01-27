# Generated by Django 5.1.1 on 2025-01-22 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('total_entrada', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_saida', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='roupa',
            name='numero',
        ),
        migrations.AddField(
            model_name='roupa',
            name='tamanho',
            field=models.CharField(default='P', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_pagamento', models.DateField(auto_now_add=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.cliente')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.roupa')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='loja.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_pago', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('numero_parcelas', models.PositiveIntegerField(default=0)),
                ('parcelas_pagas', models.PositiveIntegerField(default=0)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.cliente')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loja.pedido')),
            ],
        ),
    ]
