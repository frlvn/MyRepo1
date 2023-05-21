from django.shortcuts import render

def main(request):
    y = ''
    if request.method == 'POST':
        text = request.POST.get('text')

        # Преобразуем весь текст в нижний регистр для сравнения слов
        text_lower = text.lower()

        # Разбиваем текст на отдельные слова
        words = text_lower.split()

        # Используем множество для хранения уникальных слов
        unique_words = set(words)

        for i in unique_words:
            y = y + i + ' '

    #text = "This is a sample text. It contains multiple words, some of which are repeated multiple times. Some words may appear in different cases like uppercase and lowercase, but we need to count them as the same word."

    return render(request, 'main/main.html', {'y': y})
