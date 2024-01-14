from api import PetFriends
from settings import valid_email, valid_password, notvalid_password, notvalid_email
import json

pf = PetFriends()

#1 Неагтивный тест. Проверка получения ключа авторизации при невалидном email
def test_negative_get_api_key_for_user_notvalid_email(email = notvalid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

#2 Негативный тест. Авторизация с невалидным логином и получения списка всех животных
def test_negative_get_list_all_pets_with_notvalid_password(filter=''):
    _, auth_key = pf.get_api_key(valid_email, notvalid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert  status == 200
    assert len(result['pets']) > 0

#3 Негативный тест. Проверка передачи пустого значения полей (Имя, Порода, Возраст)
def test_negativ_zerro_info_my_ped(name = '', animal_type = '', age = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name and result['animal_type'] == animal_type and result['age'] == age

#4 Негативный тест. Проверка передачи спецсимволов в поля (Имя, Порода, Возраст)
def test_negativ_specsimvol_info_my_ped(name = '!@#', animal_type = '%^*', age = '&?'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name and result['animal_type'] == animal_type and result['age'] == age

#5 Негативный тест. Проверка передачи буквенного значения в поле (Возраст)
def test_negativ_text_age_info_my_ped(name = 'Рекс', animal_type = 'Собака', age = 'Пять'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['age'] == age