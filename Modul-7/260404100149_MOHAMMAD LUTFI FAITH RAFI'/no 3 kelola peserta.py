undangan = set()
webinar_a = set()
webinar_b = set()

print("===== DATA PESERTA WEBINAR =====")

data = input("Masukkan nama seluruh tamu undangan: ")
if data:
    undangan.update(data.replace(", ", ",").split(","))

data = input("Masukkan peserta Webinar A: ")
if data:
    webinar_a.update(data.replace(", ", ",").split(","))

data = input("Masukkan peserta Webinar B: ")
if data:
    webinar_b.update(data.replace(", ", ",").split(","))

semua_peserta = webinar_a | webinar_b

keduanya = webinar_a & webinar_b

satu_webinar = webinar_a ^ webinar_b

tidak_hadir = undangan - semua_peserta

print("\n===== HASIL DATA WEBINAR =====")
print("Semua peserta:", semua_peserta)
print("Hadir di kedua webinar:", keduanya)
print("Hadir di salah satu webinar:", satu_webinar)
print("Tidak hadir di webinar mana pun:", tidak_hadir)
