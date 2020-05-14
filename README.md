# Stepik_autotest_final

Задание:

1. Убедитесь, что в репозитории есть все нужные файлы.

2. Проверьте requirements.txt и убедитесь что там указаны нужные версии пакетов, как минимум:
   pytest==5.1.1
   selenium==3.14.0

3. Проверьте, что все тесты, описанные в test_main_page.py и test_product_page.py запускаются и проходят (очевидно, за исключением тех, которые помечены как xfail/skip).

4. Проверьте стиль кода.

5. Откройте test_product_page.py. Убедитесь, что там есть следующие тесты:
   1. test_user_can_add_product_to_basket
   2. test_guest_can_add_product_to_basket
   3. test_guest_cant_see_product_in_basket_opened_from_product_page
   4. test_guest_can_go_to_login_page_from_product_page

Отмаркируйте эти тесты меткой:
@pytest.mark.need_review

Убедитесь, что при запуске с помощью следующей команды тесты запускаются и успешно проходят:

pytest -v --tb=line --language=en -m need_review test_product_page.py

6. Убедитесь, что все тесты написаны в стиле PageObject: нет assert в теле тестов, все методы действия и проверки выделены в отдельные методы в классах PageObject, все селекторы лежат в locators.py.
