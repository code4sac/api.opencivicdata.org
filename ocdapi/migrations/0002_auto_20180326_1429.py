# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-26 14:29
from __future__ import unicode_literals
import re

from django.db import migrations
from django.db import connection, transaction

from opencivicdata.legislative.models import Bill

class Migration(migrations.Migration):
    def unmangle_identifier(apps, schema_editor):
        '''
        The `fix_bill_id` function mangled nearly all Chicago bill identifiers by adding a space, e.g., 'R2010-1185' (original) vs. 'R 2010-1185' (mangled).

        This migration unmangles identifiers. 
        '''

        print('Running CHICAGO MIGRATION')

        added_space = r'^([A-Za-z]+)\s([-\d]+)$'

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute("""
                DECLARE bills_cursor CURSOR FOR
                SELECT identifier FROM opencivicdata_bill as bill
                INNER JOIN opencivicdata_organization as organization
                ON bill.from_organization_id=organization.id 
                WHERE organization.jurisdiction_id='ocd-jurisdiction/country:us/state:il/place:chicago/government' 
                AND bill.identifier ~* '(^([A-Za-z]+)\s([-\d]+)$)'
            """)

            while True:
                cursor.execute("FETCH 1000 FROM bills_cursor")
                bill_chunk = cursor.fetchall()

                if not bill_chunk:
                    break
                else: 
                    for bill in bill_chunk:
                        identifier = bill[0]
                        match = re.match(added_space, identifier)
                        unmangled_identifier = '{mangled_prefix}{count}'.format(mangled_prefix=match.group(1), 
                                                                                count=match.group(2))

                        print('{} becomes {}'.format(identifier, unmangled_identifier))
                        try:
                            duplicate = Bill.objects.get(identifier=unmangled_identifier)
                            print('{} - duplicate found. Deleting.'.format(unmangled_identifier))
                            duplicate.delete()
                        except Bill.DoesNotExist: 
                            pass

                        Bill.objects.filter(identifier=identifier).update(identifier=unmangled_identifier)

    dependencies = [
        ('ocdapi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(unmangle_identifier)
    ]