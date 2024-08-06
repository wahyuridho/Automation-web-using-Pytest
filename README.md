# Automation-web-using-Pytest
Project ini adalah project latihan saya untuk membuat web automation pada website saucedemo, dengan menggunakan framework Pytest

# Generate allure report
Untuk menggenerate allure report anda bisa menggunakan perintah berikut:
"pytest --alluredir=allure-results"

note: cek terlebih dahulu pada file pytest.ini, jika pada bagian addopts tidak ada "--alluredir=allure-results" maka anda harus menambahkan manual ketika run command

Setelah selesai anda dapat menggunakan perintah dibawah untuk melihat hasil reportnya.
"allure serve allure-results"
