from .models import MCC, MNCOperator, MOBIL

class ICCIDValidator:
    """Класс для валидации ICCID номеров."""
    
    def __init__(self):
        """Инициализация валидатора ICCID с данными из базы данных."""
        self.MCC = {mcc.code: mcc.country for mcc in MCC.objects.all()}
        self.MNC_OPERATORS = {mnc.code: mnc.operator for mnc in MNCOperator.objects.all()}
        self.MOBIL = {mobil.code: mobil.country for mobil in MOBIL.objects.all()}
        self.ICCID_LENGTH = 20

    def validate_iccid(self, iccid):
        result = {"iccid": iccid, "is_valid": False, "message": "", "operator": None, "country": None}

        if len(iccid) != self.ICCID_LENGTH:
            result["message"] = f"Ошибка - длина ICCID не равна {self.ICCID_LENGTH} цифрам"
            return result

        mobil = iccid[:2]
        if mobil not in self.MOBIL:
            result["message"] = f"Ошибка - неверный MOBIL код ({mobil})"
            return result

        mcc = iccid[2:5]
        if mcc not in self.MCC:
            result["message"] = f"Ошибка - неверный MCC код ({mcc})"
            return result

        mnc = iccid[5:8]
        if mnc not in self.MNC_OPERATORS:
            result["message"] = f"Ошибка - неверный MNC код ({mnc})"
            return result

        result["is_valid"] = True
        result["message"] = "Валидный ICCID"
        result["operator"] = self.MNC_OPERATORS[mnc]
        result["country"] = self.MCC[mcc]
        return result

    def validate_iccid_list(self, iccid_list):
        return [self.validate_iccid(iccid) for iccid in iccid_list]