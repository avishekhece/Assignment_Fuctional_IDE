from builtins import print
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import TestCase
from .utility import compile_python_code


def index(request):
    return render(request, 'index.html')


class CodeExecutor(CreateAPIView):

    def post(self, request, *args, **kwargs):
        execution_obj = None
        # test_cases_ids = None
        # test_cases_ids = request.data.get('test_cases', None)
        code_string = request.data.get('code', None)
        test_case_ids_queryset = TestCase.objects.values_list('id', flat=True)
        test_case_ids = list(test_case_ids_queryset)
        test_cases_objs = TestCase.objects.filter(id__in=test_case_ids)
        passed = True
        # import pdb;pdb.set_trace()
        for i in test_cases_objs:

            i.executions.add(execution_obj)
            # print(code_string)
            # print(i.input_data)
            compile_resp = compile_python_code(code_string, i.input_data)
            expected_output = i.expected_output
            print("code_string: " + str(code_string))
            # test_cases_ids = request.data.get('test_cases', None)

            # test_cases_objs = TestCase.objects.filter(id__in=test_cases_ids)
            # print("test_cases_objs==" + test_cases_objs)
            passed = True
            # for i in test_cases_objs:
            #     i.executions.add(execution_obj)
            compilation_success = compile_resp[1]
            if compilation_success:
                output = compile_resp[0]
                message = 'Executed successfully : OutPut :' + str(output)
                if expected_output != compile_resp[0]:
                    passed = False
                    break
            else:
                output = None
                message = compile_resp[0]
                passed = False
        execution = Execution(code=code_string,
                              response_message=message, output_value=output, success_status=passed)
        execution.save()
        print({'passed': passed, 'message': message})
        return Response({'passed': passed, 'message': message})


class ExecutionList(APIView):
    def get(self, request):
        executions = Execution.objects.all()
        serializer = ExecutionSerializer(executions, many=True)
        return Response(serializer.data)


from rest_framework import serializers
from .models import Execution


class ExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execution
        fields = '__all__'
