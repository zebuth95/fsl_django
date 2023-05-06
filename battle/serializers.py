from rest_framework import serializers

from battle.models import Battle
from battle.utils import fight
from monster.models import Monster

from monster.nested_serializers import MonsterListRetrieveUpdateSerializer


class BattleListSerializer(serializers.ModelSerializer):
    monsterA = serializers.SerializerMethodField("get_monsterA")
    monsterB = serializers.SerializerMethodField("get_monsterB")
    winner = serializers.SerializerMethodField("get_winner")

    def get_monsterA(self, obj):
        return MonsterListRetrieveUpdateSerializer(Monster.objects.get(pk=obj.monsterA), many=False).data

    def get_monsterB(self, obj):
        return MonsterListRetrieveUpdateSerializer(Monster.objects.get(pk=obj.monsterB), many=False).data

    def get_winner(self, obj):
        return MonsterListRetrieveUpdateSerializer(Monster.objects.get(pk=obj.winner), many=False).data

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Battle
        extra_kwargs = {
            "winner": {"read_only": True}
        }
        fields = "__all__"

    def validate_monsterA(self, value):
        try:
            return Monster.objects.get(pk=value)
        except Monster.DoesNotExist:
            raise serializers.ValidationError(f"Object id={value} do not exists")

    def validate_monsterB(self, value):
        try:
            return Monster.objects.get(pk=value)
        except Monster.DoesNotExist:
            raise serializers.ValidationError(f"Object id={value} do not exists")

    def validate(self, attrs):
        attrs["winner"] = fight(attrs.get("monsterA"), attrs.get("monsterB")).id
        attrs["monsterA"] = attrs.get("monsterA").id
        attrs["monsterB"] = attrs.get("monsterB").id
        return attrs

