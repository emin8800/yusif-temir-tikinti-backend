from rest_framework import serializers
from .models import Work

class WorkSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = "__all__"

    def get_file(self, obj):
        request = self.context.get('request')

        if obj.file:
            # Render / production safe variant
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url

        return None
