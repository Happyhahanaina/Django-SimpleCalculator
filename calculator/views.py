from django.http import HttpResponse
from django.shortcuts import render


def calculate(request):
    result = None  # default is None to distinguish no result yet
    error = None

    if request.method == 'POST':
        try:
            n1 = float(request.POST.get('num1'))
            n2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = n1 + n2
            elif operation == 'subtract':
                result = n1 - n2
            elif operation == 'multiply':
                result = n1 * n2
            elif operation == 'divide':
                if n2 != 0:
                    result = n1 / n2
                else:
                    error = "Error: Division by zero is not allowed."
            else:
                error = "Invalid operation selected."

        except (ValueError, TypeError):
            error = "Invalid input. Please enter valid numbers."
        except Exception as e:
            error = f"Unexpected error: {e}"

    context = {
        'result': result,
        'error': error
    }

    return render(request, "calculator.html", context)
