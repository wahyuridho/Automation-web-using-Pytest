# Automation-web-using-Pytest
Project ini adalah project latihan saya untuk membuat web automation pada website saucedemo, dengan menggunakan framework Pytest

# How to Use
1. Pastikan pada laptop anda sudah terinstall Python, silahkan bukan terminal anda lalu ketikan "python --version" jika sudah terinstall maka akan muncul seperti berikut:

![image](https://github.com/user-attachments/assets/0fdc0101-4955-4f1e-8d30-1d52353cb785)

Pastikan juga anda sudah menginstall PIP, gunakan perintah "pip --version", jika sudah terinstall maka akan muncul seperti di bawah

![image](https://github.com/user-attachments/assets/5fc7e205-ab71-4ae6-92b6-9b544cd58981)
Note: jika belum ada python dan pip silahkan install terlebih dahulu
3. Setelah dipastikan python dan pip sudah terinstall, silahkan install terlebih dahulu "PIPENV", ini digunakan untuk membuat virtual environtment agar library yang terinstall di internal PC tidak bentrok dengan project ini. Gunakan perintah "pip install pipenv" untuk menginstall PIPENV
4. Setelah itu silahkan lakukan cloning project dengan cara ketikan perintah "git clone https://github.com/wahyuridho/Automation-web-using-Pytest.git", jika berhasil maka akan seperti gambar berikut:
![image](https://github.com/user-attachments/assets/c2e062dd-95be-4df7-a6f7-d58a795fa896)

5. Setelah itu silahkan masuk ke folder hasil cloning github, lalu buka code editor anda atau buka editor anda lalu arahkan project ke folder hasil clone tersebut.
6. Setelah itu buka terminal pada code editor anda, lalu ketikan "pipenv shell", maka sistem akan membuatkan virtual env berdasarkan project tersebut.
![image](https://github.com/user-attachments/assets/c04b313c-3827-4076-a564-38df55b95d4d)

7. Setelah berhasil membuat virtual env, silahkan ketikan perintah "pipenv install --dev", untuk menginstall framework yang akan digunakan berdasarkan file "pipfile".
![image](https://github.com/user-attachments/assets/0211bd55-c15e-4797-8699-647c6bc07647)

Note: anda bisa memastikan bahwa library berhasil di install dengan menjalankan "pip list" pada terminal, lalu memastikan bahwa library yang ada di file "pipfile" berhasil terinstall

# How to run
Untuk menjalankan semua testcase anda bisa menjalankan perintah berikut: "pytest"
![image](https://github.com/user-attachments/assets/e24e22b6-6e01-4ea6-9ff4-dbf0b28f7fd3)

Untuk menjalankan berdasarkan marker anda dapat menjalankan perintha berikut : "pytest -m nama-marker"
![image](https://github.com/user-attachments/assets/719c357a-bf7a-441f-ab88-4cbb89f96465)


# Generate allure report
Untuk menggenerate allure report anda bisa menggunakan perintah berikut:
"pytest --alluredir=allure-results"

note: cek terlebih dahulu pada file pytest.ini, jika pada bagian addopts tidak ada "--alluredir=allure-results" maka anda harus menambahkan manual ketika run command

Setelah selesai anda dapat menggunakan perintah dibawah untuk melihat hasil reportnya.
"allure serve allure-results", berikut hasil report mengguakan allure
![image](https://github.com/user-attachments/assets/541922b2-b352-4f58-875b-a8f5c2a287a6)
