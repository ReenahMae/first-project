from django.shortcuts import render
def home(request):
    result  = None;

    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "addition":
                result = int(num1 + num2)
            elif operation == "subtraction":
                result = int(num1 - num2)
            elif operation == "multiplication":
                result = int(num1 * num2)
            elif operation == "division":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Invalid! Cannot divide by zero."
        except ValueError:
            result = "Invalid input"
    return render(request, "firstapp/home.html", {"result": result})