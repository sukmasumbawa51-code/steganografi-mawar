# LAPORAN SINGKAT STEGANOGRAFI

## Penyembunyian Pesan pada Media Digital

### 1. Pendahuluan

Perkembangan teknologi informasi menyebabkan pertukaran data menjadi semakin cepat dan mudah. Namun, hal ini juga menimbulkan risiko terhadap keamanan informasi. Oleh karena itu, diperlukan teknik untuk melindungi data agar tidak mudah diketahui oleh pihak yang tidak berwenang. Salah satu teknik yang dapat digunakan adalah **steganografi**.

Steganografi merupakan metode untuk menyembunyikan pesan rahasia di dalam suatu media sehingga keberadaan pesan tersebut tidak terlihat. Berbeda dengan kriptografi yang menyamarkan isi pesan, steganografi menyembunyikan pesan agar orang lain tidak menyadari bahwa ada pesan rahasia di dalam media tersebut.

Dalam tugas ini dilakukan contoh sederhana penyembunyian pesan menggunakan media gambar sebagai wadah penampung.

---

### 2. Tujuan

Adapun tujuan dari kegiatan ini adalah:

1. Memahami konsep dasar steganografi.
2. Mengetahui bagaimana cara menyembunyikan pesan pada media digital.
3. Mempelajari komponen utama dalam proses steganografi.

---

### 3. Komponen Steganografi

Dalam proses steganografi terdapat beberapa komponen utama, yaitu:

#### 1. Wadah Penampung (Cover Object)

Wadah penampung adalah media yang digunakan untuk menyisipkan pesan rahasia. Media ini harus dipilih sedemikian rupa agar perubahan yang terjadi setelah penyisipan pesan tidak terlihat oleh manusia.

Pada tugas ini, wadah penampung yang digunakan adalah:

**Gambar digital berformat PNG dengan ukuran 1024 × 768 piksel.**

Gambar dipilih karena memiliki banyak piksel sehingga memungkinkan pesan disisipkan tanpa merusak kualitas gambar secara signifikan.

---

#### 2. Pesan yang Disembunyikan (Secret Message)

Pesan yang disembunyikan adalah informasi rahasia yang ingin disisipkan ke dalam media penampung.

Pada contoh ini, pesan yang disembunyikan adalah:

**"STI PRODI YANG DICINTAI"**

Pesan tersebut akan dimasukkan ke dalam gambar menggunakan metode penyisipan data pada bagian tertentu dari piksel gambar.

---

#### 3. Stego Object

Stego object adalah media hasil akhir setelah proses penyisipan pesan dilakukan. Secara visual, stego object biasanya terlihat sama dengan media aslinya sehingga orang lain tidak menyadari bahwa terdapat pesan rahasia di dalamnya.

Dalam tugas ini, hasil akhirnya adalah:

**Gambar PNG yang telah disisipi pesan "STI PRODI YANG DICINTAI".**

Gambar tersebut terlihat sama seperti gambar asli, tetapi sebenarnya sudah mengandung informasi tersembunyi yang hanya dapat dibaca menggunakan metode atau program tertentu.

---

### 4. Proses Penyembunyian Pesan

Secara umum proses steganografi dilakukan melalui beberapa langkah berikut:

1. Menentukan media penampung (cover object), misalnya gambar.
2. Menentukan pesan rahasia yang akan disembunyikan.
3. Menggunakan metode steganografi untuk menyisipkan pesan ke dalam media.
4. Menghasilkan media baru yang disebut stego object.
5. Pesan dapat diambil kembali menggunakan proses ekstraksi.

---

### 5. Kesimpulan

Steganografi merupakan teknik keamanan informasi yang digunakan untuk menyembunyikan pesan rahasia di dalam suatu media digital. Teknik ini bertujuan agar keberadaan pesan tidak diketahui oleh orang lain. Dalam contoh tugas ini digunakan gambar berformat PNG sebagai wadah penampung dan pesan yang disembunyikan adalah "STI PRODI YANG DICINTAI". Hasil dari proses tersebut adalah gambar stego yang secara tampilan sama dengan gambar asli tetapi mengandung pesan rahasia.

Dengan memahami konsep steganografi, kita dapat mengetahui salah satu cara untuk menjaga keamanan informasi dalam komunikasi digital.
