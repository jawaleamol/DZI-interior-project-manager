from rest_framework import serializers

from .models import Bill, BillItem


class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = [
            'id',
            'bill',
            'description',
            'quantity',
            'unit_price',
            'total_price',
        ]


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = [
            'id',
            'project',
            'agency',
            'bill_number',
            'status',
            'total_amount',
            'gst_amount',
            'submitted_at',
            'items',
        ]
