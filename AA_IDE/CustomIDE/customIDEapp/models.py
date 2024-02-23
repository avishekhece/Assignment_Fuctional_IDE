from django.db import models
import json
from django.core.exceptions import ValidationError

# class PythonDataField(models.TextField):
#     description = "A field that stores Python data types as JSON strings"
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def from_db_value(self, value, expression, connection):
#         if value is None:
#             return value
#         return json.loads(value)
#
#     def to_python(self, value):
#         if isinstance(value, list) or isinstance(value, dict):
#             return value
#         if value is None:
#             return value
#         return json.loads(value)
#
#     def get_prep_value(self, value):
#         if value is None:
#             return value
#         return json.dumps(value)

# class PythonDataField(models.TextField):
#     description = "A field that stores Python data types as JSON strings"
#
#     def from_db_value(self, value, expression, connection):
#         """Converts the value retrieved from the database to a Python object."""
#         if value is None:
#             return value
#         return json.loads(value)
#
#     def to_python(self, value):
#         """Converts the value received from forms or serialization to a Python object."""
#         if isinstance(value, list) or isinstance(value, dict):
#             return value
#         if value is None:
#             return value
#         return json.loads(value)
#
#     def get_prep_value(self, value):
#         """Converts the Python object to a JSON string for storage in the database."""
#         if value is None:
#             return value
#         return json.dumps(value)
#

class PythonDataField(models.TextField):
    description = "A field that stores Python data types as JSON strings"

    def from_db_value(self, value, expression, connection):
        """Converts the value retrieved from the database to a Python object."""
        if value is None:
            return value
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise ValidationError("Invalid JSON data in the database.")

    def to_python(self, value):
        """Converts the value received from forms or serialization to a Python object."""
        if isinstance(value, list) or isinstance(value, dict):
            return value
        if value is None:
            return value
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise ValidationError("Invalid JSON data received.")

    def get_prep_value(self, value):
        """Converts the Python object to a JSON string for storage in the database."""
        if value is None:
            return value
        return json.dumps(value)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # accepted_input_type = PythonDataField()
    # accepted_output_type = PythonDataField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Execution(models.Model):
    objects = None
    DoesNotExist = None
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='executions')
    code = models.TextField()
    response_message = models.TextField()
    output_value = models.TextField(null=True, blank=True)
    success_status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class TestCase(models.Model):
    DoesNotExist = None
    objects = None
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    input_data = models.TextField()
    expected_output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    executions = models.ManyToManyField(Execution, related_name='test_cases')
