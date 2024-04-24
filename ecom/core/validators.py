from collections import Counter

from rest_framework.serializers import ValidationError


def validate_equipments(self, data):
    """
    Проверяет уникальность equipment ID в списке equipments.
    """
    equipments_data = data.get("equipments", [])
    equipment_ids = [eq["equipment"]["id"] for eq in equipments_data]

    equipment_count = Counter(equipment_ids)
    duplicates = [
        eq_id for eq_id, count in equipment_count.items() if count > 1
    ]

    if duplicates:
        raise ValidationError(
            {
                "equipments": f"Оборудование с ID {duplicates} указано более одного раза. Необходимо устранить дублирующие записи."
            }
        )

    return data
