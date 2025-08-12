from datacenter.models import Schoolkid


def get_schoolkid_by_name(schoolkid_name):
    """Находит ученика по имени или части имени.
    Returns:
        - объект ученика, если найден ровно один
        - None, если не найден или найдено несколько
    При этом выводит соответствующие сообщения
    """
    students = Schoolkid.objects.filter(full_name__icontains=schoolkid_name)
    
    if not students.exists():
        print(f"Учеников с именем '{schoolkid_name}' не найдено")
        print("   Проверьте правильность ввода имени")
        return None
        
    if students.count() > 1:
        print(f"Найдено {students.count()} учеников с именем содержащим '{schoolkid_name}':")
        print("----------------------------------------")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.full_name} (класс {student.year_of_study}{student.group_letter})")
        print("Пожалуйста, уточните полное имя ученика из списка выше")
        return None
        
    return students.first()
