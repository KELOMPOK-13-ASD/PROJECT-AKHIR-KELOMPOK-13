#  Project Akhir Algoritma dan Struktur Data
#### Tema : Perpustakaan
###### Kelompok 13
---
### Deskripsi Program
Program ini dibuat dengan tujuan menawarkan kemudahan bagi pengguna perpustakaan untuk membuka akses seluas-luasnya terhadap informasi yang telah dipublikasikan. Selain itu program ini juga dapat memfasilitasi perkembangan secara sistematis dengan cara mengumpulkan, menyimpan, dan mengatur data atau informasi buku yang kemudian akan disajikan kepada pengunjung perpustakaan.
Program ini diharapkan mampu membantu admin perpustakaan dalam melakukan tata kelola buku-buku yang ada di perpustakaan, dan juga diharapkan mampu membantu pengunjung perpustakaan dalam melakukan proses pinjam meminjam buku yang ada di perpustakaan.
Program ini dibuat dengan menggunakan salah satu struktur data yaitu linked list yang berfungsi untuk mengorganisasikan data sedemikian rupa sehingga implementasi ( penerapan ) atau pemeliharaan logika program menjadi lebih terstruktur.Program ini juga menggunakan algoritma merge sort untuk melakukan sorting dan menggunakan jump search untuk melakukan searching.
Program ini menggunakan database mysql pada registrasi dan login dengan cara kerjanya adalah membuat database yang dapat memodifikasi, menyimpan data, dan menentukan keterkaitan tabel-tabel yang ada di dalam software, kemudian perangkat pengguna membuat request dengan perintah spesifik menggunakan bahasa SQL, setelah itu server akan menerima dan menjalankan perintah.

### Struktur Project
1. Menu utama : berisi opsi yang dapat dipilih oleh user untuk kemudian diekseskusi oleh program sesuai dengan pilihan yang telah dipilih oleh user.
2. Login admin : merupakan suatu proses untuk masuk ke dalam menu admin, yang dimana user akan dimintai untuk memasukkan username dan juga password yang telah ditentukan sebelumnya.
3. Login pengunjung : merupakan suatu proses untuk masuk ke dalam menu pengunjung, yang dimana user akan dimintai untuk memasukkan username dan juga password yang telah dibuat sebelumnya pada saat melakukan registrasi pengunjung. 
4. Registrasi pengunjung : hanya dapat dilakukan oleh user yang belum memliki akun sebelumnya karena username dan juga password dibutuhkan sebagai pintu masuk ke dalam program. User yang melakukan registrasi akan otomatis memiliki role sebagai pengunjung, bukan admin.
5. Menu admin : berisi opsi yang dapat dipilih oleh admin seperti melihat, mencari, menambahkan, dan menghapus buku. Previlage yang dimiliki oleh admin tentu berbeda dengan yang dimiki oleh pengunjung.
6. Menu pengunjung : berisi opsi yang dapat dipilih oleh pengunjung seperti melihat, mencari, meminjam, dan mengembalikan buku, juga dapat menampilkan daftar riwayat  bacaan. Pengunjung tidak dapat melakukan tata kelola data buku yang ada di perpustakaan karena hal ini hanya dapat dilakukan oleh admin.

### Fitur dan Fungsionalitas
| Fitur | Fungsionalitas |
| ------ | ------ |
| Login/Register | pintu masuk bagi admin ataupun pengunjung untuk mengakses program. Login atau registrasi dimaksudkan untuk mengatur proses identifikasi. |
| Lihat buku | menampilkan informasi/data dari buku-buku yang ada di perpustakaan. Informasi tersebut dapat berupa judul, pengarang, penerbit, genre, tahun terbit, dan juga status. Status disini diperuntukkan untuk memberi informasi mengenai ketersediaan buku yang akan dpinjam, apakah buku tersebut sedang dalam kondisi dipinjam oleh pengunjung yang lain atau tidak. | 
| Cari buku | membantu memudahkan user untuk menemukan data/informasi dari buku yang ingin dicari. |
| Tambah buku | menambahkan data buku ke dalam  perpustakaan yang kemudian akan ditampilkan kepada user sehingga dapat menambah pilihan buku yang dapat dipinjam oleh pengunjung. |
| Hapus buku | menghapus atau menghilangkan data buku yang mungkin sudah tidak dapat lagi disajikan atau dipinjamkan kepada pengunjung. |
| Pinjam buku | menambahkan buku ke dalam daftar antrean untuk kemudian dilakukan persetujuan oleh admin sebelum buku dapat dipinjam oleh pengunjung |
| Kembalikan buku | mengubah status buku dari yang sebelumnya unavailable menjadi available yang berarti buku tersebut sudah dapat dipinjam oleh pengunjung yang lain. |
| Lihat daftar bacaan | menampilkan daftar riwayat buku yang telah dipinjam oleh pengunjung selama menjadi anggota perpustakaan |

