# Logistic Regression Model From Scratch

## Latar Belakang
Pada project ini saya akan membuat algoritma *logistic regression* dari dasar dengan menggunakan bahasa pemograman *python* serta *library numpy* yang digunakan untuk penghitungan matrix dan operasi matematika lainnya.

Algoritma *logistic regression* merupakan algoritma yang umum digunakan pada *machine learning* untuk kasus klasifikasi. Dengan algoritma tersebut dapat membantu untuk memberikan keputusan dan prediksi terkait kasus kasus klasifikasi dengan memberikan informasi data atau fitur - fitur terkait yang dapat digunakan untuk membangun model algoritma tersebut.

Pada proses pembangunan model algoritma *logistic regression* dibutuhkan langkah - langkah secara garis besar sebagai berikut:

1. **Menyiapkan data.** Data yang disiapkan harus memiliki fitur - fitur masukkan dan fitur yang ingin di prediksi. Untuk kemudian data tersebut pecah menjadi data latih *(train data)* dan data pengujian *(test data)*.

2. **Inisisasi parameter model.** Saat pelatihan model akan menginisiasi *weight* dan *bias*.

3. **Optimisasi model.** Optimisasi dilakukan dengan meminimkan *cost function*. *cost function* dijadikan tolak ukur kesalahan prediksi pada model. Metode optimisasi yang umum digunakan ialah *gradient descent*.

## Component Learning
### 1. Algortima *Logistic Regression*
![graph logit](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Exam_pass_logistic_curve.svg/400px-Exam_pass_logistic_curve.svg.png "Logistic Regression")

*Logistic regression* merupakan metode statistik dan *machine learning* yang digunakan untuk klasifikasi biner dengan keluaran atau output berupa 0 atau 1.

![formula logit](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/05/E4.png "Logistic Regression Formula")

- **Y** merupakan *output* atau hasil prediksi, dengan nilai berupa probabilitas terhadap target 1 atau 0.
- **e** adalah pangkat dari bilangan Euler (berkisar 2.71828).
- **β0** adalah *bias*.
- **β1..n** adalah *weight* atau koefisien.
- **X** adalah fitur yang digunakan untuk memprediksi variabel target.

Pada prosesnya pembentukan model *logistic regression* memperlukan cara untuk mendapatkan hasil terbaik. Dikarenakan saat inisiasi awal *weight* dan *bias* masih memberikan banyak hasil klasifikasi yang keliru. Maka itu diperlukan proses optimisasi untuk mencari *weight* dan *bias* terbaik pada model *logistic regression* untuk memberikan hasil klasifikasi yang baik.



Algoritma optimisasi yang umum digunakan ialah *gradient descent*. algoritma tersebut bekerja dengan melakukan iterasi berulang kali untuk mencari *cost function* yang paling kecil. Pada prosesnya untuk mengecilkan *cost function* pada model *logistic regression* dilakukan cara dengan mengubah nilai *weight* dan *bias* pada model. 