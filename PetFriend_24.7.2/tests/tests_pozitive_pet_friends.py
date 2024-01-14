from api import PetFriends
from settings import valid_email, valid_password
import json

pf = PetFriends()

#1 Проверка получения ключа авторизации
def test_get_api_key_for_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

#2 Проверка получения списка всех животны
def test_get_list_all_pets(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

#3 Проверка добавления питомца без фото
def test_add_pet_without_foto(name = 'Пушок', animal_type = 'Кот', age = '5'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_foto(auth_key, name, animal_type, age)
    assert status == 200
    assert result['animal_type'] == animal_type

#4 Проверка добавления фото к моему питомцу
def test_add_foto_in_my_pet(pet_photo = 'image/Cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_foto_in_my_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != ""

#5 Проверка добавления питомца с фото
def test_add_pet_with_foto(name = 'Пес', animal_type = 'Собака', age = '2', pet_photo = 'image/Dog.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#6 обновляем фото питомца в карточке питомца с фото
def test_replace_foto_in_my_pet(pet_photo = 'image/Cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    id_foto = my_pets['pets'][0]['pet_photo']
    status, result = pf.add_foto_in_my_pet(auth_key, pet_id, pet_photo)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    id_foto_new = my_pets['pets'][0]['pet_photo']
    assert status == 200
    assert id_foto_new != id_foto

#7 Проверка обновления инфо о питомце
def test_update_info_pet(name = 'Пес', animal_type = 'Шпиц', age = '3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

#8 Проверка факта удаления питомца
def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_my_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id != my_pets.values()
