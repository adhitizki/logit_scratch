# Logistic Regression Model From Scratch

## Latar Belakang
Pada project ini saya akan membuat algoritma *logistic regression* dari dasar dengan menggunakan bahasa pemograman *python* serta *library numpy* yang digunakan untuk penghitungan matrix dan operasi matematika lainnya.

Algoritma *logistic regression* merupakan algoritma yang umum digunakan pada *machine learning* untuk kasus klasifikasi. Dengan algoritma tersebut dapat membantu untuk memberikan keputusan dan prediksi terkait kasus kasus klasifikasi dengan memberikan informasi data atau fitur - fitur terkait yang dapat digunakan untuk membangun model algoritma tersebut.

Pada proses pembangunan model algoritma *logistic regression* dibutuhkan langkah - langkah secara garis besar sebagai berikut:

1. **Menyiapkan data.** Data yang disiapkan harus memiliki fitur - fitur masukkan dan fitur yang ingin di prediksi. Untuk kemudian data tersebut pecah menjadi data latih *(train data)* dan data pengujian *(test data)*.

2. **Inisisasi parameter model.** Saat pelatihan model akan menginisiasi *weight* dan *bias*.

3. **Optimisasi model.** Optimisasi dilakukan dengan meminimkan *cost function*. *cost function* dijadikan tolak ukur kesalahan prediksi pada model. Metode optimisasi yang umum digunakan ialah *gradient descent*.

## Component Learning 
![graph logit](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Exam_pass_logistic_curve.svg/400px-Exam_pass_logistic_curve.svg.png "Logistic Regression")

*Logistic regression* merupakan metode statistik dan *machine learning* yang digunakan untuk klasifikasi biner dengan keluaran atau output berupa 0 atau 1.

![formula logit](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2020/05/E4.png "Logistic Regression Formula")

- **Y** merupakan *output* atau hasil prediksi, dengan nilai berupa probabilitas terhadap target 1 atau 0.
- **e** adalah pangkat dari bilangan Euler (berkisar 2.71828).
- **β0** adalah *bias*.
- **β1..n** adalah *weight* atau koefisien.
- **X** adalah fitur yang digunakan untuk memprediksi variabel target.

*Cost Function* sendiri digunakan untuk mengevaluasi performa sebuah model dalam memprediksi *output* atau keluaran yang benar. *Cost function* yang umum digunakan pada model *logistric regression* ialah *binary cross-entropy* atau *log loss*. *cost funtion* tersebut mengukur kesalahan prediksi dari model dengan membandingkan nilai prediksi yang dihasilkan oleh model dengan nilai target yang sebenarnya.

![log loss](https://miro.medium.com/v2/resize:fit:720/format:webp/1*rdBw0E-My8Gu3f_BOB6GMA.png "Binary Cross Entropy or Log Loss")

- **H(q)** merupakan nilai *cost function*.
- **N** adalah total data.
- **yi** nilai target sesungguhnya.
- **p(yi)** nilai prediksi (probabilitas target).

Pada prosesnya pembentukan model *logistic regression* memperlukan cara untuk mendapatkan hasil terbaik. Dikarenakan saat inisiasi awal *weight* dan *bias* masih memberikan banyak hasil klasifikasi yang keliru. Maka itu diperlukan proses optimisasi untuk mencari *weight* dan *bias* terbaik pada model *logistic regression* untuk memberikan hasil klasifikasi yang baik.

![graph gradient descent](https://suboptimal.wiki/images/gd_3.jpg "Gradient Descent")

Algoritma optimisasi yang umum digunakan ialah *gradient descent*. algoritma tersebut bekerja dengan melakukan iterasi berulang kali untuk mencari *cost function* yang paling kecil. Pada prosesnya untuk mengecilkan *cost function* pada model *logistic regression* dilakukan cara dengan mengubah nilai *weight* dan *bias* pada model. pembaruan nilai *weight* dan *bias* dilakukan dengan menghitung *learning rate* terhadap gradient. penentuan *learning rate* sangat penting untuk menentukan efisiensi pada optimisasi.

![gradient descent formula](https://suboptimal.wiki/images/gd_4.jpg "Gradient Descent Formula")

- **w** adalah *weight*.
- **η** merupakan *learning rate*, parameter langkah dalam iterasi optimisasi.
- **∇Q(wθ)** adalah gradient dari *cost function*.

Setelah melakukan optimisasi didaptkan **weight* dan *bias* terbaik sehingga menghasilkan model *logistic regression* terbaik berdasarkan nilai *cost funtion* paling kecil. model tersebut dapat digunakan untuk memprediksi target atau *output* berupa probabilitas terhadap kelas 0 atau 1. sehingga diperlukan *threshold* untuk menentukan nilai target kelas 0 atau 1. Umumnya *threshold* yang digunakan ialah 0,5.

## Alur Kode Algoritma
Alur program untuk membentuk model *logistic regression*
> 1. Masukkan data latih
> 2. Penentuan nilai awal *parameter*, *weight* dan *bias*
>       - *learning rate*
>       - *jumlah iterasi optimisasi*
>       - *weight*
>       - *bias*
> 3. Iterasi dengan batas jumlah iterasi
> 4. Perhitungan linear model
> 5. Perhitungan sigmoid (measukan nilai linear model ke model)
> 6. Perhitungan gradient
> 7. Pembaruan nilai *weight* dan *bias* dengan proses mengkalikan *learning rate* dengan gradient
> 8. Selesai iterasi
> 9. Pencatatan nilai *log loss* 
> 10. Selesai

Alur program untuk prediksi
> 1. Masukkan data yang ingin diprediksi
> 2. Perhitung linear model dengan *weight* dan *bias* terbaik
> 3. Perhitungan fungsi sigmoid dengan memasukkan hasil perhitungan linear model (nilai probabilitas)
> 4. Jika nilai probabilitas diatas proba termasuk kelas 1, jika tidak masuk kedalam kelas 0
> 5. Selesai

## Hyperparameter
Implementasi model algoritma *logistic regression* terlihat pada notebook `implement.ipynb`. Pembentukan model awal dengan parameter bawaan yaitu `learning_rate 0.01`, `num_iterations 1000` dengan `threhsold 0.5` didapatkan hasil akurasi sebesat 94,7%. Sudah dilakukan coba pencarian *threshold* terbaik berdasarkan akurasi menemui nilai 0,01. Namun hasil akurasi nya bila dibandingkan dengan *threshold* default sama yaitu sebesar 94,7%.

Dilakukan *hyperparameter tuning* dengan melakukan *grid search* dan didapatkan hasil parameter terbaik yaitu `learning_rate 0.0001`, `num_iterations 2000` dan `threshold 0.5` dengan akurasi 94,7%. Penentuan parameter terbaik untuk *learning rate* dan jumlah iterasi didapatkan dari *cost function log loss* yang paling kecil yaitu dengan nilai sebesar 0,366. Juga dilakukan pencarian nilai untuk *threshold* sama seperti penentuan model awal yaitu nilai akurasi *threshold* terbaik sama dengan *threshold* default.

## Referensi
- https://suboptimal.wiki/explanation/gradient-descent/
- https://cs229.stanford.edu/lectures-spring2022/main_notes.pdf
- https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a