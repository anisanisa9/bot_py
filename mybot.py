import telebot
import mysql.connector

from datetime import datetime

TOKEN='880954834:AAHWsHMrffdkdZyINScyz_B0-87EFdDnTYs'
SAPA="Selamat Datang Di Bot SMK Taruna Bhakti"

myBot = telebot.TeleBot(TOKEN)

myDb=mysql.connector.connect(host='localhost',user='root',database='database')
sql=myDb.cursor()

from telebot import apihelper

waktusekarang=datetime.now()


    # start
class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        teks = SAPA + "\n-- admin & developer @Anisanis - SMK Taruna Bhakti Depok - Ketik /help Untuk Info Lebih Lanjut--"+"\n"\
        "hari ini tanggal " +str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def start(message):
        help = "/jurusan = Untuk info jurusan yang ada di SMK Taruna Bhakti\n/fasilitas = Info Fasilitas yang ada di SMK Taruna Bhakti\n/sosmed = Info Sosmed yang dimiliki" \
               "\n/guru = Data Guru SMK Taruna Bhakti \n \n \n /guru #reg#nipd = Untuk mendaftar sebagai guru SMK tarunabhakti "
        myBot.reply_to(message, help)

    @myBot.message_handler(commands=['jurusan'])
    def start(message):
        juru = "Hallo!!! \nJurusan Di SMK Taruna Bhakti ada 5 lohhh... \n 1. Rekayasa Perangkat Lunak \n 2. Teknik Komputer Jaringan \n 3. Multimedia \n 4. broadcast \n 5. Teknik Elekronika Industri" \
               "\nSemua jurusan di SMK Taruna Bhakti punya keahliannya masing masing lohh!!"
        myBot.reply_to(message, juru)

    @myBot.message_handler(commands=['sosmed'])
    def start(message):
        sosmed = "SMK Taruna Bhakti itu sekolah IT, jadi sosmed nya selalu update \n1. Instagram : @starbhak.official (ini instagram Taruna Bhakti yang real) " \
               "\n2. Website : WWW.Smktarunabhakti.net (Semua info sekolah ada disana) \n3. Portal : portal.smktarunabhakti.net (Semua pembelajaran siswa dilakukan di sini)"
        myBot.reply_to(message, sosmed)

    @myBot.message_handler(commands=['fasilitas'])
    def start(message):
        fasilitas = "SMK Taruna Bhakti memiliki banyak fasilitas yang sangatt memadaii contohnyaa: " \
               "\n1. Ruang Laboratorium yang memadai \n2. Wifi yang bisa digunakan \n3. Area kantin dan taman yang nyaman" \
               "\nUntuk fasilitas lainnya cek di website nya yaa..."
        myBot.reply_to(message, fasilitas)

    @myBot.message_handler(commands=['guru'])
    def start(message):
        query = "select id,nama,komli from `tabel_siswa` "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            # print(data)
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message, str(kumpuldata))


    print(myDb)

    print("-- Bot sedang berjalan --")
    myBot.polling(none_stop=True)


