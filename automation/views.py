from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'automation/dashboard.html')
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt  # temporarily disables CSRF token (safe since no login yet)
def summarize_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')

            # Simple mock "AI" summarization
            sentences = text.split('.')
            summary = '. '.join(sentences[:2]) + '.' if len(sentences) > 2 else text

            return JsonResponse({'summary': summary})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'POST request required'})

import pandas as pd
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        file_path = default_storage.save('temp.csv', csv_file)
        df = pd.read_csv(file_path)

        # simple analysis
        summary = {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
        }

        # if numeric columns exist, include their averages
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            summary["averages"] = df[numeric_cols].mean().to_dict()

        return JsonResponse(summary)
    return JsonResponse({'error': 'Please upload a CSV file using POST.'})


@csrf_exempt
def draft_email(request):
    """
    Receives raw notes and returns a mock 'AI-written' email.
    """
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        notes = data.get("notes", "")

        if not notes.strip():
            return JsonResponse({"error": "Empty notes."})

        # ----- mock AI logic -----
        subject = "Regarding Your Recent Request"
        body = (
            f"Hi there,\n\n"
            f"I hope you're doing well. {notes.capitalize()}.\n\n"
            f"Please let me know if you have any questions.\n\n"
            f"Best regards,\nAutoFlow Assistant"
        )

        return JsonResponse({"subject": subject, "body": body})
    return JsonResponse({"error": "POST only."})
