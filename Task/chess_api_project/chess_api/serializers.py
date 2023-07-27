from rest_framework import serializers

class ChessPiecePositionSerializer(serializers.Serializer):
    positions = serializers.DictField(child=serializers.CharField())
