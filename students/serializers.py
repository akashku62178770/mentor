from rest_framework import serializers
from .models import *
from rest_framework.authtoken.views import Token
from django.contrib.auth.models import User

# 1
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# 2
class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = [
            # "get_user",
            "usn",
            "image",
            "fatherName",
            "fatherOccupation",
            "fatherPhone",
            "motherName",
            "motherOccupation",
            "motherPhone",
            "motherMail",
            "currentAddress",
            "permanentAddress",
            "hobby",
            "interest",
            "ambition",
            "health",
        ]
        def get_user(self, value):
            request = self.context.get('request')
            user = request.user
            print(user)
            return user


# 3
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"


# 4
class ParentInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentInteraction
        fields = "__all__"


# 5
class MentorGeneralRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorGeneralRemark
        fields = "__all__"


# # 6
# class StudentAcademicPerformanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentAcademicPerformance
#         fields = "__all__"


# 7
class StudentInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInteraction
        fields = "__all__"