### Cara penggunaan
![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Menu%20Utama.png?raw=true)
- Pertama tama user memilih pilihan yang ada pada menu utama, apakah user ingin login sebagai admin, login sebagai pengunjung atau ingin melakukan registrasi terlebih dahulu

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Username%20Admin.png?raw=true)
- Jika user memilih login admin maka user akan dimintai untuk memasukkan username dan passwaord yang sudah ditentukan sebelumnya

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Username%20Pengunjung.png?raw=true)
- Jika user memilih login pengunjung maka user akan dimintai untuk memasukkan username dan juga password yang telah dbuat oleh user pada saat registrasi atau pembuatan akun

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Registrasi.png?raw=true)
- Jika user memilih registrasi maka user akan  dimintai untuk membuat username dan password terlebih dahulu, jika username ternyata telah ada di dalam database, maka user akan dimintai untuk memasukkan username yang lain

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Menu%20Admin.png?raw=true)
- Sebagai admin, kita dapat melakukan beberapa hal seperti melihat, mencari, menambah dan menghapus data buku. Intinya admin dapat melakukan pengelolaan data pada setiap buku

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%201%20(Admin).png?raw=true)
- Jika admin ingin melihat daftar buku yang tersedia di dalam perpustakkan, maka admin dapat memilih pilihan pertama dan kemudian akan ditampilkan tampilan seperti yang ada pada gambar diatas.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%202%20(Admin).png?raw=true)
- Jika admin ingin mencari dan melihat detail buku, maka admin dapat memilih pilihan kedua, kemudian admin dapat memasukkan judul buku yang ingin dicari. Setelah itu akan ditampilkan tampilan seperti yang ada pada gambar yang ada di atas.

![alt](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%203%20(Admin).png?raw=true)
- Jika admin ingin menambahkan buku, maka admin dapat memilih pilihan ketiga, setelah itu admin dapat melengkapi data buku seperti judul, pengarang, penerbit, genre, tahun dan status. Jika semua data telah dilengkapi, maka kemudian buku akan ditambahkan ke dalam daftar buku yang tersedia di perpustakaan.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%204%20(Admin).png?raw=true)
- Jika admin ingin menghapus buku, maka admin dapat memilih pilihan keempat, setelah itu admin dapat memasukkan nomor buku yang ingin dihapus.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Menu%20User.png?raw=true)
- Sebagai pengunjung, kita dapat melihat, mencari, meminjam dan mengembalikan buku yang telah dipinjam, juga dapat melihat riwayat daftar bacaan atau riwayat peminjaman buku.

![alt](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%201%20(User).png?raw=true)
- Jika pengunjung ingin melihat daftar buku apa saja yang tersedia di dalam perpustakaan, maka pengunjung dapat memilih pilihan pertama. Kemudian akan ditampilkan tampilan seperti yang ada pada gambar diatas.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%202%20(User).png?raw=true)
- Jika pengunjung ingin mecari dam melihat detail buku, maka pengunjung dapat memilih pilihan kedua, kemudian pengunjung dapat memasukkan judul buku yang ingin dicari. Setelah itu akan ditampilkan tampilan sperti yang ada pada gambar yang ada diatas.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%203%20(User)%20(2).png?raw=true)
- Jika pengunjung ingin meminjam buku, maka pengunjung dapat memilih pilihan ketiga, kemudian pengunjung dapat memilih buku yang akan di pinjam. Setelah itu akan ditampilkan konfirmasi peminjaman seperti gambar yang ada di atas.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%204%20(User).png?raw=true)
- Jika pengunjung ingin mengembalikan buku yang sudah dipinjam, maka pengunjung dpat memilih pilihan ke keempat, kemudian pengunjung dapat memilih nomor buku yang ingin dikembalikan.

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%205%20(User)%20(2).png?raw=true)
- Jika pengunjung ingin melihat daftar buku yang dipinjam, maka pengunjung dapat memilih pilihan kelima, kemudian akan ditampilkan tampilan seperti yang ada pada gambar yang ada di atas. Jika pengunjung sudah mengembalikan semua buku yang dipinjam, maka yang akan ditampilkan adalah "tidak ada catatan peminjaman".

![alt text](https://github.com/KELOMPOK-13-ASD/Project-Akhir_Kelompok-13/blob/master/Pilihan%206%20(User).png?raw=true)
- Jika pengunjung ingin keluar dari program, maka pengunjung dapat memilih pilihan keenam, kemudian akan ditampilkan tampilan seperti yang ada pada gambar diatas.
